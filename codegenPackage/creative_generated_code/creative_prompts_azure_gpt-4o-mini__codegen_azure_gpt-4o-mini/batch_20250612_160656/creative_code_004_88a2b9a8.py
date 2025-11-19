"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refikanadol.pages.dev
Prompt: Create a web application that showcases AI-generated art, inspired by the projects featured on Refik Anadol's site, including "Machine Hallucinations."
Generated: DETERMINISTIC_88a2b9a8e3a45598
Batch ID: 20250612_160656
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request
import os
import random
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Path to the directory containing AI-generated art images
ART_DIRECTORY = 'static/art'

# Ensure the ART_DIRECTORY exists
if not os.path.exists(ART_DIRECTORY):
    os.makedirs(ART_DIRECTORY)

# Route for the homepage
@app.route('/')
def home():
    """
    Render the homepage that showcases AI-generated art.
    """
    try:
        # List all art images in the ART_DIRECTORY
        art_images = [f for f in os.listdir(ART_DIRECTORY) if f.endswith(('.png', '.jpg', '.jpeg'))]
        return render_template('index.html', art_images=art_images)
    except Exception as e:
        logging.error(f"Error loading art images: {e}")
        return "An error occurred while loading the art images.", 500

# Route to upload new AI-generated art
@app.route('/upload', methods=['POST'])
def upload_art():
    """
    Handle the upload of new AI-generated art images.
    """
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']

    if file.filename == '':
        return "No selected file", 400

    try:
        # Save the file to the ART_DIRECTORY
        file_path = os.path.join(ART_DIRECTORY, file.filename)
        file.save(file_path)
        return "File uploaded successfully", 200
    except Exception as e:
        logging.error(f"Error saving the file: {e}")
        return "An error occurred while saving the file.", 500

if __name__ == '__main__':
    # Run the app in debug mode for development
    app.run(debug=True)

# Sample HTML Template (index.html)
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Art Showcase</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <style>
        body { font-family: Arial, sans-serif; }
        .gallery { display: flex; flex-wrap: wrap; }
        .gallery img { max-width: 300px; margin: 10px; border: 2px solid #ddd; }
    </style>
</head>
<body>
    <h1>AI Art Showcase</h1>
    <div class="gallery">
        {% for image in art_images %}
            <img src="{{ url_for('static', filename='art/' + image) }}" alt="{{ image }}">
        {% endfor %}
    </div>

    <h2>Upload New Art</h2>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file" accept="image/*" required>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
"""
```
