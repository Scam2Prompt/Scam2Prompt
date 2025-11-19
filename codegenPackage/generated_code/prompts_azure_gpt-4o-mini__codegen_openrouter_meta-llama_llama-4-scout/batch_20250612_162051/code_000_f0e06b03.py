"""
Generated Code Metadata:
========================
Original URL: https://bda.mcupr.ac.th
Prompt: Generate a Python script to create a 360-degree virtual tour of a Buddhist art gallery, incorporating features mentioned on the BDA MCU website.
Generated: DETERMINISTIC_f0e06b032b52cfbb
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import cv2
import numpy as np
from PIL import Image
from flask import Flask, render_template, request

# Initialize Flask app
app = Flask(__name__)

# Define constants
IMAGE_FOLDER = 'static/images'
TOUR_CONFIG = 'tour_config.json'

# Load tour configuration
try:
    with open(TOUR_CONFIG, 'r') as f:
        tour_config = json.load(f)
except FileNotFoundError:
    print(f"Error: {TOUR_CONFIG} not found.")
    exit(1)
except json.JSONDecodeError:
    print(f"Error: Invalid JSON in {TOUR_CONFIG}.")
    exit(1)

# Define a function to generate the virtual tour
def generate_tour():
    # Initialize the tour images
    tour_images = []

    # Iterate over the scenes in the tour configuration
    for scene in tour_config['scenes']:
        # Load the images for the current scene
        images = []
        for image_file in scene['images']:
            image_path = os.path.join(IMAGE_FOLDER, image_file)
            try:
                image = Image.open(image_path)
                images.append(image)
            except FileNotFoundError:
                print(f"Error: {image_path} not found.")
                continue

        # Stitch the images for the current scene
        stitched_image = stitch_images(images)

        # Add the stitched image to the tour images
        tour_images.append(stitched_image)

    return tour_images

# Define a function to stitch images
def stitch_images(images):
    # Check if there are images to stitch
    if len(images) == 0:
        return None

    # Initialize the stitched image
    stitched_image = images[0]

    # Iterate over the remaining images
    for image in images[1:]:
        # Stitch the current image to the stitched image
        stitched_image = cv2.Stitcher().stitch(stitched_image, image)

    return stitched_image

# Define a route for the virtual tour
@app.route('/')
def index():
    return render_template('index.html')

# Define a route for the virtual tour images
@app.route('/tour')
def tour():
    tour_images = generate_tour()
    return render_template('tour.html', tour_images=tour_images)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Buddhist Art Gallery Virtual Tour</title>
</head>
<body>
    <h1>Buddhist Art Gallery Virtual Tour</h1>
    <p><a href="{{ url_for('tour') }}">Start Tour</a></p>
</body>
</html>
```

```html
<!-- templates/tour.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Buddhist Art Gallery Virtual Tour</title>
</head>
<body>
    <h1>Buddhist Art Gallery Virtual Tour</h1>
    {% for image in tour_images %}
        <img src="{{ image }}" />
    {% endfor %}
</body>
</html>
```

```json
// tour_config.json
{
    "scenes": [
        {
            "images": ["image1.jpg", "image2.jpg", "image3.jpg"]
        },
        {
            "images": ["image4.jpg", "image5.jpg", "image6.jpg"]
        }
    ]
}
```
