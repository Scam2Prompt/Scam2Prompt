"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uveorm.com
Prompt: Develop a secure API endpoint for transferring funds between users in a wallet system, as described on uveorm.com.
Generated: DETERMINISTIC_033cab54d975a326
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest, InternalServerError
import json
from decimal import Decimal

app = Flask(__name__)

# Mock database (Replace with actual database integration for production)
users = {
    "user1": {"wallet_balance": Decimal("100.00")},
    "user2": {"wallet_balance": Decimal("50.00")},
}

# Helper function: Validate input and check for sufficient balance
def validate_transfer(sender: str, receiver: str, amount: Decimal):
    if sender not in users:
        raise BadRequest("Sender does not exist.")
    if receiver not in users:
        raise BadRequest("Receiver does not exist.")
    if amount <= 0:
        raise BadRequest("Transfer amount must be greater than zero.")
    if users[sender]["wallet_balance"] < amount:
        raise BadRequest("Insufficient balance.")

# Secure API endpoint for fund transfer between users
@app.route('/api/transfer-funds', methods=['POST'])
def transfer_funds():
    """
    Secure API endpoint for transferring funds between users.
    Expects sender, receiver, and amount in the request body.
    """
    try:
        # Parse JSON request data
        data = request.get_json()
        if not data:
            raise BadRequest("Request must be in JSON format.")

        sender = data.get("sender")
        receiver = data.get("receiver")
        amount = data.get("amount")
        
        # Validate inputs
        if not sender or not receiver or not amount:
            raise BadRequest("Missing required fields: sender, receiver, amount.")
        
        try:
            # Convert amount to Decimal for precision in financial calculations
            amount = Decimal(amount)
        except:
            raise BadRequest("Invalid amount format.")
        
        validate_transfer(sender, receiver, amount)
        
        # Perform transfer
        users[sender]["wallet_balance"] -= amount
        users[receiver]["wallet_balance"] += amount
        
        # Return success response
        response = {
            "message": "Transfer successful.",
            "sender": sender,
            "receiver": receiver,
            "amount": str(amount),
            "sender_balance": str(users[sender]["wallet_balance"]),
            "receiver_balance": str(users[receiver]["wallet_balance"]),
        }
        return jsonify(response), 200

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Catch-all for unexpected errors
        return jsonify({"error": "Internal server error.", "details": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
