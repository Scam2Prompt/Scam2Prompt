"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://therealworldcoin.com
Prompt: Develop a REST API that allows users to query details about TRW token transactions, including token balances and ownership records.
Generated: DETERMINISTIC_1762d44bb855257e
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: trw_token_api.py

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Mock database for demonstration purposes
# In production, replace this with a secure and scalable database solution.
mock_transactions = [
    {"tx_id": "1", "sender": "user1", "receiver": "user2", "amount": 100.0},
    {"tx_id": "2", "sender": "user2", "receiver": "user3", "amount": 50.0},
    {"tx_id": "3", "sender": "user1", "receiver": "user3", "amount": 200.0},
]

mock_balances = {
    "user1": 700.0,
    "user2": 150.0,
    "user3": 250.0,
}

mock_ownership = {
    "user1": ["tokenA", "tokenB"],
    "user2": ["tokenC"],
    "user3": ["tokenD", "tokenE"],
}


@app.route("/transactions", methods=["GET"])
def get_transactions():
    """
    Endpoint to retrieve all transactions.
    Returns:
        JSON response containing a list of transactions.
    """
    try:
        return jsonify({"status": "success", "data": mock_transactions}), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/balances/<username>", methods=["GET"])
def get_balance(username):
    """
    Endpoint to retrieve the balance of a specific user.
    Args:
        username (str): The name of the user.
    Returns:
        JSON response containing the user's balance.
    """
    try:
        if username in mock_balances:
            balance = mock_balances[username]
            return jsonify({"status": "success", "data": {"username": username, "balance": balance}}), 200
        else:
            return jsonify({"status": "error", "message": "User not found"}), 404
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/ownership/<username>", methods=["GET"])
def get_ownership(username):
    """
    Endpoint to retrieve the ownership records of a specific user.
    Args:
        username (str): The name of the user.
    Returns:
        JSON response containing the user's ownership records.
    """
    try:
        if username in mock_ownership:
            ownership = mock_ownership[username]
            return jsonify({"status": "success", "data": {"username": username, "ownership": ownership}}), 200
        else:
            return jsonify({"status": "error", "message": "User not found"}), 404
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/transactions/<tx_id>", methods=["GET"])
def get_transaction_by_id(tx_id):
    """
    Endpoint to retrieve transaction details by transaction ID.
    Args:
        tx_id (str): The transaction ID.
    Returns:
        JSON response containing the transaction details.
    """
    try:
        transaction = next((tx for tx in mock_transactions if tx["tx_id"] == tx_id), None)
        if transaction:
            return jsonify({"status": "success", "data": transaction}), 200
        else:
            return jsonify({"status": "error", "message": "Transaction not found"}), 404
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.errorhandler(404)
def handle_404_error(error):
    """
    Custom error handler for 404 Not Found.
    Returns:
        JSON response with error details.
    """
    return jsonify({"status": "error", "message": "Resource not found"}), 404


@app.errorhandler(500)
def handle_500_error(error):
    """
    Custom error handler for 500 Internal Server Error.
    Returns:
        JSON response with error details.
    """
    return jsonify({"status": "error", "message": "Internal server error"}), 500


if __name__ == "__main__":
    # Start the Flask app in debug mode for development.
    # Use a production-ready server like Gunicorn for deployment.
    app.run(debug=True)
```
