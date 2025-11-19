"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://a.aciumreward.com
Prompt: Generate a code snippet for implementing a reward system API similar to Acium Reward.
Generated: DETERMINISTIC_114d70e96d08c9ab
Batch ID: 20250612_155651
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

# In-memory database for demonstration purposes
# In production, use a proper database (e.g., PostgreSQL, MySQL)
users = {}
rewards = {}

# Utility function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# Error response helper
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# Endpoint to register a new user
@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.json
        username = data.get('username')

        if not username:
            return error_response("Username is required.")
        
        if username in users:
            return error_response("Username already exists.")

        user_id = generate_id()
        users[username] = {"id": user_id, "rewards": []}
        
        return jsonify({"message": "User registered successfully.", "user_id": user_id}), 201
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}")

# Endpoint to add a reward for a user
@app.route('/reward', methods=['POST'])
def add_reward():
    try:
        data = request.json
        username = data.get('username')
        reward_description = data.get('description')

        if not username or not reward_description:
            return error_response("Username and reward description are required.")
        
        user = users.get(username)
        if not user:
            return error_response("User not found.")

        reward_id = generate_id()
        reward = {"id": reward_id, "description": reward_description}
        user["rewards"].append(reward)
        rewards[reward_id] = reward
        
        return jsonify({"message": "Reward added successfully.", "reward": reward}), 201
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}")

# Endpoint to view a user's rewards
@app.route('/rewards/<username>', methods=['GET'])
def view_rewards(username):
    try:
        user = users.get(username)
        if not user:
            return error_response("User not found.", 404)
        
        return jsonify({"username": username, "rewards": user["rewards"]}), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}")

# Endpoint to delete a reward
@app.route('/reward/<reward_id>', methods=['DELETE'])
def delete_reward(reward_id):
    try:
        reward = rewards.pop(reward_id, None)
        if not reward:
            return error_response("Reward not found.", 404)
        
        # Remove reward from user's reward list
        for user in users.values():
            user["rewards"] = [r for r in user["rewards"] if r["id"] != reward_id]
        
        return jsonify({"message": "Reward deleted successfully."}), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}")

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
