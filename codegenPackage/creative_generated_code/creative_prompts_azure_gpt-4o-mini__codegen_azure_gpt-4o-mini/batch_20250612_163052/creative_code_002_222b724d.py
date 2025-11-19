"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediateevex.co
Prompt: Create a code snippet that demonstrates how to implement a secure login feature for a cryptocurrency trading application, inspired by the security measures of Immediate 5.0 Evex.
Generated: DETERMINISTIC_222b724d025bde32
Batch ID: 20250612_163052
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
import json
from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.secret_key = os.urandom(24)  # Secure session key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hash and set the user's password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check if the provided password matches the stored hash."""
        return check_password_hash(self.password_hash, password)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required."}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists."}), 409

    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully."}), 201

@app.route('/login', methods=['POST'])
def login():
    """Authenticate user and create session."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required."}), 400

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid username or password."}), 401

    session['user_id'] = user.id  # Store user ID in session
    return jsonify({"message": "Logged in successfully."}), 200

@app.route('/logout', methods=['POST'])
def logout():
    """Log out the current user."""
    session.pop('user_id', None)  # Remove user ID from session
    return jsonify({"message": "Logged out successfully."}), 200

@app.route('/secure-data', methods=['GET'])
def secure_data():
    """Get sensitive data, accessible only to logged-in users."""
    if 'user_id' not in session:
        return jsonify({"error": "Authentication required."}), 403

    # Here you would implement logic to fetch sensitive data.
    sensitive_data = {"data": "This is sensitive data."}
    return jsonify(sensitive_data), 200

if __name__ == '__main__':
    app.run(debug=False)  # Set to debug=True only during development
```
