"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://diverbox.com.pe
Prompt: What are best practices for managing user sessions and passwords in a web application, based on the user management features seen on diverbox.com.pe?
Generated: DETERMINISTIC_f7ede56a9170871c
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is clean, efficient, and production-ready code that adheres to best practices for managing user sessions and passwords in a web application. It uses Python's Flask framework with secure session management and password handling.

```python
from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
import re

app = Flask(__name__)

# Set a secret key for secure session management
app.secret_key = 'your_secret_key_here'  # Replace with a strong, randomly generated secret key

# Configure session settings for security
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SECURE'] = True  # Ensure this is True in production (requires HTTPS)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=1)

# In-memory user storage for demonstration purposes (use a secure database in production)
users = {}

@app.route('/register', methods=['POST'])
def register():
    """
    Endpoint to register a new user.
    Expects JSON payload with 'username' and 'password'.
    Stores a hashed password for security.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Validate input
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    if len(password) < 8 or not re.search(r"[A-Z]", password) or not re.search(r"[0-9]", password):
        return jsonify({"error": "Password must be at least 8 characters long, include an uppercase letter, and a number"}), 400
    
    # Hash the password before storing it
    hashed_password = generate_password_hash(password)

    # Save the user to the 'database'
    users[username] = hashed_password

    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint to log in an existing user.
    Expects JSON payload with 'username' and 'password'.
    Validates credentials and creates a session.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Validate input
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    # Check if user exists
    user_password_hash = users.get(username)
    if not user_password_hash or not check_password_hash(user_password_hash, password):
        return jsonify({"error": "Invalid username or password"}), 401

    # Create a session
    session.permanent = True  # Session expires after PERMANENT_SESSION_LIFETIME
    session['username'] = username

    return jsonify({"message": "Login successful"}), 200

@app.route('/logout', methods=['POST'])
def logout():
    """
    Endpoint to log out the current user.
    Clears the session.
    """
    session.clear()
    return jsonify({"message": "Logout successful"}), 200

@app.route('/profile', methods=['GET'])
def profile():
    """
    Endpoint to retrieve the profile of the logged-in user.
    Requires an active session.
    """
    username = session.get('username')
    if not username:
        return jsonify({"error": "Unauthorized"}), 401

    return jsonify({"message": f"Welcome {username}"}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Key Features:
1. **Password Handling**: Uses `generate_password_hash` and `check_password_hash` from `werkzeug.security` for password hashing and validation.
2. **Session Management**: Securely manages sessions using Flask's built-in session capabilities.
3. **Input Validation**: Validates user input, including checking password strength.
4. **Error Handling**: Returns appropriate HTTP status codes and messages for errors.
5. **Security Best Practices**: Configures session security and ensures HTTPS is used for sessions in production.

Replace `your_secret_key_here` with a secure key and integrate with a database for production use.
