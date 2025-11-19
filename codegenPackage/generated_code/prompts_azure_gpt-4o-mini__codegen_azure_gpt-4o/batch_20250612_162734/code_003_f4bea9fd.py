"""
Generated Code Metadata:
========================
Original URL: https://theentrepreneursstudio.blogspot.com
Prompt: Can you provide an example of an API that could be used to manage user registrations for a contest, like the one detailed on theentrepreneursstudio.blogspot.com?
Generated: DETERMINISTIC_f4bea9fd81372ffd
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory database to store user registrations
registrations = {}

# Helper function to validate user input
def validate_registration_data(data):
    required_fields = ['name', 'email', 'age']
    for field in required_fields:
        if field not in data:
            return f"Missing required field: {field}"
    if not isinstance(data['age'], int) or data['age'] <= 0:
        return "Age must be a positive integer"
    return None

@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a user for the contest.
    Expects JSON payload with 'name', 'email', and 'age'.
    """
    try:
        # Parse JSON payload
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400

        # Validate input data
        validation_error = validate_registration_data(data)
        if validation_error:
            return jsonify({"error": validation_error}), 400

        # Generate a unique ID for the user
        user_id = str(uuid.uuid4())

        # Store the registration in the in-memory database
        registrations[user_id] = {
            "name": data['name'],
            "email": data['email'],
            "age": data['age']
        }

        # Return success response
        return jsonify({"message": "Registration successful", "user_id": user_id}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.route('/registrations', methods=['GET'])
def get_registrations():
    """
    Endpoint to retrieve all user registrations.
    """
    try:
        return jsonify({"registrations": registrations}), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.route('/registration/<user_id>', methods=['GET'])
def get_registration(user_id):
    """
    Endpoint to retrieve a specific user's registration by user_id.
    """
    try:
        if user_id not in registrations:
            return jsonify({"error": "User not found"}), 404
        return jsonify({"registration": registrations[user_id]}), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.route('/registration/<user_id>', methods=['DELETE'])
def delete_registration(user_id):
    """
    Endpoint to delete a specific user's registration by user_id.
    """
    try:
        if user_id not in registrations:
            return jsonify({"error": "User not found"}), 404
        del registrations[user_id]
        return jsonify({"message": "Registration deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
