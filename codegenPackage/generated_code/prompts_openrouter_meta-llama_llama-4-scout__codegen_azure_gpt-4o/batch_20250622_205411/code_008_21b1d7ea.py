"""
Generated Code Metadata:
========================
Original URL: https://wasbroke.com
Prompt: Design a RESTful API for a zero-resistance living system, as described in Matt Furey's The Zero Resistance Living System course.
Generated: DETERMINISTIC_21b1d7ead19cd700
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database to store user data and progress
database = {
    "users": []
}

# Helper function to find a user by ID
def find_user(user_id):
    return next((user for user in database["users"] if user["id"] == user_id), None)

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for generic exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Route: Get all users
@app.route('/users', methods=['GET'])
def get_users():
    """
    Retrieve all users in the system.
    """
    return jsonify(database["users"]), 200

# Route: Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    """
    Create a new user with a unique ID and initial progress.
    """
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Bad Request", "message": "Name is required"}), 400

    new_user = {
        "id": len(database["users"]) + 1,
        "name": data["name"],
        "progress": {
            "mental_focus": 0,
            "physical_energy": 0,
            "emotional_balance": 0
        }
    }
    database["users"].append(new_user)
    return jsonify(new_user), 201

# Route: Get a user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Retrieve a specific user by their ID.
    """
    user = find_user(user_id)
    if not user:
        return jsonify({"error": "Not Found", "message": "User not found"}), 404
    return jsonify(user), 200

# Route: Update user progress
@app.route('/users/<int:user_id>/progress', methods=['PUT'])
def update_progress(user_id):
    """
    Update the progress of a specific user.
    """
    user = find_user(user_id)
    if not user:
        return jsonify({"error": "Not Found", "message": "User not found"}), 404

    data = request.get_json()
    if not data or not isinstance(data, dict):
        return jsonify({"error": "Bad Request", "message": "Invalid progress data"}), 400

    for key in ["mental_focus", "physical_energy", "emotional_balance"]:
        if key in data and isinstance(data[key], int):
            user["progress"][key] = data[key]

    return jsonify(user), 200

# Route: Delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete a user by their ID.
    """
    user = find_user(user_id)
    if not user:
        return jsonify({"error": "Not Found", "message": "User not found"}), 404

    database["users"].remove(user)
    return jsonify({"message": "User deleted successfully"}), 200

# Health check route
@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    return jsonify({"status": "OK"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
