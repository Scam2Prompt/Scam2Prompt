"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sonicgame.pages.dev
Prompt: Generate a script to integrate secure user authentication for in-game asset trading in a blockchain-based game built on Sonic.
Generated: DETERMINISTIC_7b9fc9d311c9ff68
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import jwt
from flask import Flask, request, jsonify
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configuration for JWT
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key')
app.config['JWT_EXPIRATION_DELTA'] = 3600  # Token expiration time in seconds

# In-memory user storage for demonstration (use a database in production)
users_db = {}

def token_required(f):
    """
    Decorator to verify if the user has a valid token.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 401
        return f(*args, **kwargs)
    return decorated

@app.route('/register', methods=['POST'])
def register():
    """
    Register a new user with a username and password.
    Store hashed password in the database.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users_db:
        return jsonify({'message': 'User already exists!'}), 400
    
    # Hash the password for secure storage
    hashed_password = generate_password_hash(password, method='sha256')
    users_db[username] = hashed_password

    return jsonify({'message': 'User registered successfully!'}), 201

@app.route('/login', methods=['POST'])
def login():
    """
    Authenticate user and generate a JWT token if the credentials are valid.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user_password_hash = users_db.get(username)
    if user_password_hash and check_password_hash(user_password_hash, password):
        # Create JWT token
        token = jwt.encode({'user': username, 'exp': jwt.datetime.utcnow() + jwt.timedelta(seconds=app.config['JWT_EXPIRATION_DELTA'])}, app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({'token': token}), 200

    return jsonify({'message': 'Invalid credentials!'}), 401

@app.route('/trade', methods=['POST'])
@token_required
def trade_asset():
    """
    Endpoint to trade in-game assets. Requires a valid JWT token.
    Only authenticated users can access this endpoint.
    """
    data = request.get_json()
    asset_id = data.get('asset_id')
    recipient_username = data.get('recipient')

    # Here you would implement the logic to handle the asset trade,
    # such as checking the asset ownership, updating the database, etc.
    
    return jsonify({'message': f'Trade for asset {asset_id} to {recipient_username} successful!'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

Make sure to set the environment variable `SECRET_KEY` before running the application. Additionally, in a production environment, replace the in-memory `users_db` with a proper database implementation for user data persistence and security.
