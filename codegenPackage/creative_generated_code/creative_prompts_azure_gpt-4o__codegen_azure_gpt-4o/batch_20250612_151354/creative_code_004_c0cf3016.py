"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enacip.edu.pe
Prompt: Suggest an API for managing certifications with QR codes, ensuring the generated codes are legally valid under Peruvian norms, as highlighted on the Enacip website.
Generated: DETERMINISTIC_c0cf301636321bc5
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from qrcode import make as make_qr
from io import BytesIO
import base64
import datetime
import os

app = Flask(__name__)

# Constants related to certification requirements
PERUVIAN_LEGAL_TEXT = "Certificación válida bajo normas peruanas según Enacip."
CERTIFICATES_DIR = "certificates"
QR_CODES_DIR = os.path.join(CERTIFICATES_DIR, "qr_codes")

# Ensure storage directories exist
os.makedirs(QR_CODES_DIR, exist_ok=True)

@app.route("/generate_certificate", methods=["POST"])
def generate_certificate():
    """
    Endpoint to generate a certification with a QR code.
    Expects a JSON payload with `name` and `details` attributes.
    """
    try:
        # Validate input
        data = request.json
        if not data or "name" not in data or "details" not in data:
            return jsonify({"error": "Invalid input. Provide 'name' and 'details'."}), 400
        
        name = data["name"]
        details = data["details"]

        # Generate certificate details
        certificate_id = f"CERT-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        certificate_content = f"ID: {certificate_id}\nName: {name}\nDetails: {details}\n{PERUVIAN_LEGAL_TEXT}"

        # Generate QR Code
        qr_data = f"ID={certificate_id}&Name={name}&Details={details}&LegalText={PERUVIAN_LEGAL_TEXT}"
        qr_code = make_qr(qr_data)
        qr_code_image = BytesIO()
        qr_code.save(qr_code_image)
        qr_code_image.seek(0)

        # Save QR code image to file
        qr_image_path = os.path.join(QR_CODES_DIR, f"{certificate_id}.png")
        with open(qr_image_path, "wb") as qr_file:
            qr_file.write(qr_code_image.getvalue())
        
        # Encode QR image in Base64 for API response
        qr_base64 = base64.b64encode(qr_code_image.getvalue()).decode()

        # Return response
        return jsonify({
            "certificate_id": certificate_id,
            "certificate_content": certificate_content,
            "qr_code_base64": qr_base64,
            "qr_code_file_path": qr_image_path,
        })
    
    except Exception as e:
        # Handle unexpected server errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route("/validate_certificate", methods=["POST"])
def validate_certificate():
    """
    Endpoint to validate a certification based on its ID.
    Expects a JSON payload with `certificate_id` attribute.
    """
    try:
        # Validate input
        data = request.json
        if not data or "certificate_id" not in data:
            return jsonify({"error": "Invalid input. Provide 'certificate_id'."}), 400
        
        certificate_id = data["certificate_id"]

        # Check if QR code exists
        qr_image_path = os.path.join(QR_CODES_DIR, f"{certificate_id}.png")
        if not os.path.exists(qr_image_path):
            return jsonify({"error": "Certificate not found or invalid."}), 404

        # Return validation status
        return jsonify({"certificate_id": certificate_id, "status": "Valid"}), 200
    
    except Exception as e:
        # Handle unexpected server errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
```
