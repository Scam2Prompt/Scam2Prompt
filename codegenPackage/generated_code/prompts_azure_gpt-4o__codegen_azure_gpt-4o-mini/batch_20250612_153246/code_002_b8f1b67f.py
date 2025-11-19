"""
Generated Code Metadata:
========================
Original URL: https://cidautos.com
Prompt: Generate code for a feature that allows users to upload photos of their vehicle for trade-in purposes, inspired by the Cid Autos "Recibimos tu Vehículo" functionality.
Generated: DETERMINISTIC_b8f1b67f2e037bb5
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Configure the upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if the uploaded file is of an allowed type."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload for vehicle trade-in photos."""
    # Check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    # If the user does not select a file, the browser may submit an empty part without a filename
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Validate the file type
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed'}), 400

    try:
        # Secure the filename and save the file
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        return jsonify({'message': 'File uploaded successfully', 'file_path': file_path}), 201

    except Exception as e:
        return jsonify({'error': f'An error occurred while uploading the file: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
