"""
Generated Code Metadata:
========================
Original URL: https://phanytom.com
Prompt: Write Python code to implement a cloud-based identification and access management (IAM) system with multifactor authentication (MFA) and role-based access control, as described in Techmaestropus solutions.
Generated: DETERMINISTIC_a860ba670c9e2966
Batch ID: 20250612_155024
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
import random
import string
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# Initialize Flask app, database, bcrypt, and login manager
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iam_system.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User model for the database
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable=False)
    mfa_secret = db.Column(db.String(50), nullable=True)

# MFA Code Generation
def generate_mfa_code():
    return ''.join(random.choices(string.digits, k=6))

# Send MFA code via email
def send_mfa_code(email, code):
    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login('your_email@example.com', 'your_password')
            message = f'Subject: Your MFA Code\n\nYour MFA code is: {code}'
            server.sendmail('your_email@example.com', email, message)
    except Exception as e:
        print(f"Error sending email: {e}")

# Load user for login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], password=hashed_password, email=data['email'], role=data['role'])
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    
    if user and bcrypt.check_password_hash(user.password, data['password']):
        mfa_code = generate_mfa_code()
        user.mfa_secret = mfa_code
        db.session.commit()
        send_mfa_code(user.email, mfa_code)
        session['user_id'] = user.id
        return jsonify({"message": "MFA code sent to your email."}), 200
    return jsonify({"error": "Invalid credentials."}), 401

# Route for MFA verification
@app.route('/verify_mfa', methods=['POST'])
@login_required
def verify_mfa():
    data = request.get_json()
    user = User.query.get(session['user_id'])
    
    if user.mfa_secret == data['mfa_code']:
        login_user(user)
        user.mfa_secret = None  # Clear MFA secret after successful login
        db.session.commit()
        return jsonify({"message": "Login successful!"}), 200
    return jsonify({"error": "Invalid MFA code."}), 401

# Route for user logout
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully!"}), 200

# Route for role-based access control
@app.route('/protected', methods=['GET'])
@login_required
def protected():
    if current_user.role != 'admin':
        return jsonify({"error": "Access denied."}), 403
    return jsonify({"message": "Welcome to the protected route!"}), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found."}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error."}), 500

# Main entry point
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the Flask app
```
