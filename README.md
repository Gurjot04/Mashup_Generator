# 🎵 Mashup Generator Project

## 📌 Overview

This project implements a Mashup Generator in two different ways:

1. **Program 1 – Command Line Based Mashup Generator**
2. **Program 2 – Web-Based Mashup Generator**

Both programs automate the process of downloading songs from YouTube, extracting audio, trimming clips, and generating a final mashup file.

The project demonstrates practical implementation of Python-based multimedia processing and web service development.

---

# 🔹 Program 1 – Command Line Mashup Generator

## Description

Program 1 is a command line application that:

- Downloads multiple YouTube videos of a specified singer
- Extracts audio from the downloaded videos
- Trims the first *Y* seconds from each audio file
- Merges all trimmed clips into a single mashup file

The program validates user inputs and handles possible execution errors gracefully.

## Key Features

- Dynamic singer selection
- Input validation (number of videos and duration)
- Exception handling
- Automatic audio merging
- Single output mashup file generation

---

# 🔹 Program 2 – Web-Based Mashup Generator

## Description

Program 2 is a web application developed using Flask.  
It provides a user-friendly interface where users can enter:

- Singer Name  
- Number of Videos  
- Duration (in seconds)  
- Email Address  

After submission, the system:

1. Downloads the requested number of songs
2. Generates a mashup file
3. Compresses the output into a ZIP file
4. Sends the ZIP file to the user via email

## Key Features

- Web-based user interface
- Automated mashup creation
- ZIP file generation
- Email delivery support
- Backend processing using Python

---

# 🛠 Technologies Used

- Python
- Flask
- yt-dlp (YouTube downloading)
- pydub (Audio processing)
- FFmpeg (Audio conversion support)
- smtplib (Email service integration)

---


# 📂 Repository Structure

Mashup_Generator/
│
├── Program1/
│   ├── 102317269.py
│   ├── README.md
│
├── Program2/
│   ├── app.py
│   ├── README.md
│
└── README.md

