"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vidhyaclinic.com
Prompt: What are the best practices for ensuring user data security on a betting website like vidhyaclinic.com?
Generated: DETERMINISTIC_b68e6d1219ec903a
Batch ID: 20250612_163336
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
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the database and secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Replace with your database URI
app.config['SECRET_KEY'] = os.urandom(24)  # Generate a random secret key
db = SQLAlchemy(app)

# User model for database representation
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Initialize the database
with app.app_context():
    db.create_all()

# Function to encrypt sensitive data
def encrypt_data(data):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return key, encrypted_data

# Function to decrypt sensitive data
def decrypt_data(key, encrypted_data):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    try:
        if not data or 'username' not in data or 'password' not in data or 'email' not in data:
            return jsonify({'error': 'Bad Request, please provide username, password, and email.'}), 400
        
        username = data['username']
        password = data['password']
        email = data['email']

        # Hash the password for security
        hashed_password = generate_password_hash(password)

        # Create a new user and add to the database
        new_user = User(username=username, password_hash=hashed_password, email=email)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    try:
        if not data or 'username' not in data or 'password' not in data:
            return jsonify({'error': 'Bad Request, please provide username and password.'}), 400
        
        user = User.query.filter_by(username=data['username']).first()

        if user and check_password_hash(user.password_hash, data['password']):
            session['user_id'] = user.id
            return jsonify({'message': 'Login successful!'}), 200
        else:
            return jsonify({'error': 'Invalid username or password.'}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to handle user data retrieval securely
@app.route('/user/data', methods=['GET'])
def get_user_data():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized access.'}), 401
    
    user = User.query.get(session['user_id'])
    return jsonify({'username': user.username, 'email': user.email}), 200

# Main block to run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
