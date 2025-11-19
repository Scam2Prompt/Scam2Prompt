"""
Generated Code Metadata:
========================
Original URL: https://vxp.pertinencemediaa.com
Prompt: Generate a Python script using Flask to implement a login and registration system for a VIP membership, ensuring secure password storage and user authentication.
Generated: DETERMINISTIC_25d494a41196728f
Batch ID: 20250612_150119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
import os

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the database and session
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vip_membership.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)  # Secure random key for session management

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hash the password for secure storage."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check the provided password against the stored hash."""
        return check_password_hash(self.password_hash, password)

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required.'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists.'}), 400

    new_user = User(username=username)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully.'}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        session['user_id'] = user.id
        return jsonify({'message': 'Login successful.'}), 200
    else:
        return jsonify({'message': 'Invalid username or password.'}), 401

# Route for user logout
@app.route('/logout', methods=['POST'])
def logout():
    """Log out the current user."""
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully.'}), 200

# Route to check if user is logged in
@app.route('/status', methods=['GET'])
def status():
    """Check the login status of the user."""
    if 'user_id' in session:
        return jsonify({'message': 'User is logged in.'}), 200
    else:
        return jsonify({'message': 'User is not logged in.'}), 401

# Error handling for database errors
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle exceptions and return a JSON response."""
    return jsonify({'error': str(e)}), 500

# Main entry point to run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application in debug mode
```
