"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.hdadpanaderos.es
Prompt: Create a library recommendation for building a gallery of images that showcases events, similar to the "GALERIA DE IMAGENES" on the Hermandad de los Panaderos site.
Generated: DETERMINISTIC_148d97e75a5bb1cc
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

# Initialize the Flask application
app = Flask(__name__)

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to upload images
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return "No file part", 400
        
        file = request.files['file']
        
        # If user does not select file, browser also submits an empty part without filename
        if file.filename == '':
            return "No selected file", 400
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('gallery'))

    return render_template('upload.html')

# Route to display the image gallery
@app.route('/gallery')
def gallery():
    # List all uploaded images
    images = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('gallery.html', images=images)

# Main execution point
if __name__ == '__main__':
    # Run the app in debug mode for development
    app.run(debug=True)
```

**HTML Templates:**

1. **upload.html**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Upload Image</title>
</head>
<body>
    <h1>Upload an Image</h1>
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="file" accept="image/*" required>
        <button type="submit">Upload</button>
    </form>
    <a href="{{ url_for('gallery') }}">View Gallery</a>
</body>
</html>
```

2. **gallery.html**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Image Gallery</title>
</head>
<body>
    <h1>Image Gallery</h1>
    <div>
        {% for image in images %}
            <img src="{{ url_for('static', filename=image) }}" alt="Image" style="max-width: 200px; margin: 10px;">
        {% endfor %}
    </div>
    <a href="{{ url_for('upload_file') }}">Upload More Images</a>
</body>
</html>
```

**Note:** Ensure you have Flask installed in your environment to run this code. You can install Flask via pip:

```bash
pip install Flask
```
