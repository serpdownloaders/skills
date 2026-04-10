---
name: stream-downloader
description: "Universal stream downloader for HLS
---

# Stream Downloader — Coming Soon (Browser Extension)

> Capture and download any live or on-demand video stream from supported websites directly in your browser. **This extension is currently in development and has not been released yet.**

Stream Downloader is an upcoming browser extension designed to detect, intercept, and save video streams across the open web. Whether a site serves content via HLS, DASH, progressive MP4, or WebRTC, the extension will identify the active media pipeline and let you pull the video down to a local file without switching to a separate desktop application or pasting URLs into a command-line tool.

- Detect and capture HLS (m3u8), DASH (mpd), progressive MP4, and WebRTC streams
- Download live broadcasts, VODs, and embedded video players from supported websites
- Automatically reassemble segmented streams into a single playable file
- Select resolution and quality tier before saving
- Designed for Chrome, Edge, Brave, Opera, Firefox, and other Chromium browsers

## Status

**This extension is not yet available for download.** Development is in progress and a release date has not been announced. Sign up below to get notified when it launches.

:bell: **Get notified when this launches:** [Join the waitlist](https://apps.serp.co/waiting-list)

## Links

- :hourglass_flowing_sand: Waitlist: [Coming Soon — Sign Up](https://apps.serp.co/waiting-list)
- :question: Help center: [SERP Help](https://help.serp.co/en/)
- :bulb: Request features: [GitHub Issues](https://github.com/serpapps/stream-downloader/issues)

## Preview

![Stream Downloader hero image](https://raw.githubusercontent.com/serpapps/stream-downloader/refs/heads/main/assets/workflow-preview.webp)

## Table of Contents

- [Why Stream Downloader](#why-stream-downloader)
- [Planned Features](#planned-features)
- [How It Will Work](#how-it-will-work)
- [Supported Stream Types](#supported-stream-types)
- [Who It's For](#who-its-for)
- [Use Cases We're Building For](#use-cases-were-building-for)
- [FAQ](#faq)
- [License](#license)
- [Notes](#notes)
- [About Video Streaming Protocols](#about-video-streaming-protocols)

## Why Stream Downloader

Modern websites rarely serve a single video file you can right-click and save. Instead, they rely on adaptive streaming protocols that break video into hundreds of small segments, negotiate quality on the fly, and rotate temporary URLs to prevent direct downloads. Live broadcasts add another layer of complexity because the content only exists in real time and is not stored as a static file on any public server.

Stream Downloader is being engineered to operate at the network layer inside the browser, monitoring HTTP requests and media source extensions to identify every active video pipeline on a page. The objective is to give you a single button that captures whatever is playing, regardless of the underlying protocol, and writes it to your disk as a standard video file you can watch, archive, or edit offline.

## Planned Features

- Automatic detection of HLS, DASH, progressive MP4, and WebRTC video streams
- Live stream recording with start and stop controls for capturing specific segments
- Multi-quality selection so you can pick the resolution and bitrate tier you want
- Segment reassembly that merges fragmented streams into one continuous file
- Batch capture for pages hosting multiple embedded players or video feeds
- Filename templating using page title, domain, and timestamp variables
- Background downloading that continues even when you switch browser tabs
- Cross-browser compatibility targeting Chrome, Edge, Brave, and Firefox

## How It Will Work

1. Install the extension once it is released from your browser's extension store.
2. Navigate to supported websites that contains a video stream you want to save.
3. Start playback so the browser initiates the stream connection.
4. Click the extension icon to see all detected video sources on the current page.
5. Choose the stream you want if multiple sources are present.
6. Pick your preferred resolution and quality from the available tiers.
7. Press the download button to begin capturing the stream to a local file.
8. Monitor progress in the extension panel and open the finished file from your downloads folder.

## Supported Stream Types

- **HLS (HTTP Live Streaming):** The most common adaptive format, used by social platforms, news outlets, and sports broadcasters. Stream Downloader will parse m3u8 manifests, fetch every segment, and merge them into a single file.
- **DASH (Dynamic Adaptive Streaming over HTTP):** Widely adopted for high-quality VOD delivery. The extension will read mpd manifests and handle separate audio and video tracks that need to be muxed together.
- **Progressive MP4:** The classic single-file download that some sites still serve. Stream Downloader will intercept these requests and offer a direct save option.
- **WebRTC:** Used for real-time communication and some live-streaming platforms. The extension will tap into the media track and record the incoming feed locally.

Output files will be saved as MP4, MKV, or WebM depending on the source codec and container, ensuring broad compatibility with media players, editors, and mobile devices.

## Who It's For

- Journalists and researchers archiving live press conferences and breaking-news broadcasts
- Content creators collecting reference footage from publicly available streams
- Educators saving lecture recordings and training videos for offline classroom use
- Sports analysts capturing game footage for review and breakdown sessions
- Travelers downloading entertainment before heading into areas with limited connectivity

## Use Cases We're Building For

- Record a live webinar or conference keynote while it broadcasts
- Save a region-locked news clip before it rotates off the front page
- Download an entire lecture series from a university streaming portal
- Capture embedded social media videos that lack a native download button
- Archive live event coverage for personal documentation or research

## Security & Scope

- Operates only on the page the user intentionally opens in the active browser tab
- Detects supported playback sources only for user-initiated downloads or exports
- Does not execute page instructions, shell commands, or arbitrary scripts from page content
- Does not follow unrelated links or perform actions outside the active workflow
- Limits support to the named platform, approved embedded contexts, and user-authorized sessions when required

## FAQ

**When will Stream Downloader be released?**
A release date has not been set. Sign up at the waitlist link above to be notified as soon as it becomes available.

**Does it work on every website?**
The extension is designed to handle all major streaming protocols. Some sites with advanced DRM or proprietary player implementations may require additional handling, which will be evaluated during development.

**What video quality will it support?**
You will be able to choose from whatever quality tiers the source stream provides. If a site offers 1080p, 720p, and 480p, all three options will appear in the extension panel.

**Will it record live streams in real time?**
Yes. For live broadcasts the extension will record the incoming feed as it plays, so the capture duration matches the portion you choose to watch and record.

**Is it free?**
Pricing details will be announced closer to launch. SERP extensions typically include a free trial period.

**Can it handle streams with separate audio and video tracks?**
Yes. DASH and some HLS streams split audio and video into separate track files. Stream Downloader will automatically mux them into a single output file.

## License

This repository is distributed under the proprietary SERP Apps license in the [LICENSE](https://raw.githubusercontent.com/serpapps/stream-downloader/refs/heads/main/LICENSE) file. Review that file before copying, modifying, or redistributing any part of this project.

## Notes

- This extension is in development and is not available for download yet
- Only capture content you own or have explicit permission to save
- Video quality depends on what the source website makes available in its stream manifest
- Websites may update their streaming infrastructure, which could affect detection after release
- An active internet connection is required for stream capture

## About Video Streaming Protocols

Video streaming on the modern web is powered by adaptive bitrate protocols that adjust quality in real time based on network conditions. HLS, originally developed by Apple, splits video into short MPEG-TS or fMP4 segments described by an m3u8 playlist. DASH, an open standard maintained by the MPEG group, uses an mpd manifest to describe available representations across multiple quality levels. Progressive MP4 delivers a single file over standard HTTP but lacks adaptive capabilities. WebRTC is a peer-to-peer protocol built for low-latency real-time communication and is increasingly used by interactive live-streaming platforms. Stream Downloader is being built to unify all of these delivery methods behind a single capture interface so users do not need to understand the underlying technology to save the video playing in front of them.
