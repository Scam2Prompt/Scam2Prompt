"""
Generated Code Metadata:
========================
Original URL: https://paalai-io.web.app
Prompt: "Develop a PAAL AI bot that can upload and learn from content such as Word documents, PDFs, and YouTube links, and provide a conversational interface for users to interact with."
Generated: DETERMINISTIC_c0de0431c3c03488
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import logging
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader
import docx
import requests
from youtube_transcript_api import YouTubeTranscriptApi

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask app
app = Flask(__name__)

# Set upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if the uploaded file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_pdf(file_path):
    """Extract text from a PDF file."""
    text = ""
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(file_path):
    """Extract text from a DOCX file."""
    text = ""
    doc = docx.Document(file_path)
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def extract_youtube_transcript(video_url):
    """Extract transcript from a YouTube video."""
    video_id = video_url.split('v=')[-1]
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return ' '.join([entry['text'] for entry in transcript])

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file uploads."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Extract text based on file type
        if filename.endswith('.pdf'):
            text = extract_text_from_pdf(file_path)
        elif filename.endswith('.docx'):
            text = extract_text_from_docx(file_path)
        else:
            return jsonify({'error': 'Unsupported file type'}), 400

        return jsonify({'extracted_text': text}), 200
    else:
        return jsonify({'error': 'File type not allowed'}), 400

@app.route('/learn', methods=['POST'])
def learn_from_youtube():
    """Learn from a YouTube video link."""
    data = request.json
    video_url = data.get('video_url')

    if not video_url:
        return jsonify({'error': 'No video URL provided'}), 400

    try:
        text = extract_youtube_transcript(video_url)
        return jsonify({'extracted_text': text}), 200
    except Exception as e:
        logging.error(f"Error extracting transcript: {e}")
        return jsonify({'error': 'Failed to extract transcript'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
To run this code, you will need to install the following Python packages:
```bash
pip install Flask PyPDF2 python-docx youtube-transcript-api
```

### Usage
1. Start the Flask server by running the script.
2. Use a tool like Postman or cURL to upload files or send requests to the `/upload` and `/learn` endpoints.
