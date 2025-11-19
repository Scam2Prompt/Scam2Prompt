"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connecting-collabs.top
Prompt: What are best practices for managing user sessions in a RESTful API?
Generated: DETERMINISTIC_bfaf27d6ed03d85a
Batch ID: 20250612_164012
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
from itsdangerous import URLSafeTimedSerializer
import os

app = Flask(__name__)

# Configuration settings
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this-is-a-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'sqlite:///site.db')
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'

db = SQLAlchemy(app)

# User model for storing user data
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Serializer for generating and validating tokens
s = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# Function to create a new user
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Username and password are required."}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully."}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "User creation failed.", "error": str(e)}), 500

# Function to authenticate user and create a session
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    
    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id
        return jsonify({"message": "Login successful."}), 200
    return jsonify({"message": "Invalid username or password."}), 401

# Function to log out the user
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({"message": "Logged out successfully."}), 200

# Middleware to protect routes
@app.before_request
def require_login():
    if request.endpoint in ['protected_route'] and 'user_id' not in session:
        return jsonify({"message": "Login required."}), 401

# Example protected route
@app.route('/protected', methods=['GET'])
def protected_route():
    return jsonify({"message": "This is a protected route."}), 200

if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application
```

In this code:
- A basic user registration and login system is implemented using Flask.
- Passwords are securely hashed.
- User session management is handled using Flask's `session`.
- Error handling is provided for user registration and login failures.
- A protected route demonstrates session checks before granting access.
