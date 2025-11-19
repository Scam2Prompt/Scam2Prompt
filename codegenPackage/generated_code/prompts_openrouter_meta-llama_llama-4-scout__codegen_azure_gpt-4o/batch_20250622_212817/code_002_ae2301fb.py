"""
Generated Code Metadata:
========================
Original URL: https://fxtasian.com
Prompt: "Write a Python script using libraries such as Flask or Django to create a simple REST API for a cryptocurrency exchange platform similar to IJEX Exchange."
Generated: DETERMINISTIC_ae2301fb9f2c5f8f
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data for cryptocurrencies and user balances
cryptocurrencies = [
    {"id": 1, "name": "Bitcoin", "symbol": "BTC", "price_usd": 27000.00},
    {"id": 2, "name": "Ethereum", "symbol": "ETH", "price_usd": 1800.00},
    {"id": 3, "name": "Cardano", "symbol": "ADA", "price_usd": 0.35},
]

user_balances = {
    "user1": {"BTC": 0.5, "ETH": 2.0, "ADA": 1000},
    "user2": {"BTC": 0.1, "ETH": 0.5, "ADA": 500},
}

# Error response helper function
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# Route to get all available cryptocurrencies
@app.route('/api/cryptocurrencies', methods=['GET'])
def get_cryptocurrencies():
    """
    Returns a list of all available cryptocurrencies with their details.
    """
    return jsonify(cryptocurrencies)

# Route to get details of a specific cryptocurrency by symbol
@app.route('/api/cryptocurrencies/<symbol>', methods=['GET'])
def get_cryptocurrency(symbol):
    """
    Returns details of a specific cryptocurrency by its symbol.
    """
    crypto = next((c for c in cryptocurrencies if c["symbol"].lower() == symbol.lower()), None)
    if not crypto:
        return error_response(f"Cryptocurrency with symbol '{symbol}' not found.", 404)
    return jsonify(crypto)

# Route to get user balances
@app.route('/api/users/<username>/balances', methods=['GET'])
def get_user_balances(username):
    """
    Returns the cryptocurrency balances of a specific user.
    """
    balances = user_balances.get(username)
    if not balances:
        return error_response(f"User '{username}' not found.", 404)
    return jsonify(balances)

# Route to perform a trade (buy/sell cryptocurrency)
@app.route('/api/trade', methods=['POST'])
def trade():
    """
    Handles buying or selling of cryptocurrencies.
    Expects JSON payload with 'username', 'symbol', 'action', and 'amount'.
    """
    data = request.get_json()
    if not data:
        return error_response("Invalid request. JSON payload is required.")

    username = data.get("username")
    symbol = data.get("symbol")
    action = data.get("action")  # 'buy' or 'sell'
    amount = data.get("amount")

    # Validate input
    if not username or not symbol or not action or not amount:
        return error_response("Missing required fields: 'username', 'symbol', 'action', 'amount'.")
    if action not in ["buy", "sell"]:
        return error_response("Invalid action. Must be 'buy' or 'sell'.")
    if amount <= 0:
        return error_response("Amount must be greater than zero.")

    # Check if user exists
    user_balance = user_balances.get(username)
    if not user_balance:
        return error_response(f"User '{username}' not found.", 404)

    # Check if cryptocurrency exists
    crypto = next((c for c in cryptocurrencies if c["symbol"].lower() == symbol.lower()), None)
    if not crypto:
        return error_response(f"Cryptocurrency with symbol '{symbol}' not found.", 404)

    # Perform trade
    if action == "buy":
        # Simulate buying by adding to user's balance
        user_balance[symbol] = user_balance.get(symbol, 0) + amount
    elif action == "sell":
        # Simulate selling by subtracting from user's balance
        if user_balance.get(symbol, 0) < amount:
            return error_response(f"Insufficient balance to sell {amount} {symbol}.")
        user_balance[symbol] -= amount

    return jsonify({"message": f"Trade successful: {action} {amount} {symbol} for user '{username}'."})

# Error handling for 404 routes
@app.errorhandler(404)
def not_found(error):
    """
    Handles 404 errors for undefined routes.
    """
    return error_response("Resource not found.", 404)

# Main entry point
if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
