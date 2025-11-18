"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://megami.live
Prompt: Create a Python script using Flask or Django to manage user accounts for a VOD platform offering Japanese female martial arts movies.
Generated: DETERMINISTIC_d3a49751ecc9e6e6
Batch ID: 20250612_145633
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
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import os

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vod_users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'default_jwt_secret_key')

# Initialize extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def to_dict(self):
        """Return user data as a dictionary (excluding sensitive fields)."""
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    
    # Validate input
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    if not username or not email or not password:
        return jsonify({'error': 'All fields are required'}), 400

    # Check if the user already exists
    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return jsonify({'error': 'User with the same username or email already exists'}), 409

    # Hash the password and create the user
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, email=email, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully', 'user': new_user.to_dict()}), 201

@app.route('/login', methods=['POST'])
def login():
    """Authenticate user and return a JWT token."""
    data = request.get_json()

    # Validate input
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    # Find the user
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password_hash, password):
        # Generate a JWT token
        access_token = create_access_token(identity=user.id)
        return jsonify({'message': 'Login successful', 'access_token': access_token}), 200

    return jsonify({'error': 'Invalid username or password'}), 401

@app.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    """Get the authenticated user's profile."""
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({'user': user.to_dict()}), 200

@app.route('/delete_account', methods=['DELETE'])
@jwt_required()
def delete_account():
    """Delete the authenticated user's account."""
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'Account deleted successfully'}), 200

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Resource not found'}), 404

# Error handler for 500
@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Run the Flask server
    app.run(debug=True)
```
