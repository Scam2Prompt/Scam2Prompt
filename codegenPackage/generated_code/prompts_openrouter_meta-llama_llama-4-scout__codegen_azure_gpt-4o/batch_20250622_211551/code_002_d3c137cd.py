"""
Generated Code Metadata:
========================
Original URL: https://amexgiftcardbalance.net
Prompt: Generate a RESTful API endpoint to retrieve the balance of an Amex gift card, considering secure encryption and no expiration date.
Generated: DETERMINISTIC_d3c137cd545f3e96
Batch ID: 20250622_211551
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from cryptography.fernet import Fernet
import logging

# Initialize Flask app
app = Flask(__name__)

# Generate a secure encryption key (this should be stored securely in production)
# For demonstration purposes, we are generating it here.
ENCRYPTION_KEY = Fernet.generate_key()
cipher_suite = Fernet(ENCRYPTION_KEY)

# Mock database for gift card balances (In production, use a secure database)
gift_card_db = {
    "encrypted_card_1": cipher_suite.encrypt(b"100.00").decode(),  # Example encrypted balance
    "encrypted_card_2": cipher_suite.encrypt(b"250.50").decode(),
}

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/api/giftcard/balance', methods=['GET'])
def get_gift_card_balance():
    """
    Endpoint to retrieve the balance of an Amex gift card.
    Request Parameters:
        - card_id: The unique identifier of the gift card (encrypted).
    Response:
        - JSON object containing the balance or an error message.
    """
    try:
        # Retrieve card_id from query parameters
        card_id = request.args.get('card_id')
        if not card_id:
            return jsonify({"error": "Missing 'card_id' parameter"}), 400

        # Check if the card_id exists in the database
        encrypted_balance = gift_card_db.get(card_id)
        if not encrypted_balance:
            return jsonify({"error": "Gift card not found"}), 404

        # Decrypt the balance securely
        decrypted_balance = cipher_suite.decrypt(encrypted_balance.encode()).decode()

        # Return the balance as a JSON response
        return jsonify({"balance": decrypted_balance}), 200

    except Exception as e:
        # Log the error and return a generic error message
        logging.error(f"Error retrieving gift card balance: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
