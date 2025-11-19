"""
Generated Code Metadata:
========================
Original URL: https://mplas.com.br
Prompt: Generate a REST API documentation for a simple file hosting service that allows listing files, uploading, and downloading.
Generated: DETERMINISTIC_aff5db8dfc500f6a
Batch ID: 20250622_205541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
REST API Documentation for a Simple File Hosting Service

Endpoints:
1. GET /files - List all files
2. POST /upload - Upload a file
3. GET /download/<filename> - Download a file

This API is built using Flask and assumes files are stored in a directory called 'uploads'.
"""

from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# Directory to store uploaded files
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure the upload folder exists
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions for upload
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    """
    Check if the file has an allowed extension.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/files', methods=['GET'])
def list_files():
    """
    List all files in the upload directory.
    Returns:
        JSON response containing a list of filenames.
    """
    try:
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        return jsonify({'files': files}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Upload a file to the server.
    Request:
        Multipart form-data with a file field.
    Returns:
        JSON response indicating success or failure.
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        try:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return jsonify({'message': f'File {filename} uploaded successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'File type not allowed'}), 400

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    """
    Download a file from the server.
    Parameters:
        filename (str): Name of the file to download.
    Returns:
        The requested file or an error message.
    """
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True), 200
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
