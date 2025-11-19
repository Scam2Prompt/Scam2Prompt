"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://risesparksolution.com
Prompt: Illustrate how to implement two-factor authentication in a trading application, referencing the security protocols used by RiseSparkSolution.
Generated: DETERMINISTIC_7a3667d88b374e44
Batch ID: 20250612_163149
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
import smtplib
import hashlib
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import URLSafeTimedSerializer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    two_factor_enabled = db.Column(db.Boolean, default=False)

# Function to send email (for two-factor authentication)
def send_email(to_email, subject, message):
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login('your_email@gmail.com', 'your_email_password')
            server.sendmail('your_email@gmail.com', to_email, f"Subject: {subject}\n{message}")
    except Exception as e:
        print(f"Error sending email: {e}")

# Generate a random 6-digit code for 2FA
def generate_2fa_code():
    return str(random.randint(100000, 999999))

# Hashing function for passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Endpoint for user login with 2FA
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    
    if user and user.password_hash == hash_password(password):
        if user.two_factor_enabled:
            # Generate and send 2FA code
            code = generate_2fa_code()
            session['2fa_code'] = code
            send_email(user.email, "Your 2FA Code", f"Your code is: {code}")
            return jsonify({"message": "2FA code sent to your email."}), 200
        else:
            return jsonify({"message": "Login successful."}), 200
    return jsonify({"message": "Invalid credentials."}), 401

# Endpoint to verify 2FA code
@app.route('/verify_2fa', methods=['POST'])
def verify_2fa():
    data = request.json
    code = data.get('code')

    if session.get('2fa_code') == code:
        del session['2fa_code']  # Clear the session code
        return jsonify({"message": "2FA verification successful. You are logged in."}), 200
    return jsonify({"message": "Invalid 2FA code."}), 401

# Endpoint to enable 2FA
@app.route('/enable_2fa', methods=['POST'])
def enable_2fa():
    data = request.json
    email = data.get('email')
    
    user = User.query.filter_by(email=email).first()
    
    if user:
        user.two_factor_enabled = True
        db.session.commit()
        return jsonify({"message": "Two-factor authentication enabled."}), 200
    return jsonify({"message": "User not found."}), 404

# Main function to run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application
```
