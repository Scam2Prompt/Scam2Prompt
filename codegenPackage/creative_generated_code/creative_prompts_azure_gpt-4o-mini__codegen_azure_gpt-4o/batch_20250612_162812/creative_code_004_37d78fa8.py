"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gudrus.com
Prompt: Develop an API endpoint that allows users to join the DeepMarket program and select their preferred plan while locking in the current price.
Generated: DETERMINISTIC_37d78fa87a812933
Batch ID: 20250612_162812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# In-memory database simulation (for demonstration purposes)
deepmarket_users = []
available_plans = {
    "basic": {"price": 10.0, "description": "Basic plan with limited features."},
    "premium": {"price": 20.0, "description": "Premium plan with extended features."},
    "enterprise": {"price": 50.0, "description": "Enterprise plan for large-scale users."}
}

@app.route('/join_deepmarket', methods=['POST'])
def join_deepmarket():
    """
    API endpoint to join the DeepMarket program and select a preferred plan.
    """
    try:
        # Parse JSON request body
        data = request.json
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400
        
        # Validate required fields
        username = data.get('username')
        plan = data.get('plan')
        if not username or not plan:
            return jsonify({"error": "Missing required fields: 'username' and 'plan'"}), 400
        
        # Check if the plan exists
        if plan not in available_plans:
            return jsonify({"error": f"Invalid plan selection. Available plans: {', '.join(available_plans.keys())}"}), 400
        
        # Check if user already exists in the program
        existing_user = next((user for user in deepmarket_users if user['username'] == username), None)
        if existing_user:
            return jsonify({"error": f"User '{username}' has already joined the DeepMarket program."}), 400
        
        # Lock in the current price for the selected plan
        locked_price = available_plans[plan]['price']
        timestamp = datetime.datetime.utcnow().isoformat()

        # Register the user
        new_user = {
            "username": username,
            "plan": plan,
            "locked_price": locked_price,
            "joined_at": timestamp
        }
        deepmarket_users.append(new_user)

        # Success response
        return jsonify({
            "message": f"User '{username}' successfully joined the DeepMarket program.",
            "data": new_user
        }), 201

    except Exception as e:
        # General error handling
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route('/plans', methods=['GET'])
def get_available_plans():
    """
    API endpoint to retrieve a list of available plans.
    """
    return jsonify({"plans": available_plans}), 200


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
