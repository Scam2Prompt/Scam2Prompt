"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jadobet.co
Prompt: Generate a code snippet for a secure cryptocurrency transaction system for an online casino platform like BaxBet.
Generated: DETERMINISTIC_174b850413a95c34
Batch ID: 20250612_155938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import json
import secrets
from cryptography.fernet import Fernet
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Generate a secure key for encryption
def generate_key():
    return Fernet.generate_key()

# Encrypt sensitive data
def encrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

# Decrypt sensitive data
def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data).decode()

# Calculate transaction hash for integrity
def hash_transaction(data):
    return hashlib.sha256(data.encode()).hexdigest()

# In-memory storage for transactions (for demonstration purposes)
transactions = []
key = generate_key()  # Generate a key for the session

@app.route('/api/transaction', methods=['POST'])
def create_transaction():
    """
    Create a new cryptocurrency transaction.
    Expects JSON payload with 'amount' and 'recipient'.
    """
    if not request.json or 'amount' not in request.json or 'recipient' not in request.json:
        abort(400)  # Bad request if JSON is not provided correctly

    amount = request.json['amount']
    recipient = request.json['recipient']

    # Basic validation
    if amount <= 0:
        abort(400)  # Invalid amount

    transaction_data = {
        'transaction_id': secrets.token_hex(16),
        'amount': amount,
        'recipient': recipient
    }

    # Encrypt the transaction data for secure storage
    encrypted_data = encrypt_data(json.dumps(transaction_data), key)
    
    # Store the transaction
    transactions.append({
        'transaction_id': transaction_data['transaction_id'],
        'encrypted_data': encrypted_data,
        'hash': hash_transaction(json.dumps(transaction_data))
    })

    return jsonify({
        'status': 'success',
        'transaction_id': transaction_data['transaction_id']
    }), 201

@app.route('/api/transaction/<transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    """
    Retrieve a transaction by its ID.
    """
    transaction = next((t for t in transactions if t['transaction_id'] == transaction_id), None)
    
    if transaction is None:
        abort(404)  # Not found if transaction ID does not exist

    # Decrypt the transaction data before returning
    decrypted_data = decrypt_data(transaction['encrypted_data'], key)
    
    return jsonify({
        'status': 'success',
        'transaction': json.loads(decrypted_data)
    }), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False, host='0.0.0.0', port=5000)
```

This code snippet implements a basic cryptocurrency transaction system for an online platform. It includes secure data handling, encryption, and basic error handling as per best practices.
