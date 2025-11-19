"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centroabakadabra.com
Prompt: Illustrate how to implement a user authentication system for a web platform that provides access to multidisciplinary health services, inspired by the offerings of Centro Abakadabra.
Generated: DETERMINISTIC_aeb2fd959d70fcb8
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import os

# Initialize the Flask application
app = Flask(__name__)

# Set the configuration for the database and secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = os.urandom(24)
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Create the database
with app.app_context():
    db.create_all()

# Decorator to require authentication
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({"message": "Authentication required!"}), 403
        return f(*args, **kwargs)
    return decorated_function

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if username is provided
    if not username or not password:
        return jsonify({"message": "Username and password are required!"}), 400

    # Check if the username already exists
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists!"}), 400

    # Hash the password and create the user
    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(username=username, password=hashed_password)

    # Add the user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if username and password are provided
    if not username or not password:
        return jsonify({"message": "Username and password are required!"}), 400

    user = User.query.filter_by(username=username).first()

    # Validate user credentials
    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"message": "Invalid credentials!"}), 401

# Route for user logout
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    session.pop('user_id', None)
    return jsonify({"message": "Logout successful!"}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
