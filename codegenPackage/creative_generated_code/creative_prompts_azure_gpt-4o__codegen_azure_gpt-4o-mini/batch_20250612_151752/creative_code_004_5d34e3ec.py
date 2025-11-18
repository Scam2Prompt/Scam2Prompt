"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paywithcrypto.pages.dev
Prompt: Develop a secure and decentralized payment system using cryptocurrency, incorporating QR code scanning and manual wallet payment instructions similar to the features on the "Pay With Crypto" website.
Generated: DETERMINISTIC_5d34e3ec28dfdb9b
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
import hashlib
import json
import requests
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from web3 import Web3

# Initialize Flask app and CORS
app = Flask(__name__)
CORS(app)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing payment transactions
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wallet_address = db.Column(db.String(42), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)

# Initialize database
db.create_all()

# Function to generate QR code for payment
def generate_qr_code(wallet_address, amount):
    """Generate a QR code for the payment."""
    data = json.dumps({"address": wallet_address, "amount": amount})
    qr = qrcode.make(data)
    qr_path = f"qr_codes/{wallet_address}_{amount}.png"
    qr.save(qr_path)
    return qr_path

@app.route('/create_payment', methods=['POST'])
def create_payment():
    """Endpoint to create a new payment."""
    try:
        data = request.json
        wallet_address = data['wallet_address']
        amount = data['amount']

        # Validate inputs
        if not Web3.isAddress(wallet_address):
            return jsonify({"error": "Invalid wallet address"}), 400
        if amount <= 0:
            return jsonify({"error": "Amount must be greater than zero"}), 400

        # Create payment record
        new_payment = Payment(wallet_address=wallet_address, amount=amount, status='Pending')
        db.session.add(new_payment)
        db.session.commit()

        # Generate QR code
        qr_code_path = generate_qr_code(wallet_address, amount)

        return jsonify({
            "message": "Payment created successfully",
            "payment_id": new_payment.id,
            "qr_code_path": qr_code_path
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/payment_status/<int:payment_id>', methods=['GET'])
def payment_status(payment_id):
    """Endpoint to check the status of a payment."""
    try:
        payment = Payment.query.get(payment_id)
        if not payment:
            return jsonify({"error": "Payment not found"}), 404

        return jsonify({
            "payment_id": payment.id,
            "wallet_address": payment.wallet_address,
            "amount": payment.amount,
            "status": payment.status
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/webhook', methods=['POST'])
def webhook():
    """Webhook to update payment status (mock implementation)."""
    try:
        data = request.json
        payment_id = data['payment_id']
        status = data['status']

        payment = Payment.query.get(payment_id)
        if not payment:
            return jsonify({"error": "Payment not found"}), 404
        
        # Update payment status
        payment.status = status
        db.session.commit()

        return jsonify({"message": "Payment status updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

**Note**: Make sure you have the necessary dependencies installed in your Python environment for this code to run:

```bash
pip install Flask Flask-SQLAlchemy Flask-CORS qrcode[pil] web3
```

Ensure to adjust the database URI (`SQLALCHEMY_DATABASE_URI`) as needed for your production environment.
