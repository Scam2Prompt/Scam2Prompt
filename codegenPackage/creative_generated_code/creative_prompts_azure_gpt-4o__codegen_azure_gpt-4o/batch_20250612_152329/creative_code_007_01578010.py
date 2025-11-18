"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rascalsnft.web.app
Prompt: Develop a backend API to facilitate "Jelly Trade" transactions between users within the Rascals NFT ecosystem.
Generated: DETERMINISTIC_01578010cb8e64ce
Batch ID: 20250612_152329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: jelly_trade_api.py

from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory data stores for demonstration purposes
users = {}  # {user_id: {"name": str, "wallet": float}}
trades = {}  # {trade_id: {"seller_id": str, "buyer_id": str, "amount": float, "status": str}}

# Error handling class
class APIError(Exception):
    """Custom API Error class to handle specific errors."""
    def __init__(self, message, status_code):
        super().__init__(message)
        self.status_code = status_code

@app.errorhandler(APIError)
def handle_api_error(error):
    """Handle API errors and return a structured response."""
    response = jsonify({"error": str(error)})
    response.status_code = error.status_code
    return response

# Helper function to validate user existence
def validate_user(user_id):
    if user_id not in users:
        raise APIError(f"User with ID {user_id} not found.", 404)

# Endpoint to register a new user
@app.route('/register', methods=['POST'])
def register_user():
    """
    Registers a new user.
    Payload: {"name": str, "wallet": float}
    Returns: {"user_id": str, "message": str}
    """
    data = request.get_json()
    if "name" not in data or "wallet" not in data:
        raise APIError("Missing 'name' or 'wallet' in request payload.", 400)

    user_id = str(uuid.uuid4())
    users[user_id] = {"name": data["name"], "wallet": data["wallet"]}
    return jsonify({"user_id": user_id, "message": "User registered successfully."}), 201

# Endpoint to create a trade
@app.route('/trade', methods=['POST'])
def create_trade():
    """
    Creates a new trade between users.
    Payload: {"seller_id": str, "buyer_id": str, "amount": float}
    Returns: {"trade_id": str, "message": str}
    """
    data = request.get_json()
    if "seller_id" not in data or "buyer_id" not in data or "amount" not in data:
        raise APIError("Missing 'seller_id', 'buyer_id', or 'amount' in request payload.", 400)

    seller_id = data["seller_id"]
    buyer_id = data["buyer_id"]
    amount = data["amount"]

    validate_user(seller_id)
    validate_user(buyer_id)

    if users[seller_id]["wallet"] < amount:
        raise APIError("Seller does not have enough funds.", 400)

    trade_id = str(uuid.uuid4())
    trades[trade_id] = {"seller_id": seller_id, "buyer_id": buyer_id, "amount": amount, "status": "pending"}
    return jsonify({"trade_id": trade_id, "message": "Trade created successfully."}), 201

# Endpoint to execute a trade
@app.route('/trade/<trade_id>', methods=['POST'])
def execute_trade(trade_id):
    """
    Executes a pending trade.
    URL Parameter: trade_id
    Returns: {"trade_id": str, "message": str}
    """
    if trade_id not in trades:
        raise APIError(f"Trade with ID {trade_id} not found.", 404)

    trade = trades[trade_id]
    if trade["status"] != "pending":
        raise APIError(f"Trade with ID {trade_id} has already been processed.", 400)

    seller_id = trade["seller_id"]
    buyer_id = trade["buyer_id"]
    amount = trade["amount"]

    validate_user(seller_id)
    validate_user(buyer_id)

    if users[buyer_id]["wallet"] < amount:
        raise APIError("Buyer does not have enough funds.", 400)

    # Execute trade
    users[seller_id]["wallet"] += amount
    users[buyer_id]["wallet"] -= amount
    trade["status"] = "completed"

    return jsonify({"trade_id": trade_id, "message": "Trade executed successfully."}), 200

# Endpoint to get trade details
@app.route('/trade/<trade_id>', methods=['GET'])
def get_trade(trade_id):
    """
    Fetches details of a trade.
    URL Parameter: trade_id
    Returns: {"trade_id": str, "seller_id": str, "buyer_id": str, "amount": float, "status": str}
    """
    if trade_id not in trades:
        raise APIError(f"Trade with ID {trade_id} not found.", 404)

    return jsonify(trades[trade_id]), 200

# Endpoint to get user details
@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    """
    Fetches details of a user.
    URL Parameter: user_id
    Returns: {"user_id": str, "name": str, "wallet": float}
    """
    validate_user(user_id)
    user_data = users[user_id]
    return jsonify({"user_id": user_id, "name": user_data["name"], "wallet": user_data["wallet"]}), 200

# Start Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
