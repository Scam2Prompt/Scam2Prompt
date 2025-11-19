"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allocating-zerolend.app
Prompt: Can you provide code examples for implementing user authentication to prevent phishing attempts, referencing the warnings from the Cloudflare flagged site?
Generated: DETERMINISTIC_18790b276a1cdd9d
Batch ID: 20250612_162504
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
import secrets
from flask import Flask, request, jsonify, session, redirect, url_for, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Use a secure random key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirect to login page if not authenticated

# User model for storing user data
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Load user callback for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    try:
        username = data['username']
        password = data['password']
        
        # Check for existing user
        if User.query.filter_by(username=username).first():
            return jsonify({'message': 'User already exists!'}), 400
        
        # Hash the password for secure storage
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password=hashed_password)
        
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully!'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 500

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    try:
        username = data['username']
        password = data['password']
        
        user = User.query.filter_by(username=username).first()
        
        # Validate username and password
        if user and check_password_hash(user.password, password):
            login_user(user)
            return jsonify({'message': 'Login successful!'}), 200
        return jsonify({'message': 'Invalid credentials!'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 500

# Route for user logout
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    try:
        logout_user()
        return jsonify({'message': 'Logout successful!'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

# Route for checking authentication status
@app.route('/status', methods=['GET'])
@login_required
def status():
    return jsonify({'message': f'Logged in as {current_user.username}'}), 200

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=False)  # Run the app with debug disabled for production
```

### Notes
- This code implements a basic Flask application for user authentication with hashed passwords for security.
- Ensure you have Flask and Flask-Login installed in your Python environment.
- Use secure practices when handling passwords and user sessions.
- Remember to handle database migrations and additional security features in a production environment, like rate limiting and account lockout mechanisms.
