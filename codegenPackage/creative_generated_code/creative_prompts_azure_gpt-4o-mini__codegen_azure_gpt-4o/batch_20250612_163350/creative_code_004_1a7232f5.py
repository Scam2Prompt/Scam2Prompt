"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binancebtc.epizy.com
Prompt: Illustrate how to manage unlimited disk space and bandwidth in a web application hosted on iFastNet.
Generated: DETERMINISTIC_1a7232f5015b87f7
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import os
from flask import Flask, request, send_from_directory, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Set a directory to store uploaded files
UPLOAD_FOLDER = 'uploaded_files'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure the directory exists
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Configuration to manage large file uploads
MAX_FILE_SIZE_MB = 100  # Example: Set max upload size to 100 MB per file
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE_MB * 1024 * 1024  # Convert MB to bytes

# Check and ensure 'unlimited' disk space is managed by external monitoring (pseudo-unlimited)
def check_disk_space():
    # Function to monitor disk usage and clean old files if required
    # Admin-defined policies can enforce file retention or cleanup
    disk_usage = os.statvfs(app.config['UPLOAD_FOLDER'])
    remaining_space = disk_usage.f_frsize * disk_usage.f_bavail
    if remaining_space < 1024 * 1024 * 100:  # Less than 100 MB remaining
        # Implement a cleanup policy (e.g., delete oldest files)
        delete_oldest_files(app.config['UPLOAD_FOLDER'])

def delete_oldest_files(directory, num_files=10):
    # Deletes the oldest 'num_files' in the specified directory
    files = sorted(
        (os.path.join(directory, f) for f in os.listdir(directory)),
        key=os.path.getctime
    )
    for file in files[:num_files]:
        os.remove(file)

# Route to upload a file
@app.route('/upload', methods=['POST'])
def upload_file():
    check_disk_space()  # Ensure there's sufficient space before accepting new uploads
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'}), 400
    try:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        return jsonify({'message': 'File uploaded successfully', 'filename': file.filename}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to download a file
@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404

# Route to list all files stored on the server
@app.route('/files', methods=['GET'])
def list_files():
    try:
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        return jsonify({'files': files}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main entry point of the server
if __name__ == '__main__':
    # Ensure the application is run in a production-ready WSGI server
    app.run(host='0.0.0.0', port=5000, debug=False)
```
