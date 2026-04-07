#!/usr/bin/env bash

set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  run-skills-add-loop.sh \
    --runs-per-cycle N \
    --seconds-between-cycles N \
    --seconds-between-runs N \
    --seconds-after-cycle N

Runs:
  npx skills add https://github.com/serpdownloaders/skills --skills skool-video-downloader loom-video-downloader -y

Parameters:
  --runs-per-cycle         Number of times to run the command per cycle
  --seconds-between-cycles Number of seconds to wait before starting the next cycle
  --seconds-between-runs   Number of seconds to wait between runs inside a cycle
  --seconds-after-cycle    Number of seconds to wait after each cycle completes

Example:
  ./run-skills-add-loop.sh \
    --runs-per-cycle 3 \
    --seconds-between-cycles 600 \
    --seconds-between-runs 15 \
    --seconds-after-cycle 60
EOF
}

require_integer() {
  local name="$1"
  local value="$2"

  if ! [[ "$value" =~ ^[0-9]+$ ]]; then
    echo "Invalid value for $name: $value" >&2
    exit 1
  fi
}

runs_per_cycle=""
seconds_between_cycles=""
seconds_between_runs=""
seconds_after_cycle=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --runs-per-cycle)
      if [[ $# -lt 2 ]]; then
        echo "Missing value for $1" >&2
        usage >&2
        exit 1
      fi
      runs_per_cycle="${2:-}"
      shift 2
      ;;
    --seconds-between-cycles)
      if [[ $# -lt 2 ]]; then
        echo "Missing value for $1" >&2
        usage >&2
        exit 1
      fi
      seconds_between_cycles="${2:-}"
      shift 2
      ;;
    --seconds-between-runs)
      if [[ $# -lt 2 ]]; then
        echo "Missing value for $1" >&2
        usage >&2
        exit 1
      fi
      seconds_between_runs="${2:-}"
      shift 2
      ;;
    --seconds-after-cycle)
      if [[ $# -lt 2 ]]; then
        echo "Missing value for $1" >&2
        usage >&2
        exit 1
      fi
      seconds_after_cycle="${2:-}"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    --*)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 1
      ;;
    *)
      echo "Unexpected argument: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

if [[ -z "$runs_per_cycle" || -z "$seconds_between_cycles" || -z "$seconds_between_runs" || -z "$seconds_after_cycle" ]]; then
  usage >&2
  exit 1
fi

require_integer "runs_per_cycle" "$runs_per_cycle"
require_integer "seconds_between_cycles" "$seconds_between_cycles"
require_integer "seconds_between_runs" "$seconds_between_runs"
require_integer "seconds_after_cycle" "$seconds_after_cycle"

if (( runs_per_cycle < 1 )); then
  echo "runs_per_cycle must be at least 1" >&2
  exit 1
fi

command=(
  npx
  skills
  add
  https://github.com/serpdownloaders/skills
  --skills
  skool-video-downloader
  loom-video-downloader
  -y
)

cycle_number=1

while true; do
  echo "Starting cycle $cycle_number"

  for (( run_number = 1; run_number <= runs_per_cycle; run_number++ )); do
    echo "Cycle $cycle_number, run $run_number/$runs_per_cycle"
    "${command[@]}"

    if (( run_number < runs_per_cycle && seconds_between_runs > 0 )); then
      echo "Sleeping $seconds_between_runs seconds before the next run"
      sleep "$seconds_between_runs"
    fi
  done

  if (( seconds_after_cycle > 0 )); then
    echo "Sleeping $seconds_after_cycle seconds after cycle $cycle_number"
    sleep "$seconds_after_cycle"
  fi

  if (( seconds_between_cycles > 0 )); then
    echo "Sleeping $seconds_between_cycles seconds before cycle $((cycle_number + 1))"
    sleep "$seconds_between_cycles"
  fi

  cycle_number=$(( cycle_number + 1 ))
done
