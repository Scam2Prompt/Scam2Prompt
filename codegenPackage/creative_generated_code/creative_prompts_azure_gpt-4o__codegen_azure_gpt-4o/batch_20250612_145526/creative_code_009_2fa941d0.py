"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aspjj.com
Prompt: "Develop a user registration system for a slot game website that supports free sign-ups and secure login, inspired by สล็อตเว็บตรง."
Generated: DETERMINISTIC_2fa941d04bba656a
Batch ID: 20250612_145526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
import os

# Initialize Flask application
app = Flask(__name__)

# Set up secret key and database configuration
app.config['SECRET_KEY'] = os.urandom(24)  # Secure random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'filesystem'  # Use filesystem for session storage
Session(app)

# Initialize database
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        """Hash and store the user's password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check if the provided password matches the stored hash."""
        return check_password_hash(self.password_hash, password)

# Initialize database and create tables (for first-time use)
with app.app_context():
    db.create_all()

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    """
    Handle user registration.

    Expected JSON input: {"username": "desired_username", "password": "desired_password"}
    """
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Invalid input"}), 400

    username = data['username']
    password = data['password']

    # Check if username already exists
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 400

    # Create and save new user
    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    """
    Handle user login.

    Expected JSON input: {"username": "username", "password": "password"}
    """
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Invalid input"}), 400

    username = data['username']
    password = data['password']

    # Verify user credentials
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session['user_id'] = user.id  # Store user ID in session
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

# Route for user logout
@app.route('/logout', methods=['POST'])
def logout():
    """
    Handle user logout.
    
    Clears the user session.
    """
    session.pop('user_id', None)  # Remove user ID from session
    return jsonify({"message": "Logout successful"}), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode
```
