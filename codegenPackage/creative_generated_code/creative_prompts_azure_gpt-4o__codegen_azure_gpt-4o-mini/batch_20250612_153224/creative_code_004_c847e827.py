"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bee-property.com
Prompt: Develop a system that uses professional property photography to enhance rental listings and increase conversion rates. Include tools or libraries for image processing and optimization.
Generated: DETERMINISTIC_c847e8279da104d8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, request, jsonify
from PIL import Image, ImageEnhance
import uuid

# Initialize the Flask application
app = Flask(__name__)

# Directory to save uploaded images
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Allowed image extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    """Check if the uploaded file is a valid image type."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_image(image_path):
    """Enhance the image and save the optimized version."""
    try:
        with Image.open(image_path) as img:
            # Enhance brightness, contrast, and color
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(1.1)  # Increase brightness by 10%
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(1.2)   # Increase contrast by 20%
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(1.1)    # Increase color by 10%
            
            # Save the enhanced image
            optimized_path = os.path.join(UPLOAD_FOLDER, f"optimized_{uuid.uuid4().hex}.jpg")
            img.save(optimized_path, "JPEG", quality=85)
            return optimized_path
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return None

@app.route('/upload', methods=['POST'])
def upload_file():
    """Upload an image file and return the optimized image path."""
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "File type not allowed"}), 400

    try:
        # Save the uploaded file
        image_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(image_path)

        # Process the image
        optimized_image_path = process_image(image_path)
        if optimized_image_path:
            return jsonify({"optimized_image_path": optimized_image_path}), 200
        else:
            return jsonify({"error": "Image processing failed"}), 500
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=False, host='0.0.0.0', port=5000)
```
