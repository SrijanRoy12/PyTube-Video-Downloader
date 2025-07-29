# 🎬 YouTube Video Downloader (1080p + Best Audio)

> ⚡ Effortlessly download Full HD YouTube videos with top-tier audio and real-time progress — all in a beginner-friendly Python tool.

---

## 🚀 Overview

Say goodbye to buffering and online converters.  
This Python-based utility uses `yt-dlp` to fetch **1080p video** and the **best available audio**, merges them seamlessly into a high-quality `.mp4`, and provides **real-time progress tracking**.  
Perfect for content collectors, educators, and productivity enthusiasts.

---

## ✨ Features

- 🎥 Downloads full **1080p HD video**
- 🎵 Fetches **highest quality audio**
- ⏳ Displays **live download progress + ETA**
- 🛠️ Auto-merges video/audio into a single **MP4 file**
- 🧰 Minimal setup, **clean & readable codebase**

---

## 📦 Requirements

Install `yt-dlp` using pip:

```bash
pip install yt-dlp
yt-dlp is a modern fork of youtube-dl with enhanced features and performance.

🧰 One-Time Setup for FFmpeg
FFmpeg is required to merge the downloaded video and audio into one .mp4 file.

🪟 Windows Installation Guide
Go to: 👉 https://www.gyan.dev/ffmpeg/builds/

Under “Release Builds”, download:
ffmpeg-release-essentials.zip

Extract the archive and rename the folder to:
ffmpeg

Move it to the root of your C: drive:
C:\ffmpeg

➕ Add FFmpeg to System PATH
Open Start Menu → Search: Environment Variables

Select ➤ Edit the system environment variables

Click ➤ Environment Variables

Under System Variables, find and select Path → Click Edit

Click ➕ New → Add:

makefile
Copy
Edit
C:\ffmpeg\bin
Click OK on all windows to save and apply the changes.

✅ Verify Installation
Open CMD or terminal and run:

bash
Copy
Edit
ffmpeg -version
If correctly installed, you’ll see:

nginx
Copy
Edit
ffmpeg version 6.x ...
💡 Why This Project?
This isn’t a huge framework — it's a practical time-saving tool.
Whether you're a Python beginner or just tired of browser-based downloaders, this simple script does the job beautifully.

💡 Ideas for Extension
Add GUI with Tkinter or PyQt

Support YouTube Playlists

Allow custom resolutions

Integrate download history

🛠️ Built With
yt-dlp — For video/audio extraction

FFmpeg — For merging media streams
