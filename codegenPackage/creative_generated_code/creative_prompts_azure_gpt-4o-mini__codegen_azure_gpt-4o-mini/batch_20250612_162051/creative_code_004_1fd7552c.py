"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecg-eg.net
Prompt: Illustrate how to implement a secure data handling process in a web application, ensuring confidentiality as emphasized by Experts Consulting Group.
Generated: DETERMINISTIC_1fd7552cb3fe07de
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import hashlib
import hmac
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configuration for the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Set the user's password by hashing it."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check the hashed password against a provided password."""
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def generate_token(user_id):
        """Generate a secure token for the user session."""
        secret_key = os.getenv('SECRET_KEY').encode()
        token = hmac.new(secret_key, str(user_id).encode(), hashlib.sha256).hexdigest()
        return token

# Helper function for error responses
def create_error_response(message, status_code):
    """Create a standardized error response."""
    response = jsonify({'error': message})
    response.status_code = status_code
    return response

@app.route('/register', methods=['POST'])
def register():
    """Handle user registration."""
    data = request.get_json()
    
    if not data or 'username' not in data or 'password' not in data:
        return create_error_response("Invalid input.", 400)

    username = data['username']
    password = data['password']
    
    if User.query.filter_by(username=username).first():
        return create_error_response("Username already exists.", 409)

    new_user = User(username=username)
    new_user.set_password(password)

    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return create_error_response("Database error.", 500)

    return jsonify({"message": "User registered successfully."}), 201

@app.route('/login', methods=['POST'])
def login():
    """Handle user login."""
    data = request.get_json()
    
    if not data or 'username' not in data or 'password' not in data:
        return create_error_response("Invalid input.", 400)

    user = User.query.filter_by(username=data['username']).first()
    
    if user is None or not user.check_password(data['password']):
        return create_error_response("Invalid username or password.", 401)

    token = User.generate_token(user.id)
    return jsonify({"token": token}), 200

@app.route('/protected', methods=['GET'])
def protected():
    """Protected route that requires a valid token."""
    token = request.headers.get('Authorization')
    
    if not token:
        return create_error_response("Token is missing.", 403)

    # Example token validation (In production, validate the token properly)
    user_id = int(token)  # This is a simplistic approach for illustration
    
    # Assuming we have a method to check the validity of the token
    # In real applications, use JWT or similar for better token management.
    if user_id <= 0:
        return create_error_response("Invalid token.", 403)

    return jsonify({"message": "Welcome to the protected route!"}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if not exist
    app.run(debug=True)
```
