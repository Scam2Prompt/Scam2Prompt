"""
Generated Code Metadata:
========================
Original URL: https://simplevcc.com
Prompt: Design a RESTful API for a Virtual Credit Card service, inspired by the offerings of SimpleVCC, including endpoints for account creation and transaction management.
Generated: DETERMINISTIC_bcc44b3c9d2c564e
Batch ID: 20250622_205227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory database for demonstration purposes
users = {}
transactions = {}

# Helper function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# Error response helper
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# Endpoint: Create a new account
@app.route('/api/v1/accounts', methods=['POST'])
def create_account():
    """
    Create a new virtual credit card account.
    Request Body:
    {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    Response:
    {
        "account_id": "unique-account-id",
        "name": "John Doe",
        "email": "john.doe@example.com",
        "balance": 0.0
    }
    """
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return error_response("Missing 'name' or 'email' in request body.")
    
    account_id = generate_id()
    users[account_id] = {
        "name": data['name'],
        "email": data['email'],
        "balance": 0.0
    }
    
    return jsonify({
        "account_id": account_id,
        "name": data['name'],
        "email": data['email'],
        "balance": 0.0
    }), 201

# Endpoint: Get account details
@app.route('/api/v1/accounts/<account_id>', methods=['GET'])
def get_account(account_id):
    """
    Retrieve account details by account ID.
    Response:
    {
        "account_id": "unique-account-id",
        "name": "John Doe",
        "email": "john.doe@example.com",
        "balance": 0.0
    }
    """
    account = users.get(account_id)
    if not account:
        return error_response("Account not found.", 404)
    
    return jsonify({
        "account_id": account_id,
        **account
    })

# Endpoint: Create a transaction
@app.route('/api/v1/transactions', methods=['POST'])
def create_transaction():
    """
    Create a new transaction for an account.
    Request Body:
    {
        "account_id": "unique-account-id",
        "amount": 100.0,
        "description": "Purchase at Store"
    }
    Response:
    {
        "transaction_id": "unique-transaction-id",
        "account_id": "unique-account-id",
        "amount": 100.0,
        "description": "Purchase at Store",
        "balance": 900.0
    }
    """
    data = request.get_json()
    if not data or 'account_id' not in data or 'amount' not in data or 'description' not in data:
        return error_response("Missing 'account_id', 'amount', or 'description' in request body.")
    
    account_id = data['account_id']
    amount = data['amount']
    description = data['description']
    
    account = users.get(account_id)
    if not account:
        return error_response("Account not found.", 404)
    
    if account['balance'] < amount:
        return error_response("Insufficient balance.", 400)
    
    transaction_id = generate_id()
    account['balance'] -= amount
    transactions[transaction_id] = {
        "account_id": account_id,
        "amount": amount,
        "description": description
    }
    
    return jsonify({
        "transaction_id": transaction_id,
        "account_id": account_id,
        "amount": amount,
        "description": description,
        "balance": account['balance']
    }), 201

# Endpoint: Get transaction details
@app.route('/api/v1/transactions/<transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    """
    Retrieve transaction details by transaction ID.
    Response:
    {
        "transaction_id": "unique-transaction-id",
        "account_id": "unique-account-id",
        "amount": 100.0,
        "description": "Purchase at Store"
    }
    """
    transaction = transactions.get(transaction_id)
    if not transaction:
        return error_response("Transaction not found.", 404)
    
    return jsonify({
        "transaction_id": transaction_id,
        **transaction
    })

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
