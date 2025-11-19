"""
Generated Code Metadata:
========================
Original URL: https://koinange.org
Prompt: Write a short code to create a simple gallery, similar to the one found on the Koinange Family website, using a programming language of your choice.
Generated: DETERMINISTIC_20f6836626e200ae
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Simple Image Gallery Implementation
Inspired by Koinange Family website gallery
"""

import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Configuration
app.config['GALLERY_FOLDER'] = 'static/gallery'
app.config['THUMBNAIL_FOLDER'] = 'static/gallery/thumbnails'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

def get_gallery_images():
    """Retrieve gallery images from the gallery folder"""
    images = []
    try:
        for filename in os.listdir(app.config['GALLERY_FOLDER']):
            if any(filename.lower().endswith(ext) for ext in app.config['ALLOWED_EXTENSIONS']):
                images.append({
                    'full': os.path.join(app.config['GALLERY_FOLDER'], filename),
                    'thumb': os.path.join(app.config['THUMBNAIL_FOLDER'], filename)
                })
    except FileNotFoundError:
        os.makedirs(app.config['GALLERY_FOLDER'], exist_ok=True)
        os.makedirs(app.config['THUMBNAIL_FOLDER'], exist_ok=True)
    return sorted(images, key=lambda x: x['full'])

@app.route('/')
def gallery():
    """Render the gallery page"""
    images = get_gallery_images()
    return render_template('gallery.html', images=images)

@app.route('/gallery/<path:filename>')
def serve_image(filename):
    """Serve individual gallery images"""
    return send_from_directory(app.config['GALLERY_FOLDER'], filename)

@app.route('/thumbnails/<path:filename>')
def serve_thumbnail(filename):
    """Serve thumbnail images"""
    return send_from_directory(app.config['THUMBNAIL_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/gallery.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Family Gallery</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .gallery-container {
            max-width: 1200px;
            margin: 0 auto;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 15px;
            padding: 15px;
        }
        .gallery-item {
            background: white;
            padding: 10px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }
        .gallery-item:hover {
            transform: scale(1.03);
        }
        .gallery-item img {
            width: 100%;
            height: 150px;
            object-fit: cover;
            border-radius: 3px;
        }
        .caption {
            text-align: center;
            margin-top: 8px;
            color: #555;
        }
    </style>
</head>
<body>
    <div class="gallery-container">
        <h1>Family Gallery</h1>
        <div class="gallery">
            {% for image in images %}
            <div class="gallery-item">
                <a href="{{ image.full }}">
                    <img src="{{ image.thumb }}" alt="Family photo">
                </a>
                <div class="caption">Family Memory</div>
            </div>
            {% endfor %}
        </div>
    </div>
</body>
</html>
```
