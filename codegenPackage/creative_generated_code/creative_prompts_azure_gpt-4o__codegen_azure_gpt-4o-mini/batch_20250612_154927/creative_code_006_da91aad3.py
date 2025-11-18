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
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail, Message
import random
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_password'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
mail = Mail(app)

# User model for storing user information
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    otp = db.Column(db.String(6), nullable=True)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/login', methods=['POST'])
def login():
    """Handles user login with email and password or OTP."""
    data = request.json
    email = data.get('email')
    password = data.get('password')
    otp = data.get('otp')
    
    user = User.query.filter_by(email=email).first()
    
    if not user:
        return jsonify({'message': 'User not found'}), 404

    # Check for password authentication
    if password:
        if bcrypt.check_password_hash(user.password, password):
            session['user_id'] = user.id
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'message': 'Invalid password'}), 401

    # Check for OTP authentication
    if otp:
        if user.otp == otp:
            session['user_id'] = user.id
            return jsonify({'message': 'Login successful with OTP'}), 200
        else:
            return jsonify({'message': 'Invalid OTP'}), 401
    
    return jsonify({'message': 'Provide password or OTP'}), 400

@app.route('/request_otp', methods=['POST'])
def request_otp():
    """Generates and sends a one-time password (OTP) to the user's email."""
    data = request.json
    email = data.get('email')
    
    user = User.query.filter_by(email=email).first()
    
    if not user:
        return jsonify({'message': 'User not found'}), 404

    # Generate a random 6-digit OTP
    user.otp = str(random.randint(100000, 999999))
    db.session.commit()
    
    # Send OTP via email
    msg = Message('Your OTP Code', sender='your_email@example.com', recipients=[email])
    msg.body = f'Your OTP code is {user.otp}'
    
    try:
        mail.send(msg)
        return jsonify({'message': 'OTP sent successfully'}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to send OTP', 'error': str(e)}), 500

@app.route('/logout', methods=['POST'])
def logout():
    """Handles user logout by clearing the session."""
    session.pop('user_id', None)
    return jsonify({'message': 'Logout successful'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
