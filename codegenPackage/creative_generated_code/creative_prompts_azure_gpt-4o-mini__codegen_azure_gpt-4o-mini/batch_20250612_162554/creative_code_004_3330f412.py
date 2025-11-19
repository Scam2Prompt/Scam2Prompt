"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kriptmart.com
Prompt: Illustrate how to implement a secure login system for a cryptocurrency application, referencing the user experience of Coinbase's sign-in process.
Generated: DETERMINISTIC_3330f4128580085f
Batch ID: 20250612_162554
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
import hmac
import base64
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer

# Initialize Flask application and database
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Secret key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use SQLite for demonstration
db = SQLAlchemy(app)

# User model for database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Utility function to send verification email (Placeholder)
def send_verification_email(email, token):
    # Placeholder for an email sending logic
    pass

# Token generation for password reset
def generate_token(email):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt='password-reset-salt')

# Verify the token for password reset
def verify_token(token):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        email = serializer.loads(token, salt='password-reset-salt', max_age=3600)  # 1 hour expiry
    except Exception as e:
        return None
    return email

# Registration route
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({'message': 'Email and password are required.'}), 400
    
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'User already exists.'}), 400
    
    # Hash the password and store it
    hashed_password = generate_password_hash(password)
    new_user = User(email=email, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully.'}), 201

# Login route
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({'message': 'Email and password are required.'}), 400
    
    user = User.query.filter_by(email=email).first()
    
    # Check if user exists and verify password
    if user and check_password_hash(user.password_hash, password):
        session['user_id'] = user.id  # Set session for user
        return jsonify({'message': 'Login successful.'}), 200
    
    return jsonify({'message': 'Invalid email or password.'}), 401

# Logout route
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)  # Clear user session
    return jsonify({'message': 'Logout successful.'}), 200

# Password reset request route
@app.route('/reset_password', methods=['POST'])
def reset_password_request():
    data = request.json
    email = data.get('email')
    
    if not email:
        return jsonify({'message': 'Email is required.'}), 400
    
    user = User.query.filter_by(email=email).first()
    if user:
        token = generate_token(email)
        send_verification_email(email, token)
    
    return jsonify({'message': 'If the email is registered, a password reset link has been sent.'}), 200

# Password reset route
@app.route('/reset_password/<token>', methods=['POST'])
def reset_password(token):
    data = request.json
    new_password = data.get('password')
    
    email = verify_token(token)
    if email is None:
        return jsonify({'message': 'Invalid or expired token.'}), 400
    
    user = User.query.filter_by(email=email).first()
    if user:
        user.password_hash = generate_password_hash(new_password)
        db.session.commit()
        return jsonify({'message': 'Password has been reset successfully.'}), 200
    
    return jsonify({'message': 'User not found.'}), 404

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
