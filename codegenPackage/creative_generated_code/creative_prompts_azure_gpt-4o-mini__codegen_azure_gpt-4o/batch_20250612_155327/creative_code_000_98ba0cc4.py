"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panicinpolkadots.com
Prompt: Generate a code snippet for a web application that allows users to upload their old t-shirts for creating custom quilts, similar to the services offered by Panic in Polkadots.
Generated: DETERMINISTIC_98ba0cc4eab1d99e
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based web application for uploading old t-shirts to create custom quilts.

from flask import Flask, request, render_template, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)

# Configuration for file uploads
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit uploaded files to 16MB
app.secret_key = 'your_secret_key_here'

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """Check if the uploaded file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """
    Render the homepage.
    Provides a form for users to upload t-shirt images.
    """
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Handle file upload from the user. Validate and store the file.
    """
    if 'file' not in request.files:
        flash('No file part in the request')
        return redirect(url_for('index'))
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('index'))
    
    if file and allowed_file(file.filename):
        try:
            # Secure the filename to prevent injection attacks
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File uploaded successfully!')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'An error occurred while uploading the file: {str(e)}')
            return redirect(url_for('index'))
    else:
        flash('Invalid file type. Only .png, .jpg, and .jpeg are allowed.')
        return redirect(url_for('index'))

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Custom Quilt T-shirt Upload</title>
</head>
<body>
    <h1>Upload Your T-shirt Images for Custom Quilts</h1>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <button type="submit">Upload T-shirt</button>
    </form>
    {% with messages = get_flashed_messages() %}
    {% if messages %}
        <ul>
        {% for message in messages %}
            <li>{{ message }}</li>
        {% endfor %}
        </ul>
    {% endif %}
    {% endwith %}
</body>
</html>
```
