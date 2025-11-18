"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virgocx-login.webflow.io
Prompt: Generate code to implement a user login system with two-factor authentication (2FA) for a cryptocurrency exchange platform similar to VirgoCX.
Generated: DETERMINISTIC_f958130908f90570
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import bcrypt
import jwt
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import pyotp
import datetime

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use SQLite for simplicity
app.config['SECRET_KEY'] = os.urandom(24)
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Configure mail server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

# Initialize SQLAlchemy and Mail
db = SQLAlchemy(app)
mail = Mail(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    secret = db.Column(db.String(16), nullable=False)  # For 2FA

# Create database tables
with app.app_context():
    db.create_all()

# Function to send email with 2FA code
def send_2fa_code(email, code):
    msg = Message('Your 2FA Code', sender='noreply@example.com', recipients=[email])
    msg.body = f'Your 2FA code is: {code}'
    mail.send(msg)

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Email and password are required.'}), 400

    hashed_pw = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    secret = pyotp.random_base32()
    new_user = User(email=data['email'], password=hashed_pw, secret=secret)

    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully.'}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Email and password are required.'}), 400

    user = User.query.filter_by(email=data['email']).first()
    if user is None or not bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
        return jsonify({'error': 'Invalid email or password.'}), 401

    # Generate 2FA code
    totp = pyotp.TOTP(user.secret)
    code = totp.now()
    send_2fa_code(user.email, code)
    
    return jsonify({'message': '2FA code sent to your email.'}), 200

# Route for 2FA verification
@app.route('/verify-2fa', methods=['POST'])
def verify_2fa():
    data = request.json
    if not data or 'email' not in data or 'code' not in data:
        return jsonify({'error': 'Email and code are required.'}), 400

    user = User.query.filter_by(email=data['email']).first()
    if user is None:
        return jsonify({'error': 'Invalid email.'}), 401

    # Verify the 2FA code
    totp = pyotp.TOTP(user.secret)
    if not totp.verify(data['code']):
        return jsonify({'error': 'Invalid 2FA code.'}), 401

    # Generate JWT token
    token = jwt.encode({'email': user.email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, app.config['SECRET_KEY'])
    
    return jsonify({'token': token}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**Note:** Make sure to configure the mailing settings correctly for the `flask_mail` to work in your production environment, and consider using a more robust database system for scaling purposes.
