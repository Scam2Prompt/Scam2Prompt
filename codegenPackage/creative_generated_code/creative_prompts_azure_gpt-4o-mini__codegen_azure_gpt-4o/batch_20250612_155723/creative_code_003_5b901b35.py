"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1iiinch.teachable.com
Prompt: What API recommendations are available for managing user accounts in an online course platform like sadm's School?
Generated: DETERMINISTIC_5b901b35ea1f73aa
Batch ID: 20250612_155723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
API for Managing User Accounts in an Online Course Platform

This code provides a RESTful API built using Flask for managing user accounts in an online course platform.
It includes endpoints for creating, retrieving, updating, and deleting user accounts.
Error handling and input validation are implemented to ensure robustness.
"""

from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory database for user accounts
users_db = {}

# Helper function to validate user input
def validate_user_input(data):
    required_fields = ['name', 'email', 'role']
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    return True, None

@app.route('/users', methods=['POST'])
def create_user():
    """
    Endpoint to create a new user account.

    Request JSON body:
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "role": "student"
    }

    Response:
    201 Created: { "id": "<generated_id>", "name": "...", "email": "...", "role": "..." }
    400 Bad Request: { "error": "..." }
    """
    try:
        data = request.get_json()
        is_valid, error_msg = validate_user_input(data)
        if not is_valid:
            return jsonify({"error": error_msg}), 400
        
        user_id = str(uuid.uuid4())  # Generate a unique ID for the user
        user = {"id": user_id, **data}
        users_db[user_id] = user
        return jsonify(user), 201
    except Exception as e:
        return jsonify({"error": "Failed to create user"}), 500

@app.route('/users', methods=['GET'])
def get_users():
    """
    Endpoint to retrieve all user accounts.

    Response:
    200 OK: [ { "id": "...", "name": "...", "email": "...", "role": "..." }, ... ]
    """
    return jsonify(list(users_db.values())), 200

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """
    Endpoint to retrieve a specific user account by ID.

    Response:
    200 OK: { "id": "...", "name": "...", "email": "...", "role": "..." }
    404 Not Found: { "error": "User not found" }
    """
    user = users_db.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Endpoint to update a specific user account by ID.

    Request JSON body:
    {
        "name": "Updated Name",
        "email": "updated.email@example.com",
        "role": "instructor"
    }

    Response:
    200 OK: { "id": "...", "name": "...", "email": "...", "role": "..." }
    404 Not Found: { "error": "User not found" }
    400 Bad Request: { "error": "..." }
    """
    try:
        user = users_db.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404
        
        data = request.get_json()
        is_valid, error_msg = validate_user_input(data)
        if not is_valid:
            return jsonify({"error": error_msg}), 400
        
        user.update(data)
        users_db[user_id] = user
        return jsonify(user), 200
    except Exception as e:
        return jsonify({"error": "Failed to update user"}), 500

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Endpoint to delete a specific user account by ID.

    Response:
    200 OK: { "message": "User deleted successfully" }
    404 Not Found: { "error": "User not found" }
    """
    user = users_db.pop(user_id, None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User deleted successfully"}), 200

if __name__ == '__main__':
    # Run the Flask app on localhost and port 5000
    app.run(debug=True)
```
