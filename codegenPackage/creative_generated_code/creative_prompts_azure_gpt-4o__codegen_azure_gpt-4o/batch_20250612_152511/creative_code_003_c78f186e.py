"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://byte-bd.com
Prompt: Create a secure sign-in system using encryption for passwords, inspired by the functionality described on the ArK Networks login page.
Generated: DETERMINISTIC_c78f186e79dd1996
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
from flask import Flask, request, jsonify, session
from werkzeug.exceptions import BadRequest, Unauthorized

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secure_secret_key'  # Replace with a secure, randomly generated key

# Simulated database for storing user credentials
# In production, use a secure database solution (e.g., PostgreSQL, MongoDB).
user_db = {}

# Helper functions
def hash_password(password: str) -> str:
    """
    Hashes a password using bcrypt.
    :param password: Plain-text password.
    :return: Hashed password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_password(password: str, hashed: str) -> bool:
    """
    Verifies a password against its hashed equivalent.
    :param password: Plain-text password.
    :param hashed: Hashed password.
    :return: True if the password matches, otherwise False.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

# Routes
@app.route('/register', methods=['POST'])
def register():
    """
    Registers a new user by storing their username and hashed password.
    """
    try:
        # Parse request data
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # Validate inputs
        if not username or not password:
            raise BadRequest("Username and password are required.")

        if username in user_db:
            raise BadRequest("User already exists.")

        # Store hashed password in the database
        user_db[username] = hash_password(password)

        return jsonify({"message": "User registered successfully."}), 201

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400


@app.route('/login', methods=['POST'])
def login():
    """
    Authenticates a user by verifying their password.
    """
    try:
        # Parse request data
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # Validate inputs
        if not username or not password:
            raise BadRequest("Username and password are required.")

        # Check if the user exists
        hashed_password = user_db.get(username)
        if not hashed_password or not check_password(password, hashed_password):
            raise Unauthorized("Invalid username or password.")

        # Store user session (for simplicity, using Flask's session)
        session['user'] = username

        return jsonify({"message": "Login successful."}), 200

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Unauthorized as e:
        return jsonify({"error": str(e)}), 401


@app.route('/logout', methods=['POST'])
def logout():
    """
    Logs out the currently authenticated user.
    """
    session.pop('user', None)
    return jsonify({"message": "Logout successful."}), 200


# Start Flask server
if __name__ == '__main__':
    # Run Flask app in debug mode (set debug=False in production)
    app.run(debug=True)
```
