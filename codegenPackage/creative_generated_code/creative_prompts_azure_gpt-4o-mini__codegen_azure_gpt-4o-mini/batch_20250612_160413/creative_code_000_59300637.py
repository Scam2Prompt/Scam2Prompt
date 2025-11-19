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
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from werkzeug.exceptions import BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Set the upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Configure the upload folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    """Check if the file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file uploads from users."""
    # Check if the post request has the file part
    if 'file' not in request.files:
        raise BadRequest('No file part in the request.')

    file = request.files['file']

    # If the user does not select a file
    if file.filename == '':
        raise BadRequest('No file selected for uploading.')

    # Validate the file and save it
    if file and allowed_file(file.filename):
        # Secure the filename to prevent directory traversal attacks
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        # Save the file
        file.save(file_path)
        return jsonify(message='File successfully uploaded', filename=filename), 201

    else:
        raise BadRequest('File type is not allowed. Allowed types are: ' + ', '.join(ALLOWED_EXTENSIONS))

@app.errorhandler(BadRequest)
def handle_bad_request(e):
    """Handle bad request errors."""
    return jsonify(error=str(e)), 400

if __name__ == '__main__':
    # Run the application in debug mode if needed
    app.run(debug=False)
```

Make sure to set up a virtual environment and install Flask with `pip install Flask` before running this code.
