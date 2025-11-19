"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://westrockhomo.multitransportador.com.br
Prompt: Generate code for a secure user authentication system for a TMS (Transportation Management System) similar to MultiTMS.
Generated: DETERMINISTIC_74fd70a3be733f4b
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: app.py
# Description: Secure user authentication system for a Transportation Management System (TMS)

from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from peewee import SqliteDatabase, Model, CharField
import os

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Use a secure random key for session management.

# Database configuration
DATABASE = 'tms_users.db'
db = SqliteDatabase(DATABASE)

# User model
class User(Model):
    username = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db

# Create tables if they don't exist
db.connect()
db.create_tables([User], safe=True)

# Register endpoint
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')
        
        # Validate input
        if not username or not password:
            return jsonify({'error': 'Username and password are required.'}), 400

        # Hash the password securely
        hashed_password = generate_password_hash(password)

        # Save user details to the database
        user = User.create(username=username, password=hashed_password)
        return jsonify({'message': 'User registered successfully!'}), 201
    except Exception as e:
        return jsonify({'error': 'Registration failed.', 'details': str(e)}), 500

# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')
        
        # Validate input
        if not username or not password:
            return jsonify({'error': 'Username and password are required.'}), 400

        # Fetch user from the database
        user = User.get_or_none(User.username == username)
        if not user or not check_password_hash(user.password, password):
            return jsonify({'error': 'Invalid username or password.'}), 401

        # Store user in session
        session['user'] = user.username
        return jsonify({'message': 'Login successful!'}), 200
    except Exception as e:
        return jsonify({'error': 'Login failed.', 'details': str(e)}), 500

# Logout endpoint
@app.route('/logout', methods=['POST'])
def logout():
    try:
        # Clear the session
        session.pop('user', None)
        return jsonify({'message': 'Logout successful!'}), 200
    except Exception as e:
        return jsonify({'error': 'Logout failed.', 'details': str(e)}), 500

# Protected endpoint
@app.route('/protected', methods=['GET'])
def protected():
    try:
        # Check if user is logged in
        if 'user' not in session:
            return jsonify({'error': 'Unauthorized access. Please log in.'}), 401

        return jsonify({'message': f'Welcome {session["user"]}! This is a protected route.'}), 200
    except Exception as e:
        return jsonify({'error': 'Failed to access protected resource.', 'details': str(e)}), 500

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements:
- Install Flask for the web server:
  ```
  pip install flask
  ```
- Install Peewee for SQLite database ORM:
  ```
  pip install peewee
  ```
- Install Werkzeug for password hashing:
  ```
  pip install werkzeug
  ```

### Notes:
- This code is ready to run and provides a basic authentication system using Flask, Peewee, and Werkzeug.
- Ensure you secure the application in production (e.g., use HTTPS, secure cookies, etc.).
