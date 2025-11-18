"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://empower.gr
Prompt: Write code to handle invalid login attempts and display appropriate error messages, similar to the functionality implied on the Empower login page.
Generated: DETERMINISTIC_634f4f79761a2c81
Batch ID: 20250612_150645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Mock database for user credentials (In production, use a secure database)
mock_users = {
    "user1": "password123",
    "user2": "securepassword"
}

# Configuration for maximum login attempts and lockout duration
MAX_LOGIN_ATTEMPTS = 3
LOCKOUT_DURATION_SECONDS = 300  # 5 minutes

# Data store to track login attempts and lockout status
login_attempts = {}
lockout_status = {}

@app.route('/login', methods=['POST'])
def login():
    """
    Handle login requests, validate credentials, and manage invalid login attempts.
    """
    try:
        # Parse JSON request data
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        # Validate request data
        if not username or not password:
            return jsonify({"error": "Username and password are required."}), 400

        # Check if the user is in lockout status
        if username in lockout_status:
            remaining_lockout = max(0, LOCKOUT_DURATION_SECONDS - (time.monotonic() - lockout_status[username]))
            if remaining_lockout > 0:
                return jsonify({"error": f"Account locked due to multiple invalid attempts. Try again in {int(remaining_lockout)} seconds."}), 403
            else:
                # Reset lockout status if the lockout duration has passed
                lockout_status.pop(username, None)
                login_attempts[username] = 0

        # Validate credentials
        if username in mock_users and mock_users[username] == password:
            # Reset login attempts on successful login
            login_attempts[username] = 0
            return jsonify({"message": "Login successful!"}), 200
        else:
            # Increment login attempts
            login_attempts[username] = login_attempts.get(username, 0) + 1

            # Check if login attempts exceed the maximum allowed
            if login_attempts[username] >= MAX_LOGIN_ATTEMPTS:
                lockout_status[username] = time.monotonic()
                return jsonify({"error": "Account locked due to multiple invalid attempts. Try again later."}), 403

            return jsonify({"error": "Invalid username or password."}), 401

    except Exception as e:
        # Handle unexpected server errors gracefully
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
