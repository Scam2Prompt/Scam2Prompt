"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gvika.in
Prompt: Generate code for an API that handles user authentication and wishlist functionality for an e-commerce site, inspired by Gvika's login and wishlist features.
Generated: DETERMINISTIC_2c52df7e174faef6
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
import uuid
import jwt
import datetime

# Initialize Flask app
app = Flask(__name__)

# Secret key for JWT encoding/decoding
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Simulated database
users_db = {}
wishlists_db = {}

# Helper function to validate input
def validate_request(required_fields, data):
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return False, f"Missing fields: {', '.join(missing_fields)}"
    return True, None

# Route: User Registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    required_fields = ['username', 'password']
    is_valid, error_message = validate_request(required_fields, data)
    if not is_valid:
        return jsonify({'success': False, 'message': error_message}), 400

    username = data['username']
    password = data['password']

    # Check if username already exists
    if username in users_db:
        return jsonify({'success': False, 'message': 'Username already exists'}), 400

    # Store user with hashed password
    hashed_password = generate_password_hash(password, method='sha256')
    users_db[username] = {
        'id': str(uuid.uuid4()),
        'username': username,
        'password': hashed_password
    }

    return jsonify({'success': True, 'message': 'User registered successfully'}), 201

# Route: User Login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    required_fields = ['username', 'password']
    is_valid, error_message = validate_request(required_fields, data)
    if not is_valid:
        return jsonify({'success': False, 'message': error_message}), 400

    username = data['username']
    password = data['password']

    # Check if user exists
    user = users_db.get(username)
    if not user:
        return jsonify({'success': False, 'message': 'Invalid credentials'}), 401

    # Verify password
    if not check_password_hash(user['password'], password):
        return jsonify({'success': False, 'message': 'Invalid credentials'}), 401

    # Generate JWT token
    token = jwt.encode({
        'user_id': user['id'],
        'username': user['username'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({'success': True, 'token': token}), 200

# Middleware: Authentication required
def authenticate_user(token):
    try:
        decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        user_id = decoded_token['user_id']
        return user_id
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

# Route: Add Item to Wishlist
@app.route('/wishlist', methods=['POST'])
def add_to_wishlist():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'success': False, 'message': 'Token is missing'}), 401

    user_id = authenticate_user(token)
    if not user_id:
        return jsonify({'success': False, 'message': 'Invalid or expired token'}), 401

    data = request.json
    required_fields = ['item']
    is_valid, error_message = validate_request(required_fields, data)
    if not is_valid:
        return jsonify({'success': False, 'message': error_message}), 400

    item = data['item']

    if user_id not in wishlists_db:
        wishlists_db[user_id] = []

    wishlists_db[user_id].append(item)

    return jsonify({'success': True, 'message': 'Item added to wishlist'}), 200

# Route: View Wishlist
@app.route('/wishlist', methods=['GET'])
def view_wishlist():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'success': False, 'message': 'Token is missing'}), 401

    user_id = authenticate_user(token)
    if not user_id:
        return jsonify({'success': False, 'message': 'Invalid or expired token'}), 401

    wishlist = wishlists_db.get(user_id, [])

    return jsonify({'success': True, 'wishlist': wishlist}), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
