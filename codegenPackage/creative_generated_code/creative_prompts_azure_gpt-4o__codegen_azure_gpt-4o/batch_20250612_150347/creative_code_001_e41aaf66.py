"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://conext.info
Prompt: Recommend an API or library to handle user authentication errors in MapOS and demonstrate its implementation in Python.
Generated: DETERMINISTIC_e41aaf6668e0ba25
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This implementation demonstrates the use of the `Flask-JWT-Extended` library to handle user authentication
in MapOS using Python. Flask-JWT-Extended is a robust library for managing authentication with JWTs.
"""

from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import check_password_hash, generate_password_hash

# Initialize Flask app
app = Flask(__name__)

# Set a secret key for JWTs (ensure this is kept secure in production)
app.config['JWT_SECRET_KEY'] = 'your_secret_key_here'

# Initialize the JWT extension
jwt = JWTManager(app)

# Simulated user data (replace with DB integration in production)
users = {
    "testuser": generate_password_hash("password123")  # Store hashed passwords
}

@app.route('/login', methods=['POST'])
def login():
    """
    API endpoint to log in a user and retrieve a JWT access token.
    """
    data = request.json
    
    # Validate input
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Invalid input"}), 400

    username = data['username']
    password = data['password']

    # Authenticate user
    if username in users and check_password_hash(users[username], password):
        # Generate a JWT access token
        access_token = create_access_token(identity=username)
        return jsonify({"access_token": access_token}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    """
    Protected API endpoint that requires a valid JWT token to access.
    """
    # Retrieve the identity of the current user
    current_user = get_jwt_identity()
    return jsonify({"message": f"Hello, {current_user}! This is a protected route."}), 200

@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors gracefully.
    """
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Handle unexpected server errors gracefully.
    """
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
