"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldlibertyfiduciary.com
Prompt: Develop a secure login interface for a Telegram bot management system, incorporating features like session expiration after 24 hours.
Generated: DETERMINISTIC_ecef2bf5283eaf9e
Batch ID: 20250612_150135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import hashlib
import hmac
import secrets
from flask import Flask, request, jsonify, session

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)  # Secret key for session management

# Configuration for session expiration (24 hours in seconds)
SESSION_EXPIRATION_TIME = 24 * 60 * 60 

# Simulated database for storing user credentials (hashed passwords)
USER_DATABASE = {
    "admin": hashlib.sha256("securepassword123".encode()).hexdigest()
}

def generate_session_token():
    """Generate a secure random session token."""
    return secrets.token_hex(64)

def validate_password(username, password):
    """Validate user credentials."""
    if username in USER_DATABASE:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hmac.compare_digest(USER_DATABASE[username], hashed_password)
    return False

@app.route('/login', methods=['POST'])
def login():
    """
    Login endpoint.
    Request must include 'username' and 'password'.
    """
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400
    
    # Validate credentials
    if validate_password(username, password):
        # Generate session token and set session variables
        session_token = generate_session_token()
        session['session_token'] = session_token
        session['username'] = username
        session['login_time'] = time.time()  # Track login timestamp
        
        return jsonify({"message": "Login successful", "session_token": session_token}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

@app.route('/validate_session', methods=['GET'])
def validate_session():
    """
    Validate session endpoint.
    Checks if the session is active and has not expired.
    """
    session_token = session.get('session_token')
    login_time = session.get('login_time')
    username = session.get('username')
    
    # Check if session exists
    if not session_token or not login_time or not username:
        return jsonify({"error": "Session not active"}), 403
    
    # Check if session has expired
    current_time = time.time()
    if current_time - login_time > SESSION_EXPIRATION_TIME:
        session.clear()  # Clear expired session
        return jsonify({"error": "Session expired"}), 403
    
    return jsonify({"message": "Session is active", "username": username}), 200

@app.route('/logout', methods=['POST'])
def logout():
    """
    Logout endpoint.
    Clears the session data.
    """
    session.clear()
    return jsonify({"message": "Logged out successfully"}), 200

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```
