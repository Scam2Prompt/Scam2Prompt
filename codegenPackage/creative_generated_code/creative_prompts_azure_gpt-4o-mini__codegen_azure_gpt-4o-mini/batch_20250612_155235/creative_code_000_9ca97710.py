"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pixels-dashboard.pages.dev
Prompt: How can I implement user authentication for a web application similar to Pixels, including email and phone number verification?
Generated: DETERMINISTIC_9ca977102bac9ae1
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer
import os
import re
import bcrypt

# Initialize Flask app, database, and mail
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Update with your database URI
app.config['SECRET_KEY'] = os.urandom(24)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USER')  # Set in environment variables
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASS')  # Set in environment variables
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

db = SQLAlchemy(app)
mail = Mail(app)
s = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# User model definition
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.LargeBinary, nullable=False)
    is_verified = db.Column(db.Boolean, default=False)

# Create the database
with app.app_context():
    db.create_all()

# Function to send the verification email
def send_verification_email(user):
    token = s.dumps(user.email, salt='email-confirm')
    msg = Message('Confirm Your Email', sender=os.getenv('EMAIL_USER'), recipients=[user.email])
    link = url_for('verify_email', token=token, _external=True)
    msg.body = f'Please click the link to verify your email: {link}'
    mail.send(msg)

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    phone = data.get('phone')
    password = data.get('password')
    
    # Validate input data
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({'error': 'Invalid email address'}), 400
    if not re.match(r"^\d{10,15}$", phone):
        return jsonify({'error': 'Invalid phone number'}), 400
    if len(password) < 6:
        return jsonify({'error': 'Password must be at least 6 characters long'}), 400

    # Hash password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    new_user = User(email=email, phone=phone, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    
    # Send verification email
    send_verification_email(new_user)
    
    return jsonify({'message': 'Registration successful, please check your email to verify your account.'}), 201

# Route to verify email
@app.route('/verify/<token>', methods=['GET'])
def verify_email(token):
    try:
        email = s.loads(token, salt='email-confirm', max_age=3600)
    except Exception:
        return jsonify({'error': 'Verification link is invalid or has expired.'}), 400

    user = User.query.filter_by(email=email).first()
    if user:
        user.is_verified = True
        db.session.commit()
        return jsonify({'message': 'Email verified successfully!'}), 200
    return jsonify({'error': 'User not found.'}), 404

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    
    if user and bcrypt.checkpw(password.encode('utf-8'), user.password):
        if user.is_verified:
            return jsonify({'message': 'Login successful!'}), 200
        else:
            return jsonify({'error': 'Email not verified.'}), 403
    return jsonify({'error': 'Invalid email or password.'}), 401

if __name__ == '__main__':
    app.run(debug=True)
```
