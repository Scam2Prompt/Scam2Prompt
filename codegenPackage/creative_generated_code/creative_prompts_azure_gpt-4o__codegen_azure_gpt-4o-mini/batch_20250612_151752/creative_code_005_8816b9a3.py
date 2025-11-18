"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cem-seven.vercel.app
Prompt: Suggest a method to create a user interface for uploading files and generating tokens with custom metadata, referencing the Co-Edition platform's features.
Generated: DETERMINISTIC_8816b9a3f4e5bd95
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from flask import Flask, request, jsonify, render_template, redirect, url_for
from werkzeug.utils import secure_filename

# Configure Flask application
app = Flask(__name__)

# Set upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if the uploaded file is allowed based on its extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """Render the file upload form."""
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and generate token with custom metadata."""
    # Check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    # Check if the user actually selected a file
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Validate the file
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Generate a token (placeholder logic for token generation)
        token = generate_token(file_path)

        # Get custom metadata from the request JSON
        metadata = request.form.get('metadata', '{}')
        try:
            metadata = json.loads(metadata)
        except json.JSONDecodeError:
            return jsonify({'error': 'Invalid metadata format'}), 400

        # Return response with token and metadata
        return jsonify({
            'message': 'File uploaded successfully',
            'token': token,
            'metadata': metadata
        }), 201

    return jsonify({'error': 'File type not allowed'}), 400

def generate_token(file_path):
    """Simulate token generation for the uploaded file."""
    # In production, use a proper token generation mechanism (e.g., JWT)
    return os.path.basename(file_path) + '_token'

if __name__ == "__main__":
    app.run(debug=True)
```

**upload.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload</title>
</head>
<body>
    <h1>Upload a File</h1>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <textarea name="metadata" placeholder='{"key": "value"}' rows="4" cols="50"></textarea>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```
