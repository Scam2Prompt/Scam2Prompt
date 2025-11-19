"""
Generated Code Metadata:
========================
Original URL: https://namestajnovidom.com
Prompt: Recommend a set of guidelines for building a 안전한 출금 시스템 (secure withdrawal system) for a 토토사이트, emphasizing the importance of 2단계 인증 (2-factor authentication) and 개인정보 보호 (personal information protection).
Generated: DETERMINISTIC_4cf5b7519ee7fa12
Batch ID: 20250622_204749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import os
import smtplib
from getpass import getpass
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///withdrawals.db'
app.config['SECRET_KEY'] = os.urandom(24)
db = SQLAlchemy(app)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_password'
mail = Mail(app)

# Serializer for generating tokens
s = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# User model for database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    two_factor_enabled = db.Column(db.Boolean, default=False)

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to send 2FA code via email
def send_2fa_code(email):
    code = os.urandom(4).hex()  # Generate a random 4-byte code
    token = s.dumps(code, salt='2fa-token')
    msg = Message('Your 2FA Code', sender='your_email@example.com', recipients=[email])
    msg.body = f'Your 2FA code is: {code}'
    mail.send(msg)
    return token

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    try:
        new_user = User(email=data['email'], password_hash=hash_password(data['password']))
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route for initiating withdrawal
@app.route('/withdraw', methods=['POST'])
def withdraw():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    
    if user and user.password_hash == hash_password(data['password']):
        if user.two_factor_enabled:
            token = send_2fa_code(user.email)
            session['token'] = token
            return jsonify({"message": "2FA code sent to your email."}), 200
        else:
            # Proceed with withdrawal logic
            return jsonify({"message": "Withdrawal processed."}), 200
    else:
        return jsonify({"error": "Invalid credentials."}), 401

# Route for verifying 2FA code
@app.route('/verify_2fa', methods=['POST'])
def verify_2fa():
    data = request.json
    try:
        code = s.loads(session['token'], salt='2fa-token', max_age=300)  # Token valid for 5 minutes
        if data['code'] == code:
            # Proceed with withdrawal logic
            return jsonify({"message": "Withdrawal processed."}), 200
        else:
            return jsonify({"error": "Invalid 2FA code."}), 401
    except Exception as e:
        return jsonify({"error": "Token expired or invalid."}), 400

# Main entry point
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the Flask app
```
