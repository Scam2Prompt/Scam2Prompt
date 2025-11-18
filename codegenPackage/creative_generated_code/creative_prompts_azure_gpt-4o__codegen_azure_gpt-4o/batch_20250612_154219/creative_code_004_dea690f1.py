"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://api-collab.info
Prompt: Suggest best practices for implementing session-based authentication in APIs, including handling session expiration.
Generated: DETERMINISTIC_dea690f1c30f28ab
Batch ID: 20250612_154219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Code for implementing session-based authentication in APIs with session expiration.

from flask import Flask, request, jsonify, make_response
from datetime import datetime, timedelta
import uuid

app = Flask(__name__)

# Configuration for session timeout (e.g., 30 minutes)
SESSION_TIMEOUT_MINUTES = 30

# In-memory store for sessions (use a persistent store like Redis in production)
sessions = {}

# Helper function to create a new session
def create_session(user_id):
    session_id = str(uuid.uuid4())  # Generate a unique session ID
    expiration_time = datetime.utcnow() + timedelta(minutes=SESSION_TIMEOUT_MINUTES)
    sessions[session_id] = {
        "user_id": user_id,
        "expires_at": expiration_time
    }
    return session_id, expiration_time

# Helper function to validate a session
def validate_session(session_id):
    session_data = sessions.get(session_id)
    if not session_data:
        return False, "Invalid session."
    
    # Check if the session has expired
    if datetime.utcnow() > session_data["expires_at"]:
        del sessions[session_id]  # Remove expired session
        return False, "Session expired."
    
    return True, session_data

# Example login route
@app.route("/login", methods=["POST"])
def login():
    # Mock user authentication (replace with actual authentication logic)
    body = request.json
    username = body.get("username")
    password = body.get("password")
    
    if username == "admin" and password == "password123":  # Example credentials
        user_id = 1  # Mock user ID
        session_id, expires_at = create_session(user_id)
        response = make_response(jsonify({
            "message": "Login successful.",
            "session_id": session_id,
            "expires_at": expires_at.strftime("%Y-%m-%d %H:%M:%S")
        }))
        response.status_code = 200
        return response
    else:
        response = make_response(jsonify({"message": "Invalid credentials."}))
        response.status_code = 401
        return response

# Example protected route
@app.route("/protected", methods=["GET"])
def protected_route():
    session_id = request.headers.get("Session-ID")
    
    if not session_id:
        response = make_response(jsonify({"message": "Session-ID header is required."}))
        response.status_code = 400
        return response
    
    valid, session_or_error = validate_session(session_id)
    if not valid:
        response = make_response(jsonify({"message": session_or_error}))
        response.status_code = 401
        return response
    
    # If the session is valid, allow access to the protected resource
    user_id = session_or_error["user_id"]
    return jsonify({
        "message": "Welcome to the protected resource.",
        "user_id": user_id
    })

# Example logout route
@app.route("/logout", methods=["POST"])
def logout():
    session_id = request.headers.get("Session-ID")
    
    if not session_id:
        response = make_response(jsonify({"message": "Session-ID header is required."}))
        response.status_code = 400
        return response
    
    if session_id in sessions:
        del sessions[session_id]
        response = make_response(jsonify({"message": "Logout successful."}))
        response.status_code = 200
        return response
    else:
        response = make_response(jsonify({"message": "Invalid session."}))
        response.status_code = 401
        return response

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
```
