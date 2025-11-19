"""
Generated Code Metadata:
========================
Original URL: https://a68.net
Prompt: Design a simple authentication system using a library or framework of your choice (e.g., OAuth, JWT), and write a code snippet to demonstrate the verification process.
Generated: DETERMINISTIC_e105e3d71928d18c
Batch ID: 20250622_212110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

# Initialize the Flask application
app = Flask(__name__)

# Configure the JWT secret key and token expiration
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Change this to a strong secret key
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

# Initialize the JWT manager
jwt = JWTManager(app)

# In-memory user storage (for demonstration purposes)
users_db = {}

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    """Register a new user with a username and password."""
    username = request.json.get('username')
    password = request.json.get('password')

    if username in users_db:
        return jsonify({"msg": "User already exists"}), 400

    # Hash the password and store the user
    users_db[username] = generate_password_hash(password)
    return jsonify({"msg": "User registered successfully"}), 201

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user and return a JWT token."""
    username = request.json.get('username')
    password = request.json.get('password')

    user_password_hash = users_db.get(username)

    if user_password_hash and check_password_hash(user_password_hash, password):
        # Create a new access token
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Bad username or password"}), 401

# Protected route example
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    """A protected route that requires a valid JWT token."""
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

# Error handling for JWT errors
@jwt.unauthorized_loader
def unauthorized_response(callback):
    """Return a custom response for unauthorized access."""
    return jsonify({"msg": "Missing or invalid token"}), 401

@jwt.expired_token_loader
def expired_token_response(callback):
    """Return a custom response for expired tokens."""
    return jsonify({"msg": "Token has expired"}), 401

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
