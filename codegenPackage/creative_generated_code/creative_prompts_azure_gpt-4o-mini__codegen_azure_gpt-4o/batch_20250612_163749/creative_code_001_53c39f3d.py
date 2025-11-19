"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gemi-nilogn.godaddysites.com
Prompt: Write a code snippet that demonstrates cookie management for user sessions, inspired by the Gemini login site.
Generated: DETERMINISTIC_53c39f3d3b6255bc
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, make_response, jsonify
import uuid
import time

app = Flask(__name__)

# Fake in-memory session store for demonstration purposes.
# In production, consider using a proper database or external session management tool.
session_store = {}

# Constants for cookie management
COOKIE_NAME = "gemini_session"
COOKIE_TIMEOUT = 3600  # 1 hour in seconds

def create_session():
    """Create a new session entry in the session store."""
    session_id = str(uuid.uuid4())
    session_store[session_id] = {
        "created_at": time.time(),
        "user_data": {}  # Add user-related info here as needed.
    }
    return session_id

def validate_session(session_id):
    """Validate the session and check expiration."""
    session = session_store.get(session_id)
    if session:
        elapsed_time = time.time() - session["created_at"]
        if elapsed_time < COOKIE_TIMEOUT:
            return True
    return False

@app.route('/login', methods=['POST'])
def login():
    """
    Handle the login process.
    This is a mock implementation; replace it with actual login verification logic.
    """
    # Simulated login validation
    username = request.form.get('username')
    password = request.form.get('password')

    if username == "test_user" and password == "password123":
        # Create session if login is successful
        session_id = create_session()

        # Set cookie with the session ID
        response = make_response(jsonify({"message": "Login successful"}))
        response.set_cookie(
            COOKIE_NAME, 
            session_id, 
            max_age=COOKIE_TIMEOUT, 
            httponly=True, 
            secure=True  # Use `secure=True` in production to enforce HTTPS
        )
        return response
    else:
        # Invalid credentials
        return jsonify({"message": "Invalid username or password"}), 401

@app.route('/dashboard', methods=['GET'])
def dashboard():
    """
    Handle requests to a protected dashboard endpoint.
    """
    session_id = request.cookies.get(COOKIE_NAME)

    if session_id and validate_session(session_id):
        return jsonify({"message": "Welcome to your dashboard!"})
    else:
        # Invalid or expired session
        return jsonify({"message": "Session expired or invalid"}), 403

@app.route('/logout', methods=['POST'])
def logout():
    """
    Handle the logout process.
    """
    session_id = request.cookies.get(COOKIE_NAME)

    if session_id and session_id in session_store:
        # Remove session from store
        session_store.pop(session_id)

    # Remove the cookie
    response = make_response(jsonify({"message": "Logged out successfully"}))
    response.delete_cookie(COOKIE_NAME)
    return response

if __name__ == "__main__":
    # Start the Flask development server
    app.run(debug=True)
```
