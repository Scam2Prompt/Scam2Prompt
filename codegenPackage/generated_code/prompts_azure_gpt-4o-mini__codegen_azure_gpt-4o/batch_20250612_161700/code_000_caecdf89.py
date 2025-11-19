"""
Generated Code Metadata:
========================
Original URL: https://appdevistorias.com.br
Prompt: How can I implement a digital signature feature in a property inspection app similar to BeSoft's application?
Generated: DETERMINISTIC_caecdf8978b14477
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python implementation of a digital signature feature using Flask for a web-based property inspection app. It uses the `Pillow` library for image processing and `Flask` for the backend.

```python
from flask import Flask, request, jsonify, send_file
from PIL import Image, ImageDraw
import os
import io

app = Flask(__name__)

# Directory to store signed images
SIGNATURES_DIR = "signatures"
os.makedirs(SIGNATURES_DIR, exist_ok=True)

@app.route('/upload_signature', methods=['POST'])
def upload_signature():
    """
    Endpoint to upload a digital signature.
    Expects a JSON payload with 'signature_data' (base64-encoded image) and 'inspection_id'.
    """
    try:
        # Parse request data
        data = request.json
        signature_data = data.get('signature_data')
        inspection_id = data.get('inspection_id')

        if not signature_data or not inspection_id:
            return jsonify({"error": "Missing 'signature_data' or 'inspection_id'"}), 400

        # Decode the base64 image
        signature_image = Image.open(io.BytesIO(base64.b64decode(signature_data)))

        # Save the signature image
        signature_path = os.path.join(SIGNATURES_DIR, f"{inspection_id}_signature.png")
        signature_image.save(signature_path)

        return jsonify({"message": "Signature uploaded successfully", "path": signature_path}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/apply_signature', methods=['POST'])
def apply_signature():
    """
    Endpoint to apply a digital signature to a property inspection image.
    Expects a JSON payload with 'inspection_id' and 'inspection_image' (base64-encoded image).
    """
    try:
        # Parse request data
        data = request.json
        inspection_id = data.get('inspection_id')
        inspection_image_data = data.get('inspection_image')

        if not inspection_id or not inspection_image_data:
            return jsonify({"error": "Missing 'inspection_id' or 'inspection_image'"}), 400

        # Load the inspection image
        inspection_image = Image.open(io.BytesIO(base64.b64decode(inspection_image_data)))

        # Load the signature image
        signature_path = os.path.join(SIGNATURES_DIR, f"{inspection_id}_signature.png")
        if not os.path.exists(signature_path):
            return jsonify({"error": "Signature not found for the given inspection ID"}), 404

        signature_image = Image.open(signature_path)

        # Apply the signature to the inspection image (bottom-right corner)
        inspection_width, inspection_height = inspection_image.size
        signature_width, signature_height = signature_image.size
        position = (inspection_width - signature_width - 10, inspection_height - signature_height - 10)
        inspection_image.paste(signature_image, position, signature_image)

        # Save the signed inspection image
        signed_image_path = os.path.join(SIGNATURES_DIR, f"{inspection_id}_signed.png")
        inspection_image.save(signed_image_path)

        return jsonify({"message": "Signature applied successfully", "path": signed_image_path}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/get_signed_image/<inspection_id>', methods=['GET'])
def get_signed_image(inspection_id):
    """
    Endpoint to retrieve the signed inspection image.
    """
    try:
        signed_image_path = os.path.join(SIGNATURES_DIR, f"{inspection_id}_signed.png")
        if not os.path.exists(signed_image_path):
            return jsonify({"error": "Signed image not found"}), 404

        return send_file(signed_image_path, mimetype='image/png')

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements:
1. Install dependencies:
   ```bash
   pip install flask pillow
   ```

2. Ensure the app is running in a secure environment, especially when handling sensitive data like signatures.

3. Use HTTPS for secure communication in production.

4. Add authentication and authorization mechanisms to protect endpoints.
