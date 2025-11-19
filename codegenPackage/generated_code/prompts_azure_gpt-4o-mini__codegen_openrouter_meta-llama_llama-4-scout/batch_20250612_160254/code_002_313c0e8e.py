"""
Generated Code Metadata:
========================
Original URL: https://www.pics3dstudio.com
Prompt: Write a function that integrates 360-degree panoramic images into a web application, inspired by the projects listed on PICS3DStudio.
Generated: DETERMINISTIC_313c0e8e22cb1208
Batch ID: 20250612_160254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from PIL import Image
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Define a function to integrate 360-degree panoramic images
def integrate_panoramic_image(image_path, image_id):
    """
    Integrates a 360-degree panoramic image into the web application.

    Args:
        image_path (str): The path to the panoramic image.
        image_id (str): A unique identifier for the image.

    Returns:
        A dictionary containing the image data and metadata.
    """
    try:
        # Open the image using PIL
        with Image.open(image_path) as img:
            # Get the image dimensions
            width, height = img.size

            # Validate the image dimensions
            if width < 2 or height < 2:
                raise ValueError("Invalid image dimensions")

            # Convert the image to a numpy array
            img_array = np.array(img)

            # Process the image data (e.g., resize, normalize)
            # For demonstration purposes, we'll just resize the image
            img_array = np.resize(img_array, (height, width, 3))

            # Create a dictionary to store the image data and metadata
            image_data = {
                "image_id": image_id,
                "image_path": image_path,
                "width": width,
                "height": height,
                "image_data": img_array.tolist()
            }

            return image_data

    except Exception as e:
        # Handle any exceptions that occur during image processing
        print(f"Error integrating panoramic image: {str(e)}")
        return None

# Define a route to handle image uploads
@app.route('/upload_image', methods=['POST'])
def upload_image():
    try:
        # Get the image file and ID from the request
        image_file = request.files['image_file']
        image_id = request.form['image_id']

        # Save the image file to a temporary location
        image_path = f"./temp/{image_id}.jpg"
        image_file.save(image_path)

        # Integrate the panoramic image
        image_data = integrate_panoramic_image(image_path, image_id)

        # Return the image data and metadata as JSON
        return jsonify(image_data)

    except Exception as e:
        # Handle any exceptions that occur during image upload
        print(f"Error uploading image: {str(e)}")
        return jsonify({"error": "Failed to upload image"}), 500

# Define a route to render the panoramic image
@app.route('/render_image/<image_id>')
def render_image(image_id):
    try:
        # Load the image data and metadata from storage
        image_data = load_image_data(image_id)

        # Render the panoramic image using a template
        return render_template('panoramic_image.html', image_data=image_data)

    except Exception as e:
        # Handle any exceptions that occur during image rendering
        print(f"Error rendering image: {str(e)}")
        return "Error rendering image", 500

# Define a function to load image data and metadata from storage
def load_image_data(image_id):
    # For demonstration purposes, we'll just return some sample data
    return {
        "image_id": image_id,
        "image_path": f"./images/{image_id}.jpg",
        "width": 2048,
        "height": 1024,
        "image_data": []
    }

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- panoramic_image.html template -->
<!DOCTYPE html>
<html>
<head>
    <title>Panoramic Image</title>
    <style>
        /* Add some basic styling to the image */
        #panoramic-image {
            width: 100%;
            height: 100vh;
            object-fit: cover;
        }
    </style>
</head>
<body>
    <img id="panoramic-image" src="{{ image_data.image_path }}" />
    <script>
        // Add some JavaScript to handle image loading and rendering
        const image = document.getElementById('panoramic-image');

        // Use a library like Three.js to render the panoramic image
        // For demonstration purposes, we'll just add some basic event handling
        image.addEventListener('load', () => {
            console.log('Image loaded');
        });
    </script>
</body>
</html>
```
