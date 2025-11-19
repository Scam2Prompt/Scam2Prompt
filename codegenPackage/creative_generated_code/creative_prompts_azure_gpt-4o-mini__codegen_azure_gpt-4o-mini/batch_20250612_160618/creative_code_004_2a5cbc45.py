"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.mirrorcommunity.com
Prompt: How do I set up user authentication for a store that requires a password, as seen on Mirror Mirror Community?
Generated: DETERMINISTIC_2a5cbc457fa6f832
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# user_auth.py

import hashlib
import os
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from werkzeug.exceptions import NotFound, BadRequest

# Initialize Flask app and database
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    """Register a new user with a username and password."""
    data = request.get_json()
    
    if not data or 'username' not in data or 'password' not in data:
        raise BadRequest("Username and password are required")

    username = data['username']
    password = data['password']
    
    # Hash the password
    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    
    # Check if user already exists
    if User.query.filter_by(username=username).first() is not None:
        raise BadRequest("User already exists")

    new_user = User(username=username, password_hash=password_hash)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify(message="User registered successfully"), 201

@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user with username and password."""
    data = request.get_json()
    
    if not data or 'username' not in data or 'password' not in data:
        raise BadRequest("Username and password are required")

    username = data['username']
    password = data['password']
    
    # Retrieve user and check password
    user = User.query.filter_by(username=username).first()
    if user is None or not bcrypt.check_password_hash(user.password_hash, password):
        raise BadRequest("Invalid username or password")

    # Store user session
    session['user_id'] = user.id
    return jsonify(message="Login successful"), 200

@app.route('/logout', methods=['POST'])
def logout():
    """Log out the current user."""
    session.pop('user_id', None)
    return jsonify(message="Logout successful"), 200

@app.route('/user', methods=['GET'])
def get_user():
    """Retrieve the current user's information."""
    if 'user_id' not in session:
        raise NotFound("User not logged in")

    user = User.query.get(session['user_id'])
    return jsonify(username=user.username), 200

if __name__ == '__main__':
    app.run(debug=True)
```

**Dependencies:**
- Flask
- Flask-SQLAlchemy
- Flask-Bcrypt

**Installation:**
```bash
pip install Flask Flask-SQLAlchemy Flask-Bcrypt
```

**Run the Application:**
```bash
python user_auth.py
```

Make sure to handle the database migrations and ensure the SQLite database is properly set up in a production environment.
