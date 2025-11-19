"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://charosnavarro.com
Prompt: Write a Python script using Flask to serve a photography website inspired by Charos Navarro Fotografía.
Generated: DETERMINISTIC_75cbeca9fafa5d44
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure secret key for session management (e.g., for flash messages)
app.secret_key = os.getenv("SECRET_KEY", "your_secret_key_here")

# Configure the upload folder and allowed extensions for image upload
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def allowed_file(filename):
    """
    Check if the uploaded file has an allowed extension.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    """
    Route for the homepage. Displays a gallery of photos.
    """
    # List all image files in the upload folder
    images = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', images=images)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    """
    Route for uploading new photos to the gallery.
    """
    if request.method == 'POST':
        # Check if a file is included in the form submission
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        # Check if the file is valid and allowed
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            # Save the file to the upload folder
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File uploaded successfully!')
            return redirect(url_for('home'))

        flash('Invalid file type. Please upload an image file.')
        return redirect(request.url)

    # Render the upload form
    return render_template('upload.html')


@app.errorhandler(404)
def page_not_found(e):
    """
    Custom 404 error page.
    """
    return render_template('404.html'), 404


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

### Directory Structure:
To make this functional, ensure you have the following directory structure:
```
your_project/
│
├── static/
│   └── uploads/   # Directory where uploaded photos are stored
│
├── templates/
│   ├── index.html # Homepage template
│   ├── upload.html # Upload page template
│   └── 404.html   # Custom 404 page template
│
└── app.py         # This Python script
```

### HTML Templates:
You can create simple HTML templates (`index.html`, `upload.html`, and `404.html`) to suit your photography website design requirements.
