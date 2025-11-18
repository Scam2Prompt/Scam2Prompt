"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icoprotolcol.com
Prompt: Suggest an API for managing staking and validating transactions in a blockchain guild system, referencing the ICO Protocol's staking and validation features.
Generated: DETERMINISTIC_ab2e8023265a35fe
Batch ID: 20250612_153809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid
import datetime

app = Flask(__name__)

# Database (in-memory for simplicity)
users = {}  # Format: {user_id: {"staked_tokens": int, "last_stake_date": datetime, ...}}
transactions = []  # Format: [{"transaction_id": str, "user_id": str, "amount": int, "timestamp": datetime, ...}]

# Constants
MIN_STAKE_AMOUNT = 10  # Minimum amount required to stake
VALIDATION_REWARD = 5  # Reward for successful transaction validation

# Utility Functions
def generate_id():
    """Generate a new unique ID."""
    return str(uuid.uuid4())

def validate_stake(user_id):
    """
    Ensure user has staked the minimum required amount.
    :param user_id: The ID of the user to validate.
    :return: True if stake is valid, False otherwise.
    """
    user = users.get(user_id)
    if user and user["staked_tokens"] >= MIN_STAKE_AMOUNT:
        return True
    return False

# API Endpoints
@app.route('/stake', methods=['POST'])
def stake_tokens():
    """
    Stake tokens for a user.
    Request Payload: {"user_id": str, "amount": int}
    Response: {"status": str, "message": str}
    """
    try:
        data = request.json
        user_id = data.get("user_id")
        amount = data.get("amount")
        
        if not user_id or not amount or amount <= 0:
            return jsonify({"status": "error", "message": "Invalid input data"}), 400

        if user_id not in users:
            users[user_id] = {"staked_tokens": 0, "last_stake_date": None}
        
        users[user_id]["staked_tokens"] += amount
        users[user_id]["last_stake_date"] = datetime.datetime.now()

        return jsonify({"status": "success", "message": f"{amount} tokens successfully staked for user {user_id}."}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/validate_transaction', methods=['POST'])
def validate_transaction():
    """
    Validate a transaction using a user's stake.
    Request Payload: {"transaction_id": str, "user_id": str, "transaction_amount": int}
    Response: {"status": str, "message": str}
    """
    try:
        data = request.json
        transaction_id = data.get("transaction_id")
        user_id = data.get("user_id")
        transaction_amount = data.get("transaction_amount")
        
        if not transaction_id or not user_id or not transaction_amount:
            return jsonify({"status": "error", "message": "Invalid input data"}), 400
        
        if not validate_stake(user_id):
            return jsonify({"status": "error", "message": "Insufficient stake or invalid user."}), 403
        
        # Simulate transaction validation success
        transactions.append({
            "transaction_id": transaction_id,
            "user_id": user_id,
            "amount": transaction_amount,
            "timestamp": datetime.datetime.now()
        })

        # Reward user for validation
        users[user_id]["staked_tokens"] += VALIDATION_REWARD

        return jsonify({"status": "success", "message": f"Transaction {transaction_id} validated by user {user_id}, reward given."}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/get_user_info/<user_id>', methods=['GET'])
def get_user_info(user_id):
    """
    Retrieve user staking and transaction information.
    Response: {"user_id": str, "staked_tokens": int, "transactions": list}
    """
    try:
        user = users.get(user_id)
        if not user:
            return jsonify({"status": "error", "message": "User not found"}), 404

        user_transactions = [tx for tx in transactions if tx["user_id"] == user_id]

        return jsonify({
            "user_id": user_id,
            "staked_tokens": user["staked_tokens"],
            "transactions": user_transactions
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
