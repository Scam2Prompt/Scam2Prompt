"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appdevistorias.com.br
Prompt: Recommend libraries or APIs that can enable photo annotation and defect marking in a mobile app, similar to the functionality described in the BeSoft App Vistoria.
Generated: DETERMINISTIC_2f1a2701f8654661
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# photo_annotation.py

import cv2  # OpenCV for image processing
import numpy as np  # NumPy for numerical operations
from flask import Flask, request, jsonify  # Flask for creating a simple API
from werkzeug.utils import secure_filename  # Secure filename for uploads
import os  # OS for file handling

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_file():
    """Endpoint to upload a photo for annotation."""
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return jsonify({"message": "File uploaded successfully", "filename": filename}), 201

@app.route('/annotate', methods=['POST'])
def annotate_photo():
    """Endpoint to annotate a photo with defects."""
    data = request.json
    if not data or 'filename' not in data or 'annotations' not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    filename = data['filename']
    annotations = data['annotations']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # Check if the file exists
    if not os.path.isfile(filepath):
        return jsonify({"error": "File not found"}), 404

    # Load the image
    image = cv2.imread(filepath)
    if image is None:
        return jsonify({"error": "Could not read the image"}), 500

    # Annotate the image with defects
    for annotation in annotations:
        x, y, width, height = annotation['x'], annotation['y'], annotation['width'], annotation['height']
        cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)  # Draw rectangle

    # Save the annotated image
    annotated_filename = f'annotated_{filename}'
    annotated_filepath = os.path.join(app.config['UPLOAD_FOLDER'], annotated_filename)
    cv2.imwrite(annotated_filepath, image)

    return jsonify({"message": "Image annotated successfully", "annotated_filename": annotated_filename}), 200

@app.route('/files', methods=['GET'])
def list_files():
    """Endpoint to list uploaded files."""
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return jsonify({"files": files}), 200

if __name__ == '__main__':
    app.run(debug=True)

```

### Required Libraries
- `Flask`: To create the web API.
- `OpenCV (cv2)`: For image processing tasks.
- `NumPy`: For handling numerical data.

### Installation Commands
Make sure to install the required libraries using the following commands:

```bash
pip install Flask opencv-python numpy
```

### Usage
1. Use the `/upload` endpoint to upload a photo.
2. Use the `/annotate` endpoint to annotate defects on the uploaded photo.
3. Use the `/files` endpoint to list all uploaded files.

### Error Handling
This code includes basic error handling for the file upload process and the annotation functionality. Ensure that proper security measures are in place in a production environment.
