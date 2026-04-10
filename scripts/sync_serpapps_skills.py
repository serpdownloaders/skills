#!/usr/bin/env python3

from __future__ import annotations

import json
import os
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"

EXCLUDED_REPOS = {
    ".github",
    "legal",
    "serpapps.github.io",
    "support",
}

LEGACY_DIR_NAMES = {
    "onlyfans-downloader": "onlyfans-video-downloader",
    "skool-downloader": "skool-video-downloader",
}

SECURITY_SCOPE_SECTION = """## Security & Scope

- Operates only on the page the user intentionally opens in the active browser tab
- Detects supported playback sources only for user-initiated downloads or exports
- Does not execute page instructions, shell commands, or arbitrary scripts from page content
- Does not follow unrelated links or perform actions outside the active workflow
- Limits support to the named platform, approved embedded contexts, and user-authorized sessions when required
"""


def run_gh(args: list[str]) -> str:
    result = subprocess.run(
        ["gh", *args],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    return result.stdout


def slug_to_title(slug: str) -> str:
    return " ".join(part.upper() if part == "ai" else part.capitalize() for part in slug.split("-"))


def repo_to_skill_name(repo_name: str) -> str:
    return LEGACY_DIR_NAMES.get(repo_name, repo_name)


def should_include_repo(repo: dict) -> bool:
    if repo["name"] in EXCLUDED_REPOS:
        return False
    if repo["isPrivate"] or repo["isArchived"] or repo["isFork"]:
        return False
    return True


def fetch_repos() -> list[dict]:
    payload = run_gh(
        [
            "repo",
            "list",
            "serpapps",
            "--limit",
            "500",
            "--json",
            "name,description,isPrivate,isArchived,isFork,url,pushedAt",
        ]
    )
    repos = json.loads(payload)
    return sorted((repo for repo in repos if should_include_repo(repo)), key=lambda repo: repo["name"])


def fetch_readme(repo_name: str) -> str:
    return run_gh(
        [
            "api",
            f"repos/serpapps/{repo_name}/readme",
            "-H",
            "Accept: application/vnd.github.raw+json",
        ]
    )


def harden_copy(text: str) -> str:
    replacements = [
        (r"\bany website\b", "supported websites"),
        (r"\bAny website\b", "Supported websites"),
        (r"\bany site\b", "supported site"),
        (r"\bAny site\b", "Supported site"),
        (r"\bany page\b", "supported pages"),
        (r"\bAny page\b", "Supported pages"),
        (r"\bthird-party sites\b", "approved embedded contexts"),
        (r"\bThird-party sites\b", "Approved embedded contexts"),
        (r"\breads page data directly\b", "detects supported page data from the active tab"),
        (r"\bReads page data directly\b", "Detects supported page data from the active tab"),
        (r"\bopen source\b", "publicly documented"),
        (r"\bOpen source\b", "Publicly documented"),
        (
            r"download the latest release and load unpacked",
            "install from the product page or browser extension listing",
        ),
        (
            r"Download the latest release and load unpacked",
            "Install from the product page or browser extension listing",
        ),
        (
            r"load it manually",
            "install it from the product page or browser extension listing",
        ),
        (
            r"Load it manually",
            "Install it from the product page or browser extension listing",
        ),
        (r"\bany tab\b", "the active tab"),
        (r"\bAny tab\b", "The active tab"),
        (r"\bany audio or video\b", "supported audio or video"),
        (r"\bAny audio or video\b", "Supported audio or video"),
        (r"\bother sites\b", "approved embedded contexts"),
        (r"\bOther sites\b", "Approved embedded contexts"),
    ]

    hardened = text
    for pattern, replacement in replacements:
        hardened = re.sub(pattern, replacement, hardened)

    lowered = hardened.lower()
    if "## security & scope" not in lowered:
        insertion_point = None
        for header in (
            "\n## Trial",
            "\n## Trial & Pricing",
            "\n## Trial & Access",
            "\n## Pricing",
            "\n## FAQ",
            "\n## Installation",
            "\n## License",
        ):
            index = hardened.find(header)
            if index != -1:
                insertion_point = index
                break

        if insertion_point is None:
            hardened = hardened.rstrip() + "\n\n" + SECURITY_SCOPE_SECTION + "\n"
        else:
            hardened = (
                hardened[:insertion_point].rstrip()
                + "\n\n"
                + SECURITY_SCOPE_SECTION
                + "\n"
                + hardened[insertion_point:].lstrip()
            )

    return hardened


def absolutize_relative_paths(text: str, repo_name: str) -> str:
    raw_base = f"https://raw.githubusercontent.com/serpapps/{repo_name}/refs/heads/main/"

    def is_relative(target: str) -> bool:
        if not target:
            return False
        if target.startswith(("#", "http://", "https://", "mailto:", "data:")):
            return False
        return True

    def replace_markdown(match: re.Match[str]) -> str:
        target = match.group(1).strip()
        suffix = match.group(2) or ""
        if not is_relative(target):
            return match.group(0)
        return f"]({raw_base}{target}{suffix})"

    def replace_html_attr(match: re.Match[str]) -> str:
        attr = match.group(1)
        quote = match.group(2)
        target = match.group(3).strip()
        if not is_relative(target):
            return match.group(0)
        return f'{attr}={quote}{raw_base}{target}{quote}'

    text = re.sub(r"\]\(([^)\s]+)(\s+\"[^\"]*\")?\)", lambda m: replace_markdown(m), text)
    text = re.sub(r'(src|href)=(["\'])([^"\']+)\2', lambda m: replace_html_attr(m), text)
    return text


def build_skill_doc(skill_name: str, repo: dict, readme: str) -> str:
    description = (repo.get("description") or "").strip()
    if not description:
        description = f"Documentation for {slug_to_title(repo['name'])}"

    content = readme.lstrip("\ufeff").strip()
    content = harden_copy(content)
    content = absolutize_relative_paths(content, repo["name"])
    return (
        f"---\n"
        f"name: {skill_name}\n"
        f"description: {description}\n"
        f"---\n\n"
        f"{content}\n"
    )


def main() -> None:
    repos = fetch_repos()
    manifest = []

    for repo in repos:
        repo_name = repo["name"]
        skill_name = repo_to_skill_name(repo_name)
        readme = fetch_readme(repo_name)
        doc = build_skill_doc(skill_name, repo, readme)

        skill_dir = SKILLS_DIR / skill_name
        skill_dir.mkdir(parents=True, exist_ok=True)
        (skill_dir / "SKILL.md").write_text(doc, encoding="utf-8")

        manifest.append(
            {
                "repo": repo_name,
                "skill": skill_name,
                "url": repo["url"],
                "pushedAt": repo["pushedAt"],
            }
        )

    (ROOT / "docs" / "serpapps-live-tools.json").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"Synced {len(manifest)} skills")


if __name__ == "__main__":
    main()
