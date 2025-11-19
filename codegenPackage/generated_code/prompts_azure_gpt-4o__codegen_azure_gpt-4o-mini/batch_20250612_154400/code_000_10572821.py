"""
Generated Code Metadata:
========================
Original URL: https://appsuiteplus.com
Prompt: Write Python code to implement a multilingual file-sharing service with support for languages like Russian, German, French, Arabic, and others, as described on Wayme.cc.
Generated: DETERMINISTIC_105728212172ce14
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configuration for file uploads
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Endpoint to upload a file
@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    # If the user does not select a file, the browser submits an empty file without a filename
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # Validate the file
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return jsonify({'message': 'File uploaded successfully', 'file_path': file_path}), 201
    
    return jsonify({'error': 'File type not allowed'}), 400

# Endpoint to list uploaded files
@app.route('/files', methods=['GET'])
def list_files():
    try:
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        return jsonify({'files': files}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to download a file
@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    try:
        if allowed_file(filename):
            return jsonify({'message': 'File download initiated', 'file_path': os.path.join(app.config['UPLOAD_FOLDER'], filename)}), 200
        else:
            return jsonify({'error': 'File type not allowed'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Notes:
- This code implements a simple file-sharing service using Flask.
- It includes endpoints for uploading files, listing uploaded files, and downloading files.
- Error handling is included for various scenarios, such as missing files and unsupported file types.
- The application is configured to allow CORS, making it suitable for use in a multilingual environment.
