"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coin-qr.to
Prompt: Write a tutorial for integrating a Bitcoin QR Code generator into a cryptocurrency payment system, using the features described on coin-qr.to.
Generated: DETERMINISTIC_3df729df2bd79b96
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
from flask import Flask, request, jsonify
from urllib.parse import urlencode

app = Flask(__name__)

# Function to generate a Bitcoin payment URI
def generate_bitcoin_uri(address, amount=None, label=None, message=None):
    """
    Generate a Bitcoin payment URI.

    :param address: The Bitcoin wallet address
    :param amount: The amount to request, in BTC (optional)
    :param label: A label for the transaction (optional)
    :param message: A message for the transaction (optional)
    :return: A formatted Bitcoin URI
    """
    uri = f"bitcoin:{address}"
    params = {}
    
    if amount:
        params['amount'] = amount
    if label:
        params['label'] = label
    if message:
        params['message'] = message
    
    if params:
        uri += '?' + urlencode(params)
    
    return uri

# Function to generate a QR code image for the Bitcoin URI
def generate_qr_code(data):
    """
    Generate a QR code for the given data.

    :param data: The data to encode in the QR code
    :return: QR code image
    """
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        return img
    except Exception as e:
        raise RuntimeError("Failed to generate QR code") from e

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    """
    API endpoint to generate a Bitcoin QR code.

    :return: JSON response containing the QR code image URL
    """
    data = request.json

    # Validate incoming JSON data
    required_fields = ['address']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400
    
    address = data['address']
    amount = data.get('amount')
    label = data.get('label')
    message = data.get('message')

    try:
        # Generate the Bitcoin URI
        bitcoin_uri = generate_bitcoin_uri(address, amount, label, message)

        # Generate the QR code
        qr_code_image = generate_qr_code(bitcoin_uri)

        # Save the QR code image to a file
        qr_code_image_path = 'qrcode.png'
        qr_code_image.save(qr_code_image_path)

        # Return the path to the generated QR code image
        return jsonify({"qr_code_url": qr_code_image_path}), 200

    except RuntimeError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=True for development; use False in production
```

This code provides a simple Flask application that integrates a Bitcoin QR Code generator using the coin-qr.to features. It includes functions to generate a Bitcoin URI and a QR code, and it handles basic input validation and error handling. The generated QR code is saved as a PNG file.
