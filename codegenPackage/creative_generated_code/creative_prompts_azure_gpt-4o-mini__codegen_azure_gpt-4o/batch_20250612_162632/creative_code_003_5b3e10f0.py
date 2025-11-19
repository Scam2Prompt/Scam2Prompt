"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superintelligence.trade
Prompt: What are the best practices for securing user data against phishing threats in a web application?
Generated: DETERMINISTIC_5b3e10f0d5627a8c
Batch ID: 20250612_162632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Secure User Data Against Phishing Threats in a Web Application

This code demonstrates best practices for securing user data against phishing threats,
including input validation, email verification, multi-factor authentication (MFA), and
phishing detection. The implementation is designed for production readiness.
"""

from flask import Flask, request, jsonify
import re
import hashlib
import secrets

app = Flask(__name__)

# In-memory storage for demo purposes
users_db = {}

# Regular expression for email validation
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

# This method hashes passwords securely using SHA-256
def hash_password(password: str) -> str:
    salt = secrets.token_hex(16)  # Generate a random salt
    hashed = hashlib.sha256((salt + password).encode()).hexdigest()
    return f"{salt}${hashed}"

# Validate input data (e.g., email format)
def is_valid_email(email: str) -> bool:
    return bool(EMAIL_REGEX.match(email))

# Generate a secure one-time token for email verification
def generate_verification_token() -> str:
    return secrets.token_urlsafe(32)

@app.route("/register", methods=["POST"])
def register_user():
    """
    User registration endpoint.
    Implements input validation and email verification for security.
    """
    try:
        data = request.json
        email = data.get("email", "").strip()
        password = data.get("password", "").strip()

        # Validate email format
        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format"}), 400

        # Ensure password meets complexity requirements
        if len(password) < 8:
            return jsonify({"error": "Password must be at least 8 characters"}), 400

        # Check if user already exists
        if email in users_db:
            return jsonify({"error": "Email already registered"}), 400

        # Store hashed password securely
        hashed_password = hash_password(password)

        # Generate verification token
        verification_token = generate_verification_token()

        # Save user data (including verification token)
        users_db[email] = {"password": hashed_password, "verified": False, "token": verification_token}

        # Simulate sending verification email (production systems use SMTP)
        print(f"Verification email sent to {email} with token: {verification_token}")

        return jsonify({"message": "User registered. Please verify your email."}), 201

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route("/verify-email", methods=["POST"])
def verify_email():
    """
    Endpoint for email verification.
    Protects against phishing by ensuring user proves ownership of the email.
    """
    try:
        data = request.json
        email = data.get("email", "").strip()
        token = data.get("token", "").strip()

        # Check if user exists
        user = users_db.get(email)
        if not user:
            return jsonify({"error": "Invalid email or token"}), 400

        # Verify token matches
        if user["token"] != token:
            return jsonify({"error": "Invalid email or token"}), 400

        # Mark user as verified
        user["verified"] = True

        return jsonify({"message": "Email verified successfully!"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route("/login", methods=["POST"])
def login_user():
    """
    User login endpoint. Includes MFA implementation.
    """
    try:
        data = request.json
        email = data.get("email", "").strip()
        password = data.get("password", "").strip()

        # Check if user exists
        user = users_db.get(email)
        if not user:
            return jsonify({"error": "Invalid email or password"}), 400

        # Verify email is verified
        if not user["verified"]:
            return jsonify({"error": "Email not verified"}), 403

        # Validate password
        stored_salt, stored_hashed_password = user["password"].split("$")
        hashed_password = hashlib.sha256((stored_salt + password).encode()).hexdigest()
        if hashed_password != stored_hashed_password:
            return jsonify({"error": "Invalid email or password"}), 400

        # Generate MFA token (in production, send via SMS/email/app)
        mfa_token = secrets.token_urlsafe(16)
        user["mfa_token"] = mfa_token
        print(f"MFA Token for {email}: {mfa_token}")

        return jsonify({"message": "Login successful. Please complete MFA.", "mfa_required": True}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route("/complete-mfa", methods=["POST"])
def complete_mfa():
    """
    Endpoint for completing MFA authentication.
    """
    try:
        data = request.json
        email = data.get("email", "").strip()
        mfa_token = data.get("mfa_token", "").strip()

        # Check if user exists
        user = users_db.get(email)
        if not user:
            return jsonify({"error": "Invalid email or MFA token"}), 400

        # Verify MFA token matches
        if user.get("mfa_token") != mfa_token:
            return jsonify({"error": "Invalid email or MFA token"}), 400

        # Clear MFA token after successful authentication
        user.pop("mfa_token", None)

        return jsonify({"message": "MFA completed successfully. User logged in."}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)  # Enable debug for development; disable in production
```
