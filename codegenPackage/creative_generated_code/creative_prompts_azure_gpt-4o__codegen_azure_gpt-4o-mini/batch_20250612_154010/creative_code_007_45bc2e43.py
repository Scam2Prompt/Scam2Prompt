"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://billyourtime.com
Prompt: Generate a user authentication system for a cloud-based time-tracking platform designed for legal professionals, referencing BillYourTime.com's approach.
Generated: DETERMINISTIC_45bc2e43005584df
Batch ID: 20250612_154010
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
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from werkzeug.exceptions import BadRequest, Unauthorized
import os

# Initialize Flask App
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Replace with your database URI
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirect for unauthorized users

# User Model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Load user callback for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Home route
@app.route('/')
def home():
    return jsonify(message="Welcome to the Time-Tracking Platform"), 200

# User Registration route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Validate input
    if not data or not ('username' in data and 'password' in data):
        raise BadRequest("Username and password are required.")
    
    username = data['username']
    password = data['password']
    
    # Check if user already exists
    if User.query.filter_by(username=username).first():
        raise BadRequest("Username already exists.")
    
    # Create new user
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, password=hashed_password)
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify(message="User registered successfully."), 201

# User Login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    # Validate input
    if not data or not ('username' in data and 'password' in data):
        raise BadRequest("Username and password are required.")
    
    username = data['username']
    password = data['password']
    
    user = User.query.filter_by(username=username).first()
    
    # Validate user credentials
    if not user or not bcrypt.check_password_hash(user.password, password):
        raise Unauthorized("Invalid username or password.")
    
    login_user(user)
    return jsonify(message="Logged in successfully."), 200

# User Logout route
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify(message="Logged out successfully."), 200

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Set to False in production
```
