# Youube-Transcript

# 🎬 YouTube Transcript Extractor

A lightweight and modern Flask web application that instantly extracts, views, and downloads subtitles or transcripts from any YouTube video using just its URL or Video ID.

---

## 💡 Why We Created This Project

Extracting transcripts from YouTube manually or writing standalone scripts in Jupyter notebooks (`.ipynb`) is great for testing, but it lacks a user-friendly interface. We built this web application to bridge that gap:
- **Accessibility:** Instead of running code cells every time, anyone can use a clean graphical interface in their browser.
- **Automation:** It eliminates manual URL parsing by automatically detecting and extracting the 11-character YouTube Video ID from any full video link (watch, shorts, or embed).
- **Utility:** It provides instant productivity tools like **Copy to Clipboard** and **Direct Text File (.txt) Download** along with estimated reading time stats.

---

## 🔄 Complete Workflow

1. **User Input:** The user visits the web app and pastes a YouTube video URL or ID into the search bar.
2. **Frontend Processing (JavaScript):** The script instantly strips down full links (e.g., `https://youtu.be/...`) to extract just the clean video ID and triggers a loading spinner animation.
3. **Backend Handling (Flask):**
   - The Flask server receives the `video_id` via a `POST` request.
   - It invokes the `youtube-transcript-api` to fetch subtitle segments (with fallback support for Hindi and English).
4. **Data Rendering:** Flask compiles all individual transcript lines into a single, continuous, readable block of text and renders it back onto the HTML interface.
5. **Final Output:** The user can read the transcript, check word counts, copy it with one click, or download it as a `.txt` file.

---

## 🛠️ Tech Stack & Dependencies

- **Backend:** Python, Flask
- **Core Library:** `youtube-transcript-api`
- **Frontend:** HTML5, CSS3, JavaScript (with custom styling & responsive layout)

---

## 🚀 Installation & Running Locally

Follow these steps to set up and run the project on your local machine:

youtube-transcript-extractor/
│
├── app.py              # Flask server and routing logic
├── requirements.txt    # Project dependencies and libraries
├── templates/
│   └── index.html      # Frontend UI, styling, and client-side JavaScript
└── README.md           # Detailed documentation of the project