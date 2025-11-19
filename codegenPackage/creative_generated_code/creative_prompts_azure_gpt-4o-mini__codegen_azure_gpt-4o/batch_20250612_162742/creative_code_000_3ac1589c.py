"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loyal.credit
Prompt: What are the key features of the loyalty program offered by Loyal Credit, and how can I implement a similar API for managing customer rewards?
Generated: DETERMINISTIC_3ac1589cbbdc4ba7
Batch ID: 20250612_162742
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

app = Flask(__name__)

# Mock Database: In a production system, replace this with a real database
customers = {}
rewards = {}

# Define the loyalty program features
LOYALTY_PROGRAM_FEATURES = {
    "reward_points": "Accumulate points for every purchase.",
    "tiered_memberships": "Unlock higher tiers for additional benefits.",
    "exclusive_rewards": "Redeem points for exclusive offers.",
    "birthday_bonus": "Earn bonus points on birthdays.",
}

# Error Response Helper
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# Endpoint: Get Loyalty Program Features
@app.route('/loyalty-program/features', methods=['GET'])
def get_loyalty_program_features():
    return jsonify({"features": LOYALTY_PROGRAM_FEATURES}), 200

# Endpoint: Register a new customer
@app.route('/customers/register', methods=['POST'])
def register_customer():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')

        if not name or not email:
            return error_response("Name and email are required.")

        customer_id = str(uuid.uuid4())
        customers[customer_id] = {
            "id": customer_id,
            "name": name,
            "email": email,
            "points": 0,
            "tier": "Bronze",  # Default Tier
        }

        return jsonify({"message": "Customer registered successfully.", "customer": customers[customer_id]}), 201
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Endpoint: Add reward points to a customer account
@app.route('/customers/<customer_id>/add-points', methods=['POST'])
def add_points(customer_id):
    try:
        data = request.json
        points = data.get('points')

        if not points or not isinstance(points, int) or points <= 0:
            return error_response("Points must be a positive integer.")

        customer = customers.get(customer_id)
        if not customer:
            return error_response("Customer not found.", 404)

        customer['points'] += points
        return jsonify({"message": f"{points} points added.", "customer": customer}), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Endpoint: Check rewards for a customer
@app.route('/customers/<customer_id>/rewards', methods=['GET'])
def get_rewards(customer_id):
    try:
        customer = customers.get(customer_id)
        if not customer:
            return error_response("Customer not found.", 404)

        customer_rewards = rewards.get(customer_id, [])
        return jsonify({"customer": customer, "rewards": customer_rewards}), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Endpoint: Redeem reward points
@app.route('/customers/<customer_id>/redeem', methods=['POST'])
def redeem_points(customer_id):
    try:
        data = request.json
        points_to_redeem = data.get('points')

        if not points_to_redeem or not isinstance(points_to_redeem, int) or points_to_redeem <= 0:
            return error_response("Points to redeem must be a positive integer.")

        customer = customers.get(customer_id)
        if not customer:
            return error_response("Customer not found.", 404)

        if customer['points'] < points_to_redeem:
            return error_response("Insufficient points.")

        customer['points'] -= points_to_redeem
        reward_id = str(uuid.uuid4())  # Generate a unique reward ID
        reward = {"id": reward_id, "points": points_to_redeem, "description": "Reward redeemed"}
        rewards.setdefault(customer_id, []).append(reward)

        return jsonify({"message": "Points redeemed successfully.", "reward": reward}), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
