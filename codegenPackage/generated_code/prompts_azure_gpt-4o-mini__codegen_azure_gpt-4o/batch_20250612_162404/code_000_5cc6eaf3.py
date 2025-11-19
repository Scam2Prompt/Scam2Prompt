"""
Generated Code Metadata:
========================
Original URL: https://christineheart.com
Prompt: Generate a code snippet for a travel blog that integrates Polaroid photo uploads and displays them in a gallery format.
Generated: DETERMINISTIC_5cc6eaf325df115e
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# travel_blog_gallery.py

import os
from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
from PIL import Image

# Flask app setup
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'  # Directory to store uploaded photos
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}  # Allowed file extensions
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # Max file size: 5MB
app.secret_key = 'your_secret_key'  # Secret key for flash messages

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    """
    Check if the uploaded file has an allowed extension.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def create_polaroid_effect(image_path):
    """
    Apply a Polaroid-style effect to the uploaded image.
    """
    try:
        with Image.open(image_path) as img:
            # Resize image to fit within a Polaroid frame
            img = img.resize((300, 300))  # Resize to 300x300 pixels
            # Create a white border for the Polaroid effect
            border_size = 50
            polaroid = Image.new('RGB', (img.width + border_size, img.height + border_size + 30), 'white')
            polaroid.paste(img, (border_size // 2, border_size // 2))
            # Save the modified image
            polaroid.save(image_path)
    except Exception as e:
        print(f"Error applying Polaroid effect: {e}")

@app.route('/', methods=['GET', 'POST'])
def upload_photo():
    """
    Handle photo uploads and display the gallery.
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
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            # Apply Polaroid effect to the uploaded photo
            create_polaroid_effect(file_path)
            flash('Photo uploaded successfully!')
            return redirect(url_for('upload_photo'))
        else:
            flash('Invalid file type. Please upload a PNG, JPG, or JPEG file.')
            return redirect(request.url)
    
    # Retrieve all uploaded photos for the gallery
    photos = [f for f in os.listdir(app.config['UPLOAD_FOLDER']) if allowed_file(f)]
    return render_template('gallery.html', photos=photos)

# HTML template for the gallery
@app.route('/gallery.html')
def gallery_template():
    """
    Render the gallery template.
    """
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Travel Blog Gallery</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; }
            .gallery { display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; }
            .photo { border: 1px solid #ccc; padding: 10px; background: #f9f9f9; }
            img { max-width: 100%; height: auto; }
        </style>
    </head>
    <body>
        <h1>Travel Blog Gallery</h1>
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="file" accept="image/*">
            <button type="submit">Upload Photo</button>
        </form>
        <div class="gallery">
            {% for photo in photos %}
            <div class="photo">
                <img src="{{ url_for('static', filename='uploads/' + photo) }}" alt="Polaroid Photo">
            </div>
            {% endfor %}
        </div>
    </body>
    </html>
    '''

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
