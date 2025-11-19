"""
Generated Code Metadata:
========================
Original URL: https://itmastar.pages.dev
Prompt: Generate a code snippet for a project that showcases real skills in IT development.
Generated: DETERMINISTIC_6bfe7d5f9424742a
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project: RESTful API for User Management
Language: Python
Framework: Flask
Description: A simple RESTful API to manage users with CRUD operations.
"""

from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory database to store user data
users = {}

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Route: Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({"users": list(users.values())}), 200

# Route: Get a user by ID
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

# Route: Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'email' not in data:
            return jsonify({"error": "Invalid input"}), 400

        user_id = str(uuid.uuid4())  # Generate a unique ID for the user
        user = {
            "id": user_id,
            "name": data['name'],
            "email": data['email']
        }
        users[user_id] = user
        return jsonify(user), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Update an existing user
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        user = users.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        data = request.get_json()
        if not data or ('name' not in data and 'email' not in data):
            return jsonify({"error": "Invalid input"}), 400

        user['name'] = data.get('name', user['name'])
        user['email'] = data.get('email', user['email'])
        users[user_id] = user
        return jsonify(user), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Delete a user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = users.pop(user_id, None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User deleted successfully"}), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
