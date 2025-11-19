"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mtch.pro
Prompt: What are the steps to handle email verification for user accounts in a Telegram-based login system like the one on mtch.pro?
Generated: DETERMINISTIC_e49dba1d96fa855c
Batch ID: 20250612_155956
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, url_for
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
import os

# Initialize Flask app
app = Flask(__name__)

# Configuration for email setup
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Replace with your mail server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')  # Email address for sending emails
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')  # Email password or app password
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')  # Secret key for signing tokens

# Initialize mail and serializer
mail = Mail(app)
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# Mock database for storing user data
database = {}

@app.route('/register', methods=['POST'])
def register():
    """
    Endpoint to handle user registration and send email verification link.
    Expects a JSON payload with 'email' and 'telegram_id'.
    """
    try:
        data = request.json
        email = data['email']
        telegram_id = data['telegram_id']

        if not email or not telegram_id:
            return jsonify({"error": "Email and Telegram ID are required"}), 400

        # Generate a unique token for email verification
        token = serializer.dumps(email, salt='email-verification-salt')

        # Construct verification URL
        verification_url = url_for('verify_email', token=token, _external=True)

        # Send verification email
        msg = Message('Verify Your Email', recipients=[email])
        msg.body = f"Welcome! Please verify your email by clicking the following link: {verification_url}"
        mail.send(msg)

        # Save user data in the mock database
        database[telegram_id] = {'email': email, 'verified': False}

        return jsonify({"message": "Verification email sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/verify_email/<token>', methods=['GET'])
def verify_email(token):
    """
    Endpoint to handle email verification.
    Expects a token in the URL.
    """
    try:
        # Verify token validity and extract the email
        email = serializer.loads(token, salt='email-verification-salt', max_age=3600)  # Token expires in 1 hour

        # Update user record in the mock database
        for user in database.values():
            if user['email'] == email:
                user['verified'] = True
                return jsonify({"message": "Email successfully verified"}), 200

        return jsonify({"error": "User not found"}), 404
    except SignatureExpired:
        return jsonify({"error": "Verification link has expired"}), 400
    except BadSignature:
        return jsonify({"error": "Invalid verification link"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/status/<telegram_id>', methods=['GET'])
def check_verification_status(telegram_id):
    """
    Endpoint to check the verification status of a user.
    Expects 'telegram_id' in the URL.
    """
    try:
        user = database.get(telegram_id)
        if user:
            return jsonify({"email": user['email'], "verified": user['verified']}), 200
        return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

This code sets up a simple Flask application to handle user registration, email verification, and verification status checks for a Telegram-based login system. Make sure to configure your environment variables (`MAIL_USERNAME`, `MAIL_PASSWORD`, `SECRET_KEY`) before running the application.
