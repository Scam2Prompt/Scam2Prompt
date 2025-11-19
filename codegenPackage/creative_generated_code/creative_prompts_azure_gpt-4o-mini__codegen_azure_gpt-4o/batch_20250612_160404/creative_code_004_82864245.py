"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tslaspacetrade.com
Prompt: Explain how to implement a secure user authentication system for a cryptocurrency investment platform like Tslaspacetrade, focusing on data security measures mentioned on the site.
Generated: DETERMINISTIC_828642457a54b2d9
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Secure User Authentication System for a Cryptocurrency Investment Platform.

This implementation uses Flask with secure practices for user authentication. It includes:
1. Password hashing with bcrypt.
2. Safe storage of sensitive data using environment variables.
3. JWT (JSON Web Token) for session management.
4. Proper validation and error handling.
"""

from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import os

# Initialize Flask app
app = Flask(__name__)

# Load secret key and JWT configuration from environment variables
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_default_key')  # Replace with a secure key
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Mock database (Replace with a proper database in production)
users_db = {}

# Error messages
USER_EXISTS_ERROR = "User already exists."
USER_NOT_FOUND_ERROR = "User not found."
PASSWORD_MISMATCH_ERROR = "Incorrect password."

@app.route('/register', methods=['POST'])
def register():
    """
    Handles user registration. Stores hashed passwords securely.
    """
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'error': 'Username and password are required.'}), 400

        if username in users_db:
            return jsonify({'error': USER_EXISTS_ERROR}), 400

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        users_db[username] = hashed_password

        return jsonify({'message': 'User registered successfully.'}), 201
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500


@app.route('/login', methods=['POST'])
def login():
    """
    Handles user login. Validates credentials and returns a JWT token.
    """
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'error': 'Username and password are required.'}), 400

        user_password = users_db.get(username)
        if not user_password:
            return jsonify({'error': USER_NOT_FOUND_ERROR}), 404

        # Verify password
        if not bcrypt.check_password_hash(user_password, password):
            return jsonify({'error': PASSWORD_MISMATCH_ERROR}), 401

        # Generate JWT token
        access_token = create_access_token(identity=username)

        return jsonify({'access_token': access_token}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500


@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    """
    Example of a protected route that requires a valid JWT token.
    """
    try:
        current_user = get_jwt_identity()
        return jsonify({'message': f'Welcome {current_user}, this is a protected route!'}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500


if __name__ == '__main__':
    # Ensure the server runs in secure mode
    app.run(host='0.0.0.0', port=5000, debug=False)
```

### Notes:
- Ensure proper HTTPS implementation in production to secure data transmission.
- Replace the mock database with a robust database (e.g., PostgreSQL, MySQL, MongoDB).
- Use environment variables or a secrets manager to store sensitive keys (`JWT_SECRET_KEY`).
- Regularly update dependencies and monitor for vulnerabilities.
