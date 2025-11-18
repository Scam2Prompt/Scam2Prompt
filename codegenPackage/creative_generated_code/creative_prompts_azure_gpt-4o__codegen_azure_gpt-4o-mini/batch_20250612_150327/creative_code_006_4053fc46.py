"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freeproxy.me
Prompt: Write code to implement a free online file storage service with proxy integration, inspired by FreeProxy.me's mention of Nexus Drive.
Generated: DETERMINISTIC_4053fc46e1d95106
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, request, jsonify, send_from_directory, abort
from werkzeug.utils import secure_filename

# Initialize the Flask application
app = Flask(__name__)

# Configuration for file uploads
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file uploads."""
    # Check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    # If the user does not select a file, the browser submits an empty file
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Validate the file
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Save the file
        try:
            file.save(file_path)
            return jsonify({"message": "File uploaded successfully!", "filename": filename}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return jsonify({"error": "File type is not allowed"}), 400

@app.route('/files/<filename>', methods=['GET'])
def get_file(filename):
    """Serve the uploaded files."""
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

@app.route('/files', methods=['GET'])
def list_files():
    """List all uploaded files."""
    try:
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        return jsonify({"files": files}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

This code implements a simple file upload service using Flask, with endpoints for uploading files, retrieving them, and listing all uploaded files. It includes error handling for common scenarios and ensures uploaded files are saved securely.
