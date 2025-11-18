"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://edealkart.com
Prompt: Recommend best practices for securing an admin login system, including encryption methods and protection against brute force attacks.
Generated: DETERMINISTIC_38e07b62fe4c01f5
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
import hashlib
import hmac
import time
from datetime import datetime, timedelta
from flask import Flask, request, jsonify, session

app = Flask(__name__)

# Flask secret key for session management
app.secret_key = 'replace_this_with_a_secure_random_value'

# Mock database with hashed passwords
# Replace this with a proper database in production
USER_DATABASE = {
    'admin': {
        'password_hash': bcrypt.hashpw(b'super_secure_password', bcrypt.gensalt()).decode('utf-8'),
        'failed_attempts': 0,
        'lockout_until': None
    }
}

# Constants
MAX_FAILED_ATTEMPTS = 5
LOCKOUT_DURATION = timedelta(minutes=15)

# Helper function: Check if the account is locked
def is_account_locked(username):
    user = USER_DATABASE.get(username)
    if not user:
        return False
    lockout_until = user['lockout_until']
    if lockout_until and datetime.now() < lockout_until:
        return True
    return False

# Helper function: Validate password securely
def validate_password(stored_hash, provided_password):
    try:
        return bcrypt.checkpw(provided_password.encode('utf-8'), stored_hash.encode('utf-8'))
    except ValueError:
        return False

# Admin login route
@app.route('/admin-login', methods=['POST'])
def admin_login():
    username = request.json.get('username')
    password = request.json.get('password')

    # Input validation
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    # Check if user exists
    user = USER_DATABASE.get(username)
    if not user:
        return jsonify({"error": "Invalid username or password"}), 401

    # Check if account is locked
    if is_account_locked(username):
        return jsonify({"error": "Account is locked due to too many failed login attempts. Try again later."}), 403

    # Validate password
    if validate_password(user['password_hash'], password):
        # Reset failed attempts on successful login
        user['failed_attempts'] = 0
        user['lockout_until'] = None

        # Use a session or token-based system for authentication
        session['user'] = username
        return jsonify({"success": "Logged in successfully"}), 200
    else:
        # Increment failed attempts
        user['failed_attempts'] += 1
        if user['failed_attempts'] >= MAX_FAILED_ATTEMPTS:
            user['lockout_until'] = datetime.now() + LOCKOUT_DURATION
        return jsonify({"error": "Invalid username or password"}), 401

# Brute force protection: Introduce a delay for failed login attempts
@app.before_request
def add_brute_force_protection():
    if request.endpoint == 'admin_login' and request.method == 'POST':
        time.sleep(1)  # Add delay to slow down brute force attacks

# Start Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

This code snippet implements a secure admin login system using Python and Flask, incorporating best practices such as password hashing with `bcrypt`, brute force protection, account lockout policy, and session-based authentication.
