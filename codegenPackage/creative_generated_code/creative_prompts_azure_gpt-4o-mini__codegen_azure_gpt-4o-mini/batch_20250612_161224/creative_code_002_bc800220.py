"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zushi.shop
Prompt: What are the best practices for creating a secure login system for an e-commerce site like ZUSHI WAVE SHOP?
Generated: DETERMINISTIC_bc8002206136bb37
Batch ID: 20250612_161224
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
import re
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import URLSafeTimedSerializer
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# User model for storing user data
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        # Generate a password hash
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        # Check a password against the stored hash
        return check_password_hash(self.password_hash, password)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not (username and email and password):
        return jsonify({"error": "Missing fields"}), 400

    if db.session.query(User).filter_by(username=username).first() or db.session.query(User).filter_by(email=email).first():
        return jsonify({"error": "User already exists"}), 409

    # Validate password strength
    if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password):
        return jsonify({"error": "Password must be at least 8 characters long and contain letters and numbers."}), 400

    user = User(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully!"}), 201

@app.route('/login', methods=['POST'])
def login():
    """Login an existing user."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not (username and password):
        return jsonify({"error": "Missing fields"}), 400

    user = db.session.query(User).filter_by(username=username).first()
    if user and user.check_password(password):
        session['user_id'] = user.id
        return jsonify({"message": "Login successful!"}), 200

    return jsonify({"error": "Invalid username or password"}), 401

@app.route('/logout', methods=['POST'])
def logout():
    """Logout the current user."""
    session.pop('user_id', None)
    return jsonify({"message": "Logout successful!"}), 200

if __name__ == '__main__':
    app.run(debug=False)
```
