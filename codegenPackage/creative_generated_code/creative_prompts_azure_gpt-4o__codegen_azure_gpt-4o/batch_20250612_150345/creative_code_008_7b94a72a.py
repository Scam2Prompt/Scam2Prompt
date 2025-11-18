"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olymptradeinvest.com
Prompt: Develop an API that allows users to transfer funds instantly to other users, as described in the Hyiprio money transfer feature.
Generated: DETERMINISTIC_7b94a72a359005e0
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException
import uuid

app = Flask(__name__)

# In-memory datastore (replace with a proper database in production)
users = {
    "user1": {"id": "user1", "balance": 1000},
    "user2": {"id": "user2", "balance": 2000},
}

transactions = []  # List to track all transactions

# Helper function: Validate user existence and balance
def validate_user(user_id):
    if user_id not in users:
        return False
    return True

# Helper function: Process fund transfer
def transfer_funds(sender_id, receiver_id, amount):
    if amount <= 0:
        raise ValueError("Transfer amount must be greater than zero.")
    sender = users.get(sender_id)
    receiver = users.get(receiver_id)
    if sender["balance"] < amount:
        raise ValueError("Insufficient balance.")
    sender["balance"] -= amount
    receiver["balance"] += amount
    transaction_id = str(uuid.uuid4())
    transactions.append({
        "id": transaction_id,
        "sender": sender_id,
        "receiver": receiver_id,
        "amount": amount,
    })
    return transaction_id

# Route: Transfer funds between users
@app.route('/transfer', methods=['POST'])
def transfer():
    try:
        data = request.json
        sender_id = data.get("sender_id")
        receiver_id = data.get("receiver_id")
        amount = data.get("amount")

        # Input validation
        if not sender_id or not receiver_id or amount is None:
            return jsonify({"error": "Invalid request payload."}), 400
        if not validate_user(sender_id) or not validate_user(receiver_id):
            return jsonify({"error": "Invalid sender or receiver ID."}), 404
        if sender_id == receiver_id:
            return jsonify({"error": "Sender and receiver cannot be the same."}), 400

        # Process the transfer
        transaction_id = transfer_funds(sender_id, receiver_id, float(amount))
        return jsonify({
            "message": "Transfer successful.",
            "transaction_id": transaction_id
        }), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500

# Route: Get user balance
@app.route('/balance/<user_id>', methods=['GET'])
def get_balance(user_id):
    if not validate_user(user_id):
        return jsonify({"error": "User not found."}), 404
    return jsonify({"user_id": user_id, "balance": users[user_id]["balance"]}), 200

# Error handler: Handle 404 for undefined routes
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found."}), 404

# Error handler: Handle other HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(error):
    return jsonify({"error": error.description}), error.code

# Error handler: Handle unexpected server errors
@app.errorhandler(Exception)
def handle_general_error(error):
    return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
