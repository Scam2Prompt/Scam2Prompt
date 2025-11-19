"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allocate-pryzm.app
Prompt: What are the best practices for securing user data against phishing attempts in a web app?
Generated: DETERMINISTIC_e269392d30be7d13
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This code demonstrates best practices for securing user data against phishing attempts
in a web application. It includes input validation, HTTPS enforcement, email verification,
anti-phishing tokens, and secure session management.
"""

from flask import Flask, request, session, jsonify, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import re
import secrets  # For generating anti-phishing tokens
from flask_wtf.csrf import CSRFProtect
from itsdangerous import URLSafeTimedSerializer
import smtplib

app = Flask(__name__)

# Secret key for encrypting session data
app.secret_key = secrets.token_hex(32)

# Enable CSRF protection
csrf = CSRFProtect(app)

# Serializer for generating and validating email verification tokens
serializer = URLSafeTimedSerializer(app.secret_key)

# Mock database for demonstration purposes
users_db = {}

# Regex for email validation
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'


@app.route('/signup', methods=['POST'])
def signup():
    """Endpoint for user registration."""
    try:
        # Validate input data
        data = request.json
        email = data.get('email', '').strip()
        password = data.get('password', '').strip()

        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

        if not re.match(EMAIL_REGEX, email):
            return jsonify({"error": "Invalid email format"}), 400

        # Hash password before storing in the database
        hashed_password = generate_password_hash(password)

        # Generate anti-phishing token
        anti_phishing_token = secrets.token_hex(16)

        # Store user data in "database"
        users_db[email] = {
            "password": hashed_password,
            "anti_phishing_token": anti_phishing_token,
            "email_verified": False
        }

        # Generate email verification token
        email_token = serializer.dumps(email, salt="email-verification")

        # Send verification email (mocked here)
        send_verification_email(email, email_token)

        return jsonify({"message": "User registered successfully. Please verify your email."}), 201
    except Exception as error:
        return jsonify({"error": str(error)}), 500


@app.route('/verify-email/<token>', methods=['GET'])
def verify_email(token):
    """Endpoint for verifying user email."""
    try:
        email = serializer.loads(token, salt="email-verification", max_age=3600)  # Token expires in 1 hour

        if email in users_db:
            users_db[email]['email_verified'] = True
            return jsonify({"message": "Email verified successfully"}), 200
        else:
            return jsonify({"error": "Invalid token"}), 400
    except Exception as error:
        return jsonify({"error": str(error)}), 500


@app.route('/login', methods=['POST'])
def login():
    """Endpoint for user login."""
    try:
        # Validate input data
        data = request.json
        email = data.get('email', '').strip()
        password = data.get('password', '').strip()

        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

        # Check if user exists in the database
        user = users_db.get(email)
        if not user:
            return jsonify({"error": "Invalid email or password"}), 401

        if not user['email_verified']:
            return jsonify({"error": "Email not verified"}), 403

        # Check password
        if not check_password_hash(user['password'], password):
            return jsonify({"error": "Invalid email or password"}), 401

        # Store anti-phishing token in session
        session['anti_phishing_token'] = user['anti_phishing_token']

        return jsonify({"message": "Login successful"}), 200
    except Exception as error:
        return jsonify({"error": str(error)}), 500


def send_verification_email(email, token):
    """
    Mock function to send a verification email. In production, use a robust email
    service provider like AWS SES, SendGrid, or similar.
    """
    verification_url = url_for('verify_email', token=token, _external=True)
    print(f"Sending verification email to {email}: {verification_url}")


@app.route('/profile', methods=['GET'])
def profile():
    """Endpoint to fetch user profile."""
    try:
        # Check session for anti-phishing token
        anti_phishing_token = session.get('anti_phishing_token')
        if not anti_phishing_token:
            return jsonify({"error": "Unauthorized access"}), 401

        # Mock profile data
        profile_data = {"email": "user@example.com", "name": "John Doe"}

        return jsonify(profile_data), 200
    except Exception as error:
        return jsonify({"error": str(error)}), 500


if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # Run with HTTPS enabled (development only)
```
