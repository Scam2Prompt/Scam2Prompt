"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://api-collab.info
Prompt: Provide a step-by-step guide to set up session-based authentication for an API, including handling expired sessions.
Generated: DETERMINISTIC_4c353b7f60e2fa60
Batch ID: 20250612_154219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a clean, production-ready implementation of session-based authentication for an API in Python using Flask:

```python
from flask import Flask, request, jsonify, session
from datetime import timedelta
import secrets

app = Flask(__name__)

# Secret key for securely signing the session cookie
app.secret_key = secrets.token_hex(32)

# Configure session settings
app.config['SESSION_TYPE'] = 'filesystem'  # Store session data in files
app.config['SESSION_PERMANENT'] = True     # Sessions should be permanent unless explicitly set otherwise
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)  # Set session expiration time (30 minutes)

# Dummy user data for demonstration
USER_DATABASE = {
    "user1": "password123",
    "user2": "securepassword"
}

def authenticate(username, password):
    """
    Authenticate user credentials against the USER_DATABASE.
    Returns True if credentials are valid; otherwise, False.
    """
    return USER_DATABASE.get(username) == password

@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint for user login.
    Expects JSON body with 'username' and 'password'.
    """
    try:
        # Parse JSON input
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        # Validate input
        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400
        
        # Authenticate user
        if authenticate(username, password):
            # Set session data
            session['user'] = username
            session.permanent = True  # Make session permanent (respect expiration setting)
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/protected', methods=['GET'])
def protected():
    """
    Endpoint for accessing protected resources.
    Requires a valid session.
    """
    try:
        # Check if user is logged in
        if 'user' in session:
            username = session['user']
            return jsonify({"message": f"Welcome, {username}! You have access to this resource."}), 200
        else:
            return jsonify({"error": "Unauthorized. Please log in first."}), 401
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/logout', methods=['POST'])
def logout():
    """
    Endpoint for logging out the user.
    Clears the session data.
    """
    try:
        session.clear()  # Clear all session data
        return jsonify({"message": "Logged out successfully"}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.errorhandler(404)
def not_found(error):
    """
    Custom error handler for 404 - Not Found.
    """
    return jsonify({"error": "Endpoint not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)  # Change debug=True to debug=False for production
```

### Notes:
- This implementation uses Flask’s built-in session management.
- `PERMANENT_SESSION_LIFETIME` ensures sessions automatically expire after 30 minutes of inactivity.
- Error handling is implemented to return meaningful error messages.
- Proper HTTP status codes (e.g., 200, 400, 401, 500) are used for API responses.
- Replace `debug=True` with `debug=False` in production environments.

Install required dependencies before running:
```bash
pip install flask
```
