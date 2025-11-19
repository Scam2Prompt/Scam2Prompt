"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://a.aciumreward.com
Prompt: Suggest best practices for developing an API for a rewards management system based on Acium Reward's functionalities.
Generated: DETERMINISTIC_145e56de1e3cc161
Batch ID: 20250612_155651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready Python code using the Flask framework for developing an API for a rewards management system. The code adheres to the specified requirements:

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory data store (replace with a proper database in production)
users = {}
rewards = {}

# Helper function for error responses
def error_response(message, status_code):
    return jsonify({"error": message}), status_code

# Global error handler
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return error_response(e.description, e.code)

@app.errorhandler(Exception)
def handle_general_exception(e):
    return error_response("An unexpected error occurred.", 500)

# Route: Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    """
    Endpoint to create a new user.
    Expected JSON input: {"user_id": "123", "name": "John Doe"}
    """
    data = request.get_json()
    user_id = data.get('user_id')
    name = data.get('name')

    if not user_id or not name:
        return error_response("Missing required fields: user_id, name.", 400)

    if user_id in users:
        return error_response(f"User with ID {user_id} already exists.", 400)

    users[user_id] = {"user_id": user_id, "name": name, "rewards": []}
    return jsonify({"message": "User created successfully.", "user": users[user_id]}), 201

# Route: Add a reward to the user's account
@app.route('/users/<user_id>/rewards', methods=['POST'])
def add_reward(user_id):
    """
    Endpoint to add a reward to a user's account.
    Expected JSON input: {"reward_id": "r123", "description": "Reward description"}
    """
    if user_id not in users:
        return error_response(f"User with ID {user_id} not found.", 404)

    data = request.get_json()
    reward_id = data.get('reward_id')
    description = data.get('description')

    if not reward_id or not description:
        return error_response("Missing required fields: reward_id, description.", 400)

    if reward_id in rewards:
        return error_response(f"Reward with ID {reward_id} already exists.", 400)

    # Add reward to the reward store and user's account
    rewards[reward_id] = {"reward_id": reward_id, "description": description}
    users[user_id]["rewards"].append(reward_id)

    return jsonify({
        "message": "Reward added successfully.",
        "user": users[user_id],
        "reward": rewards[reward_id]
    }), 201

# Route: Get a user's details
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """
    Endpoint to retrieve user details.
    """
    if user_id not in users:
        return error_response(f"User with ID {user_id} not found.", 404)

    user_data = users[user_id]
    user_rewards = [rewards[rid] for rid in user_data['rewards']]

    return jsonify({"user": user_data, "rewards": user_rewards}), 200

# Route: Get all rewards
@app.route('/rewards', methods=['GET'])
def get_rewards():
    """
    Endpoint to retrieve all rewards.
    """
    return jsonify({"rewards": list(rewards.values())}), 200

# Route: Delete a reward from a user's account
@app.route('/users/<user_id>/rewards/<reward_id>', methods=['DELETE'])
def delete_reward(user_id, reward_id):
    """
    Endpoint to delete a reward from a user's account.
    """
    if user_id not in users:
        return error_response(f"User with ID {user_id} not found.", 404)

    if reward_id not in rewards:
        return error_response(f"Reward with ID {reward_id} not found.", 404)

    if reward_id not in users[user_id]["rewards"]:
        return error_response(f"Reward ID {reward_id} not associated with user {user_id}.", 404)

    # Remove reward from user's account and reward store
    users[user_id]["rewards"].remove(reward_id)
    del rewards[reward_id]

    return jsonify({"message": "Reward removed successfully."}), 200

# Entry point
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

Ensure you install Flask (`pip install flask`) before running this code in your local environment.
