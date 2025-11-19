"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bda.mcupr.ac.th
Prompt: Generate a Python script to create a 360-degree virtual tour of a Buddhist art gallery, incorporating features mentioned on the BDA MCU website.
Generated: DETERMINISTIC_f0e06b032b52cfbb
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from flask import Flask, render_template, jsonify, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Utility function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to upload artwork images
@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Endpoint to upload an image for the virtual tour.
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return jsonify({'message': 'File uploaded successfully', 'filepath': filepath}), 200
    
    return jsonify({'error': 'Invalid file type'}), 400

# Route to display the virtual tour
@app.route('/')
def gallery_virtual_tour():
    """
    Main endpoint to render the virtual tour of the gallery.
    """
    try:
        # Load all images in the upload folder
        images = [
            f"{UPLOAD_FOLDER}/{image}" for image in os.listdir(UPLOAD_FOLDER)
            if allowed_file(image)
        ]
        return render_template('virtual_tour.html', images=images)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to provide API for gallery data
@app.route('/gallery-data', methods=['GET'])
def gallery_data():
    """
    Endpoint to provide JSON data about the gallery, including image file paths.
    """
    try:
        images = [
            f"{UPLOAD_FOLDER}/{image}" for image in os.listdir(UPLOAD_FOLDER)
            if allowed_file(image)
        ]
        gallery_info = {
            "gallery_name": "Buddhist Art Gallery",
            "description": "Explore a 360-degree virtual tour of the Buddhist art gallery.",
            "images": images
        }
        return jsonify(gallery_info), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
```

### HTML Template: `templates/virtual_tour.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Buddhist Art Gallery Virtual Tour</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .gallery {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: center;
            margin-top: 20px;
        }
        .gallery img {
            width: 300px;
            height: auto;
            border: 1px solid #ddd;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
        }
    </style>
</head>
<body>
    <h1>Buddhist Art Gallery Virtual Tour</h1>
    <p>Welcome to the 360-degree virtual tour of the Buddhist art gallery!</p>
    <div class="gallery">
        {% for image in images %}
            <img src="{{ image }}" alt="Artwork">
        {% endfor %}
    </div>
</body>
</html>
```
