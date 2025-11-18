"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autoswiftly.com
Prompt: Create an API endpoint for uploading identification documents securely during the car buying process, inspired by AutoSwiftly's ID uploader feature.
Generated: DETERMINISTIC_3ad1bc95f1c3ee5a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configuration for file uploads
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}
MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # Limit file size to 5MB

# Set app configurations
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Helper function to check allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# API endpoint for uploading identification documents
@app.route('/upload-id', methods=['POST'])
def upload_id_document():
    try:
        # Check if a file is provided in the request
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'}), 400
        
        file = request.files['file']
        
        # Check if a file is selected
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        
        # Validate file type
        if not allowed_file(file.filename):
            return jsonify({'error': 'File type not allowed. Allowed types: png, jpg, jpeg, pdf'}), 400
        
        # Secure the filename
        filename = secure_filename(file.filename)
        
        # Generate a unique filename with timestamp to avoid collisions
        unique_filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{filename}"
        
        # Save the file to the upload folder
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))
        
        return jsonify({'message': 'File uploaded successfully', 'filename': unique_filename}), 200

    except Exception as e:
        # Handle any unexpected errors
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Error handler for files exceeding the size limit
@app.errorhandler(413)
def request_entity_too_large(error):
    return jsonify({'error': 'File is too large. Maximum allowed size is 5MB'}), 413

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
