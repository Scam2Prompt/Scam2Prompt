"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://diskonin.id
Prompt: Suggest an API for managing secure user authentication and account registration for a gaming platform that supports premium account upgrades.
Generated: DETERMINISTIC_898844f753424ba0
Batch ID: 20250612_153246
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
import jwt
import datetime
from functools import wraps

# Initialize Flask app
app = Flask(__name__)

# Secret key for JWT encoding/decoding (ensure to keep it safe and secure in production)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Mock database for users (in production, use a real database like PostgreSQL, MySQL, etc.)
users_db = {}

# Helper function to check if a user exists
def user_exists(username):
    return username in users_db

# Decorator for token-required routes
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = users_db.get(data['username'])
            if not current_user:
                raise ValueError("Invalid token user.")
        except Exception as e:
            return jsonify({'message': f'Token is invalid: {str(e)}'}), 401

        return f(current_user, *args, **kwargs)
    return decorated

# Route for registering a new user
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    if user_exists(username):
        return jsonify({'message': 'User already exists'}), 409

    # Hash the password for secure storage
    hashed_password = generate_password_hash(password, method='sha256')
    users_db[username] = {'password': hashed_password, 'is_premium': False}
    
    return jsonify({'message': 'User registered successfully'}), 201

# Route for logging in
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    user = users_db.get(username)
    if not user:
        return jsonify({'message': 'Invalid username or password'}), 401

    if not check_password_hash(user['password'], password):
        return jsonify({'message': 'Invalid username or password'}), 401

    # Generate JWT token
    token = jwt.encode({'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
                       app.config['SECRET_KEY'], algorithm="HS256")
    
    return jsonify({'token': token}), 200

# Route for upgrading to premium account
@app.route('/upgrade', methods=['POST'])
@token_required
def upgrade(current_user):
    if current_user['is_premium']:
        return jsonify({'message': 'User is already a premium member'}), 400

    current_user['is_premium'] = True
    return jsonify({'message': 'Account upgraded to premium successfully'}), 200

# Route for accessing user account details
@app.route('/account', methods=['GET'])
@token_required
def account(current_user):
    return jsonify({'username': request.json.get('username'), "premium":current_user
                   }), 200


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
