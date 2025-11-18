"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linktreewallstmemes.pages.dev
Prompt: Generate code for a web application that allows users to buy $WSM tokens and view their staking history.
Generated: DETERMINISTIC_9b64c967b264e6a1
Batch ID: 20250612_151347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask application for $WSM token purchase and staking history
from flask import Flask, request, jsonify
import uuid
from datetime import datetime

app = Flask(__name__)

# Placeholder data storage for simplicity (use databases like MySQL/PostgreSQL in production)
users = {}  # Example: {"user_id": {"username": "john_doe", "balance": 500, "staking_history": []}}
wsm_token_price = 10  # $1 USD = 10 $WSM tokens (example conversion rate)

# Error messages for consistent responses
ERROR_MESSAGES = {
    "USER_NOT_FOUND": "User not found.",
    "INSUFFICIENT_BALANCE": "Insufficient balance to purchase tokens.",
    "INVALID_AMOUNT": "Invalid amount provided.",
}

# Create a new user
@app.route('/create_user', methods=['POST'])
def create_user():
    try:
        data = request.json
        username = data.get("username")
        if not username:
            return jsonify({"error": "Username is required."}), 400

        user_id = str(uuid.uuid4())  # Unique user ID
        users[user_id] = {
            "username": username,
            "balance": 0,  # Default balance
            "staking_history": [],
        }
        return jsonify({"message": "User created successfully.", "user_id": user_id}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


# Buy $WSM tokens
@app.route('/buy_tokens/<user_id>', methods=['POST'])
def buy_tokens(user_id):
    try:
        user = users.get(user_id)
        if not user:
            return jsonify({"error": ERROR_MESSAGES["USER_NOT_FOUND"]}), 404

        data = request.json
        usd_amount = data.get("usd_amount")
        if not usd_amount or usd_amount <= 0:
            return jsonify({"error": ERROR_MESSAGES["INVALID_AMOUNT"]}), 400

        # Calculate token amount based on $WSM token price
        token_amount = usd_amount * wsm_token_price
        user["balance"] += token_amount
        return jsonify({"message": "Tokens purchased successfully.", "balance": user["balance"]}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


# View staking history
@app.route('/staking_history/<user_id>', methods=['GET'])
def view_staking_history(user_id):
    try:
        user = users.get(user_id)
        if not user:
            return jsonify({"error": ERROR_MESSAGES["USER_NOT_FOUND"]}), 404

        return jsonify({"staking_history": user["staking_history"]}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


# Stake $WSM tokens
@app.route('/stake_tokens/<user_id>', methods=['POST'])
def stake_tokens(user_id):
    try:
        user = users.get(user_id)
        if not user:
            return jsonify({"error": ERROR_MESSAGES["USER_NOT_FOUND"]}), 404

        data = request.json
        token_amount = data.get("token_amount")
        if not token_amount or token_amount <= 0:
            return jsonify({"error": ERROR_MESSAGES["INVALID_AMOUNT"]}), 400

        if user["balance"] < token_amount:
            return jsonify({"error": ERROR_MESSAGES["INSUFFICIENT_BALANCE"]}), 400

        # Deduct tokens from the user's balance and record staking history
        user["balance"] -= token_amount
        staking_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "amount": token_amount,
        }
        user["staking_history"].append(staking_entry)

        return jsonify({"message": "Tokens staked successfully.", "balance": user["balance"]}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
