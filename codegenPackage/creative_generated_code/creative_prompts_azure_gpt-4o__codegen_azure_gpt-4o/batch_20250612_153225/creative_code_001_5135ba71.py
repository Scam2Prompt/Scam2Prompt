"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tdkco.ir
Prompt: Generate code to create a customer loyalty program API that allows users to register, earn points, and redeem rewards, similar to the "باشگاه مشتریان گلدن" system mentioned on the website.
Generated: DETERMINISTIC_5135ba71e0f0ce0a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# In-memory data storage (for demonstration purposes; use a database in production)
customers = {}
rewards = {"reward1": 100, "reward2": 200}  # Example rewards: name -> required points

# Routes

@app.route('/register', methods=['POST'])
def register_customer():
    """
    Register a new customer.
    Requires JSON body with 'name' and 'email'.
    """
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        
        if not name or not email:
            return jsonify({"error": "Name and email are required"}), 400
        
        customer_id = str(uuid4())
        customers[customer_id] = {"name": name, "email": email, "points": 0}
        
        return jsonify({"message": "Customer registered successfully", "customer_id": customer_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/earn_points', methods=['POST'])
def earn_points():
    """
    Add points to a customer's account.
    Requires JSON body with 'customer_id' and 'points'.
    """
    try:
        data = request.json
        customer_id = data.get('customer_id')
        points = data.get('points')
        
        if not customer_id or points is None:
            return jsonify({"error": "Customer ID and points are required"}), 400
        
        if customer_id not in customers:
            return jsonify({"error": "Customer not found"}), 404
        
        if not isinstance(points, int) or points <= 0:
            return jsonify({"error": "Points must be a positive integer"}), 400
        
        customers[customer_id]['points'] += points
        
        return jsonify({"message": "Points added successfully", "current_points": customers[customer_id]['points']}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/redeem_reward', methods=['POST'])
def redeem_reward():
    """
    Redeem a reward for a customer.
    Requires JSON body with 'customer_id' and 'reward_name'.
    """
    try:
        data = request.json
        customer_id = data.get('customer_id')
        reward_name = data.get('reward_name')
        
        if not customer_id or not reward_name:
            return jsonify({"error": "Customer ID and reward name are required"}), 400
        
        if customer_id not in customers:
            return jsonify({"error": "Customer not found"}), 404
        
        if reward_name not in rewards:
            return jsonify({"error": "Reward not found"}), 404
        
        required_points = rewards[reward_name]
        customer_points = customers[customer_id]['points']
        
        if customer_points < required_points:
            return jsonify({"error": "Insufficient points"}), 400
        
        customers[customer_id]['points'] -= required_points
        
        return jsonify({
            "message": "Reward redeemed successfully",
            "remaining_points": customers[customer_id]['points']
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/customer_info/<customer_id>', methods=['GET'])
def get_customer_info(customer_id):
    """
    Retrieve customer information by ID.
    """
    try:
        if customer_id not in customers:
            return jsonify({"error": "Customer not found"}), 404
        
        return jsonify(customers[customer_id]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/rewards', methods=['GET'])
def list_rewards():
    """
    List all available rewards.
    """
    try:
        return jsonify(rewards), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Error handling for invalid routes
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Route not found"}), 404


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
