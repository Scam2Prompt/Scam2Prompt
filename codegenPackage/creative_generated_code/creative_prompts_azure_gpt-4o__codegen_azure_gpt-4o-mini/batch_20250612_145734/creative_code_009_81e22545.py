"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thephantomvault.com
Prompt: Generate code to securely handle cryptocurrency payments through anonymous channels, inspired by The Phantom Vault's payment system.
Generated: DETERMINISTIC_81e22545603d9727
Batch ID: 20250612_145734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import hashlib
import secrets
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify

app = Flask(__name__)

# Generate a key for encrypting payment data
def generate_key():
    return Fernet.generate_key()

# Encrypt payment data to secure it before storage or transmission
def encrypt_data(data, key):
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

# Decrypt payment data when needed
def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    try:
        decrypted_data = fernet.decrypt(encrypted_data).decode()
        return decrypted_data
    except Exception as e:
        print(f"Decryption error: {e}")
        return None

# Hash sensitive data for integrity checks
def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Payment class handling the storage and validation of payment details
class Payment:
    def __init__(self, amount, recipient):
        self.amount = amount
        self.recipient = recipient
        self.transaction_id = secrets.token_hex(16)
        self.key = generate_key()
        self.encrypted_data = encrypt_data(f"{amount}:{recipient}", self.key)
        self.hash = hash_data(self.encrypted_data.decode())

# In-memory storage for payments (for demonstration purposes)
payments_db = {}

@app.route('/create_payment', methods=['POST'])
def create_payment():
    try:
        # Parse JSON request body
        data = request.json
        amount = data['amount']
        recipient = data['recipient']

        # Validate input data
        if amount <= 0 or not recipient:
            return jsonify({"error": "Invalid payment data"}), 400
        
        # Create a new payment
        payment = Payment(amount, recipient)
        payments_db[payment.transaction_id] = {
            'encrypted_data': payment.encrypted_data,
            'hash': payment.hash
        }

        return jsonify({"transaction_id": payment.transaction_id}), 201
    except KeyError as e:
        return jsonify({"error": f"Missing key: {e}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_payment/<transaction_id>', methods=['GET'])
def get_payment(transaction_id):
    try:
        # Retrieve payment details using transaction ID
        payment_record = payments_db.get(transaction_id)
        if not payment_record:
            return jsonify({"error": "Payment not found"}), 404
        
        # Decrypt the payment data
        decrypted_data = decrypt_data(payment_record['encrypted_data'], payment_record['hash'])
        if decrypted_data is None:
            return jsonify({"error": "Failed to decrypt payment data"}), 500
        
        return jsonify({"transaction_id": transaction_id, "data": decrypted_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```
