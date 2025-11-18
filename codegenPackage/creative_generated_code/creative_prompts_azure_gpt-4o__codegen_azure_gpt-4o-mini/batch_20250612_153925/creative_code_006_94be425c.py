"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gopulseonline.com
Prompt: Generate a Python script to register and authenticate users for the PulseChain Suite platform, leveraging the features described on GoPulse.com.
Generated: DETERMINISTIC_94be425c4e485413
Batch ID: 20250612_153925
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
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer, BadSignature

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# User model for storing user information
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hash the password and store it."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check hashed password against the provided password."""
        return check_password_hash(self.password_hash, password)

# Create the database
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Error handling for missing fields
    if not username or not email or not password:
        return jsonify({'error': 'Username, email, and password are required.'}), 400

    # Check if user already exists
    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({'error': 'Username or email already exists.'}), 400

    # Create and save the new user
    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully.'}), 201

@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Error handling for missing fields
    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    # Retrieve user by username
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session['user_id'] = user.id
        return jsonify({'message': 'Login successful.'}), 200

    return jsonify({'error': 'Invalid username or password.'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    """Log out the user."""
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully.'}), 200

@app.route('/profile', methods=['GET'])
def profile():
    """Get the logged-in user's profile."""
    user_id = session.get('user_id')

    if not user_id:
        return jsonify({'error': 'Not authenticated.'}), 401

    user = User.query.get(user_id)
    return jsonify({
        'username': user.username,
        'email': user.email
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to install the necessary dependencies before running the script:
```bash
pip install Flask Flask-SQLAlchemy Werkzeug itsdangerous
```
