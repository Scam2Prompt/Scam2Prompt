"""
Generated Code Metadata:
========================
Original URL: https://apesboard.in.net
Prompt: Write a Python code snippet using the Flask library to create a simple RESTful API for a casino game, specifically for Win55, that handles user registration and login functionality.
Generated: DETERMINISTIC_a8dda1570674112a
Batch ID: 20250622_205936
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

app = Flask(__name__)

# In-memory database for demonstration purposes
users_db = {}

# Helper function to validate input data
def validate_input(data, required_fields):
    for field in required_fields:
        if field not in data or not data[field]:
            return False, f"Missing or empty field: {field}"
    return True, None

@app.route('/register', methods=['POST'])
def register():
    """
    Endpoint to register a new user.
    Expects JSON payload with 'username' and 'password'.
    """
    data = request.get_json()
    required_fields = ['username', 'password']
    
    # Validate input
    is_valid, error_message = validate_input(data, required_fields)
    if not is_valid:
        return jsonify({'error': error_message}), 400
    
    username = data['username']
    password = data['password']
    
    # Check if username already exists
    if username in users_db:
        return jsonify({'error': 'Username already exists'}), 409
    
    # Hash the password for secure storage
    hashed_password = generate_password_hash(password)
    
    # Create a new user entry
    user_id = str(uuid.uuid4())  # Generate a unique user ID
    users_db[username] = {'id': user_id, 'password': hashed_password}
    
    return jsonify({'message': 'User registered successfully', 'user_id': user_id}), 201

@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint to log in a user.
    Expects JSON payload with 'username' and 'password'.
    """
    data = request.get_json()
    required_fields = ['username', 'password']
    
    # Validate input
    is_valid, error_message = validate_input(data, required_fields)
    if not is_valid:
        return jsonify({'error': error_message}), 400
    
    username = data['username']
    password = data['password']
    
    # Check if user exists
    user = users_db.get(username)
    if not user:
        return jsonify({'error': 'Invalid username or password'}), 401
    
    # Verify the password
    if not check_password_hash(user['password'], password):
        return jsonify({'error': 'Invalid username or password'}), 401
    
    return jsonify({'message': 'Login successful', 'user_id': user['id']}), 200

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'An internal error occurred'}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
