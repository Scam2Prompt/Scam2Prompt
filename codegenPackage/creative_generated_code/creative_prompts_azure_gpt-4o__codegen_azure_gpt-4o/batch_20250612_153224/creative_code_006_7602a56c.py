"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fanzyfashion.in
Prompt: Suggest an API or library for implementing a user authentication system with features like login, registration, and password recovery for an e-commerce website.
Generated: DETERMINISTIC_7602a56c7e00ed57
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation using `Flask` and `Flask-SQLAlchemy` for user authentication features including login, registration, and password recovery. It uses `Flask-Mail` for sending password recovery emails and `werkzeug.security` for password hashing.

```python
from flask import Flask, request, jsonify, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
import os
import uuid

# Initialize Flask app
app = Flask(__name__)

# Configuration for database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuration for email (set your SMTP settings here)
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'your-email-password'

# Initialize extensions
db = SQLAlchemy(app)
mail = Mail(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    reset_token = db.Column(db.String(120), nullable=True)

# Error handling for database issues
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'error': 'Internal Server Error'}), 500

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'error': 'Email and password are required'}), 400

        # Check if user already exists
        if User.query.filter_by(email=email).first():
            return jsonify({'error': 'User already exists'}), 400

        # Create new user
        hashed_password = generate_password_hash(password)
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'error': 'Email and password are required'}), 400

        # Find user by email
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({'error': 'Invalid email or password'}), 401

        return jsonify({'message': 'Login successful'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for password recovery
@app.route('/recover', methods=['POST'])
def recover_password():
    try:
        data = request.json
        email = data.get('email')

        if not email:
            return jsonify({'error': 'Email is required'}), 400

        # Find user by email
        user = User.query.filter_by(email=email).first()
        if not user:
            return jsonify({'error': 'User not found'}), 404

        # Generate reset token
        reset_token = str(uuid.uuid4())
        user.reset_token = reset_token
        db.session.commit()

        # Send email with reset token
        reset_url = url_for('reset_password', token=reset_token, _external=True)
        msg = Message('Password Recovery', recipients=[email])
        msg.body = f'Click the link to reset your password: {reset_url}'
        mail.send(msg)

        return jsonify({'message': 'Password recovery email sent'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for resetting password
@app.route('/reset/<token>', methods=['POST'])
def reset_password(token):
    try:
        data = request.json
        new_password = data.get('password')

        if not new_password:
            return jsonify({'error': 'Password is required'}), 400

        # Find user by reset token
        user = User.query.filter_by(reset_token=token).first()
        if not user:
            return jsonify({'error': 'Invalid reset token'}), 404

        # Update password
        user.password = generate_password_hash(new_password)
        user.reset_token = None  # Clear reset token
        db.session.commit()

        return jsonify({'message': 'Password reset successful'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    # Create database tables if not exists
    with app.app_context():
        db.create_all()

    app.run(debug=True)
```

### Requirements:
1. Install dependencies:
   ```
   pip install flask flask-sqlalchemy flask-mail werkzeug
   ```
2. Replace the placeholders in `MAIL_SERVER`, `MAIL_USERNAME`, and `MAIL_PASSWORD` with your SMTP server settings.

### Notes:
- The `reset_password` endpoint expects the reset token sent to the user's email. Ensure your email settings are properly configured for production.
- Handle sensitive configuration values securely using environment variables in production environments.
