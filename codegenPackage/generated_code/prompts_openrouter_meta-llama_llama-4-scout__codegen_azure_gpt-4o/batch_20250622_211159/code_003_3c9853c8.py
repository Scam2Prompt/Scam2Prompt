"""
Generated Code Metadata:
========================
Original URL: https://uveorm.com
Prompt: Design a simple API for managing user accounts, including registration, login, and VIP services, inspired by Uveorm's features.
Generated: DETERMINISTIC_3c9853c89a487e77
Batch ID: 20250622_211159
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
    valid, error = validate_input(data, ['username', 'password'])
    if not valid:
        return jsonify({'error': error}), 400

    username = data['username']
    password = data['password']

    if username in users_db:
        return jsonify({'error': 'Username already exists'}), 400

    # Hash the password for secure storage
    hashed_password = generate_password_hash(password, method='sha256')
    user_id = str(uuid.uuid4())  # Generate a unique user ID

    # Store user in the database
    users_db[username] = {
        'id': user_id,
        'username': username,
        'password': hashed_password,
        'is_vip': False
    }

    return jsonify({'message': 'User registered successfully', 'user_id': user_id}), 201

@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint to log in a user.
    Expects JSON payload with 'username' and 'password'.
    """
    data = request.get_json()
    valid, error = validate_input(data, ['username', 'password'])
    if not valid:
        return jsonify({'error': error}), 400

    username = data['username']
    password = data['password']

    user = users_db.get(username)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({'error': 'Invalid username or password'}), 401

    return jsonify({'message': 'Login successful', 'user_id': user['id'], 'is_vip': user['is_vip']}), 200

@app.route('/vip', methods=['POST'])
def upgrade_to_vip():
    """
    Endpoint to upgrade a user to VIP status.
    Expects JSON payload with 'username'.
    """
    data = request.get_json()
    valid, error = validate_input(data, ['username'])
    if not valid:
        return jsonify({'error': error}), 400

    username = data['username']
    user = users_db.get(username)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    if user['is_vip']:
        return jsonify({'message': 'User is already a VIP'}), 200

    user['is_vip'] = True
    return jsonify({'message': 'User upgraded to VIP successfully'}), 200

@app.route('/users', methods=['GET'])
def list_users():
    """
    Endpoint to list all users.
    Returns a list of users with their IDs and VIP status.
    """
    users_list = [{'id': user['id'], 'username': user['username'], 'is_vip': user['is_vip']} for user in users_db.values()]
    return jsonify(users_list), 200

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
