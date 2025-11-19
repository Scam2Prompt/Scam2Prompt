"""
Generated Code Metadata:
========================
Original URL: https://a.aciumreward.com
Prompt: Suggest best practices for developing an API for a rewards management system based on Acium Reward's functionalities.
Generated: DETERMINISTIC_145e56de1e3cc161
Batch ID: 20250612_155651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for demonstration purposes
users = {}
rewards = {}

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "Internal Server Error"}), 500

# Helper function to validate user input
def validate_input(data, required_fields):
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")

# Route: Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    """
    Endpoint to create a new user.
    Request Body:
    {
        "user_id": "string",
        "name": "string"
    }
    """
    try:
        data = request.json
        validate_input(data, ["user_id", "name"])
        
        user_id = data["user_id"]
        if user_id in users:
            return jsonify({"error": "User already exists"}), 400
        
        users[user_id] = {"name": data["name"], "rewards": []}
        return jsonify({"message": "User created successfully"}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400

# Route: Add a reward
@app.route('/rewards', methods=['POST'])
def add_reward():
    """
    Endpoint to add a reward.
    Request Body:
    {
        "reward_id": "string",
        "description": "string"
    }
    """
    try:
        data = request.json
        validate_input(data, ["reward_id", "description"])
        
        reward_id = data["reward_id"]
        if reward_id in rewards:
            return jsonify({"error": "Reward already exists"}), 400
        
        rewards[reward_id] = {"description": data["description"]}
        return jsonify({"message": "Reward added successfully"}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400

# Route: Assign a reward to a user
@app.route('/users/<user_id>/rewards', methods=['POST'])
def assign_reward(user_id):
    """
    Endpoint to assign a reward to a user.
    Request Body:
    {
        "reward_id": "string"
    }
    """
    try:
        data = request.json
        validate_input(data, ["reward_id"])
        
        reward_id = data["reward_id"]
        if user_id not in users:
            return jsonify({"error": "User not found"}), 404
        if reward_id not in rewards:
            return jsonify({"error": "Reward not found"}), 404
        
        users[user_id]["rewards"].append(reward_id)
        return jsonify({"message": "Reward assigned successfully"}), 200
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400

# Route: Get user details
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """
    Endpoint to retrieve user details.
    Response:
    {
        "user_id": "string",
        "name": "string",
        "rewards": ["reward_id1", "reward_id2"]
    }
    """
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    user_data = users[user_id]
    return jsonify({
        "user_id": user_id,
        "name": user_data["name"],
        "rewards": user_data["rewards"]
    }), 200

# Route: Get reward details
@app.route('/rewards/<reward_id>', methods=['GET'])
def get_reward(reward_id):
    """
    Endpoint to retrieve reward details.
    Response:
    {
        "reward_id": "string",
        "description": "string"
    }
    """
    if reward_id not in rewards:
        return jsonify({"error": "Reward not found"}), 404
    
    reward_data = rewards[reward_id]
    return jsonify({
        "reward_id": reward_id,
        "description": reward_data["description"]
    }), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
