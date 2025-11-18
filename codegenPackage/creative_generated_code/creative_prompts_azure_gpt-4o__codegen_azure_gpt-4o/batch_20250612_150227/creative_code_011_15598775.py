"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalinstantmining.com
Prompt: Create a REST API to manage user accounts, deposits, and withdrawals securely, inspired by the account management features of Globalinstantmining.
Generated: DETERMINISTIC_15598775e7c7fc1b
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for the requested REST API, written in Python using the Flask framework:

```python
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

app = Flask(__name__)

# In-memory database for demonstration purposes
users = {}

# Helper function to generate unique account IDs
def generate_account_id():
    return str(uuid.uuid4())

@app.route('/users', methods=['POST'])
def create_user():
    """
    Endpoint to create a new user account.
    Request Body:
    {
        "username": "example_user",
        "password": "example_password"
    }
    """
    data = request.get_json()

    # Input validation
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Invalid input"}), 400

    username = data['username']
    password = data['password']

    # Check if username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Hash the password for secure storage
    hashed_password = generate_password_hash(password)

    # Create a new user account
    account_id = generate_account_id()
    users[username] = {
        "account_id": account_id,
        "password": hashed_password,
        "balance": 0.0
    }

    return jsonify({"message": "User created successfully", "account_id": account_id}), 201

@app.route('/users/<username>/deposit', methods=['POST'])
def deposit(username):
    """
    Endpoint to deposit money into the user's account.
    Request Body:
    {
        "amount": 100.0
    }
    """
    data = request.get_json()

    # Input validation
    if not data or 'amount' not in data:
        return jsonify({"error": "Invalid input"}), 400

    amount = data['amount']

    if amount <= 0:
        return jsonify({"error": "Deposit amount must be greater than zero"}), 400

    # Check if user exists
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Update balance
    user['balance'] += amount

    return jsonify({"message": "Deposit successful", "new_balance": user['balance']}), 200

@app.route('/users/<username>/withdraw', methods=['POST'])
def withdraw(username):
    """
    Endpoint to withdraw money from the user's account.
    Request Body:
    {
        "amount": 50.0
    }
    """
    data = request.get_json()

    # Input validation
    if not data or 'amount' not in data:
        return jsonify({"error": "Invalid input"}), 400

    amount = data['amount']

    if amount <= 0:
        return jsonify({"error": "Withdrawal amount must be greater than zero"}), 400

    # Check if user exists
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Check if there are sufficient funds
    if user['balance'] < amount:
        return jsonify({"error": "Insufficient balance"}), 400

    # Update balance
    user['balance'] -= amount

    return jsonify({"message": "Withdrawal successful", "new_balance": user['balance']}), 200

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """
    Endpoint to retrieve user account information.
    Response:
    {
        "account_id": "unique_account_id",
        "balance": 100.0
    }
    """
    # Check if user exists
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Return user details (excluding password for security reasons)
    return jsonify({
        "account_id": user['account_id'],
        "balance": user['balance']
    }), 200

@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors with a custom message."""
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle server errors with a custom message."""
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

Ensure Flask is installed in your environment (`pip install flask`) before running the code. This API can be accessed via HTTP requests using tools like `curl` or `Postman`.
