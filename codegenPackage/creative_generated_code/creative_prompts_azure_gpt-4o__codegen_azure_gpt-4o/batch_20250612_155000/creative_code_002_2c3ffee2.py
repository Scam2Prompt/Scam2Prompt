"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assetspacifics.ltd
Prompt: Generate code for a web application that simulates the investment plans offered by assetspacifics.ltd, including features for real-time transaction tracking and customer support integration.
Generated: DETERMINISTIC_2c3ffee25258e08b
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

# Simulated database for investment plans, transactions, and customer support tickets
investment_plans = [
    {"id": 1, "name": "Basic Plan", "interest_rate": 5, "min_investment": 100},
    {"id": 2, "name": "Premium Plan", "interest_rate": 10, "min_investment": 1000},
    {"id": 3, "name": "Gold Plan", "interest_rate": 15, "min_investment": 10000},
]

transactions = []  # Stores user transactions
support_tickets = []  # Stores customer support tickets


# Endpoint to fetch available investment plans
@app.route("/api/investment-plans", methods=["GET"])
def get_investment_plans():
    """
    Retrieve the list of investment plans.
    """
    return jsonify({"success": True, "data": investment_plans})


# Endpoint to create a transaction
@app.route("/api/transactions", methods=["POST"])
def create_transaction():
    """
    Create a new investment transaction. Requires `plan_id`, `amount`, and `user_id`.
    """
    try:
        data = request.json
        # Validate required fields
        plan_id = data.get("plan_id")
        amount = data.get("amount")
        user_id = data.get("user_id")

        if not plan_id or not amount or not user_id:
            return jsonify({"success": False, "message": "Missing required fields"}), 400

        # Ensure the investment plan exists
        plan = next((p for p in investment_plans if p["id"] == plan_id), None)
        if not plan:
            return jsonify({"success": False, "message": "Invalid plan ID"}), 404

        # Ensure the investment amount meets the plan's minimum requirement
        if amount < plan["min_investment"]:
            return jsonify(
                {
                    "success": False,
                    "message": f"Amount must be at least {plan['min_investment']}",
                }
            ), 400

        # Create transaction
        transaction = {
            "id": len(transactions) + 1,
            "user_id": user_id,
            "plan_id": plan_id,
            "amount": amount,
            "interest_rate": plan["interest_rate"],
            "timestamp": datetime.datetime.utcnow().isoformat(),
        }
        transactions.append(transaction)
        return jsonify({"success": True, "data": transaction}), 201
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


# Endpoint to fetch transactions for a user
@app.route("/api/transactions/<int:user_id>", methods=["GET"])
def get_transactions(user_id):
    """
    Retrieve all transactions for a specific user.
    """
    user_transactions = [t for t in transactions if t["user_id"] == user_id]
    return jsonify({"success": True, "data": user_transactions})


# Endpoint to create a customer support ticket
@app.route("/api/support", methods=["POST"])
def create_support_ticket():
    """
    Create a new customer support ticket. Requires `user_id` and `message`.
    """
    try:
        data = request.json
        user_id = data.get("user_id")
        message = data.get("message")

        if not user_id or not message:
            return jsonify({"success": False, "message": "Missing required fields"}), 400

        ticket = {
            "id": len(support_tickets) + 1,
            "user_id": user_id,
            "message": message,
            "status": "Open",
            "timestamp": datetime.datetime.utcnow().isoformat(),
        }
        support_tickets.append(ticket)
        return jsonify({"success": True, "data": ticket}), 201
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


# Endpoint to fetch support tickets for a user
@app.route("/api/support/<int:user_id>", methods=["GET"])
def get_support_tickets(user_id):
    """
    Retrieve all customer support tickets for a specific user.
    """
    user_tickets = [t for t in support_tickets if t["user_id"] == user_id]
    return jsonify({"success": True, "data": user_tickets})


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```
