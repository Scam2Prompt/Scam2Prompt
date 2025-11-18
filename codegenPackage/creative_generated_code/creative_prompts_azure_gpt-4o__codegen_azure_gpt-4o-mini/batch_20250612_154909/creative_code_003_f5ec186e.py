"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sxabd.com
Prompt: Create a user registration system for a financial platform, ensuring it aligns with features like "Register" and "Login" on https://sxabd.com.
Generated: DETERMINISTIC_f5ec186e4586e5cb
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import re
import os

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model to represent the user in the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Create the database and the user table
with app.app_context():
    db.create_all()

# Function to validate the email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Endpoint for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json

    # Validate the request data
    if not data or 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({"error": "Username, email, and password are required."}), 400

    username = data['username']
    email = data['email']
    password = data['password']

    # Check for valid email format
    if not is_valid_email(email):
        return jsonify({"error": "Invalid email format."}), 400

    # Check if the user already exists
    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({"error": "Username or email already exists."}), 400

    # Hash the password for secure storage
    hashed_password = generate_password_hash(password, method='sha256')

    # Create and save the new user
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully."}), 201

# Endpoint for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.json

    # Validate the request data
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Username and password are required."}), 400

    username = data['username']
    password = data['password']

    # Find the user by username
    user = User.query.filter_by(username=username).first()

    # Validate user credentials
    if user and check_password_hash(user.password, password):
        return jsonify({"message": "Login successful."}), 200
    else:
        return jsonify({"error": "Invalid username or password."}), 401

# Error handling for unhandled routes
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found."}), 404

# Error handling for internal server errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error."}), 500

# Main execution
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
```
