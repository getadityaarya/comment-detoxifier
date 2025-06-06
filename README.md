# 🧠 comment-detoxifier
A machine learning-powered web application that detects and manages toxic comments on YouTube videos. This project uses trained NLP models to classify comments and optionally delete toxic ones using the YouTube Data API.

## 🔍 Features

- 🔗 Connects to YouTube using video ID
- 🧾 Fetches top-level comments from the video
- 🧠 Classifies comments as **Toxic** or **Non-Toxic**
- 🗑️ Deletes toxic comments using authenticated API (OAuth 2.0)
- 🌐 Web interface built with Flask & FastAPI backend
- 🧪 Includes testing and multiple deployment options

## 📦 Tech Stack

- Python, Flask, FastAPI
- Scikit-learn (for the ML model)
- Google YouTube Data API v3
- OAuth 2.0 (for comment deletion)
- HTML/CSS (frontend)

## 📁 Project Structure

```
youtube-toxic-detector/
│
├── backend.py                  # FastAPI-based API for ML and YouTube integration
├── Connect.py                  # Flask-based app for interactive use
├── test_api.py                 # Script to test comment fetching
├── model1.ipynb                # Notebook used for model training
├── predictor.ipynb             # Additional notebook for prediction experiments
├── toxic_comment_classifier.pkl # Trained classification model
├── client_secret_*.json        # Google OAuth client secret file
├── templates/
│   └── index.html              # HTML UI
├── README.md                   # Project documentation
└── requirements.txt            # Python dependencies
```

## 🚀 How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/youtube-toxic-detector.git
   cd youtube-toxic-detector
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Flask App**
   ```bash
   python Connect.py
   ```

5. **Run FastAPI (optional)**
   ```bash
   uvicorn backend:app --reload
   ```

6. **Open the Web Interface**
   - Navigate to `http://127.0.0.1:5000` (Flask)
   - Or for API use: `http://127.0.0.1:8000` (FastAPI)

🧪 Example
Enter a YouTube video ID (e.g., CC2VWC2uKXU) into the form and the app will fetch, analyze, and display whether each comment is Toxic 🚨 or Non-Toxic ✅.

🛡️ Disclaimer
This project is intended strictly for educational and research purposes. If you use the comment deletion feature, ensure you are properly authenticated using your own YouTube OAuth credentials and have the right permissions.

📬 Contact
If you have any questions, suggestions, or would like to collaborate, feel free to reach out via email at getadityaarya@gmail.com or connect on GitHub.
