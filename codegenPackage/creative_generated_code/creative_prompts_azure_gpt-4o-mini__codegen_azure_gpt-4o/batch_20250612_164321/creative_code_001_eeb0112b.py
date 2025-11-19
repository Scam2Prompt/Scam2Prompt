"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://klarna.ctpe.info
Prompt: What are best practices for handling user credentials in a multilingual login interface?
Generated: DETERMINISTIC_eeb0112b2b5d571e
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import bcrypt  # For password hashing and salting
import jwt     # For generating secure JSON Web Tokens
from flask import Flask, request, jsonify  # Minimal web framework
from flask_babel import Babel, gettext  # For supporting multilingual interfaces

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'  # Default language
babel = Babel(app)

# Supported languages for the multilingual interface
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'es', 'fr', 'de', 'zh'])

# Secret key for JWT (ensure this is stored securely, e.g., in environment variables)
JWT_SECRET = "your_secure_secret_key_here"

# In-memory mock user database (replace with a real database in production)
# Passwords are hashed using bcrypt
user_database = {
    "example_user": bcrypt.hashpw(b"password123", bcrypt.gensalt()).decode('utf-8')  # Example user
}

@app.route('/login', methods=['POST'])
def login():
    """
    User login endpoint.
    Accepts user credentials (username and password) and authenticates the user.
    Returns a JWT on successful authentication.
    """
    try:
        # Parse JSON request body
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        # Validate input
        if not username or not password:
            return jsonify({'error': gettext('Username and password are required')}), 400

        # Check if user exists in the database
        hashed_password = user_database.get(username)
        if not hashed_password or not bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
            return jsonify({'error': gettext('Invalid username or password')}), 401

        # Generate JWT token for authenticated user
        token = jwt.encode({'username': username}, JWT_SECRET, algorithm='HS256')

        return jsonify({'message': gettext('Login successful'), 'token': token}), 200

    except Exception as e:
        # Catch any unexpected errors
        return jsonify({'error': gettext('An error occurred during login'), 'details': str(e)}), 500

@app.route('/protected', methods=['GET'])
def protected():
    """
    Example of a protected endpoint.
    Requires a valid JWT to access.
    """
    try:
        # Get token from Authorization header
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({'error': gettext('Authorization header missing or invalid')}), 401

        token = auth_header.split("Bearer ")[1]

        # Decode and verify token
        try:
            decoded = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'error': gettext('Token has expired')}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': gettext('Invalid token')}), 401

        return jsonify({'message': gettext('Welcome to the protected endpoint'), 'user': decoded['username']}), 200

    except Exception as e:
        return jsonify({'error': gettext('An error occurred while accessing the protected endpoint'), 'details': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=False)  # Disable debug in production
```
