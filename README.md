# Audio Processing Web Application

This project is a Flask-based web application for recording, uploading, and processing audio files. The application uses Google Cloud's Vertex AI Generative Models to transcribe audio and perform sentiment analysis.

## Features

- **Record Audio**: Record audio directly from the browser.
- **Upload Audio**: Upload `.wav` audio files for processing.
- **Transcription**: Generate transcriptions of uploaded audio.
- **Sentiment Analysis**: Analyze the sentiment of the audio content.
- **Results Display**: View transcription and sentiment analysis results in the browser.
- **Downloadable Results**: Save the processed results as text files.

## Technology Stack

- **Backend**: Flask
- **Frontend**: HTML, CSS, JavaScript
- **Cloud Services**: Google Cloud Vertex AI Generative Models

## Installation

### Prerequisites

- Python 3.8 or higher
- Google Cloud project with Vertex AI enabled
- `keys/` folder containing your Google Cloud service account key

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your Google Cloud service account key to the `keys/` folder.

5. Create a `.env` file for environment variables:
   ```
   GOOGLE_APPLICATION_CREDENTIALS=keys/your-service-account-key.json
   FLASK_ENV=production
   ```

6. Start the Flask application:
   ```bash
   python main.py
   ```

7. Open the application in your browser:
   ```
   http://127.0.0.1:8080
   ```

## Deployment

This application is designed to be deployed on **Google Cloud Run**. Follow these steps to deploy:

1. **Authenticate with Google Cloud:**
   ```bash
   gcloud auth login
   gcloud config set project your-project-id
   ```

2. **Build the Docker Image:**
   ```bash
   gcloud builds submit --tag gcr.io/your-project-id/audio-processing-app
   ```

3. **Deploy to Cloud Run:**
   ```bash
   gcloud run deploy audio-processing-app \
       --image gcr.io/your-project-id/audio-processing-app \
       --platform managed \
       --region us-central1 \
       --allow-unauthenticated
   ```

4. **Access the Application:**
   Use the URL provided by Cloud Run to access your application.

## File Structure

```
project-folder
│
├── main.py                  # Flask application
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker configuration for deployment
├── templates/               # HTML templates
│   └── index.html
├── static/                  # Static files (CSS, JS)
│   ├── style.css
│   └── script.js
├── uploads/                 # Uploaded audio files and results
└── keys/                    # Google Cloud service account key (ignored by Git)
```

## Usage

1. Record or upload audio files using the web interface.
2. View the transcription and sentiment analysis results.
3. Download the results for further use.

## Environment Variables

The application uses the following environment variables:

- `GOOGLE_APPLICATION_CREDENTIALS`: Path to the Google Cloud service account key.
- `FLASK_ENV`: Set to `production` or `development`.

## Security

- Ensure that the `keys/` folder and sensitive files are included in `.gitignore`.
- Do not expose your Google Cloud credentials in the repository.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- Google Cloud Vertex AI
- Flask Framework

