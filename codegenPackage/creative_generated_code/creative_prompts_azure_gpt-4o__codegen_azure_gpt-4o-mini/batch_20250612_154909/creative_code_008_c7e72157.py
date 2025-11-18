"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getinge-torin.com
Prompt: Create a RESTful API in Python for user authentication, including endpoints for login, logout, and session management, inspired by the Torin customer portal.
Generated: DETERMINISTIC_c7e7215795d5477c
Batch ID: 20250612_154909
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
from functools import wraps
import os

# Initialize Flask app and configure SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Use a random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite database for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Error handling for database errors
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify(error=str(e)), 500

# Create the database and tables
with app.app_context():
    db.create_all()

# Decorator to check if user is authenticated
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({"message": "Login required."}), 401
        return f(*args, **kwargs)
    return decorated_function

# Endpoint for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check for existing users
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "User already exists."}), 400

    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully."}), 201

# Endpoint for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session['user_id'] = user.id
        return jsonify({"message": "Login successful."}), 200
    return jsonify({"message": "Invalid credentials."}), 401

# Endpoint for user logout
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    session.pop('user_id', None)
    return jsonify({"message": "Logout successful."}), 200

# Endpoint to check session status
@app.route('/session', methods=['GET'])
@login_required
def get_session():
    user = User.query.get(session['user_id'])
    return jsonify({"message": "User is logged in.", "username": user.username}), 200

# Main block to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
