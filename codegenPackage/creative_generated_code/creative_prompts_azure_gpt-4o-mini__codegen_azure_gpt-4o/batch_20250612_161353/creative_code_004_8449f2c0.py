"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bicho.se
Prompt: Develop a code example that uses an image gallery library to present David Bicho's photography in a visually appealing manner.
Generated: DETERMINISTIC_8449f2c0ced7f1fe
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Image Gallery Application to Showcase David Bicho's Photography
This script uses the 'Pillow' library to create an image gallery
and displays photography in a visually appealing manner.
"""

import os
from PIL import Image
from flask import Flask, render_template, url_for

app = Flask(__name__)

# Configuration
IMAGE_FOLDER = 'static/images'  # Path to the folder containing David Bicho's photography
THUMBNAIL_FOLDER = 'static/thumbnails'  # Path to store generated thumbnails
THUMBNAIL_SIZE = (300, 200)  # Thumbnail dimensions


def create_thumbnails(image_folder, thumbnail_folder):
    """
    Generates thumbnails for all images in the image folder.
    :param image_folder: Path to folder containing original images.
    :param thumbnail_folder: Path to folder where thumbnails will be stored.
    """
    if not os.path.exists(thumbnail_folder):
        os.makedirs(thumbnail_folder)

    for image_name in os.listdir(image_folder):
        image_path = os.path.join(image_folder, image_name)
        thumbnail_path = os.path.join(thumbnail_folder, image_name)
        
        try:
            with Image.open(image_path) as img:
                img.thumbnail(THUMBNAIL_SIZE)
                img.save(thumbnail_path)
        except Exception as e:
            print(f"Error creating thumbnail for {image_name}: {e}")


@app.route('/')
def gallery():
    """
    Displays the image gallery.
    """
    try:
        thumbnails = [
            url_for('static', filename=f'thumbnails/{img}')
            for img in os.listdir(THUMBNAIL_FOLDER)
        ]
    except Exception as e:
        thumbnails = []
        print(f"Error loading thumbnails: {e}")

    return render_template('gallery.html', thumbnails=thumbnails)


if __name__ == '__main__':
    # Create thumbnails upon application startup
    create_thumbnails(IMAGE_FOLDER, THUMBNAIL_FOLDER)

    # Start the Flask app
    app.run(debug=True)

```

```html
<!-- Save this HTML template as 'templates/gallery.html' -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>David Bicho's Photography Gallery</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            margin: 0;
            padding: 0;
        }
        .thumbnail {
            margin: 10px;
            border: 2px solid #ddd;
            border-radius: 5px;
            overflow: hidden;
            width: 300px;
            height: 200px;
        }
        .thumbnail img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
    </style>
</head>
<body>
    {% for thumbnail in thumbnails %}
        <div class="thumbnail">
            <img src="{{ thumbnail }}" alt="David Bicho's Photography">
        </div>
    {% endfor %}
</body>
</html>
```

### Notes:
- Place David Bicho's images in the `static/images` folder.
- The script automatically generates thumbnails in the `static/thumbnails` folder.
- Run the Flask app by executing the Python script, then visit the `localhost:5000` URL to view the gallery.
