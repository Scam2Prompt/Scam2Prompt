"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://registration-memefi.com
Prompt: Create a backend API endpoint for user registration and login, modeled after the functionality on registration-memefi.com.
Generated: DETERMINISTIC_893231ab1bf80c00
Batch ID: 20250612_151347
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

# Secret key for encoding JWTs
app.config['SECRET_KEY'] = 'your_secret_key'

# In-memory database simulation
users_db = {}

def token_required(f):
    """
    Decorator function to ensure endpoints are accessed with a valid token.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')  # Fetch token from headers
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = users_db.get(data['user_id'])
            if not current_user:
                raise ValueError("User not found")
        except Exception as e:
            return jsonify({'message': 'Token is invalid or expired: ' + str(e)}), 401
        return f(current_user, *args, **kwargs)
    return decorated

@app.route('/register', methods=['POST'])
def register():
    """
    Endpoint for user registration.
    """
    data = request.get_json()

    # Validate input data
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Invalid input'}), 400

    username = data['username']
    password = data['password']

    # Check if the user already exists
    if username in users_db:
        return jsonify({'message': 'User already exists'}), 400

    # Hash the password for secure storage
    hashed_password = generate_password_hash(password, method='sha256')

    # Create a unique user ID
    user_id = str(uuid.uuid4())

    # Add the user to the database
    users_db[username] = {
        'id': user_id,
        'username': username,
        'password': hashed_password
    }

    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint for user login.
    """
    data = request.get_json()

    # Validate input data
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Invalid input'}), 400

    username = data['username']
    password = data['password']

    # Find the user in the database
    user = users_db.get(username)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    # Verify the password
    if not check_password_hash(user['password'], password):
        return jsonify({'message': 'Incorrect password'}), 401

    # Generate a JWT token for the user
    token = jwt.encode({
        'user_id': user['id'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, app.config['SECRET_KEY'], algorithm="HS256")

    return jsonify({'message': 'Login successful', 'token': token}), 200

@app.route('/protected', methods=['GET'])
@token_required
def protected_route(current_user):
    """
    Example of a protected route that requires authentication.
    """
    return jsonify({'message': f'Welcome {current_user["username"]}, you accessed a protected route!'}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
