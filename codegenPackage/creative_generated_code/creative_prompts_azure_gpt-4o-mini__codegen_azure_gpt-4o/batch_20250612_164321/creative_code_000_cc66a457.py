"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://klarna.ctpe.info
Prompt: How can I implement a secure login system using username and password in a web application?
Generated: DETERMINISTIC_cc66a457bda11678
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Secure Login System using Flask and SQLAlchemy

from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use a production-grade database in a real application
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secure, random string
app.config['SESSION_TYPE'] = 'filesystem'  # Configure session storage
Session(app)

db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # Validate input
        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400

        # Check if the user already exists
        if User.query.filter_by(username=username).first():
            return jsonify({'error': 'Username already exists'}), 400

        # Hash the password for secure storage
        password_hash = generate_password_hash(password)

        # Create and save the user
        new_user = User(username=username, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # Validate input
        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400

        # Retrieve the user from the database
        user = User.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password_hash, password):
            return jsonify({'error': 'Invalid username or password'}), 401

        # Save user session
        session['user_id'] = user.id
        session['username'] = user.username

        return jsonify({'message': 'Login successful'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for accessing protected resource
@app.route('/protected', methods=['GET'])
def protected():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized access'}), 401

    return jsonify({'message': f'Welcome, {session["username"]}!'}), 200

# Route for user logout
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message': 'Logout successful'}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
