"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toshowbiz.com
Prompt: Describe the process of uploading a RAR or ZIP file for extraction using an online service that guarantees privacy and speed.
Generated: DETERMINISTIC_750a9a4edf4ad7ef
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import zipfile
import rarfile
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

# Flask web application setup
app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'  # Folder to store uploaded files
EXTRACT_FOLDER = 'extracted'  # Folder to store extracted files
ALLOWED_EXTENSIONS = {'zip', 'rar'}  # Allowed file extensions
MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # Maximum file size: 100MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['EXTRACT_FOLDER'] = EXTRACT_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(EXTRACT_FOLDER, exist_ok=True)


def allowed_file(filename):
    """Check if the uploaded file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def extract_file(file_path, destination):
    """
    Extract a ZIP or RAR file to the specified destination.
    Supports ZIP and RAR file formats.
    """
    try:
        if file_path.endswith('.zip'):
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(destination)
        elif file_path.endswith('.rar'):
            with rarfile.RarFile(file_path, 'r') as rar_ref:
                rar_ref.extractall(destination)
        else:
            raise ValueError("Unsupported file format.")
    except Exception as e:
        raise RuntimeError(f"Error extracting file: {e}")


@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Handle file upload and extraction.
    Responds with success or error status.
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request."}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected."}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "Unsupported file format. Only ZIP and RAR are allowed."}), 400

    try:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Extract the file
        extract_destination = os.path.join(app.config['EXTRACT_FOLDER'], filename.rsplit('.', 1)[0])
        os.makedirs(extract_destination, exist_ok=True)
        extract_file(file_path, extract_destination)

        return jsonify({"message": "File uploaded and extracted successfully.", "extracted_to": extract_destination}), 200

    except Exception as e:
        return jsonify({"error": f"Failed to process the file: {str(e)}"}), 500


@app.errorhandler(413)
def request_entity_too_large(error):
    """Handle file size exceeding the limit."""
    return jsonify({"error": "File size exceeds the maximum limit of 100MB."}), 413


if __name__ == '__main__':
    app.run(debug=False)
```
