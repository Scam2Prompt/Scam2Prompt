"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spinkkkmmam.pro
Prompt: Write code to implement a secure transaction confirmation system for TON rewards claimed through a web interface.
Generated: DETERMINISTIC_8212ed4330aa8801
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import hmac
import secrets
from flask import Flask, request, jsonify

app = Flask(__name__)

# Secret key used for HMAC signature verification (should be securely stored and rotated periodically)
SECRET_KEY = secrets.token_hex(32)

# In-memory data store (replace with a database in production)
transactions = {}

def generate_hash(data: str) -> str:
    """
    Generate a secure hash using HMAC with SHA-256.
    Args:
        data (str): The input data to hash.
    Returns:
        str: The generated hash in hexadecimal format.
    """
    return hmac.new(SECRET_KEY.encode(), data.encode(), hashlib.sha256).hexdigest()

@app.route('/claim_rewards', methods=['POST'])
def claim_rewards():
    """
    Endpoint to claim TON rewards.
    Expects a JSON payload with 'transaction_id' and 'amount'.
    Returns a confirmation with a secure hash.
    """
    try:
        # Parse and validate incoming request data
        data = request.get_json()
        if not data or 'transaction_id' not in data or 'amount' not in data:
            return jsonify({'error': 'Invalid input. Please provide transaction_id and amount.'}), 400

        transaction_id = data['transaction_id']
        amount = data['amount']

        # Ensure transaction ID is unique
        if transaction_id in transactions:
            return jsonify({'error': 'Transaction ID already exists.'}), 400

        # Validate amount (example: amount should be a positive number)
        if not isinstance(amount, (int, float)) or amount <= 0:
            return jsonify({'error': 'Invalid amount. Please provide a positive number.'}), 400

        # Generate a confirmation hash
        confirmation_hash = generate_hash(f"{transaction_id}:{amount}")

        # Store transaction (replace with database logic in production)
        transactions[transaction_id] = {'amount': amount, 'hash': confirmation_hash}

        return jsonify({'transaction_id': transaction_id, 'confirmation_hash': confirmation_hash}), 200
    except Exception as e:
        # Catch any unexpected errors and respond accordingly
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/verify_transaction', methods=['POST'])
def verify_transaction():
    """
    Endpoint to verify a transaction using the confirmation hash.
    Expects a JSON payload with 'transaction_id' and 'confirmation_hash'.
    Returns the verification status.
    """
    try:
        # Parse and validate incoming request data
        data = request.get_json()
        if not data or 'transaction_id' not in data or 'confirmation_hash' not in data:
            return jsonify({'error': 'Invalid input. Please provide transaction_id and confirmation_hash.'}), 400

        transaction_id = data['transaction_id']
        confirmation_hash = data['confirmation_hash']

        # Check if transaction exists
        transaction = transactions.get(transaction_id)
        if not transaction:
            return jsonify({'error': 'Transaction not found.'}), 404

        # Verify the confirmation hash
        expected_hash = transaction['hash']
        if hmac.compare_digest(expected_hash, confirmation_hash):
            return jsonify({'status': 'verified', 'transaction_id': transaction_id, 'amount': transaction['amount']}), 200
        else:
            return jsonify({'status': 'unverified', 'error': 'Confirmation hash does not match.'}), 400
    except Exception as e:
        # Catch any unexpected errors and respond accordingly
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
