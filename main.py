from flask import Flask, render_template, request, jsonify, send_from_directory
from vertexai.generative_models import GenerativeModel, Part
import vertexai
import os
from datetime import datetime
import logging, base64

logging.basicConfig(level=logging.DEBUG)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'wav'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

vertexai.init(project="cap5930-project-3", location="us-central1")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_uploaded_audio(file_path, file_name):
    try:
        logging.debug(f"Processing file: {file_name} at {file_path}")

        model = GenerativeModel("gemini-1.5-flash-002")

        with open(file_path, "rb") as audio_file:
            audio_data = base64.b64encode(audio_file.read()).decode('utf-8')

        audio_part = Part.from_data(mime_type="audio/wav", data=base64.b64decode(audio_data))
        promt = "Please provide a transcription of the audio followed by an analysis of the sentiment in the format: 'Transcription: [...] Sentiment Analysis: [...]'."
        response = model.generate_content(
            [audio_part, promt],
            generation_config={"temperature": 0.7, "max_output_tokens": 1024},
            safety_settings=[]
        )
        logging.debug(f"Raw response: {response.text}")

        if hasattr(response, "text") and response.text:
            result_text = response.text
        else:
            raise ValueError("No valid response received from the generative model.")

        transcript = "Transcript not available"
        sentiment = "Sentiment analysis not available"
        if "Transcription:" in result_text:
            transcript = result_text.split("Transcription:")[1].split("Sentiment Analysis:")[0].strip()
        if "Sentiment Analysis:" in result_text:
            sentiment = result_text.split("Sentiment Analysis:")[1].strip()

        results_path = os.path.splitext(file_path)[0] + "_results.txt"
        with open(results_path, 'w') as results_file:
            results_file.write(f"File: {file_name}\n\n")
            results_file.write(f"**Transcription:**\n{transcript}\n\n")
            results_file.write(f"**Sentiment Analysis:**\n{sentiment}\n")

        logging.debug(f"Results saved to: {results_path}")
        return results_path

    except Exception as e:
        logging.error(f"Error processing file {file_name}: {e}")
        return None

@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    files = [f for f in files if allowed_file(f)]
    files.sort(reverse=True)
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_audio():
    if 'audio_data' not in request.files:
        return jsonify({'error': 'No audio data in the request.'}), 400

    file = request.files['audio_data']
    if file and allowed_file(file.filename):
        filename = datetime.now().strftime("%Y%m%d-%I%M%S%p") + '_stt.wav'
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        logging.debug(f"File saved at: {file_path}")

        results_path = process_uploaded_audio(file_path, filename)

        if results_path:
            return jsonify({
                'file': filename,
                'results': os.path.basename(results_path)
            })
        else:
            return jsonify({'error': 'Processing failed'}), 500
    else:
        return jsonify({'error': 'Invalid file type'}), 400

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
