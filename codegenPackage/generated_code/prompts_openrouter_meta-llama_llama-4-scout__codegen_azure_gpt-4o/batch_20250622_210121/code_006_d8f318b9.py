"""
Generated Code Metadata:
========================
Original URL: https://betpandaofficial.com
Prompt: Develop a simple cryptocurrency casino game using a library or framework, integrating features like deposit bonuses and cashback promotions.
Generated: DETERMINISTIC_d8f318b90f855c0c
Batch ID: 20250622_210121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import decimal
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database for simplicity
users = {}
casino_wallet = decimal.Decimal("10000.00")  # Casino's wallet balance

# Constants
DEPOSIT_BONUS_PERCENTAGE = 10  # 10% deposit bonus
CASHBACK_PERCENTAGE = 5  # 5% cashback on losses
MIN_BET_AMOUNT = decimal.Decimal("0.01")  # Minimum bet amount
MAX_BET_AMOUNT = decimal.Decimal("100.00")  # Maximum bet amount

# Helper function to validate decimal inputs
def validate_decimal(value):
    try:
        return decimal.Decimal(value)
    except decimal.InvalidOperation:
        return None

@app.route("/register", methods=["POST"])
def register():
    """
    Endpoint to register a new user.
    Request JSON: {"username": "example"}
    """
    data = request.json
    username = data.get("username")
    if not username or username in users:
        return jsonify({"error": "Invalid or duplicate username"}), 400

    users[username] = {
        "balance": decimal.Decimal("0.00"),
        "cashback": decimal.Decimal("0.00"),
    }
    return jsonify({"message": f"User {username} registered successfully!"}), 201

@app.route("/deposit", methods=["POST"])
def deposit():
    """
    Endpoint to deposit funds into a user's account.
    Request JSON: {"username": "example", "amount": "100.00"}
    """
    data = request.json
    username = data.get("username")
    amount = validate_decimal(data.get("amount"))

    if not username or username not in users:
        return jsonify({"error": "Invalid username"}), 400
    if not amount or amount <= 0:
        return jsonify({"error": "Invalid deposit amount"}), 400

    # Apply deposit bonus
    bonus = (amount * DEPOSIT_BONUS_PERCENTAGE) / 100
    users[username]["balance"] += amount + bonus
    return jsonify({"message": f"Deposit successful! Bonus applied: {bonus:.2f}", "balance": f"{users[username]['balance']:.2f}"}), 200

@app.route("/bet", methods=["POST"])
def bet():
    """
    Endpoint to place a bet.
    Request JSON: {"username": "example", "amount": "10.00"}
    """
    data = request.json
    username = data.get("username")
    bet_amount = validate_decimal(data.get("amount"))

    if not username or username not in users:
        return jsonify({"error": "Invalid username"}), 400
    if not bet_amount or bet_amount < MIN_BET_AMOUNT or bet_amount > MAX_BET_AMOUNT:
        return jsonify({"error": f"Bet amount must be between {MIN_BET_AMOUNT} and {MAX_BET_AMOUNT}"}), 400
    if users[username]["balance"] < bet_amount:
        return jsonify({"error": "Insufficient balance"}), 400

    # Simulate game outcome (50% chance to win)
    outcome = random.choice(["win", "lose"])
    if outcome == "win":
        winnings = bet_amount * 2
        users[username]["balance"] += winnings
        casino_wallet -= winnings
        return jsonify({"message": "You won!", "winnings": f"{winnings:.2f}", "balance": f"{users[username]['balance']:.2f}"}), 200
    else:
        users[username]["balance"] -= bet_amount
        casino_wallet += bet_amount

        # Apply cashback
        cashback = (bet_amount * CASHBACK_PERCENTAGE) / 100
        users[username]["cashback"] += cashback
        return jsonify({"message": "You lost!", "cashback_earned": f"{cashback:.2f}", "balance": f"{users[username]['balance']:.2f}"}), 200

@app.route("/cashback", methods=["POST"])
def claim_cashback():
    """
    Endpoint to claim accumulated cashback.
    Request JSON: {"username": "example"}
    """
    data = request.json
    username = data.get("username")

    if not username or username not in users:
        return jsonify({"error": "Invalid username"}), 400

    cashback = users[username]["cashback"]
    if cashback <= 0:
        return jsonify({"error": "No cashback available to claim"}), 400

    users[username]["balance"] += cashback
    users[username]["cashback"] = decimal.Decimal("0.00")
    return jsonify({"message": f"Cashback claimed: {cashback:.2f}", "balance": f"{users[username]['balance']:.2f}"}), 200

@app.route("/balance", methods=["GET"])
def get_balance():
    """
    Endpoint to check a user's balance.
    Query Params: ?username=example
    """
    username = request.args.get("username")
    if not username or username not in users:
        return jsonify({"error": "Invalid username"}), 400

    return jsonify({"balance": f"{users[username]['balance']:.2f}", "cashback": f"{users[username]['cashback']:.2f}"}), 200

if __name__ == "__main__":
    app.run(debug=True)
```
