"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dfcloudpbx.com
Prompt: Write code to deploy the myEPP login system for secure domain management, including tunneling for remote access over 4G or Wi-Fi.
Generated: DETERMINISTIC_82c4c7dea68f1fbd
Batch ID: 20250612_151553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask application
app = Flask(__name__)

# Configuration for the application
app.config['SECRET_KEY'] = os.urandom(24)  # Use a secure random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and user authentication
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirect unauthorized users to login

# User model for storing user information
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

# Load user for session management
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check for existing user
    if User.query.filter_by(username=username).first():
        logger.warning(f"Registration failed for user '{username}': user already exists.")
        return jsonify({"message": "User already exists!"}), 409

    # Hash password and create new user
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, password=hashed_password)
    
    # Add user to the database
    db.session.add(new_user)
    db.session.commit()
    
    logger.info(f"User '{username}' registered successfully.")
    return jsonify({"message": "User registered successfully!"}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    # Verify user credentials
    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user)
        logger.info(f"User '{username}' logged in successfully.")
        return jsonify({"message": "Login successful!"}), 200

    logger.warning(f"Login failed for user '{username}': invalid credentials.")
    return jsonify({"message": "Invalid username or password!"}), 401

# Route for user logout
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    logger.info(f"User '{current_user.username}' logged out successfully.")
    return jsonify({"message": "Logout successful!"}), 200

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Entry point for the application
if __name__ == '__main__':
    try:
        app.run(debug=False, host='0.0.0.0', port=5000)  # Run on all available interfaces
    except Exception as e:
        logger.error(f"Failed to start the application: {e}")
```
