"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-alpha.nl
Prompt: Generate a code snippet for a secure user registration process for a trading platform, inspired by the security measures mentioned on the Immediate Alpha website.
Generated: DETERMINISTIC_f4783fdcac738451
Batch ID: 20250612_163029
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
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model for our database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

def create_database():
    """Create the database if it doesn't exist."""
    with app.app_context():
        db.create_all()

def validate_username(username):
    """Validate username format."""
    return re.match(r'^[a-zA-Z0-9_]{3,20}$', username) is not None

def validate_email(email):
    """Validate email format."""
    return re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email) is not None

def validate_password(password):
    """Validate password strength."""
    return (
        len(password) >= 8 and
        re.search(r'[A-Z]', password) and
        re.search(r'[a-z]', password) and
        re.search(r'[0-9]', password) and
        re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    )

@app.route('/register', methods=['POST'])
def register():
    """Handle user registration."""
    data = request.json

    # Input validation
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not (username and email and password):
        return jsonify({"error": "Missing fields"}), 400
    
    if not validate_username(username):
        return jsonify({"error": "Invalid username"}), 400
    
    if not validate_email(email):
        return jsonify({"error": "Invalid email"}), 400
    
    if not validate_password(password):
        return jsonify({"error": "Weak password"}), 400

    # Hash password
    password_hash = generate_password_hash(password)

    # Create new user
    new_user = User(username=username, email=email, password_hash=password_hash)

    try:
        db.session.add(new_user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Username or email already exists"}), 400

    return jsonify({"message": "User registered successfully"}), 201

if __name__ == '__main__':
    create_database()
    app.run(debug=False)
```
