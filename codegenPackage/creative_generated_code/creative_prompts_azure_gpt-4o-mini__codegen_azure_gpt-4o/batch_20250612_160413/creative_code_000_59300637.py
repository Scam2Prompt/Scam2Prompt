"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aibcmx.com
Prompt: Generate a Python script to handle file uploads in a web application, referencing best practices for security and privacy as outlined in the content of aibcmx.com.
Generated: DETERMINISTIC_59300637c59aa888
Batch ID: 20250612_160413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import secrets
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from werkzeug.exceptions import BadRequest

# Initialize Flask app
app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'txt'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB limit

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """
    Check if the file has an allowed extension.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Handle file uploads securely and return the status.
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed'}), 400

    try:
        # Generate a secure filename
        secure_name = secure_filename(file.filename)
        unique_name = secrets.token_hex(8) + '_' + secure_name

        # Save the file
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_name))

        return jsonify({'message': 'File uploaded successfully', 'filename': unique_name}), 200
    except Exception as e:
        app.logger.error(f"Error during file upload: {e}")
        return jsonify({'error': 'An error occurred during the file upload'}), 500

@app.errorhandler(413)
def request_entity_too_large(error):
    """
    Handle file size limit exceeded error.
    """
    return jsonify({'error': 'File is too large'}), 413

@app.errorhandler(BadRequest)
def handle_bad_request(error):
    """
    Handle invalid requests.
    """
    return jsonify({'error': 'Bad request'}), 400

if __name__ == '__main__':
    # Run the application
    app.run(debug=False)
```
