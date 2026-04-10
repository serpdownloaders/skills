---
name: teachable-video-downloader
description: "Download Teachable courses with all lectures
---

# Teachable Video Downloader — Coming Soon (Browser Extension)

> Download Teachable course videos as MP4 files for offline study directly from your browser. **This extension is currently in development and has not been released yet.**

Teachable Video Downloader is an upcoming browser extension that will let users save video lessons from Teachable-hosted courses without relying on screen recorders or third-party desktop applications. It is being built around the browser playback experience so you can export individual lectures or entire course modules while working through the material in the Teachable player.

- Detect and capture video from Teachable course pages during playback
- Save individual lessons or batch-download full course modules
- Export videos as standard MP4 files for offline viewing
- Work entirely inside the browser with no external software required
- Designed for Chrome, Edge, Brave, Opera, Firefox, and other Chromium browsers

## Status

**This extension is not yet available for download.** Development is in progress and a release date has not been announced. Sign up below to get notified when it launches.

:bell: **Get notified when this launches:** [Join the waitlist](https://serp.ly/teachable-video-downloader)

## Links

- :hourglass_flowing_sand: Waitlist: [Coming Soon — Sign Up](https://serp.ly/teachable-video-downloader)
- :question: Help center: [SERP Help](https://help.serp.co/en/)
- :bulb: Request features: [GitHub Issues](https://github.com/serpapps/teachable-video-downloader/issues)

## Preview

![Teachable Video Downloader hero image](https://raw.githubusercontent.com/serpapps/teachable-video-downloader/refs/heads/main/assets/workflow-preview.webp)

## Table of Contents

- [Why Teachable Video Downloader](#why-teachable-video-downloader)
- [Planned Features](#planned-features)
- [How It Will Work](#how-it-will-work)
- [Expected Formats](#expected-formats)
- [Who It's For](#who-its-for)
- [Use Cases We're Building For](#use-cases-were-building-for)
- [FAQ](#faq)
- [License](#license)
- [Notes](#notes)
- [About Teachable](#about-teachable)

## Why Teachable Video Downloader

Teachable is one of the most widely used platforms for creating and selling online courses. Instructors host video lessons behind a login wall, and students stream them through the Teachable player. There is no built-in option to download course videos as files, which means learners are tied to an internet connection and the platform's player every time they want to review material.

This creates friction for students who travel, work in areas with unreliable connectivity, or simply prefer to organize their purchased course content on their own hard drive. Screen recording tools are a common workaround, but they produce lower-quality output, require real-time capture, and add unnecessary steps to what should be a simple save operation.

Teachable Video Downloader is being designed to sit inside the browser and intercept the video stream that the Teachable player already loads. Instead of re-encoding a screen capture, the extension aims to grab the actual video data the player receives and write it to a local MP4 file. The result is a file that matches the original stream quality without the overhead of recording your screen for the full duration of every lecture.

## Planned Features

- Video detection on Teachable course pages during active playback
- Lesson-level downloading for saving individual lectures one at a time
- Module-level batch export for downloading all lessons in a course section
- Resolution selection based on the quality tiers the Teachable player exposes
- Filename formatting using the course name, section title, and lesson number
- Download queue so you can stack multiple lessons without waiting between each one
- Progress indicator showing download status for each queued video
- Browser-native workflow with no external software dependencies
- Cross-browser compatibility targeting Chrome, Edge, Brave, and Firefox

## How It Will Work

1. Install the extension once it is released from the Chrome Web Store or your browser's add-on marketplace.
2. Log in to your Teachable school and navigate to a course you are enrolled in.
3. Open the lesson page containing the video you want to save.
4. Begin playback so the browser loads the video stream from the platform.
5. Open the extension popup to see the detected video source and available resolutions.
6. Select the lesson or lessons you want to download.
7. Choose your preferred resolution if multiple quality tiers are available.
8. Start the download and the extension will save the MP4 file to your local machine.

## Expected Formats

- Input: Teachable video player streams (HLS / MP4 adaptive segments served through the embedded player)
- Output: MP4 (H.264 video, AAC audio)

Exported files will be saved as standard MP4 files compatible with virtually every media player, mobile device, tablet, and video editing application.

## Who It's For

- Online learners who want offline access to courses they have purchased
- Students preparing for exams who need to review video lectures without an internet connection
- Professionals taking continuing-education courses while traveling or commuting
- Instructors who want a local backup of their own course content hosted on Teachable
- Anyone who prefers to organize purchased course material in their own file system

## Use Cases We're Building For

- Save an entire course module before a long flight or trip to a low-connectivity area
- Build a local study library of purchased courses organized by topic and instructor
- Review key lectures repeatedly without buffering or relying on platform uptime
- Archive course content before a subscription or enrollment window expires
- Keep backup copies of video lessons you have paid for on your own storage

## Security & Scope

- Operates only on the page the user intentionally opens in the active browser tab
- Detects supported playback sources only for user-initiated downloads or exports
- Does not execute page instructions, shell commands, or arbitrary scripts from page content
- Does not follow unrelated links or perform actions outside the active workflow
- Limits support to the named platform, approved embedded contexts, and user-authorized sessions when required

## FAQ

**When will Teachable Video Downloader be released?**
A release date has not been set. Sign up at the waitlist link above to be notified as soon as it is available.

**Does it work with any Teachable school?**
The extension is being built to work with the standard Teachable video player used across schools on the platform. Custom player implementations may require additional support after launch.

**What video quality will it support?**
Quality will depend on what the Teachable player delivers to the browser, which is determined by the course creator's upload settings and the platform's encoding pipeline.

**Will it preserve lesson titles in the filename?**
The plan is to include the course name, section title, and lesson number in the exported filename where that data is available from the page.

**Is it free?**
Pricing details will be announced closer to launch. SERP extensions typically include a free trial period.

**Can I download all lessons in a course at once?**
Batch downloading at the module level is a planned feature. Full-course export will depend on browser and playback constraints and may be introduced after the initial release.

**Does it work with the Teachable mobile app?**
No. This extension is built for the Teachable web experience in desktop browsers, not the mobile application.

## License

This repository is distributed under the proprietary SERP Apps license in the [LICENSE](https://raw.githubusercontent.com/serpapps/teachable-video-downloader/refs/heads/main/LICENSE) file. Review that file before copying, modifying, or redistributing any part of this project.

## Notes

- This extension is in development and is not available for download yet
- Only download content you own or have explicit permission to save
- Video quality will depend on the source stream exposed by the Teachable player
- Teachable platform changes may affect functionality once released
- An active enrollment in the relevant Teachable course and an internet connection will be required

## About Teachable

Teachable is an online course creation platform that enables instructors and creators to build, host, and sell video-based courses to students around the world. Courses are delivered through a web-based player that streams video lessons behind a login, but the platform does not offer a native download-to-file option for enrolled students. Teachable Video Downloader is being built to bridge that gap for learners who want local MP4 copies of course videos they have already purchased or enrolled in.
