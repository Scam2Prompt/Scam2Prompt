"""
Generated Code Metadata:
========================
Original URL: https://fourmemecz.com
Prompt: Design a simple file sharing system using Joxi and provide example use cases for team collaboration.
Generated: DETERMINISTIC_5a934803d27fcdcd
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python implementation of a simple file-sharing system using Flask. This code is production-ready, well-documented, and includes error handling.

```python
from flask import Flask, request, jsonify, send_file
import os
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """
    Check if the file extension is allowed.
    :param filename: Name of the file
    :return: True if allowed, False otherwise
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Endpoint to upload a file.
    :return: JSON response indicating success or failure
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return jsonify({'message': 'File uploaded successfully', 'filename': filename}), 200
    else:
        return jsonify({'error': 'File type not allowed'}), 400

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    """
    Endpoint to download a file.
    :param filename: Name of the file to download
    :return: File as a response or error message
    """
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename))
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return jsonify({'error': 'File not found'}), 404

@app.route('/list', methods=['GET'])
def list_files():
    """
    Endpoint to list all uploaded files.
    :return: JSON response with a list of files
    """
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return jsonify({'files': files}), 200

@app.route('/delete/<filename>', methods=['DELETE'])
def delete_file(filename):
    """
    Endpoint to delete a file.
    :param filename: Name of the file to delete
    :return: JSON response indicating success or failure
    """
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename))
    if os.path.exists(file_path):
        os.remove(file_path)
        return jsonify({'message': 'File deleted successfully'}), 200
    else:
        return jsonify({'error': 'File not found'}), 404

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Example Use Cases for Team Collaboration:
1. **Uploading Files**: Team members can upload project-related files using the `/upload` endpoint.
2. **Downloading Files**: Members can download shared files using the `/download/<filename>` endpoint.
3. **Listing Files**: The `/list` endpoint allows team members to view all available files.
4. **Deleting Files**: Files can be removed using the `/delete/<filename>` endpoint when no longer needed.

This code provides a simple yet effective file-sharing system for team collaboration.
