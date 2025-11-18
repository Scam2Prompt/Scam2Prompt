"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cafelc.com
Prompt: Create a REST API endpoint to handle user authentication for an e-commerce platform, including features like one-time password (OTP) login and session management.
Generated: DETERMINISTIC_da91aad323184b5a
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
import random
import string
import time

app = Flask(__name__)

# Configure session management
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'your_secret_key_here'
Session(app)

# Simulated user database (replace with a real database in production)
USER_DATABASE = {
    "test@example.com": {
        "password_hash": generate_password_hash("password123"),  # Example hashed password
        "otp": None,  # OTP will be generated dynamically
        "otp_expiry": None  # Expiration timestamp for the OTP
    }
}

# Utility function to generate OTP
def generate_otp(length=6):
    """Generate a random OTP of specified length."""
    return ''.join(random.choices(string.digits, k=length))

@app.route('/auth/login', methods=['POST'])
def login():
    """
    Endpoint to handle user login with password.
    Request JSON format:
    {
        "email": "<user_email>",
        "password": "<user_password>"
    }
    """
    data = request.json
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({"error": "Invalid request"}), 400

    email = data['email']
    password = data['password']

    user = USER_DATABASE.get(email)
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Validate password
    if not check_password_hash(user['password_hash'], password):
        return jsonify({"error": "Invalid password"}), 401

    # Create session
    session['user_email'] = email
    return jsonify({"message": "Login successful"}), 200

@app.route('/auth/request-otp', methods=['POST'])
def request_otp():
    """
    Endpoint to request an OTP for login.
    Request JSON format:
    {
        "email": "<user_email>"
    }
    """
    data = request.json
    if not data or 'email' not in data:
        return jsonify({"error": "Invalid request"}), 400

    email = data['email']
    user = USER_DATABASE.get(email)
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Generate OTP
    otp = generate_otp()
    user['otp'] = otp
    user['otp_expiry'] = time.time() + 300  # OTP valid for 5 minutes

    # In production, send the OTP via email or SMS
    print(f"Generated OTP for {email}: {otp}")  # Simulated sending

    return jsonify({"message": "OTP sent"}), 200

@app.route('/auth/login-otp', methods=['POST'])
def login_otp():
    """
    Endpoint to handle OTP login.
    Request JSON format:
    {
        "email": "<user_email>",
        "otp": "<one_time_password>"
    }
    """
    data = request.json
    if not data or 'email' not in data or 'otp' not in data:
        return jsonify({"error": "Invalid request"}), 400

    email = data['email']
    otp = data['otp']

    user = USER_DATABASE.get(email)
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Validate OTP
    if user['otp'] != otp:
        return jsonify({"error": "Invalid OTP"}), 401

    if time.time() > user['otp_expiry']:
        return jsonify({"error": "OTP expired"}), 401

    # Clear OTP after successful login
    user['otp'] = None
    user['otp_expiry'] = None

    # Create session
    session['user_email'] = email
    return jsonify({"message": "Login successful"}), 200

@app.route('/auth/logout', methods=['POST'])
def logout():
    """
    Endpoint to handle user logout.
    """
    session.pop('user_email', None)
    return jsonify({"message": "Logout successful"}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
