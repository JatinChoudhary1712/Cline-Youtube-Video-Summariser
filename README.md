# Cline- 🎥 YouTube Video Summarizer

A modern web application that automatically generates concise bullet-point summaries of YouTube videos using AI. Built with Flask and OpenAI's GPT-4.

## ✨ Features

- 🎯 Extract transcripts from any YouTube video
- 🤖 Generate AI-powered summaries using GPT-4
- 🌐 Clean, responsive web interface
- 📱 Mobile-friendly design
- ⚡ Real-time processing
- 🔒 Secure API key handling

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, TailwindCSS, JavaScript
- **AI**: OpenAI GPT-4
- **APIs**: SearchAPI.io (for YouTube transcript extraction)

## 📋 Prerequisites

- Python 3.7 or higher
- SearchAPI.io API key
- OpenAI API key

## 🚀 Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/youtube-summarizer.git
cd youtube-summarizer
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your API keys
```env
SEARCHAPI_KEY=your_searchapi_key
OPENAI_API_KEY=your_openai_key
```

## 💻 Usage

1. Start the Flask server
```bash
python app.py
```

2. Open your browser and navigate to `http://localhost:5000`
3. Enter a YouTube URL and click "Generate Summary"
4. View your AI-generated bullet-point summary

## 📁 Project Structure
