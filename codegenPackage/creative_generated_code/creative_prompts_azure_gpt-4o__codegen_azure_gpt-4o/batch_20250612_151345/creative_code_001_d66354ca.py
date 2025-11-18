"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foodandwine.one
Prompt: Create an API design for managing user accounts in an online gambling platform like Hi88, including endpoints for registration, login, deposit, withdrawal, and transaction history.
Generated: DETERMINISTIC_d66354ca0bf3c182
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

app = Flask(__name__)

# In-memory database for demonstration purposes
users = {}
transactions = {}

# Helper function to validate the deposit and withdrawal amounts
def validate_amount(amount):
    if amount <= 0:
        return False
    return True

@app.route('/register', methods=['POST'])
def register():
    """
    Endpoint for user registration.
    Requires: username, password.
    """
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # Validate input
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    if username in users:
        return jsonify({"error": "User already exists"}), 400
    
    # Hash the password for security
    hashed_password = generate_password_hash(password)
    users[username] = {
        "id": str(uuid.uuid4()),
        "username": username,
        "password": hashed_password,
        "balance": 0.0
    }
    
    return jsonify({"message": "Registration successful", "user_id": users[username]['id']}), 201


@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint for user login.
    Requires: username, password.
    """
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # Validate input
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = users.get(username)

    if not user or not check_password_hash(user['password'], password):
        return jsonify({"error": "Invalid username or password"}), 401
    
    return jsonify({"message": "Login successful", "user_id": user['id']}), 200


@app.route('/deposit', methods=['POST'])
def deposit():
    """
    Endpoint for depositing money into a user's account.
    Requires: username, amount.
    """
    data = request.json
    username = data.get('username')
    amount = data.get('amount')

    # Validate input
    if not username or amount is None:
        return jsonify({"error": "Username and deposit amount are required"}), 400

    if not validate_amount(amount):
        return jsonify({"error": "Invalid deposit amount"}), 400

    user = users.get(username)

    if not user:
        return jsonify({"error": "User not found"}), 404

    user['balance'] += amount

    # Record the transaction
    transaction_id = str(uuid.uuid4())
    transactions[transaction_id] = {
        "user_id": user['id'],
        "type": "deposit",
        "amount": amount,
        "balance_after": user['balance']
    }

    return jsonify({"message": "Deposit successful", "balance": user['balance']}), 200


@app.route('/withdraw', methods=['POST'])
def withdraw():
    """
    Endpoint for withdrawing money from a user's account.
    Requires: username, amount.
    """
    data = request.json
    username = data.get('username')
    amount = data.get('amount')

    # Validate input
    if not username or amount is None:
        return jsonify({"error": "Username and withdrawal amount are required"}), 400

    if not validate_amount(amount):
        return jsonify({"error": "Invalid withdrawal amount"}), 400

    user = users.get(username)

    if not user:
        return jsonify({"error": "User not found"}), 404

    if user['balance'] < amount:
        return jsonify({"error": "Insufficient balance"}), 400

    user['balance'] -= amount

    # Record the transaction
    transaction_id = str(uuid.uuid4())
    transactions[transaction_id] = {
        "user_id": user['id'],
        "type": "withdrawal",
        "amount": amount,
        "balance_after": user['balance']
    }

    return jsonify({"message": "Withdrawal successful", "balance": user['balance']}), 200


@app.route('/transaction_history', methods=['GET'])
def transaction_history():
    """
    Endpoint for retrieving transaction history.
    Requires: username.
    """
    username = request.args.get('username')

    # Validate input
    if not username:
        return jsonify({"error": "Username is required"}), 400

    user = users.get(username)

    if not user:
        return jsonify({"error": "User not found"}), 404

    user_transactions = [
        {"transaction_id": tid, "type": t['type'], "amount": t['amount'], "balance_after": t['balance_after']}
        for tid, t in transactions.items() if t['user_id'] == user['id']
    ]

    return jsonify({"transactions": user_transactions}), 200


# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
