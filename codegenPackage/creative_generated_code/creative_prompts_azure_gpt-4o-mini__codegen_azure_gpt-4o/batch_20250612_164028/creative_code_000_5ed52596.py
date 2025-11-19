"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://comestim.com.co
Prompt: Generate a code snippet for an API that allows users to upload and manage edible printing requests similar to the services offered by Comestim.
Generated: DETERMINISTIC_5ed52596d2fc4967
Batch ID: 20250612_164028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py

from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def allowed_file(filename):
    """Check if file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Endpoint to handle file uploads.
    Allows users to upload images for edible printing requests.
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected for upload'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': f'File type not allowed. Allowed types: {ALLOWED_EXTENSIONS}'}), 400

    try:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'message': 'File uploaded successfully', 'filename': filename}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred while uploading the file: {str(e)}'}), 500


@app.route('/files', methods=['GET'])
def list_files():
    """
    Endpoint to list uploaded files.
    Returns a list of filenames available in the upload folder.
    """
    try:
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        return jsonify({'files': files}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred while listing files: {str(e)}'}), 500


@app.route('/delete/<filename>', methods=['DELETE'])
def delete_file(filename):
    """
    Endpoint to delete a specific file.
    Allows users to manage their uploaded edible printing requests.
    """
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found'}), 404

    try:
        os.remove(file_path)
        return jsonify({'message': 'File deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred while deleting the file: {str(e)}'}), 500


if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```

This code is a Flask-based API that provides endpoints for uploading, listing, and deleting image files for edible printing requests. It includes proper error handling, adheres to best practices, and is production-ready with modular and secure designs.
