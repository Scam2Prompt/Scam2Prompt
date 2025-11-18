"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sitechgt.com
Prompt: Write code to manage user authentication and access control for the Études Architect App.
Generated: DETERMINISTIC_c93c8678a0bb4e14
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import os

# Initialize the Flask application and set up the database
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key_here')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model for storing user details
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # e.g., 'admin', 'user'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Error handler for 403 Forbidden errors
@app.errorhandler(403)
def forbidden(error):
    return jsonify({"message": "Forbidden access"}), 403

# Decorator for checking user roles
def role_required(role):
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session or session.get('role') != role:
                return forbidden(403)
            return f(*args, **kwargs)
        return decorated_function
    return wrapper

# User registration route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role', 'user')  # Default to 'user'

    if not username or not password:
        return jsonify({"message": "Username and password required"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "User already exists"}), 400

    new_user = User(username=username, role=role)
    new_user.set_password(password)
    
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

# User login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user is None or not user.check_password(password):
        return jsonify({"message": "Invalid username or password"}), 401

    session['user_id'] = user.id
    session['role'] = user.role

    return jsonify({"message": "Logged in successfully"}), 200

# User logout route
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    session.pop('role', None)
    return jsonify({"message": "Logged out successfully"}), 200

# Protected route example for admin users
@app.route('/admin', methods=['GET'])
@role_required('admin')
def admin_area():
    return jsonify({"message": "Welcome to the admin area!"}), 200

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
```
