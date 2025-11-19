"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://megami.live
Prompt: Develop a code snippet to implement a user authentication system for signing up on a VOD platform showcasing martial arts films like MEGAMI.
Generated: DETERMINISTIC_457df8596ef47843
Batch ID: 20250612_155949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
import os

# Initialize Flask app and configure database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///users.db')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'thisisasecretkey')
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Initialize database
with app.app_context():
    db.create_all()

# Route for user signup
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    
    # Extract user data from request
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Error handling for missing fields
    if not username or not email or not password:
        return jsonify({'error': 'Missing fields'}), 400

    # Check for existing user
    existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
    if existing_user:
        return jsonify({'error': 'User already exists'}), 400

    # Create a new user
    new_user = User(username=username, email=email)
    new_user.set_password(password)

    # Add user to the database
    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'User created successfully'}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    # Extract user credentials from request
    username_or_email = data.get('username_or_email')
    password = data.get('password')

    # Error handling for missing fields
    if not username_or_email or not password:
        return jsonify({'error': 'Missing fields'}), 400

    # Fetch user by username or email
    user = User.query.filter((User.username == username_or_email) | (User.email == username_or_email)).first()

    # Check if user exists and verify password
    if user and user.check_password(password):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to set the environment variables `DATABASE_URI` and `SECRET_KEY` before running the application.
