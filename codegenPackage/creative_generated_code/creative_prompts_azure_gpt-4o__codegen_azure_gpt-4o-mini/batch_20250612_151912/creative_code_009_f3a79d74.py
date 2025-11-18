"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptobalancer.co.uk
Prompt: Suggest methods to implement secure login functionality for a cryptocurrency management tool like CryptoBalancer.
Generated: DETERMINISTIC_f3a79d74c7c3324e
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
import os
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a secret key for session management

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Change to your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and login manager
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

# Load user for authentication
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create the database
with app.app_context():
    db.create_all()

# Secure registration method
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Validate input
    if not username or not password:
        return jsonify({"error": "Username and password required."}), 400
    
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Create and store the new user
    new_user = User(username=username, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201

# Secure login method
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Validate input
    if not username or not password:
        return jsonify({"error": "Username and password required."}), 400

    user = User.query.filter_by(username=username).first()
    
    # Check if user exists and password is correct
    if user and bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
        login_user(user)
        return jsonify({"message": "Logged in successfully!"}), 200
    else:
        return jsonify({"error": "Invalid username or password."}), 401

# Secure logout method
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully!"}), 200

# Example endpoint requiring authentication
@app.route('/secure-data', methods=['GET'])
@login_required
def secure_data():
    return jsonify({"data": "This is secured data!"}), 200

# Error handling for unforeseen exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set to False for production
```
