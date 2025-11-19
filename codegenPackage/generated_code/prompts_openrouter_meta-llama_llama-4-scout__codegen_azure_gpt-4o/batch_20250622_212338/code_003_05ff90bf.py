"""
Generated Code Metadata:
========================
Original URL: https://revaluationway.com
Prompt: Design a simple cryptocurrency exchange system using RESTful APIs, inspired by the features of Revaluation Way, with endpoints for buying and selling cryptocurrencies like USDT, TYCO, and NEGO.
Generated: DETERMINISTIC_05ff90bfc6d47011
Batch ID: 20250622_212338
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

# In-memory database for simplicity
users = {}
cryptocurrencies = {
    "USDT": {"price": 1.0, "supply": 1000000},
    "TYCO": {"price": 50.0, "supply": 50000},
    "NEGO": {"price": 10.0, "supply": 100000},
}

# Error messages
ERRORS = {
    "USER_NOT_FOUND": "User not found.",
    "INSUFFICIENT_FUNDS": "Insufficient funds.",
    "INSUFFICIENT_SUPPLY": "Insufficient cryptocurrency supply.",
    "INVALID_CRYPTO": "Invalid cryptocurrency.",
    "INVALID_AMOUNT": "Amount must be greater than zero.",
}

# Helper function to generate unique user IDs
def generate_user_id():
    return str(uuid.uuid4())

# Endpoint: Create a new user
@app.route("/users", methods=["POST"])
def create_user():
    user_id = generate_user_id()
    users[user_id] = {"balance": 1000.0, "portfolio": {}}
    return jsonify({"message": "User created successfully.", "user_id": user_id}), 201

# Endpoint: Get user details
@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": ERRORS["USER_NOT_FOUND"]}), 404
    return jsonify({"user_id": user_id, "balance": user["balance"], "portfolio": user["portfolio"]}), 200

# Endpoint: Buy cryptocurrency
@app.route("/buy", methods=["POST"])
def buy_crypto():
    data = request.json
    user_id = data.get("user_id")
    crypto = data.get("crypto")
    amount = data.get("amount")

    # Validate input
    if not user_id or not crypto or not amount:
        return jsonify({"error": "Missing required fields."}), 400
    if amount <= 0:
        return jsonify({"error": ERRORS["INVALID_AMOUNT"]}), 400
    if crypto not in cryptocurrencies:
        return jsonify({"error": ERRORS["INVALID_CRYPTO"]}), 400

    user = users.get(user_id)
    if not user:
        return jsonify({"error": ERRORS["USER_NOT_FOUND"]}), 404

    crypto_price = cryptocurrencies[crypto]["price"]
    total_cost = crypto_price * amount

    if user["balance"] < total_cost:
        return jsonify({"error": ERRORS["INSUFFICIENT_FUNDS"]}), 400
    if cryptocurrencies[crypto]["supply"] < amount:
        return jsonify({"error": ERRORS["INSUFFICIENT_SUPPLY"]}), 400

    # Process transaction
    user["balance"] -= total_cost
    cryptocurrencies[crypto]["supply"] -= amount
    user["portfolio"][crypto] = user["portfolio"].get(crypto, 0) + amount

    return jsonify({"message": f"Successfully purchased {amount} {crypto}.", "balance": user["balance"], "portfolio": user["portfolio"]}), 200

# Endpoint: Sell cryptocurrency
@app.route("/sell", methods=["POST"])
def sell_crypto():
    data = request.json
    user_id = data.get("user_id")
    crypto = data.get("crypto")
    amount = data.get("amount")

    # Validate input
    if not user_id or not crypto or not amount:
        return jsonify({"error": "Missing required fields."}), 400
    if amount <= 0:
        return jsonify({"error": ERRORS["INVALID_AMOUNT"]}), 400
    if crypto not in cryptocurrencies:
        return jsonify({"error": ERRORS["INVALID_CRYPTO"]}), 400

    user = users.get(user_id)
    if not user:
        return jsonify({"error": ERRORS["USER_NOT_FOUND"]}), 404

    if user["portfolio"].get(crypto, 0) < amount:
        return jsonify({"error": ERRORS["INSUFFICIENT_FUNDS"]}), 400

    crypto_price = cryptocurrencies[crypto]["price"]
    total_earnings = crypto_price * amount

    # Process transaction
    user["balance"] += total_earnings
    cryptocurrencies[crypto]["supply"] += amount
    user["portfolio"][crypto] -= amount
    if user["portfolio"][crypto] == 0:
        del user["portfolio"][crypto]

    return jsonify({"message": f"Successfully sold {amount} {crypto}.", "balance": user["balance"], "portfolio": user["portfolio"]}), 200

# Endpoint: Get cryptocurrency details
@app.route("/cryptocurrencies", methods=["GET"])
def get_cryptocurrencies():
    return jsonify(cryptocurrencies), 200

# Error handling for invalid routes
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found."}), 404

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
```
