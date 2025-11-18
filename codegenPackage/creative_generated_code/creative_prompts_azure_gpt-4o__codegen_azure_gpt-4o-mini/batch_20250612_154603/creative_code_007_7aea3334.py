"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accesslinklimited.com
Prompt: Create a Python program to simulate the deposit process described on Access Link Limited, including QR code generation for cryptocurrency payments.
Generated: DETERMINISTIC_7aea3334f4d31412
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
import random
import string
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated database for storing deposits
deposits_db = {}

def generate_unique_reference():
    """Generate a unique reference code for each deposit."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

def create_qr_code(data):
    """Generate a QR code and save it as an image file."""
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    filename = f"qr_code_{data}.png"
    img.save(filename)
    return filename

@app.route('/deposit', methods=['POST'])
def deposit():
    """Endpoint to handle cryptocurrency deposit requests."""
    try:
        # Parse request data
        request_data = request.get_json()
        amount = request_data.get('amount')
        currency = request_data.get('currency')

        # Input validation
        if not isinstance(amount, (int, float)) or amount <= 0:
            return jsonify({"error": "Invalid amount. It must be a positive number."}), 400
        if not currency:
            return jsonify({"error": "Currency must be specified."}), 400

        # Create a unique reference for the deposit
        reference = generate_unique_reference()

        # Simulate storing the deposit in the database
        deposits_db[reference] = {
            "amount": amount,
            "currency": currency,
            "status": "pending"
        }

        # Generate payment link (simulated)
        payment_link = f"crypto_payment://{currency}/{amount}/{reference}"

        # Create a QR code for the payment
        qr_code_filename = create_qr_code(payment_link)

        # Return the reference and QR code filename
        return jsonify({
            "reference": reference,
            "qr_code": qr_code_filename,
            "status": "pending"
        }), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

@app.route('/status/<reference>', methods=['GET'])
def check_status(reference):
    """Endpoint to check the status of a deposit."""
    deposit_info = deposits_db.get(reference)
    if deposit_info:
        return jsonify({
            "reference": reference,
            "amount": deposit_info["amount"],
            "currency": deposit_info["currency"],
            "status": deposit_info["status"]
        }), 200
    else:
        return jsonify({"error": "Deposit not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)
```

**Requirements:**
- To run this code, ensure you have Flask and qrcode installed:
  ```bash
  pip install Flask qrcode[pil]
  ```
- Start the Flask server and use tools like Postman or curl to test the deposit and status endpoints.
