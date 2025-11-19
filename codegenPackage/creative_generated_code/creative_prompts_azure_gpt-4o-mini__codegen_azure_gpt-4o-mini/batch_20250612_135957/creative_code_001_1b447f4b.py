"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anonymouscryptoexchange.com
Prompt: How can I implement a secure cryptocurrency exchange process without KYC verification in a web application? Include code examples for transaction handling.
Generated: DETERMINISTIC_1b447f4b66fc0133
Batch ID: 20250612_135957
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import hashlib
import uuid
import os

app = Flask(__name__)

# In-memory storage for users and transactions (replace with a database in production)
users = {}
transactions = []

def generate_transaction_id():
    """Generate a unique transaction ID."""
    return str(uuid.uuid4())

def hash_password(password):
    """Hash the user's password using SHA256 for secure storage."""
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate_user(api_key):
    """Authenticate user using a simple API key check."""
    return users.get(api_key)

@app.route('/register', methods=['POST'])
def register():
    """Endpoint to register a new user."""
    data = request.json
    username = data.get('username')
    password = data.get('password')
    api_key = str(uuid.uuid4())  # Generate a unique API key for the user

    if username in users:
        return jsonify({"message": "User already exists"}), 409

    # Store the user with hashed password
    users[api_key] = {
        "username": username,
        "password": hash_password(password),
        "balance": 0.0
    }

    return jsonify({"api_key": api_key}), 201

@app.route('/deposit', methods=['POST'])
def deposit():
    """Endpoint for depositing funds into a user's account."""
    data = request.json
    api_key = data.get('api_key')
    amount = data.get('amount')

    user = authenticate_user(api_key)
    if not user:
        return jsonify({"message": "Authentication failed"}), 403

    if amount <= 0:
        return jsonify({"message": "Invalid deposit amount"}), 400

    user['balance'] += amount
    return jsonify({"message": "Deposit successful", "new_balance": user['balance']}), 200

@app.route('/transaction', methods=['POST'])
def create_transaction():
    """Endpoint for creating a new transaction between users."""
    data = request.json
    api_key = data.get('api_key')
    recipient_username = data.get('recipient_username')
    amount = data.get('amount')

    user = authenticate_user(api_key)
    if not user:
        return jsonify({"message": "Authentication failed"}), 403

    if recipient_username not in users.values():
        return jsonify({"message": "Recipient does not exist"}), 404

    if amount <= 0 or amount > user['balance']:
        return jsonify({"message": "Invalid transaction amount"}), 400

    # Create the transaction
    transaction_id = generate_transaction_id()
    transactions.append({
        "id": transaction_id,
        "from": user['username'],
        "to": recipient_username,
        "amount": amount
    })

    # Update balances
    user['balance'] -= amount
    recipient_user = next((u for k, u in users.items() if u['username'] == recipient_username), None)
    recipient_user['balance'] += amount

    return jsonify({"message": "Transaction successful", "transaction_id": transaction_id}), 201

@app.route('/balance', methods=['GET'])
def get_balance():
    """Endpoint to get the user's balance."""
    api_key = request.args.get('api_key')
    user = authenticate_user(api_key)
    if not user:
        return jsonify({"message": "Authentication failed"}), 403

    return jsonify({"balance": user['balance']}), 200

if __name__ == '__main__':
    # Ensure the application runs with debug off in production
    app.run(host='0.0.0.0', port=5000, debug=False)
```

### Important Notes:
- This implementation uses an in-memory dictionary for user and transaction storage. In a production environment, replace this with a robust database solution.
- This code sample does not include full error logging, which would be crucial for production. Consider adding logging mechanisms.
- Ensure you handle sensitive information securely, such as using HTTPS for communication.
- Adjust security measures based on application requirements, including rate limiting and additional authentication processes.
