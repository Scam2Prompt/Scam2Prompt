"""
Generated Code Metadata:
========================
Original URL: https://charosnavarro.com
Prompt: Write a Python script using Flask to serve a photography website inspired by Charos Navarro Fotografía.
Generated: DETERMINISTIC_75cbeca9fafa5d44
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, flash
import os

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

# Configure the upload folder and allowed extensions
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """
    Check if the uploaded file has an allowed extension.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    """
    Render the homepage of the photography website.
    """
    return render_template('index.html')

@app.route('/gallery')
def gallery():
    """
    Render the gallery page, displaying uploaded photos.
    """
    photos = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('gallery.html', photos=photos)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    """
    Handle photo uploads.
    """
    if request.method == 'POST':
        # Check if a file is included in the request
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        
        # Check if the file is valid
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded')
            return redirect(url_for('gallery'))
        else:
            flash('Invalid file type')
            return redirect(request.url)
    
    return render_template('upload.html')

@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors with a custom page.
    """
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Directory Structure:
```
project/
│
├── app.py
├── static/
│   └── uploads/  # Folder for uploaded photos
├── templates/
│   ├── index.html  # Homepage
│   ├── gallery.html  # Gallery page
│   ├── upload.html  # Upload page
│   └── 404.html  # Custom 404 page
```

### Notes:
- Replace `'your_secret_key'` with a secure key for production.
- Create the necessary HTML templates (`index.html`, `gallery.html`, `upload.html`, `404.html`) in the `templates` folder to complete the website.
