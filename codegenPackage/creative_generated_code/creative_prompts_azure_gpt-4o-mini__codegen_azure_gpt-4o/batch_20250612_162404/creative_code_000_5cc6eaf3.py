"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://christineheart.com
Prompt: Generate a code snippet for a travel blog that integrates Polaroid photo uploads and displays them in a gallery format.
Generated: DETERMINISTIC_5cc6eaf325df115e
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
A Python Flask-based web application for a travel blog that allows users to upload
Polaroid-style photos and display them in a gallery format.

Dependencies:
- Flask
- Flask-WTF
- WTForms
- Pillow (for image manipulation)

Ensure these dependencies are installed before running the code:
pip install flask flask-wtf wtforms pillow
"""

import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from werkzeug.utils import secure_filename
from PIL import Image

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Allowed file extensions for uploads
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    """Check if a file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class PhotoUploadForm(FlaskForm):
    """Form for uploading Polaroid-style photos."""
    photo = FileField('Upload Polaroid Photo', validators=[DataRequired()])
    submit = SubmitField('Upload')

    def validate_photo(self, field):
        """Custom validation to ensure the file is an image."""
        if not allowed_file(field.data.filename):
            raise ValidationError('File must be a valid image (png, jpg, jpeg).')

@app.route('/', methods=['GET', 'POST'])
def index():
    """Home page with photo upload functionality and gallery display."""
    form = PhotoUploadForm()
    if form.validate_on_submit():
        file = form.photo.data
        if file and allowed_file(file.filename):
            # Secure the filename
            filename = secure_filename(file.filename)
            
            # Save the uploaded file
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            # Convert the image to Polaroid-style (optional)
            with Image.open(file_path) as img:
                # Resize and add white border
                border_size = 50
                polaroid = Image.new('RGB', (img.width + border_size, img.height + int(border_size * 1.5)), 'white')
                polaroid.paste(img, (border_size // 2, border_size // 2))
                polaroid.save(file_path)

            flash('Photo uploaded successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid file type.', 'danger')

    # Collect all uploaded images for the gallery
    photos = os.listdir(app.config['UPLOAD_FOLDER'])
    photos = [os.path.join(app.config['UPLOAD_FOLDER'], photo) for photo in photos]
    
    return render_template('index.html', form=form, photos=photos)

# Run the Flask app (use a production-ready WSGI server for deployment)
if __name__ == '__main__':
    app.run(debug=True)

"""
Template: templates/index.html
Use the following HTML template to render the form and gallery.
Save it as "templates/index.html" in the same directory as the script.

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Travel Blog Gallery</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .container {
            width: 80%;
            margin: auto;
            padding: 20px;
            background: #fff;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .gallery {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
        }
        .gallery img {
            width: 200px;
            height: auto;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .form-section {
            margin-bottom: 30px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Travel Blog Gallery</h1>
        <div class="form-section">
            <form method="POST" enctype="multipart/form-data">
                {{ form.hidden_tag() }}
                <p>{{ form.photo.label }} {{ form.photo() }}</p>
                <p>{{ form.submit() }}</p>
                {% for message in get_flashed_messages() %}
                    <p style="color: green;">{{ message }}</p>
                {% endfor %}
            </form>
        </div>
        <div class="gallery">
            {% for photo in photos %}
                <img src="{{ photo }}" alt="Uploaded Photo">
            {% endfor %}
        </div>
    </div>
</body>
</html>
"""
```
