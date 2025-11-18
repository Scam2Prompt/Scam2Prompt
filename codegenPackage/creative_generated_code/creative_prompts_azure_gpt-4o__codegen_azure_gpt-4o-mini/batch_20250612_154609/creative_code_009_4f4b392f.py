"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zenixglobaltrade.com
Prompt: Create a secure login system for a trading platform that uses 256-bit encryption, as mentioned in ZenixGlobaltrade's EV SSL feature.
Generated: DETERMINISTIC_4f4b392f5df5b87c
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import bcrypt
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from cryptography.fernet import Fernet
from flask_marshmallow import Marshmallow
from werkzeug.exceptions import BadRequest, Unauthorized

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Generate a secure key for Fernet encryption
def generate_key():
    return Fernet.generate_key()

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    encryption_key = db.Column(db.LargeBinary, nullable=False)

# User schema for serialization
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

# Initialize the database
with app.app_context():
    db.create_all()

# Secure password hashing
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Verify password
def verify_password(stored_password, provided_password):
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))

# Register a new user
@app.route('/register', methods=['POST'])
def register():
    try:
        username = request.json['username']
        password = request.json['password']

        if not username or not password:
            raise BadRequest("Username and password are required.")

        # Check if username already exists
        if User.query.filter_by(username=username).first():
            raise BadRequest("Username already exists.")

        encryption_key = generate_key()
        password_hash = hash_password(password)

        new_user = User(username=username, password_hash=password_hash, encryption_key=encryption_key)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# User login
@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.json['username']
        password = request.json['password']

        if not username or not password:
            raise BadRequest("Username and password are required.")

        user = User.query.filter_by(username=username).first()
        if user and verify_password(user.password_hash, password):
            # Here we would generate a token or session for the user
            return jsonify({"message": "Login successful."}), 200
        else:
            raise Unauthorized("Invalid username or password.")
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
