"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vxp.pertinencemediaa.com
Prompt: Generate a Python script using Flask to implement a login and registration system for a VIP membership, ensuring secure password storage and user authentication.
Generated: DETERMINISTIC_25d494a41196728f
Batch ID: 20250612_150119
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
import os

# Initialize Flask app
app = Flask(__name__)

# Secret key for session management
app.secret_key = os.urandom(24)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vip_membership.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Route: Register new user
@app.route('/register', methods=['POST'])
def register():
    try:
        # Get data from request
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # Validate input
        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        # Check if username already exists
        if User.query.filter_by(username=username).first():
            return jsonify({"error": "Username already exists"}), 409

        # Hash password for secure storage
        hashed_password = generate_password_hash(password, method='sha256')

        # Create new user
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Login user
@app.route('/login', methods=['POST'])
def login():
    try:
        # Get data from request
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # Validate input
        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        # Find user by username
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({"error": "Invalid credentials"}), 401

        # Store user info in session
        session['user_id'] = user.id
        session['username'] = user.username

        return jsonify({"message": "Login successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Logout user
@app.route('/logout', methods=['POST'])
def logout():
    try:
        # Clear session data
        session.clear()
        return jsonify({"message": "Logout successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Protected VIP area
@app.route('/vip', methods=['GET'])
def vip_area():
    try:
        # Check if user is logged in
        if 'user_id' not in session:
            return jsonify({"error": "Unauthorized access"}), 401

        return jsonify({"message": f"Welcome to the VIP area, {session['username']}!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Initialize database
with app.app_context():
    db.create_all()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
