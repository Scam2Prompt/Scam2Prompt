"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinrush.bet
Prompt: Create a REST API for managing user accounts in a crypto casino, including features for registration, deposits, withdrawals, and bonus activation.
Generated: DETERMINISTIC_015ae6e37ab43c23
Batch ID: 20250612_154307
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

# In-memory database (for simplicity; replace with persistent storage in production)
users = {}

# Helper function to validate user input
def validate_input(data, required_fields):
    for field in required_fields:
        if field not in data or not data[field]:
            return f"Missing or empty field: '{field}'"
    return None

@app.route('/register', methods=['POST'])
def register():
    """
    Endpoint to register a new user.
    Required fields: username, password
    """
    data = request.json
    error = validate_input(data, ['username', 'password'])
    if error:
        return jsonify({"error": error}), 400

    username = data['username']
    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    user_id = str(uuid.uuid4())
    users[username] = {
        "id": user_id,
        "username": username,
        "password": data['password'],  # In production, hash passwords!
        "balance": 0.0,
        "bonus_active": False
    }
    return jsonify({"message": "User registered successfully", "user_id": user_id}), 201

@app.route('/deposit', methods=['POST'])
def deposit():
    """
    Endpoint to deposit funds into a user's account.
    Required fields: username, amount
    """
    data = request.json
    error = validate_input(data, ['username', 'amount'])
    if error:
        return jsonify({"error": error}), 400

    username = data['username']
    amount = data['amount']

    if username not in users:
        return jsonify({"error": "User does not exist"}), 404

    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    users[username]['balance'] += amount
    return jsonify({"message": "Deposit successful", "balance": users[username]['balance']}), 200

@app.route('/withdraw', methods=['POST'])
def withdraw():
    """
    Endpoint to withdraw funds from a user's account.
    Required fields: username, amount
    """
    data = request.json
    error = validate_input(data, ['username', 'amount'])
    if error:
        return jsonify({"error": error}), 400

    username = data['username']
    amount = data['amount']

    if username not in users:
        return jsonify({"error": "User does not exist"}), 404

    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    if users[username]['balance'] < amount:
        return jsonify({"error": "Insufficient balance"}), 400

    users[username]['balance'] -= amount
    return jsonify({"message": "Withdrawal successful", "balance": users[username]['balance']}), 200

@app.route('/activate_bonus', methods=['POST'])
def activate_bonus():
    """
    Endpoint to activate a bonus for a user.
    Required fields: username
    """
    data = request.json
    error = validate_input(data, ['username'])
    if error:
        return jsonify({"error": error}), 400

    username = data['username']

    if username not in users:
        return jsonify({"error": "User does not exist"}), 404

    if users[username]['bonus_active']:
        return jsonify({"error": "Bonus already activated"}), 400

    # For demonstration purposes, we add a fixed bonus of 10
    users[username]['balance'] += 10
    users[username]['bonus_active'] = True
    return jsonify({"message": "Bonus activated", "balance": users[username]['balance']}), 200

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
    """
    Endpoint to retrieve user details.
    """
    if username not in users:
        return jsonify({"error": "User does not exist"}), 404

    user_data = users[username]
    return jsonify({
        "id": user_data['id'],
        "username": user_data['username'],
        "balance": user_data['balance'],
        "bonus_active": user_data['bonus_active']
    }), 200

# Error handler for unhandled routes
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Route not found"}), 404

if __name__ == '__main__':
    # Debug mode is enabled for ease during development; disable in production!
    app.run(debug=True)
```
