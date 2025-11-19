"""
Generated Code Metadata:
========================
Original URL: https://phanbtom.com
Prompt: "Develop a code example for integrating multifactor authentication with an existing web application, using a library or API that supports various authentication methods."
Generated: DETERMINISTIC_bfe2bd8f07845019
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import pyotp
import os
import random
import string

# Initialize Flask app and database
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

db = SQLAlchemy(app)
mail = Mail(app)

# User model for database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    otp_secret = db.Column(db.String(16), nullable=True)

# Initialize the database
with app.app_context():
    db.create_all()

# Function to generate a random OTP secret
def generate_otp_secret():
    return pyotp.random_base32()

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required.'}), 400

    # Check if user already exists
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'User already exists.'}), 400

    # Create new user
    new_user = User(email=email, password=password)  # Password should be hashed in production
    new_user.otp_secret = generate_otp_secret()
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully.'}), 201

# Route for sending OTP
@app.route('/send_otp', methods=['POST'])
def send_otp():
    data = request.json
    email = data.get('email')

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'error': 'User not found.'}), 404

    # Generate OTP and send via email
    totp = pyotp.TOTP(user.otp_secret)
    otp = totp.now()
    msg = Message('Your OTP Code', sender='your_email@example.com', recipients=[email])
    msg.body = f'Your OTP code is: {otp}'
    mail.send(msg)

    return jsonify({'message': 'OTP sent successfully.'}), 200

# Route for verifying OTP
@app.route('/verify_otp', methods=['POST'])
def verify_otp():
    data = request.json
    email = data.get('email')
    otp = data.get('otp')

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'error': 'User not found.'}), 404

    # Verify OTP
    totp = pyotp.TOTP(user.otp_secret)
    if totp.verify(otp):
        session['user_id'] = user.id
        return jsonify({'message': 'OTP verified successfully.'}), 200
    else:
        return jsonify({'error': 'Invalid OTP.'}), 400

# Route for logging out
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully.'}), 200

# Error handling for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
