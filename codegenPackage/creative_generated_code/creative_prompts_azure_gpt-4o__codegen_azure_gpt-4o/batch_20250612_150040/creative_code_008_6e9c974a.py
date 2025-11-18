"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fantom.de
Prompt: Develop a script for photo and graphic editing on a website, utilizing Fantom Internet Dienst's expertise in photo and video processing.
Generated: DETERMINISTIC_6e9c974a14dc36ab
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready Python script using Flask for the backend and Pillow for image processing. This script allows users to upload a photo, apply basic edits (resize, rotate, grayscale), and download the edited photo.

```python
from flask import Flask, request, send_file, jsonify
from PIL import Image, ImageOps
import os
import io

app = Flask(__name__)

# Define upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    """Check if the uploaded file's extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Endpoint to upload a file.
    Expects a file and optional edit parameters: resize, rotate, and grayscale.
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    # Check if a file is selected
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    # Validate file type
    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type. Only PNG, JPG, JPEG are allowed'}), 400

    try:
        # Open the image using PIL
        image = Image.open(file.stream)

        # Parse optional parameters (resize, rotate, grayscale)
        resize = request.form.get('resize')  # Expected format: "width,height"
        rotate = request.form.get('rotate')  # Expected format: degrees (integer)
        grayscale = request.form.get('grayscale')  # Expected format: "true"

        # Resize the image if 'resize' parameter is specified
        if resize:
            try:
                width, height = map(int, resize.split(','))
                image = image.resize((width, height))
            except ValueError:
                return jsonify({'error': 'Invalid resize parameters. Expected format: width,height'}), 400

        # Rotate the image if 'rotate' parameter is specified
        if rotate:
            try:
                degrees = int(rotate)
                image = image.rotate(degrees)
            except ValueError:
                return jsonify({'error': 'Invalid rotate parameter. Expected an integer value'}), 400

        # Convert the image to grayscale if 'grayscale' parameter is set to true
        if grayscale and grayscale.lower() == 'true':
            image = ImageOps.grayscale(image)

        # Save the edited image to a temporary buffer
        output = io.BytesIO()
        image_format = image.format if image.format else 'JPEG'  # Default to JPEG if format is unknown
        image.save(output, format=image_format)
        output.seek(0)

        # Respond with the edited image
        return send_file(output, mimetype=f'image/{image_format.lower()}')

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': f'An error occurred while processing the image: {str(e)}'}), 500


@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'An internal server error occurred'}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### Key Features:
- Uploads photos securely with extension validation.
- Supports basic image editing: resize, rotate, and apply grayscale.
- Returns the edited image directly in the response.
- Handles common user and server errors with proper error messages.

To run this code:
1. Install Flask and Pillow packages: `pip install flask pillow`
2. Save the script as `app.py` and run it: `python app.py`
3. Use tools like `Postman` or `curl` to interact with the API.
