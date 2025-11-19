"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://focuscompoundingpharm.com
Prompt: What libraries are recommended for creating a user authentication system for a medical application?
Generated: DETERMINISTIC_ad85a0b32d89e392
Batch ID: 20250612_140255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python example using the `Flask` framework with libraries recommended for user authentication in a medical application. It includes `Flask-SQLAlchemy` for database management, `Flask-Bcrypt` for password hashing, and `Flask-JWT-Extended` for token-based authentication. Note that sensitive medical data must comply with regulations such as HIPAA.

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
import os

# Initialize the Flask app
app = Flask(__name__)

# Configure the app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Replace with production database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'super-secret-key')  # Replace with a secure key in production
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)  # Token expiration time

# Initialize libraries
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Create database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        # Validate input
        if not username or not password:
            return jsonify({'message': 'Username and password are required'}), 400

        # Check if username already exists
        if User.query.filter_by(username=username).first():
            return jsonify({'message': 'Username already exists'}), 409

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Create a new user
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        return jsonify({'message': 'Internal server error', 'error': str(e)}), 500

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        # Validate input
        if not username or not password:
            return jsonify({'message': 'Username and password are required'}), 400

        # Find the user
        user = User.query.filter_by(username=username).first()
        if not user or not bcrypt.check_password_hash(user.password, password):
            return jsonify({'message': 'Invalid username or password'}), 401

        # Create a JWT access token
        access_token = create_access_token(identity=user.id)
        return jsonify({'access_token': access_token}), 200
    except Exception as e:
        return jsonify({'message': 'Internal server error', 'error': str(e)}), 500

# Protected route example
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    try:
        # Get the current user's identity
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)

        if not user:
            return jsonify({'message': 'User not found'}), 404

        return jsonify({'message': f'Welcome {user.username}!'}), 200
    except Exception as e:
        return jsonify({'message': 'Internal server error', 'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

### Notes:
- Replace the SQLite database with a production-ready database such as PostgreSQL or MySQL.
- Ensure the `JWT_SECRET_KEY` is kept secure and not hardcoded in production.
- This is a basic example; for medical applications, additional security measures like HTTPS, logging, rate-limiting, and regulatory compliance must be implemented.
