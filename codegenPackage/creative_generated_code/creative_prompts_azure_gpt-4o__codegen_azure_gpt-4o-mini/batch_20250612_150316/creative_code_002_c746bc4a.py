"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jobbo.com.au
Prompt: Recommend an API or library to manage photo galleries for tractor pulling events, similar to the multiple galleries listed on jobbo.com.au.
Generated: DETERMINISTIC_c746bc4ae4b3ab09
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration for file uploads
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if the uploaded file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    """Endpoint to upload a photo for a gallery."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    
    file = request.files['file']
    
    # Check if the filename is empty
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # Validate file extension
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type is not allowed'}), 400
    
    # Secure the filename and save the file
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    
    return jsonify({'message': 'File uploaded successfully', 'file_path': file_path}), 201

@app.route('/gallery/<path:filename>', methods=['GET'])
def get_file(filename):
    """Endpoint to retrieve a photo from the gallery."""
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404

@app.route('/gallery', methods=['GET'])
def list_files():
    """Endpoint to list all photos in the gallery."""
    try:
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        return jsonify({'files': files}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
