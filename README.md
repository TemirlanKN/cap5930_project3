# Audio Processing Web Application with Sentiment Analysis

## Overview

A Flask-based web application that provides real-time audio recording, transcription, and sentiment analysis using Google Cloud's Vertex AI. The application allows users to record audio through their browser and receive both transcription and sentiment analysis results.

## Features

- **Real-time Audio Recording**: Browser-based audio capture using MediaRecorder API
- **Transcription Service**: Converts speech to text using Vertex AI
- **Sentiment Analysis**: Analyzes the emotional content of the speech
- **File Management**: Stores and manages audio files and analysis results
- **Interactive UI**: Clean, responsive interface with real-time recording timer
- **Results History**: View and manage previous recordings and their analyses

## Tech Stack

### Backend

- Python 3.11+
- Flask 3.0.3
- Google Cloud Vertex AI
- Google Cloud Speech-to-Text
- Google Cloud Storage
- Google Cloud Language API

### Frontend

- HTML5/CSS3
- JavaScript (MediaRecorder API)
- Responsive Design
- Browser Audio API

## Project Structure

```
cap5930_project3/
├── main.py                  # Flask application core
├── requirements.txt         # Python dependencies
├── Dockerfile              # Container configuration
├── static/
│   └── script.js           # Frontend JavaScript
├── templates/
│   └── index.html          # Main web interface
└── uploads/                # Stored audio files and results
```

## Setup Instructions

### Prerequisites

1. Python 3.11 or higher
2. Google Cloud Account with enabled APIs:
   - Vertex AI
   - Cloud Storage
   - Cloud Language

### Local Development

1. Clone the repository

```bash
git clone [repository-url]
cd cap5930_project3
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Set up Google Cloud credentials

```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/credentials.json"
```

4. Run the application

```bash
python main.py
```

5. Access at `http://localhost:8080`

### Docker Deployment

```bash
docker build -t audio-processing-app .
docker run -p 8080:8080 audio-processing-app
```

## API Endpoints

- `GET /`: Main application interface
- `POST /upload`: Handle audio file uploads
- `GET /uploads/<filename>`: Serve stored files

## Usage Guide

1. Click "Record an Audio" in the sidebar
2. Press the "Record" button to start recording
3. Speak into your microphone
4. Press "Stop" to end recording
5. Wait for processing (transcription and sentiment analysis)
6. View results in the browser

## Environment Variables

- `PORT`: Server port (default: 8080)
- `GOOGLE_APPLICATION_CREDENTIALS`: Path to GCP credentials
- `FLASK_ENV`: Development/Production mode

## Security Considerations

- Audio files are stored securely
- Google Cloud credentials are protected
- Input validation for file uploads
- Secure file serving implementation

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to branch
5. Submit a pull request

## License

MIT License

## Acknowledgments

- Google Cloud Platform
- Flask Framework
- Web Audio API Contributors
