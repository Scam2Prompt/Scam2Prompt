"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bluestockmarkets.com
Prompt: Develop a secure login system for BlueStockMarkets that supports multi-factor authentication and protects user data during account creation and sign-in processes.
Generated: DETERMINISTIC_1f5b68a21282fdb7
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import secrets
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import pyotp

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = os.urandom(24)
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_password'

db = SQLAlchemy(app)
mail = Mail(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    otp_secret = db.Column(db.String(16), nullable=False)

    def set_password(self, password):
        """Hashes the password for storage."""
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        """Checks the hashed password against the provided one."""
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()

# Initialize the database
with app.app_context():
    db.create_all()

def send_otp(email, otp):
    """Sends the one-time password to the user's email."""
    msg = Message('Your OTP Code', sender='your_email@example.com', recipients=[email])
    msg.body = f'Your OTP code is: {otp}'
    mail.send(msg)

@app.route('/register', methods=['POST'])
def register():
    """User registration endpoint."""
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Error handling for missing data
    if not email or not password:
        return jsonify({'error': 'Email and password are required.'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already registered.'}), 400

    user = User(email=email, otp_secret=secrets.token_urlsafe(16))
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User created successfully.'}), 201

@app.route('/login', methods=['POST'])
def login():
    """User login endpoint with multi-factor authentication."""
    data = request.json
    email = data.get('email')
    password = data.get('password')
    otp = data.get('otp')

    # Error handling for missing data
    if not email or not password or not otp:
        return jsonify({'error': 'Email, password, and OTP are required.'}), 400

    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
        totp = pyotp.TOTP(user.otp_secret)
        if totp.verify(otp):
            session['user_id'] = user.id
            return jsonify({'message': 'Login successful.'}), 200
        else:
            return jsonify({'error': 'Invalid OTP.'}), 401
    else:
        return jsonify({'error': 'Invalid email or password.'}), 401

@app.route('/send_otp', methods=['POST'])
def send_otp_endpoint():
    """Endpoint to send OTP to user email."""
    data = request.json
    email = data.get('email')

    # Error handling for missing data
    if not email:
        return jsonify({'error': 'Email is required.'}), 400

    user = User.query.filter_by(email=email).first()
    
    if user:
        totp = pyotp.TOTP(user.otp_secret)
        otp = totp.now()
        send_otp(email, otp)
        return jsonify({'message': 'OTP sent to email.'}), 200
    else:
        return jsonify({'error': 'Email not found.'}), 404

if __name__ == '__main__':
    app.run(debug=True)
```
