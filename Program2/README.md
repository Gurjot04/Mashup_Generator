# 🌐 Program 2 - Web-Based Mashup Generator

## 📌 Project Description
This is a web-based mashup generator built using Flask.  
The user provides:

- Singer Name
- Number of Videos
- Duration (in seconds)
- Email Address

The application:
1. Downloads songs from YouTube
2. Creates a mashup
3. Compresses the output into a ZIP file
4. Sends the ZIP file to the user via email

Singer Tested: **Diljit Dosanjh**

---

## ⚙️ Technologies Used
- Python 3.9+
- Flask (Web Framework)
- yt-dlp (YouTube Downloading)
- pydub (Audio Processing)
- FFmpeg (Audio Conversion)
- smtplib (Email Sending)
- zipfile (File Compression)

---


conda create -n mashup_env python=3.10
conda activate mashup_env
