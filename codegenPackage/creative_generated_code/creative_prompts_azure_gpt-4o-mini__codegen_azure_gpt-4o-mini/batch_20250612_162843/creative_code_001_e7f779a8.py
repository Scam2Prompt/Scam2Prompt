"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suiio.vercel.app
Prompt: What are the key features of Sui's zkLogin authentication for web credentials, and how can I implement it in my application?
Generated: DETERMINISTIC_e7f779a82cb93553
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import jwt
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import os
import uuid

# Initialize the Flask application
app = Flask(__name__)

# Secret key for JWT encoding/decoding
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'your_super_secret_key')

# In-memory storage for user credentials (for demonstration purposes)
users_db = {}

def create_jwt(user_id):
    """Create a JWT token for the given user_id."""
    token = jwt.encode({'user_id': user_id}, app.config['JWT_SECRET_KEY'], algorithm='HS256')
    return token

def authenticate_user(username, password):
    """Authenticate user with username and password."""
    user = users_db.get(username)
    if user and check_password_hash(user['password'], password):
        return user['id']
    return None

def register_user(username, password):
    """Register a new user with a username and password."""
    if username in users_db:
        raise ValueError("User already exists.")
    users_db[username] = {'id': str(uuid.uuid4()), 'password': generate_password_hash(password)}

@app.route('/register', methods=['POST'])
def register():
    """API endpoint for user registration."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    try:
        register_user(username, password)
        return jsonify({"message": "User registered successfully!"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/login', methods=['POST'])
def login():
    """API endpoint for user login."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user_id = authenticate_user(username, password)
    if user_id:
        token = create_jwt(user_id)
        return jsonify({"token": token}), 200
    return jsonify({"error": "Invalid credentials."}), 401

@app.route('/protected', methods=['GET'])
def protected():
    """Protected endpoint that requires JWT authentication."""
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"error": "Token is missing!"}), 401

    try:
        payload = jwt.decode(token.split(" ")[1], app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
        user_id = payload['user_id']
        return jsonify({"message": f"Welcome user {user_id}!"}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token has expired!"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token!"}), 401

if __name__ == '__main__':
    app.run(debug=True)
```
