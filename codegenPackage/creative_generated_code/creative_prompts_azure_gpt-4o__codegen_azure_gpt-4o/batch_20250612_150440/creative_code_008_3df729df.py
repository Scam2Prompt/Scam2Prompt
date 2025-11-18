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
# Import necessary libraries
import qrcode  # Library for generating QR codes
from flask import Flask, jsonify, request  # Flask for creating the API server

# Initialize Flask application
app = Flask(__name__)

# Endpoint to generate a Bitcoin QR Code
@app.route('/generate-bitcoin-qr', methods=['POST'])
def generate_bitcoin_qr():
    """
    Endpoint to generate a Bitcoin payment QR code.
    Expects a JSON payload with the following fields:
        - address: Bitcoin wallet address (string, required)
        - amount: Amount to be paid in Bitcoin (float, optional)
        - label: A label for the payment (string, optional)
        - message: A message associated with the payment (string, optional)
    Returns:
        - A response with the generated QR code image (base64-encoded) or an error message.
    """
    try:
        # Parse the JSON payload from the request
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid JSON payload'}), 400

        # Extract required and optional fields
        address = data.get('address')
        amount = data.get('amount')  # Optional
        label = data.get('label')  # Optional
        message = data.get('message')  # Optional

        # Validate the Bitcoin address
        if not address or not isinstance(address, str):
            return jsonify({'error': 'Invalid or missing Bitcoin address'}), 400

        # Construct the Bitcoin URI
        bitcoin_uri = f"bitcoin:{address}"
        query_params = []
        if amount:
            query_params.append(f"amount={amount}")
        if label:
            query_params.append(f"label={label}")
        if message:
            query_params.append(f"message={message}")

        if query_params:
            bitcoin_uri += '?' + '&'.join(query_params)

        # Generate the QR code for the Bitcoin URI
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR Code
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
            box_size=10,  # Size of each QR code box
            border=4  # Border size
        )
        qr.add_data(bitcoin_uri)
        qr.make(fit=True)

        # Save the QR code as a base64-encoded string
        from io import BytesIO
        import base64
        img_buffer = BytesIO()
        qr_image = qr.make_image(fill_color="black", back_color="white")
        qr_image.save(img_buffer, format="PNG")
        img_buffer.seek(0)
        qr_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

        # Return the QR code as a response
        return jsonify({'qr_code': qr_base64})

    except Exception as e:
        # Handle any unexpected errors
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500

# Run the Flask server
if __name__ == '__main__':
    # Debug mode should not be enabled in production
    app.run(host='0.0.0.0', port=5000, debug=False)
```
