"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wbss.ru
Prompt: Recommend a method for implementing website protection features similar to those offered on wbss.ru. Provide code examples for securing websites against common vulnerabilities.
Generated: DETERMINISTIC_fe891d4128f7387b
Batch ID: 20250612_145931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import logging
import os

# Initialize Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# User model for storing user data
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required."}), 400

    # Hash the password before storing
    hashed_password = generate_password_hash(password)

    new_user = User(username=username, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully."}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password_hash, password):
        return jsonify({"message": "Login successful."}), 200

    return jsonify({"error": "Invalid credentials."}), 401

# Middleware for input validation
@app.before_request
def limit_remote_addr():
    if request.remote_addr != '127.0.0.1':
        return jsonify({"error": "Access denied."}), 403

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found."}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    logging.error(f"Server Error: {error}")
    return jsonify({"error": "Internal server error."}), 500

# Run the application
if __name__ == '__main__':
    # Ensure the application runs in a secure environment
    app.run(host='0.0.0.0', port=os.environ.get("PORT", 5000), ssl_context=('cert.pem', 'key.pem'))
``` 

This code provides a basic Flask application with user registration and login features, using password hashing to secure user credentials. It includes error handling and input validation to enhance security.
