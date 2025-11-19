"""
Generated Code Metadata:
========================
Original URL: https://thebookkeepingdiaries.com
Prompt: Generate a code snippet for a web application that allows users to upload their financial documents securely, reflecting the services offered by The Bookkeeping Diaries.
Generated: DETERMINISTIC_cb4cfc720d7e4c16
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import os
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename

# Initialize Flask application
app = Flask(__name__)

# Configuration for file uploads
UPLOAD_FOLDER = 'uploads'  # Directory where files will be stored
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'xls', 'xlsx'}  # Allowed file types
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Maximum file size: 16 MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """
    Check if the uploaded file has an allowed extension.
    :param filename: Name of the file
    :return: True if the file extension is allowed, False otherwise
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """
    Render the homepage with the file upload form.
    """
    return render_template('index.html')  # Assumes an 'index.html' template exists

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Handle file upload securely.
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    # Check if the user uploaded a file
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    # Validate file type
    if file and allowed_file(file.filename):
        try:
            # Secure the filename to prevent directory traversal attacks
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            # Save the file to the upload folder
            file.save(file_path)

            return jsonify({'message': 'File uploaded successfully', 'filename': filename}), 200
        except Exception as e:
            return jsonify({'error': f'An error occurred while uploading the file: {str(e)}'}), 500
    else:
        return jsonify({'error': 'File type not allowed'}), 400

@app.errorhandler(413)
def request_entity_too_large(error):
    """
    Handle file size limit exceeded error.
    """
    return jsonify({'error': 'File size exceeds the maximum limit of 16 MB'}), 413

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Ensure you have Flask installed (`pip install flask`) before running this code.
- Create an `index.html` file in a `templates` folder for the file upload form.
- This code is production-ready but should be deployed behind a secure web server (e.g., Nginx) and use HTTPS for secure file uploads.
