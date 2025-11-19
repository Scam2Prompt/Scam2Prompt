"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monero-qr-code-generator.com
Prompt: Provide an example of a Monero QR Code generation API call and explain how it can be used in a web application for cryptocurrency payments.
Generated: DETERMINISTIC_0ba9ba048c06023f
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
from flask import Flask, jsonify, request

app = Flask(__name__)

# Function to generate a Monero QR Code
def generate_monero_qr(address, amount=None, payment_id=None):
    """
    Generates a Monero QR Code.

    Parameters:
        address (str): The Monero wallet address.
        amount (float, optional): Amount to send (in XMR).
        payment_id (str, optional): Payment ID for the transaction.

    Returns:
        str: Path to the generated QR Code image.
    """
    # Validate wallet address (basic validation, can be expanded)
    if not address or len(address) < 95 or len(address) > 106:
        raise ValueError("Invalid Monero wallet address.")

    # Base URI for Monero
    monero_uri = f"monero:{address}"
    
    # Append optional parameters if provided
    params = []
    if amount:
        params.append(f"amount={amount}")
    if payment_id:
        params.append(f"payment_id={payment_id}")
    if params:
        monero_uri += "?" + "&".join(params)

    # Generate the QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(monero_uri)
    qr.make(fit=True)

    # Save the QR Code as an image
    qr_image_path = f"{address}_monero_qr.png"
    img = qr.make_image(fill="black", back_color="white")
    img.save(qr_image_path)

    return qr_image_path

@app.route('/generate_qr', methods=['POST'])
def generate_qr_endpoint():
    """
    Endpoint to generate a Monero QR Code.

    Request JSON Structure:
        {
            "address": "Monero wallet address",
            "amount": Optional amount in XMR,
            "payment_id": Optional payment ID
        }

    Response:
        JSON containing the path to the generated QR Code image.
    """
    try:
        # Parse JSON request
        data = request.get_json()
        if not data or 'address' not in data:
            return jsonify({"error": "Invalid request. 'address' is required."}), 400

        # Extract parameters
        address = data['address']
        amount = data.get('amount')
        payment_id = data.get('payment_id')

        # Generate QR Code
        qr_image_path = generate_monero_qr(address, amount, payment_id)

        # Return the path to the generated QR Code
        return jsonify({"qr_image_path": qr_image_path}), 200

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    # Run the server
    app.run(debug=True)
```
