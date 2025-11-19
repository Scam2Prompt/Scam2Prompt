"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poll-pyth.app
Prompt: What are the best practices for securing user data against phishing on a web platform?
Generated: DETERMINISTIC_6115d51009267e37
Batch ID: 20250612_162646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is an example of production-ready code in Python using Flask to secure user data against phishing. The code incorporates best practices for secure user authentication and anti-phishing mechanisms:

```python
from flask import Flask, request, jsonify, session, redirect, url_for, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer
import re

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Replace with a strong secret key in production

# Serializer for email verification tokens
serializer = URLSafeTimedSerializer(app.secret_key)

# In-memory database (replace with a real database in production)
users_db = {}

# Regular expression for validating email format
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

# Strong password policy validation
def is_password_strong(password):
    """
    Check if password meets strength criteria:
    - At least 8 characters
    - Contains upper and lower case letters
    - Includes at least one number
    - Contains at least one special character
    """
    return (
        len(password) >= 8 and
        any(char.isupper() for char in password) and
        any(char.islower() for char in password) and
        any(char.isdigit() for char in password) and
        any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password)
    )

@app.route('/register', methods=['POST'])
def register():
    """
    Register a new user with secure password hashing and email validation.
    """
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not EMAIL_REGEX.match(email):
        return jsonify({"error": "Invalid email format"}), 400

    if not password or not is_password_strong(password):
        return jsonify({"error": "Password does not meet strength requirements"}), 400

    # Check if user already exists
    if email in users_db:
        return jsonify({"error": "Email already registered"}), 400

    # Hash password before storing
    hashed_password = generate_password_hash(password)

    # Store the user data
    users_db[email] = {
        "password": hashed_password,
        "verified": False
    }

    # Generate email verification token
    token = serializer.dumps(email, salt="email-confirmation")

    # Simulate sending an email (replace with actual email sending in production)
    print(f"Email verification link: {request.url_root}verify/{token}")

    return jsonify({"message": "Registration successful! Please verify your email."}), 200

@app.route('/verify/<token>', methods=['GET'])
def verify_email(token):
    """
    Verify email address using token to prevent phishing.
    """
    try:
        # Validate the token and retrieve the email
        email = serializer.loads(token, salt="email-confirmation", max_age=3600)  # 1-hour expiry

        # Check if user exists
        if email not in users_db:
            return jsonify({"error": "Invalid verification link"}), 400

        # Mark user as verified
        users_db[email]["verified"] = True

        return jsonify({"message": "Email verified successfully!"}), 200
    except Exception as e:
        return jsonify({"error": "Invalid or expired verification link"}), 400

@app.route('/login', methods=['POST'])
def login():
    """
    Authenticate the user securely.
    """
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Validate user credentials
    user = users_db.get(email)
    if not user:
        return jsonify({"error": "Invalid email or password"}), 401

    if not user["verified"]:
        return jsonify({"error": "Email not verified"}), 403

    if not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid email or password"}), 401

    # Use secure session management
    session['user'] = email

    return jsonify({"message": "Login successful!"}), 200

@app.route('/logout', methods=['POST'])
def logout():
    """
    Log the user out securely.
    """
    session.pop('user', None)
    return jsonify({"message": "Logout successful!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

**Key Features:**
1. Input validation for email and password.
2. Password hashing using `werkzeug.security`.
3. Email verification to prevent phishing.
4. Secure session management.
5. Well-commented and production-ready structure.
