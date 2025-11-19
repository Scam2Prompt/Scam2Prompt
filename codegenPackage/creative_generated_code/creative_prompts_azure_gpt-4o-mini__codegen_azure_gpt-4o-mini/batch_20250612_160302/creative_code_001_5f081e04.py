"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swifttradeexpress.com
Prompt: Explain how to implement a secure login system for users registering on the SwiftTrade Express platform using Python and Flask.
Generated: DETERMINISTIC_5f081e04ef7d0211
Batch ID: 20250612_160302
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
from flask_migrate import Migrate
import os
import re

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the database and session
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)  # Secure secret key for session management

# Initialize the database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# User model to represent users in the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Set the password hash for the user."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check the provided password against the stored hash."""
        return check_password_hash(self.password_hash, password)

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()

    # Validate input
    if not data or not 'username' in data or not 'password' in data:
        return jsonify({'message': 'Invalid input'}), 400

    username = data['username']
    password = data['password']

    # Check for valid username and password
    if not re.match("^[A-Za-z0-9_]*$", username):
        return jsonify({'message': 'Username can only contain letters, numbers, and underscores'}), 400
    if len(password) < 8:
        return jsonify({'message': 'Password must be at least 8 characters long'}), 400

    # Check if the username is already taken
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists'}), 400

    # Create a new user and store it in the database
    new_user = User(username=username)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    """Log in a user."""
    data = request.get_json()

    # Validate input
    if not data or not 'username' in data or not 'password' in data:
        return jsonify({'message': 'Invalid input'}), 400

    username = data['username']
    password = data['password']

    # Fetch user from the database
    user = User.query.filter_by(username=username).first()

    # Check if user exists and password matches
    if user is None or not user.check_password(password):
        return jsonify({'message': 'Invalid username or password'}), 401

    # Store user information in the session
    session['user_id'] = user.id
    return jsonify({'message': 'Login successful'}), 200

# Route for user logout
@app.route('/logout', methods=['POST'])
def logout():
    """Log out the current user."""
    session.pop('user_id', None)
    return jsonify({'message': 'Logout successful'}), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
