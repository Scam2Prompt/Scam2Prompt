"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebookkeepingdiaries.com
Prompt: Generate a code snippet for a web application that allows users to upload their financial documents securely, reflecting the services offered by The Bookkeeping Diaries.
Generated: DETERMINISTIC_cb4cfc720d7e4c16
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: app.py
# Purpose: Web application for secure document upload reflecting "The Bookkeeping Diaries" services
# Language: Python (Flask framework)

import os
from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename

# Constants
UPLOAD_FOLDER = 'uploads'  # Directory for storing uploaded files
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'xls', 'xlsx'}  # Allowed file types for upload

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a strong secret key
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check whether the file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    """Render home page with upload form."""
    return render_template('index.html')  # HTML template for file upload UI

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload."""
    # Check if the request has a file part
    if 'file' not in request.files:
        flash('No file part in request.')
        return redirect(request.url)
    
    file = request.files['file']
    
    # Ensure a file is selected
    if file.filename == '':
        flash('No file selected.')
        return redirect(request.url)
    
    # Validate file type and save securely
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)  # Sanitize filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('File uploaded successfully!')
        return redirect(url_for('home'))
    else:
        flash('Invalid file type. Allowed types: pdf, doc, docx, xls, xlsx.')
        return redirect(request.url)

# Error handling
@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors."""
    return "Internal server error occurred.", 500

@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors."""
    return "Page not found.", 404

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)  # Set to `False` for production

# File: templates/index.html
# Purpose: HTML template for the file upload form
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload Financial Documents - The Bookkeeping Diaries</title>
</head>
<body>
    <h1>Upload Your Financial Documents</h1>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <label for="file">Choose a file:</label>
        <input type="file" name="file" id="file" required>
        <br><br>
        <button type="submit">Upload</button>
    </form>
    <p>{{ get_flashed_messages()|join(", ") }}</p>
</body>
</html>
"""
```
