"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustverxt.com
Prompt: Provide an example of how to implement secure data handling when managing user information for a trading platform like Trustverxt.
Generated: DETERMINISTIC_bafe7a886c5221d8
Batch ID: 20250612_160413
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
import json
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# User model for SQLAlchemy
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    sensitive_data = db.Column(db.LargeBinary, nullable=False)

def hash_password(password):
    """Hash a password for secure storage."""
    return hashlib.sha256(password.encode()).hexdigest()

def encrypt_data(data):
    """Encrypt sensitive user data using Fernet symmetric encryption."""
    return cipher_suite.encrypt(data.encode())

def decrypt_data(encrypted_data):
    """Decrypt sensitive user data."""
    return cipher_suite.decrypt(encrypted_data).decode()

@app.route('/register', methods=['POST'])
def register_user():
    """Endpoint to allow user registration."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    sensitive_info = data.get('sensitive_info')

    try:
        # Hash the password and encrypt sensitive information
        hashed_password = hash_password(password)
        encrypted_info = encrypt_data(sensitive_info)

        # Create new user and save to database
        new_user = User(username=username, password_hash=hashed_password, email=email, sensitive_data=encrypted_info)
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({"message": "User registered successfully."}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "User already exists."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/login', methods=['POST'])
def login_user():
    """Endpoint to allow user login."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and user.password_hash == hash_password(password):
        return jsonify({"message": "Login successful."}), 200
    else:
        return jsonify({"error": "Invalid credentials."}), 401

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user_info(user_id):
    """Endpoint to retrieve user information securely."""
    user = User.query.get(user_id)

    if user:
        decrypted_info = decrypt_data(user.sensitive_data)
        return jsonify({
            "username": user.username,
            "email": user.email,
            "sensitive_info": decrypted_info
        }), 200
    else:
        return jsonify({"error": "User not found."}), 404

if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    app.run(debug=False)
```
