"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elan-life.com
Prompt: Generate a code snippet for a web application that displays image galleries categorized by lifestyle and travel, similar to the structure found on the élán-life website.
Generated: DETERMINISTIC_bd0a2c891451d6bc
Batch ID: 20250612_161017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required Libraries
from flask import Flask, render_template, jsonify
import os

# Initialize Flask App
app = Flask(__name__)

# Define Paths for Image Categories
LIFESTYLE_IMAGES_PATH = "static/images/lifestyle"
TRAVEL_IMAGES_PATH = "static/images/travel"

def get_images_from_directory(directory: str):
    """
    Helper function to retrieve image file names from a given directory.
    :param directory: Directory path where images are stored.
    :return: List of image file paths relative to the server.
    """
    try:
        return [f"{directory}/{file}" for file in os.listdir(directory) if file.endswith((".jpg", ".png", ".jpeg", ".gif"))]
    except FileNotFoundError:
        # If directory doesn't exist, return an empty list
        return []

@app.route("/")
def home():
    """
    Route for the homepage of the web application.
    :return: Rendered HTML template.
    """
    try:
        # Fetch images from predefined directories
        lifestyle_images = get_images_from_directory(LIFESTYLE_IMAGES_PATH)
        travel_images = get_images_from_directory(TRAVEL_IMAGES_PATH)

        # Render template with categorized images
        return render_template("gallery.html", lifestyle_images=lifestyle_images, travel_images=travel_images)
    except Exception as e:
        # Log and handle unexpected errors
        return jsonify({"error": "An error occurred while loading the gallery.", "details": str(e)}), 500

# Create Template Directory (For demonstration purpose only)
if not os.path.exists("templates"):
    os.makedirs("templates")

# Sample HTML Template
sample_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Gallery</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
        .gallery { display: flex; flex-wrap: wrap; gap: 1rem; }
        .gallery img { width: 200px; height: 200px; object-fit: cover; border: 1px solid #ccc; }
        h2 { margin: 1rem 0; }
    </style>
</head>
<body>
    <h1>Image Galleries</h1>
    <h2>Lifestyle</h2>
    <div class="gallery">
        {% for image in lifestyle_images %}
            <img src="{{ image }}" alt="Lifestyle Image">
        {% endfor %}
    </div>
    <h2>Travel</h2>
    <div class="gallery">
        {% for image in travel_images %}
            <img src="{{ image }}" alt="Travel Image">
        {% endfor %}
    </div>
</body>
</html>
"""

# Save Sample HTML Template to File
with open("templates/gallery.html", "w") as f:
    f.write(sample_html)

# Run the Flask App
if __name__ == "__main__":
    app.run(debug=True)
```
