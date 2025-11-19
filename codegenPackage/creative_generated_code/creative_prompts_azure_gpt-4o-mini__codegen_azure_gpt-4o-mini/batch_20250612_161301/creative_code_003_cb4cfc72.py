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
from flask import Flask, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Set a secret key for session management
app.secret_key = 'your_secret_key'  # Change this to a strong key in production

# Define the upload folder and allowed file types
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'xls', 'xlsx'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """Check if the uploaded file is of an allowed type."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """Render the upload form."""
    return '''
    <!doctype html>
    <title>Upload Financial Documents</title>
    <h1>Upload your Financial Documents</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/', methods=['POST'])
def upload_file():
    """Handle file upload and save to the designated folder."""
    # Check if a file is part of the request
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']

    # If the user does not select a file, the browser submits an empty file
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    # Validate the file type and save it
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('File successfully uploaded')
        return redirect(url_for('index'))

    # Handle file type not allowed
    flash('File type not allowed')
    return redirect(request.url)

if __name__ == '__main__':
    # Run the application in debug mode
    app.run(debug=True)
```
