"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradetoearnoptions.com
Prompt: Write code to implement a secure registration and login system for an investment platform, using SSL encryption as specified by Tradetoearnoption.
Generated: DETERMINISTIC_99bb8fb8ee4f6c28
Batch ID: 20250612_154622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required, current_user
import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')  # Secret key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')  # Database connection URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications to save resources

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirect to login page if user is not logged in

# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Load user
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Registration route
@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Username and password are required."}), 400

    # Check if user exists
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"message": "User already exists."}), 400

    # Hash the password and create a new user
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully."}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Registration failed.", "error": str(e)}), 500

# Login route
@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user and create a session."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Username and password are required."}), 400

    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user)
        return jsonify({"message": "Login successful."}), 200
    else:
        return jsonify({"message": "Invalid credentials."}), 401

# Logout route
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    """Log out the logged-in user."""
    logout_user()
    return jsonify({"message": "Logout successful."}), 200

# Secure route example
@app.route('/secure-data', methods=['GET'])
@login_required
def secure_data():
    """A secure endpoint that requires login."""
    return jsonify({"message": "This is secured data!", "user": current_user.username}), 200

if __name__ == '__main__':
    # Run the app with SSL context
    app.run(ssl_context=('path/to/cert.pem', 'path/to/key.pem'))  # Update with your SSL certificate paths
```

Make sure to replace `path/to/cert.pem` and `path/to/key.pem` with the actual paths to your SSL certificate and key. Additionally, ensure that your `.env` file contains the necessary `SECRET_KEY` and `DATABASE_URL` for the application to function correctly.
