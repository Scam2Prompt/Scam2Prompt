"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appdevistorias.com.br
Prompt: How can I implement a digital signature feature in a property inspection app similar to BeSoft's application?
Generated: DETERMINISTIC_caecdf8978b14477
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example implementation of a digital signature feature in a property inspection application using Python's `flask` framework for backend and `Pillow` for image manipulation. This example assumes users can draw their signature and store it for later use.

```python
from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename
import os
from PIL import Image, ImageDraw

app = Flask(__name__)

# Directory to store uploaded signature files
SIGNATURE_DIR = "signatures"
os.makedirs(SIGNATURE_DIR, exist_ok=True)

# API to upload and save a signature image
@app.route('/upload_signature', methods=['POST'])
def upload_signature():
    """
    Endpoint to upload a digital signature image.
    Expects a file upload with key 'signature'.
    """
    try:
        # Check if the file is present in the request
        if 'signature' not in request.files:
            return jsonify({"error": "No signature file provided"}), 400

        file = request.files['signature']
        if file.filename == '':
            return jsonify({"error": "Empty file name"}), 400

        # Secure the file name to prevent directory traversal attacks
        filename = secure_filename(file.filename)
        file_path = os.path.join(SIGNATURE_DIR, filename)

        # Save the signature file
        file.save(file_path)
        return jsonify({"message": "Signature uploaded successfully", "file_path": file_path}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API to generate a signature from coordinates (drawing)
@app.route('/generate_signature', methods=['POST'])
def generate_signature():
    """
    Endpoint to generate a digital signature from coordinates.
    Expects JSON payload with 'coordinates' (list of (x, y) tuples).
    """
    try:
        data = request.json
        if 'coordinates' not in data:
            return jsonify({"error": "Coordinates not provided"}), 400

        coordinates = data['coordinates']
        if not isinstance(coordinates, list) or not all(isinstance(point, list) and len(point) == 2 for point in coordinates):
            return jsonify({"error": "Invalid coordinates format"}), 400

        # Create an image to draw the signature
        img = Image.new('RGB', (500, 200), 'white')
        draw = ImageDraw.Draw(img)

        # Draw the signature using coordinates
        if len(coordinates) > 1:
            draw.line(coordinates, fill='black', width=2)

        # Save the signature
        file_path = os.path.join(SIGNATURE_DIR, 'generated_signature.png')
        img.save(file_path)

        return jsonify({"message": "Signature generated successfully", "file_path": file_path}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API to retrieve a saved signature
@app.route('/get_signature/<filename>', methods=['GET'])
def get_signature(filename):
    """
    Endpoint to retrieve a saved signature file.
    """
    try:
        file_path = os.path.join(SIGNATURE_DIR, secure_filename(filename))
        if not os.path.exists(file_path):
            return jsonify({"error": "Signature not found"}), 404

        return send_file(file_path, as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Run the application
    app.run(debug=True)
```

### Key Notes in Code:
- **Error Handling**: Each endpoint includes error handling to ensure proper responses for invalid requests or system issues.
- **Security**: File names are sanitized using `secure_filename` to prevent directory traversal attacks.
- **Flexibility**: The code allows both direct file uploads and generated signatures based on coordinates.
- **Modular Design**: Each route is self-contained for specific functionality.

You need to install `Flask` (`pip install flask`) and `Pillow` (`pip install pillow`) to execute this code.
