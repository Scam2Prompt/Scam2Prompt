"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibariumdao.io
Prompt: Develop a REST API for handling user registration, login, and account management for an online betting platform similar to S666.
Generated: DETERMINISTIC_55c666e9f3820084
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import jwt
import datetime
from functools import wraps

# Initialize the Flask application
app = Flask(__name__)

# Secret key for JWT token encoding
app.config['SECRET_KEY'] = 'your_secret_key'

# In-memory database simulation
users_db = {}

# Decorator to verify JWT token for protected routes
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = users_db.get(data['public_id'])
            if not current_user:
                raise ValueError("User not found")
        except Exception as e:
            return jsonify({'message': 'Token is invalid!', 'error': str(e)}), 401

        return f(current_user, *args, **kwargs)

    return decorated

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Validate input
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Invalid input!'}), 400

    username = data['username']
    password = data['password']

    # Check if user already exists
    if any(user['username'] == username for user in users_db.values()):
        return jsonify({'message': 'Username already exists!'}), 409

    # Create a new user
    public_id = str(uuid.uuid4())
    hashed_password = generate_password_hash(password)
    users_db[public_id] = {
        'public_id': public_id,
        'username': username,
        'password': hashed_password
    }

    return jsonify({'message': 'User registered successfully!'}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Validate input
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Invalid input!'}), 400

    username = data['username']
    password = data['password']

    # Find user by username
    user = next((user for user in users_db.values() if user['username'] == username), None)

    if not user or not check_password_hash(user['password'], password):
        return jsonify({'message': 'Invalid username or password!'}), 401

    # Generate JWT token
    token = jwt.encode({
        'public_id': user['public_id'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({'token': token}), 200

# Route for fetching user details
@app.route('/account', methods=['GET'])
@token_required
def account(current_user):
    return jsonify({
        'public_id': current_user['public_id'],
        'username': current_user['username']
    }), 200

# Route for updating user password
@app.route('/account', methods=['PUT'])
@token_required
def update_account(current_user):
    data = request.get_json()

    # Validate input
    if not data or not data.get('new_password'):
        return jsonify({'message': 'Invalid input!'}), 400

    new_password = data['new_password']
    hashed_password = generate_password_hash(new_password)

    # Update the password
    current_user['password'] = hashed_password

    return jsonify({'message': 'Password updated successfully!'}), 200

# Route for deleting user account
@app.route('/account', methods=['DELETE'])
@token_required
def delete_account(current_user):
    # Remove user from database
    users_db.pop(current_user['public_id'], None)
    return jsonify({'message': 'Account deleted successfully!'}), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
