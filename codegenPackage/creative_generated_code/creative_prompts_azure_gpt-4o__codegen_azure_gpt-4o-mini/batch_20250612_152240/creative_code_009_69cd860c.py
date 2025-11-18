"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koalamemecoin.pages.dev
Prompt: Generate a play-to-earn game concept where users can earn KoalaKash tokens for completing tasks and competing against other players worldwide.
Generated: DETERMINISTIC_69cd860c437ad608
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# A dictionary to store user information and their KoalaKash balance
users = {}

# Constants for the game
TOKEN_NAME = "KoalaKash"
INITIAL_BALANCE = 100  # Starting balance for new users

# Error messages
ERROR_USER_NOT_FOUND = "User not found."
ERROR_INVALID_TASK = "Invalid task."
ERROR_INSUFFICIENT_FUNDS = "Insufficient funds."

# Define possible tasks
TASKS = {
    "complete_survey": 10,
    "share_on_social_media": 5,
    "win_a_game": 20,
}

@app.route('/register', methods=['POST'])
def register_user():
    """Register a new user with an initial KoalaKash balance."""
    username = request.json.get('username')
    if username in users:
        return jsonify({"error": "User already exists."}), 400
    
    users[username] = {'balance': INITIAL_BALANCE}
    return jsonify({"message": f"User {username} registered successfully.", "balance": INITIAL_BALANCE}), 201

@app.route('/earn_tokens', methods=['POST'])
def earn_tokens():
    """Earn tokens by completing a task."""
    username = request.json.get('username')
    task = request.json.get('task')

    if username not in users:
        return jsonify({"error": ERROR_USER_NOT_FOUND}), 404

    if task not in TASKS:
        return jsonify({"error": ERROR_INVALID_TASK}), 400

    # Award tokens for the completed task
    tokens_earned = TASKS[task]
    users[username]['balance'] += tokens_earned
    return jsonify({"message": f"You earned {tokens_earned} {TOKEN_NAME}!", "new_balance": users[username]['balance']}), 200

@app.route('/balance', methods=['GET'])
def check_balance():
    """Check the user's KoalaKash balance."""
    username = request.args.get('username')
    if username not in users:
        return jsonify({"error": ERROR_USER_NOT_FOUND}), 404

    balance = users[username]['balance']
    return jsonify({"username": username, "balance": balance}), 200

@app.route('/redeem_tokens', methods=['POST'])
def redeem_tokens():
    """Redeem tokens for rewards."""
    username = request.json.get('username')
    amount = request.json.get('amount')

    if username not in users:
        return jsonify({"error": ERROR_USER_NOT_FOUND}), 404

    if users[username]['balance'] < amount:
        return jsonify({"error": ERROR_INSUFFICIENT_FUNDS}), 400

    users[username]['balance'] -= amount
    return jsonify({"message": f"You redeemed {amount} {TOKEN_NAME}!", "new_balance": users[username]['balance']}), 200

@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    """Get the leaderboard of users sorted by balance."""
    sorted_users = sorted(users.items(), key=lambda item: item[1]['balance'], reverse=True)
    leaderboard_data = [{ "username": user[0], "balance": user[1]['balance']} for user in sorted_users]
    return jsonify(leaderboard_data), 200

if __name__ == '__main__':
    app.run(debug=True)
```
