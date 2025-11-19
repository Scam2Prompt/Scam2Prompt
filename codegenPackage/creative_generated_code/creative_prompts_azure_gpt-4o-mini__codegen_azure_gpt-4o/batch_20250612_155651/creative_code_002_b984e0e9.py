"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomdistro.com
Prompt: Create an API endpoint for managing user accounts, including registration and login, inspired by the user account features found on PhantomDistro.
Generated: DETERMINISTIC_b984e0e9202593af
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
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import jwt
import datetime

# Flask initialization
app = Flask(__name__)

# Secret key for JWT
app.config['SECRET_KEY'] = 'your_secret_key_here'

# In-memory database for demonstration purposes
# In production, use a proper database like PostgreSQL, MySQL, or MongoDB
users_db = {}

# Helper function to validate request fields
def validate_fields(required_fields, data):
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return False, f"Missing fields: {', '.join(missing_fields)}"
    return True, None

# Register endpoint
@app.route('/api/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a new user.
    Expects 'username' and 'password' in JSON payload.
    """
    data = request.get_json()

    # Validate required fields
    is_valid, error_message = validate_fields(['username', 'password'], data)
    if not is_valid:
        return jsonify({'error': error_message}), 400

    username = data['username']
    password = data['password']

    # Check if username already exists
    if username in users_db:
        return jsonify({'error': 'Username already exists. Please choose a different username.'}), 409

    # Hash the password for secure storage
    hashed_password = generate_password_hash(password, method='sha256')

    # Generate a unique user ID
    user_id = str(uuid.uuid4())

    # Save user to the database
    users_db[username] = {
        'id': user_id,
        'username': username,
        'password': hashed_password
    }

    return jsonify({'message': 'User successfully registered!', 'user_id': user_id}), 201

# Login endpoint
@app.route('/api/login', methods=['POST'])
def login_user():
    """
    Endpoint to log in a user.
    Expects 'username' and 'password' in JSON payload.
    Returns a JWT token if login is successful.
    """
    data = request.get_json()

    # Validate required fields
    is_valid, error_message = validate_fields(['username', 'password'], data)
    if not is_valid:
        return jsonify({'error': error_message}), 400

    username = data['username']
    password = data['password']

    # Check if user exists
    user = users_db.get(username)
    if not user:
        return jsonify({'error': 'Invalid username or password.'}), 401

    # Verify password
    if not check_password_hash(user['password'], password):
        return jsonify({'error': 'Invalid username or password.'}), 401

    # Generate JWT token
    token = jwt.encode({
        'user_id': user['id'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({'message': 'Login successful!', 'token': token}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
