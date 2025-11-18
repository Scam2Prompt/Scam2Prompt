"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phanytom.com
Prompt: Write Python code to implement a cloud-based identification and access management (IAM) system with multifactor authentication (MFA) and role-based access control, as described in Techmaestropus solutions.
Generated: DETERMINISTIC_a860ba670c9e2966
Batch ID: 20250612_155024
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
import smtplib
import random
import string
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user

# Initialize Flask app and database
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Secret key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iam_system.db'  # SQLite database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

# Database model for User
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable=False)  # User role for RBAC
    mfa_enabled = db.Column(db.Boolean, default=False)  # MFA enabled status

# Database model for MFA tokens
class MFAToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    token = db.Column(db.String(6), nullable=False)
    is_used = db.Column(db.Boolean, default=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Login manager user loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to send MFA token via email
def send_mfa_token(email, token):
    try:
        # Replace with your email server settings
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login('your_email@example.com', 'your_password')
            message = f'Subject: Your MFA Token\n\nYour MFA token is: {token}'
            server.sendmail('your_email@example.com', email, message)
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to generate a random MFA token
def generate_mfa_token():
    return ''.join(random.choices(string.digits, k=6))

# Route to register a new user
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    role = data.get('role', 'user')  # Default role is user

    # Check for existing user
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists'}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email already exists'}), 400

    # Hash the password and create a new user
    new_user = User(username=username, password_hash=hash_password(password), email=email, role=role)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

# Route to login user
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and user.password_hash == hash_password(password):
        # If MFA is enabled, generate and send MFA token
        if user.mfa_enabled:
            token = generate_mfa_token()
            mfa_entry = MFAToken(user_id=user.id, token=token)
            db.session.add(mfa_entry)
            db.session.commit()
            send_mfa_token(user.email, token)
            return jsonify({'message': 'MFA token sent to email'}), 200
        login_user(user)
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

# Route to verify MFA token
@app.route('/verify_mfa', methods=['POST'])
@login_required
def verify_mfa():
    data = request.json
    token = data.get('token')

    mfa_entry = MFAToken.query.filter_by(token=token, is_used=False).first()
    if mfa_entry:
        mfa_entry.is_used = True  # Mark token as used
        db.session.commit()
        return jsonify({'message': 'MFA verified, login successful'}), 200
    return jsonify({'message': 'Invalid or expired MFA token'}), 401

# Route to logout user
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful'}), 200

# Route to update MFA settings
@app.route('/set_mfa', methods=['POST'])
@login_required
def set_mfa():
    user = load_user(session['_user_id'])
    user.mfa_enabled = True
    db.session.commit()
    return jsonify({'message': 'MFA enabled'}), 200

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
