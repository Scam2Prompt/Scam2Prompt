"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://energiakert.com
Prompt: Write a code snippet that demonstrates how to implement secure payment processing for an e-commerce site like EnergiaKert using advanced encryption methods.
Generated: DETERMINISTIC_b7cde0a23f2c3835
Batch ID: 20250612_155446
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
import logging
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Generate a secure key for encryption and decryption
def generate_key():
    return Fernet.generate_key()

# Load the encryption key from environment variable or generate a new one
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY", generate_key())
cipher = Fernet(ENCRYPTION_KEY)

# Sample payment data structure
class Payment:
    def __init__(self, amount, card_number, card_expiry, cvv):
        self.amount = amount
        self.card_number = card_number
        self.card_expiry = card_expiry
        self.cvv = cvv

    def to_json(self):
        return json.dumps({
            "amount": self.amount,
            "card_number": cipher.encrypt(self.card_number.encode()).decode(),
            "card_expiry": cipher.encrypt(self.card_expiry.encode()).decode(),
            "cvv": cipher.encrypt(self.cvv.encode()).decode(),
        })

# Payment processing endpoint
@app.route('/process_payment', methods=['POST'])
def process_payment():
    try:
        # Get payment data from the request
        data = request.json
        logging.info("Received payment data: %s", data)

        # Validate incoming data
        if not all(key in data for key in ('amount', 'card_number', 'card_expiry', 'cvv')):
            return jsonify({"error": "Missing payment information"}), 400
        
        # Create payment instance
        payment = Payment(data['amount'], data['card_number'], data['card_expiry'], data['cvv'])
        
        # Here you would normally process the payment with a payment processor
        # For simulation, we'll just log the payment information
        logging.info("Processing payment: %s", payment.to_json())
        
        # Simulate payment processing result
        return jsonify({"message": "Payment processed successfully"}), 200

    except Exception as e:
        logging.error("Error processing payment: %s", str(e))
        return jsonify({"error": "An error occurred while processing the payment"}), 500

if __name__ == '__main__':
    # Run the application
    app.run(host='0.0.0.0', port=5000)
```

### Note:
- Make sure to set the environment variable `ENCRYPTION_KEY` for production or it will generate a new key each time.
- Replace the payment processing simulation with actual integration with a payment gateway for real-world use.
