"""
Generated Code Metadata:
========================
Original URL: https://olymptradeinvest.com
Prompt: Generate code for a secure user registration and email verification system, following the steps outlined in Hyiprio's account setup process.
Generated: DETERMINISTIC_13df2c2c0e099cf1
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Secure User Registration and Email Verification System**
===========================================================

**dependencies:**
* `flask`: For building the web application
* `flask_sqlalchemy`: For database operations
* `werkzeug`: For password hashing and verification
* `flask_mail`: For sending verification emails

**Code:**
```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-email-password'

db = SQLAlchemy(app)
mail = Mail(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    verified = db.Column(db.Boolean, default=False)

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)

    def __repr__(self):
        return f"User('{self.email}', '{self.verified}')"

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        if not email or not password:
            return jsonify({'error': 'Email and password are required'}), 400

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({'error': 'Email already exists'}), 400

        new_user = User(email, password)
        db.session.add(new_user)
        db.session.commit()

        # Send verification email
        msg = Message('Verify your email', sender='your-email@gmail.com', recipients=[email])
        msg.body = f"Verify your email: {request.url_root}verify/{new_user.id}"
        mail.send(msg)

        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/verify/<int:user_id>', methods=['GET'])
def verify(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        user.verified = True
        db.session.commit()
        return jsonify({'message': 'Email verified successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        if not email or not password:
            return jsonify({'error': 'Email and password are required'}), 400

        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({'error': 'Invalid credentials'}), 401

        if not user.verified:
            return jsonify({'error': 'Email not verified'}), 403

        return jsonify({'message': 'Logged in successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
