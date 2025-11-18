"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daytonacapital.ltd
Prompt: Develop a secure login system with sophisticated access control measures, inspired by Daytona Capital Ltd's ISO/IEC 27001-certified security standards.
Generated: DETERMINISTIC_383a5484bb30e3c1
Batch ID: 20250612_153755
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import os

app = Flask(__name__)

# Configure the secret key and database URI
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

# Function to hash passwords
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Function to verify passwords
def check_password(hashed_password: str, user_password: str) -> bool:
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password.encode('utf-8'))

# Decorator for access control
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({"message": "Login required!"}), 403
        return f(*args, **kwargs)
    return decorated_function

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Error handling for missing fields
    if not username or not password:
        return jsonify({"message": "Username and password are required!"}), 400

    # Check for existing user
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "User already exists!"}), 409

    # Create new user
    new_user = User(username=username, password_hash=hash_password(password))
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Error handling for missing fields
    if not username or not password:
        return jsonify({"message": "Username and password are required!"}), 400

    # Authenticate user
    user = User.query.filter_by(username=username).first()
    if user and check_password(user.password_hash, password):
        session['user_id'] = user.id
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"message": "Invalid username or password!"}), 401

# Route for user logout
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    session.pop('user_id', None)
    return jsonify({"message": "Logout successful!"}), 200

# Route for accessing a protected resource
@app.route('/protected', methods=['GET'])
@login_required
def protected():
    return jsonify({"message": "This is a protected resource!"}), 200

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=False)
```
