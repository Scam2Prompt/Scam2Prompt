"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://test-1ww.pages.dev
Prompt: Write a code snippet to integrate multi-factor authentication for the Outgrid Security Network.
Generated: DETERMINISTIC_1981ff255aa001f3
Batch ID: 20250612_163502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import smtplib
from random import randint
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import URLSafeTimedSerializer

# Initialize Flask App
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///users.db')
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_verified = db.Column(db.Boolean, default=False)

# Function to send email for MFA
def send_email(to, subject, body):
    try:
        # Setup your email server here
        smtp_server = 'smtp.example.com'
        smtp_port = 587
        smtp_user = os.getenv('SMTP_USER')
        smtp_password = os.getenv('SMTP_PASSWORD')

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, to, f'Subject: {subject}\n\n{body}')
    except Exception as e:
        print(f"Error sending email: {e}")

# Route to initiate login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if user and user.password == password:
        # Generate MFA token
        mfa_token = randint(100000, 999999)
        session['mfa_token'] = mfa_token
        session['user_email'] = email
        # Send MFA token via email
        send_email(email, 'Your MFA Code', f'Your MFA code is: {mfa_token}')
        return jsonify({'message': 'MFA code sent to your email.'}), 200
    return jsonify({'message': 'Invalid login credentials.'}), 401

# Route to verify MFA code
@app.route('/verify_mfa', methods=['POST'])
def verify_mfa():
    data = request.json
    mfa_code = data.get('mfa_code')

    if session.get('mfa_token') and int(mfa_code) == session['mfa_token']:
        # MFA verified, proceed with login
        session.pop('mfa_token', None)
        return jsonify({'message': 'MFA verified, login successful.'}), 200
    return jsonify({'message': 'Invalid MFA code.'}), 401

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
