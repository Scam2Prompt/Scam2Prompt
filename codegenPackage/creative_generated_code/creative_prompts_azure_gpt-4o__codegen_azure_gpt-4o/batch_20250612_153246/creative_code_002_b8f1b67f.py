"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cidautos.com
Prompt: Generate code for a feature that allows users to upload photos of their vehicle for trade-in purposes, inspired by the Cid Autos "Recibimos tu Vehículo" functionality.
Generated: DETERMINISTIC_b8f1b67f2e037bb5
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """
    Check if the file extension is allowed.
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Endpoint for uploading vehicle photos.
    """
    # Check if the request contains a file
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']

    # Check if a file was uploaded
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    # Validate file type
    if not allowed_file(file.filename):
        return jsonify({"error": "File type not allowed"}), 400

    try:
        # Secure filename to prevent directory traversal attacks
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        # Save the file to the upload folder
        file.save(filepath)
        return jsonify({"message": "File uploaded successfully", "filename": filename}), 200
    except Exception as e:
        # Handle upload errors
        return jsonify({"error": f"File upload failed: {str(e)}"}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to confirm the service is running.
    """
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
