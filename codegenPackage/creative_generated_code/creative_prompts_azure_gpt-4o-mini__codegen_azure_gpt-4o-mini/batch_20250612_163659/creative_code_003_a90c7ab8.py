"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadots.work
Prompt: Develop a tool that converts URLs into QR codes without displaying the link, similar to the free tool featured on コピーツールラボ.
Generated: DETERMINISTIC_a90c7ab8c43e025a
Batch ID: 20250612_163659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
from flask import Flask, request, send_file, jsonify
import os
import io

app = Flask(__name__)

# Ensure the output directory exists
OUTPUT_DIR = 'qr_codes'
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    """Endpoint to generate a QR code from a URL.

    Expects a JSON payload with a 'url' key.
    Returns the generated QR code image in PNG format.
    """
    try:
        data = request.get_json()
        url = data.get('url')

        # Validate the input
        if not url:
            return jsonify({"error": "No URL provided"}), 400

        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to a bytes buffer
        img_buffer = io.BytesIO()
        img.save(img_buffer, format='PNG')
        img_buffer.seek(0)

        # Send the generated QR code image back to the user
        return send_file(img_buffer, mimetype='image/png', as_attachment=True, download_name='qr_code.png')

    except Exception as e:
        # Generic error handling
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
