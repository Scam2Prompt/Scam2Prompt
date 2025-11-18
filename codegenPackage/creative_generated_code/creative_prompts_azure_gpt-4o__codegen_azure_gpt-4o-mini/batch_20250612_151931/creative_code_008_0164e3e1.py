"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cajicacompra.com
Prompt: Write code to implement a secure login system for an e-commerce site, referencing the "Iniciar Sesión" functionality of Cajicá Compra.
Generated: DETERMINISTIC_0164e3e16bc824b2
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
import re

app = Flask(__name__)

# Configurations
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to register a new user
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Validate input
    if not username or not password or not re.match(r'^[a-zA-Z0-9_]{3,}$', username):
        return jsonify({"error": "Invalid input"}), 400

    # Check if user already exists
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "User already exists"}), 400

    # Create new user
    new_user = User(username=username, password_hash=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully"}), 201

# Route to login a user
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Validate input
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = User.query.filter_by(username=username).first()

    # Check if user exists and password is correct
    if user and check_password_hash(user.password_hash, password):
        session['user_id'] = user.id  # Store user ID in session
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

# Route to logout a user
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)  # Remove user ID from session
    return jsonify({"message": "Logout successful"}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```
