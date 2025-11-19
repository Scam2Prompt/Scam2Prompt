"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ehajj.ph
Prompt: What libraries can I use to enhance user login security for a site like ehajj.ph?
Generated: DETERMINISTIC_362e31ebfa8ad99f
Batch ID: 20250612_162519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Enhancing user login security for a web-based application like ehajj.ph using Python Flask and recommended libraries.
This code demonstrates the use of libraries for password hashing, session management, and rate limiting.
"""

from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_limiter import Limiter
from flask_session import Session
import os

app = Flask(__name__)

# Configuration for session management
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)  # Strong secret key for session signing
Session(app)

# Rate limiting to prevent brute-force attacks
limiter = Limiter(
    get_identifier=lambda: request.remote_addr,
    app=app,
    default_limits=["5 per minute"],  # Limit login attempts to prevent brute force
)

# In-memory "database" for demonstration purposes
# Replace this with a proper database in production (e.g., PostgreSQL, MySQL)
users_db = {
    "test_user": generate_password_hash("secure_password123")
}

@app.route('/login', methods=['POST'])
@limiter.limit("5/minute")  # Apply rate limiting to the login route
def login():
    """
    Handle user login requests.
    """
    try:
        data = request.json
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        # Retrieve stored hashed password for the username
        stored_password_hash = users_db.get(username)

        if not stored_password_hash or not check_password_hash(stored_password_hash, password):
            return jsonify({"error": "Invalid username or password"}), 401

        # Successful login
        session['user'] = username  # Store user's session
        return jsonify({"message": f"Welcome {username}!"}), 200

    except Exception as e:
        # Catch unexpected errors and return a safe response
        return jsonify({"error": "An unexpected error occurred"}), 500


@app.route('/logout', methods=['POST'])
def logout():
    """
    Handle user logout requests.
    """
    session.pop('user', None)  # Remove user from session
    return jsonify({"message": "Logged out successfully"}), 200


@app.route('/register', methods=['POST'])
def register():
    """
    Handle user registration requests.
    """
    try:
        data = request.json
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        if username in users_db:
            return jsonify({"error": "Username already exists"}), 409

        # Store hashed password in the "database"
        users_db[username] = generate_password_hash(password)
        return jsonify({"message": "Registration successful"}), 201

    except Exception as e:
        # Catch unexpected errors and return a safe response
        return jsonify({"error": "An unexpected error occurred"}), 500


if __name__ == '__main__':
    # Run the Flask development server
    # Use a production-ready server like Gunicorn in actual deployment
    app.run(debug=True)
```

This code uses Flask, Werkzeug for password hashing, Flask-Limiter for rate limiting, and Flask-Session for session management, all of which are commonly recommended libraries to enhance user login security. Replace the in-memory `users_db` with a secure database in production.
