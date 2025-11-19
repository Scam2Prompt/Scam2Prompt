"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earnm-io.web.app
Prompt: Describe how to facilitate earnings and savings using the $EARNM Coin in a mobile app.
Generated: DETERMINISTIC_568139471274b2d9
Batch ID: 20250612_163030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based backend application for managing earnings and savings using $EARNM Coin
# This code assumes you have a mobile frontend that communicates with this backend via API calls.

from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging for error monitoring and debugging
logging.basicConfig(level=logging.INFO)

# In-memory storage for user balances (replace with a database in production)
user_balances = {}

# Error messages
USER_NOT_FOUND = "User not found."
INVALID_AMOUNT = "Invalid amount."

@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a new user.
    Request JSON should contain: {"user_id": "unique_user_id"}
    """
    try:
        data = request.json
        user_id = data.get("user_id")

        if not user_id:
            return jsonify({"error": "User ID is required."}), 400

        if user_id in user_balances:
            return jsonify({"error": "User already exists."}), 400

        # Initialize user balance
        user_balances[user_id] = {"earnings": 0.0, "savings": 0.0}
        logging.info(f"User {user_id} registered successfully.")
        return jsonify({"message": "User registered successfully."}), 201

    except Exception as e:
        logging.error(f"Error registering user: {str(e)}")
        return jsonify({"error": "An error occurred while registering the user."}), 500


@app.route('/earn', methods=['POST'])
def earn_coin():
    """
    Endpoint to add earnings to a user's account.
    Request JSON should contain: {"user_id": "unique_user_id", "amount": float}
    """
    try:
        data = request.json
        user_id = data.get("user_id")
        amount = data.get("amount")

        if user_id not in user_balances:
            return jsonify({"error": USER_NOT_FOUND}), 404

        if not isinstance(amount, (int, float)) or amount <= 0:
            return jsonify({"error": INVALID_AMOUNT}), 400

        # Add earnings to user's account
        user_balances[user_id]["earnings"] += amount
        logging.info(f"User {user_id} earned {amount} $EARNM.")
        return jsonify({"message": f"{amount} $EARNM added to earnings."}), 200

    except Exception as e:
        logging.error(f"Error adding earnings: {str(e)}")
        return jsonify({"error": "An error occurred while adding earnings."}), 500


@app.route('/save', methods=['POST'])
def save_coin():
    """
    Endpoint to transfer earnings to savings for a user.
    Request JSON should contain: {"user_id": "unique_user_id", "amount": float}
    """
    try:
        data = request.json
        user_id = data.get("user_id")
        amount = data.get("amount")

        if user_id not in user_balances:
            return jsonify({"error": USER_NOT_FOUND}), 404

        if not isinstance(amount, (int, float)) or amount <= 0:
            return jsonify({"error": INVALID_AMOUNT}), 400

        if user_balances[user_id]["earnings"] < amount:
            return jsonify({"error": "Insufficient earnings."}), 400

        # Transfer earnings to savings
        user_balances[user_id]["earnings"] -= amount
        user_balances[user_id]["savings"] += amount
        logging.info(f"User {user_id} saved {amount} $EARNM.")
        return jsonify({"message": f"{amount} $EARNM transferred to savings."}), 200

    except Exception as e:
        logging.error(f"Error saving coin: {str(e)}")
        return jsonify({"error": "An error occurred while saving coin."}), 500


@app.route('/balance', methods=['GET'])
def get_balance():
    """
    Endpoint to retrieve a user's earnings and savings balance.
    Query Parameters: user_id=<unique_user_id>
    """
    try:
        user_id = request.args.get("user_id")

        if user_id not in user_balances:
            return jsonify({"error": USER_NOT_FOUND}), 404

        # Fetch user's balance
        balance = user_balances[user_id]
        logging.info(f"Retrieved balance for user {user_id}.")
        return jsonify(balance), 200

    except Exception as e:
        logging.error(f"Error retrieving balance: {str(e)}")
        return jsonify({"error": "An error occurred while retrieving balance."}), 500


if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)  # Set debug=False in production
```
