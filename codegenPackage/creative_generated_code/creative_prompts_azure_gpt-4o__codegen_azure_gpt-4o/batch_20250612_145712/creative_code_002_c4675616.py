"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://microlab.world
Prompt: Recommend libraries or APIs to securely manage user authentication and password recovery for a platform similar to MicroLab.
Generated: DETERMINISTIC_c4675616d1143623
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates a production-ready implementation for managing user authentication
and password recovery for a platform similar to MicroLab. It uses the Flask web framework 
along with Flask extensions like Flask-JWT-Extended for token-based authentication and 
Flask-Mail for secure email-based password recovery.

Dependencies:
- Flask
- Flask-JWT-Extended
- Flask-SQLAlchemy
- Flask-Mail
- Passlib (for password hashing)

Install these libraries by running:
pip install flask flask-jwt-extended flask-sqlalchemy flask-mail passlib
"""

from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from passlib.hash import bcrypt
import os

# Flask application setup
app = Flask(__name__)

# Configuration setup for JWT, Database, and Mail
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change this for production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Replace with your SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your_email_password'  # Replace with your email password

# Initialize extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)
mail = Mail(app)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    reset_token = db.Column(db.String(120), nullable=True)

# Create database schema
with app.app_context():
    db.create_all()

# Route to register a new user
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"msg": "All fields are required"}), 400

    # Check if user already exists
    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({"msg": "User already exists"}), 400

    # Hash the password and create a new user
    hashed_password = bcrypt.hash(password)
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully"}), 201

# Route to authenticate a user and generate a token
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"msg": "All fields are required"}), 400

    user = User.query.filter_by(username=username).first()
    if user and bcrypt.verify(password, user.password):
        # Generate JWT token
        access_token = create_access_token(identity=user.username)
        return jsonify({"access_token": access_token}), 200
    else:
        return jsonify({"msg": "Invalid credentials"}), 401

# Route to initiate password reset
@app.route('/forgot-password', methods=['POST'])
def forgot_password():
    data = request.json
    email = data.get('email')

    if not email:
        return jsonify({"msg": "Email is required"}), 400

    user = User.query.filter_by(email=email).first()
    if user:
        # Generate a simple reset token (in production, use a secure method)
        reset_token = os.urandom(24).hex()
        user.reset_token = reset_token
        db.session.commit()

        # Send password reset email
        msg = Message(
            "Password Reset Request",
            sender=app.config['MAIL_USERNAME'],
            recipients=[email]
        )
        msg.body = f"Use the following token to reset your password: {reset_token}"
        mail.send(msg)

    # Always return a success message to prevent user enumeration
    return jsonify({"msg": "If the email exists, a reset link has been sent"}), 200

# Route to reset the password
@app.route('/reset-password', methods=['POST'])
def reset_password():
    data = request.json
    reset_token = data.get('reset_token')
    new_password = data.get('new_password')

    if not reset_token or not new_password:
        return jsonify({"msg": "All fields are required"}), 400

    user = User.query.filter_by(reset_token=reset_token).first()
    if user:
        # Hash the new password and update the user's password
        user.password = bcrypt.hash(new_password)
        user.reset_token = None  # Clear the reset token
        db.session.commit()
        return jsonify({"msg": "Password reset successful"}), 200
    else:
        return jsonify({"msg": "Invalid reset token"}), 400

# Protected route to demonstrate JWT authentication
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({"msg": f"Hello, {current_user}. This is a protected route."}), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
