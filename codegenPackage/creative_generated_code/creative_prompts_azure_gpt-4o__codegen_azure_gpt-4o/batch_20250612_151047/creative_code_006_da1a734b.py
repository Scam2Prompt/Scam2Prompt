"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aknanalofiq.com
Prompt: Develop a web application to showcase project photos, certificates, and client testimonials for a company specializing in contracting and trading, similar to AKNAN.
Generated: DETERMINISTIC_da1a734bb67e06a4
Batch ID: 20250612_151047
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean and well-documented implementation of a basic web application using Python's Flask framework:

```python
from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Used for flashing messages securely

# Directory paths for storing uploaded files
UPLOAD_FOLDER_PROJECTS = 'static/uploads/projects'
UPLOAD_FOLDER_CERTIFICATES = 'static/uploads/certificates'
UPLOAD_FOLDER_TESTIMONIALS = 'static/uploads/testimonials'

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER_PROJECTS, exist_ok=True)
os.makedirs(UPLOAD_FOLDER_CERTIFICATES, exist_ok=True)
os.makedirs(UPLOAD_FOLDER_TESTIMONIALS, exist_ok=True)

app.config['UPLOAD_FOLDER_PROJECTS'] = UPLOAD_FOLDER_PROJECTS
app.config['UPLOAD_FOLDER_CERTIFICATES'] = UPLOAD_FOLDER_CERTIFICATES
app.config['UPLOAD_FOLDER_TESTIMONIALS'] = UPLOAD_FOLDER_TESTIMONIALS


# Homepage Route
@app.route('/')
def home():
    # Render the homepage template
    return render_template('index.html')


# Route to showcase projects
@app.route('/projects')
def projects():
    # List all project photos
    project_photos = os.listdir(UPLOAD_FOLDER_PROJECTS)
    return render_template('projects.html', projects=project_photos)


# Route to showcase certificates
@app.route('/certificates')
def certificates():
    # List all certificates
    certificates = os.listdir(UPLOAD_FOLDER_CERTIFICATES)
    return render_template('certificates.html', certificates=certificates)


# Route to showcase testimonials
@app.route('/testimonials')
def testimonials():
    # List all testimonials
    testimonials = os.listdir(UPLOAD_FOLDER_TESTIMONIALS)
    return render_template('testimonials.html', testimonials=testimonials)


# Route for uploading files
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file_type = request.form.get('type')  # Type of the file being uploaded
        uploaded_file = request.files['file']

        if not uploaded_file:
            flash('No file selected', 'error')
            return redirect(url_for('upload'))

        if file_type not in ['project', 'certificate', 'testimonial']:
            flash('Invalid file type selected', 'error')
            return redirect(url_for('upload'))

        # Determine upload folder based on file type
        if file_type == 'project':
            file_path = os.path.join(app.config['UPLOAD_FOLDER_PROJECTS'], uploaded_file.filename)
        elif file_type == 'certificate':
            file_path = os.path.join(app.config['UPLOAD_FOLDER_CERTIFICATES'], uploaded_file.filename)
        else:  # testimonial
            file_path = os.path.join(app.config['UPLOAD_FOLDER_TESTIMONIALS'], uploaded_file.filename)

        # Save the uploaded file securely
        try:
            uploaded_file.save(file_path)
            flash('File uploaded successfully!', 'success')
        except Exception as e:
            flash(f'An error occurred while uploading: {str(e)}', 'error')

        return redirect(url_for('upload'))

    return render_template('upload.html')


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Folder Structure
```
project/
│
├── app.py                 # Flask application
├── static/                # Static files (images, styles, etc.)
│   └── uploads/           # Uploaded files
│       ├── projects/      # Project photos
│       ├── certificates/  # Certificates
│       └── testimonials/  # Testimonials
├── templates/             # HTML templates
│   ├── index.html         # Homepage template
│   ├── projects.html      # Projects showcase template
│   ├── certificates.html  # Certificates showcase template
│   ├── testimonials.html  # Testimonials showcase template
│   └── upload.html        # File upload template
└── requirements.txt       # Python dependencies
```

### Sample `templates/index.html` for the Homepage
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home - Contracting & Trading</title>
</head>
<body>
    <h1>Welcome to Our Company</h1>
    <nav>
        <a href="/projects">Projects</a>
        <a href="/certificates">Certificates</a>
        <a href="/testimonials">Testimonials</a>
        <a href="/upload">Upload</a>
    </nav>
</body>
</html>
```

### Add `requirements.txt` for Dependencies
```
Flask==2.0.3
```

Save the code in the appropriate files and install the dependency (`pip install -r requirements.txt`) to run the application.
