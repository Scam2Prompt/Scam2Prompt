"""
Generated Code Metadata:
========================
Original URL: https://phantpm.com
Prompt: **Design a basic IAM system with multifactor authentication for a medium-sized business, including the key features and benefits.**
Generated: DETERMINISTIC_1d1be635c4d68d26
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here is a Python implementation of a basic IAM (Identity and Access Management) system with multifactor authentication (MFA). This code uses Flask for the web framework and simulates MFA using email-based OTP (One-Time Password). It includes user registration, login, and MFA verification.

```python
from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
import random
import smtplib
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# In-memory user database (for demonstration purposes)
users_db = {}

# In-memory OTP store
otp_store = {}

# Email configuration (replace with your SMTP server details)
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your-email@example.com"
EMAIL_PASSWORD = "your-email-password"


def send_email(to_email, subject, body):
    """
    Sends an email using the configured SMTP server.
    """
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            message = f"Subject: {subject}\n\n{body}"
            server.sendmail(EMAIL_ADDRESS, to_email, message)
    except Exception as e:
        print(f"Error sending email: {e}")


@app.route('/register', methods=['POST'])
def register():
    """
    Endpoint to register a new user.
    Expects JSON payload with 'username', 'password', and 'email'.
    """
    data = request.json
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if not username or not password or not email:
        return jsonify({"error": "All fields are required"}), 400

    if username in users_db:
        return jsonify({"error": "Username already exists"}), 400

    # Hash the password for secure storage
    hashed_password = generate_password_hash(password)
    users_db[username] = {"password": hashed_password, "email": email}
    return jsonify({"message": "User registered successfully"}), 201


@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint to log in a user.
    Expects JSON payload with 'username' and 'password'.
    """
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "All fields are required"}), 400

    user = users_db.get(username)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"error": "Invalid username or password"}), 401

    # Generate OTP for MFA
    otp = random.randint(100000, 999999)
    otp_store[username] = otp

    # Send OTP to user's email
    send_email(user['email'], "Your OTP Code", f"Your OTP code is: {otp}")

    # Store username in session for MFA verification
    session['username'] = username
    return jsonify({"message": "OTP sent to your email"}), 200


@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    """
    Endpoint to verify the OTP for MFA.
    Expects JSON payload with 'otp'.
    """
    data = request.json
    otp = data.get('otp')

    if 'username' not in session:
        return jsonify({"error": "No login session found"}), 401

    username = session['username']
    expected_otp = otp_store.get(username)

    if not otp or int(otp) != expected_otp:
        return jsonify({"error": "Invalid OTP"}), 401

    # Clear OTP after successful verification
    otp_store.pop(username, None)
    session.pop('username', None)
    return jsonify({"message": "Login successful"}), 200


@app.route('/logout', methods=['POST'])
def logout():
    """
    Endpoint to log out a user.
    """
    session.clear()
    return jsonify({"message": "Logged out successfully"}), 200


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

### Key Features:
1. **User Registration**: Allows users to register with a username, password, and email.
2. **Password Hashing**: Securely stores passwords using hashing.
3. **Login with MFA**: Requires both password and OTP for authentication.
4. **Email-based OTP**: Sends a one-time password to the user's email for MFA.
5. **Session Management**: Uses Flask sessions to manage user state.

### Benefits:
- **Enhanced Security**: MFA adds an extra layer of protection.
- **Ease of Use**: Simple email-based OTP for medium-sized businesses.
- **Scalable**: Can be extended to use databases and advanced MFA methods.

Replace the email configuration with your SMTP server details to test the code.
