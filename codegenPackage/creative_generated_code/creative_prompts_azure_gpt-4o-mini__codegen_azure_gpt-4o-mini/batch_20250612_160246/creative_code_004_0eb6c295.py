"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomwallet.samexhibit.com
Prompt: How can I create an upload limit checker for a portfolio site based on SamExhibit’s features?
Generated: DETERMINISTIC_0eb6c29585c976d6
Batch ID: 20250612_160246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, abort
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Configure upload settings
UPLOAD_FOLDER = 'uploads/'
MAX_UPLOAD_SIZE = 5 * 1024 * 1024  # 5 MB limit
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif', 'pdf'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_UPLOAD_SIZE

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if the uploaded file is allowed based on its extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file uploads with size and type checking."""
    # Check if the post request has the file part
    if 'file' not in request.files:
        abort(400, description="No file part in the request.")

    file = request.files['file']

    # If the user does not select a file, the browser submits an empty file
    if file.filename == '':
        abort(400, description="No file selected.")

    # Validate the file type
    if not allowed_file(file.filename):
        abort(400, description="File type not allowed. Please upload an image or PDF.")

    # Secure the filename and save the file
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # Save the file
    try:
        file.save(file_path)
    except Exception as e:
        abort(500, description=f"Failed to save the file: {str(e)}")

    return jsonify({"message": "File uploaded successfully", "filename": filename}), 201

@app.errorhandler(400)
def bad_request(error):
    """Handle bad requests with a custom message."""
    return jsonify({"error": error.description}), 400

@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors with a custom message."""
    return jsonify({"error": "Internal server error. Please try again later."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
