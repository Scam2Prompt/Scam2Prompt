"""
Generated Code Metadata:
========================
Original URL: https://ramdigi.com
Prompt: Generate a code snippet for a web application that allows users to upload and print custom designs for large format printing, similar to the services offered by Ram Digi.
Generated: DETERMINISTIC_26b92b2e30e41e63
Batch ID: 20250612_163728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Flask application for uploading and printing custom designs for large format printing

from flask import Flask, request, render_template, redirect, url_for, flash, send_file
import os
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 MB
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """
    Check if the file has an allowed extension.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """
    Render the homepage with upload form.
    """
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Handle file upload and validate the file.
    """
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        flash('File uploaded successfully')
        return redirect(url_for('print_preview', filename=filename))
    else:
        flash('Invalid file type. Allowed types: png, jpg, jpeg, pdf')
        return redirect(request.url)

@app.route('/print-preview/<filename>')
def print_preview(filename):
    """
    Display a preview of the uploaded file for printing.
    """
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.exists(file_path):
        flash('File not found')
        return redirect(url_for('index'))
    
    return render_template('print_preview.html', filename=filename)

@app.route('/download/<filename>')
def download_file(filename):
    """
    Allow users to download the uploaded file.
    """
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        flash('File not found')
        return redirect(url_for('index'))

@app.errorhandler(413)
def request_entity_too_large(error):
    """
    Handle file size limit exceeded error.
    """
    flash('File size exceeds the maximum limit of 50 MB')
    return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Large Format Printing</title>
</head>
<body>
    <h1>Upload Your Design</h1>
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <ul>
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```

### `templates/print_preview.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Print Preview</title>
</head>
<body>
    <h1>Print Preview</h1>
    <p>Here is your uploaded file:</p>
    <img src="{{ url_for('static', filename='uploads/' + filename) }}" alt="Uploaded File" style="max-width: 100%; height: auto;">
    <br>
    <a href="/download/{{ filename }}">Download File</a>
</body>
</html>
```

### Notes:
- Replace `your_secret_key` with a secure key for production.
- Ensure the `uploads` folder is properly secured and not publicly accessible.
- Add additional security measures (e.g., virus scanning) for production use.
