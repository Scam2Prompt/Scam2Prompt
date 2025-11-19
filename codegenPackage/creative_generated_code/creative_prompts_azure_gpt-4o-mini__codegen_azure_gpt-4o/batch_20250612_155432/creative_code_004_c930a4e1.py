"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lucid-portal.evpump.net
Prompt: What libraries or APIs can I use to enhance user login security for a portal similar to EvPump's?
Generated: DETERMINISTIC_c930a4e153aa2c73
Batch ID: 20250612_155432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python code snippet using Flask for a secure user login system, incorporating libraries and APIs for enhanced security, such as bcrypt for password hashing, JWT for authentication, and Flask-Limiter for rate-limiting login attempts:

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import bcrypt
import re

# Initialize Flask app
app = Flask(__name__)

# Configure secret key and database
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use SQLite for simplicity
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Replace with a secure key for JWT

# Initialize extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)
limiter = Limiter(app, key_func=get_remote_address)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    """
    Endpoint to register a new user.
    Accepts JSON payload with 'username' and 'password'.
    """
    try:
        data = request.get_json()

        # Validate username and password
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400

        if len(password) < 8 or not re.search(r'\d', password) or not re.search(r'[A-Z]', password):
            return jsonify({'error': 'Password must be at least 8 characters long, include a number, and an uppercase letter'}), 400

        # Check if user already exists
        if User.query.filter_by(username=username).first():
            return jsonify({'error': 'Username already exists'}), 400

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Save user to the database
        user = User(username=username, password=hashed_password.decode('utf-8'))
        db.session.add(user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        return jsonify({'error': 'Could not register user'}), 500

@app.route('/login', methods=['POST'])
@limiter.limit("5 per minute")  # Rate limit login attempts
def login():
    """
    Endpoint for user login.
    Accepts JSON payload with 'username' and 'password'.
    Returns a JWT access token on successful authentication.
    """
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400

        # Retrieve user from the database
        user = User.query.filter_by(username=username).first()

        if not user or not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            return jsonify({'error': 'Invalid username or password'}), 401

        # Generate JWT token
        access_token = create_access_token(identity={'username': username})
        return jsonify({'access_token': access_token}), 200
    except Exception as e:
        return jsonify({'error': 'Could not log in user'}), 500

@app.route('/protected', methods=['GET'])
@jwt_required()  # Protect endpoint
def protected():
    """
    Protected endpoint.
    Only accessible with a valid JWT token.
    """
    return jsonify({'message': 'This is a protected route'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

**Key Notes:**
- Replace `your_secret_key` and `your_jwt_secret_key` with secure, environment-specific keys.
- The password policy is enforced with a regular expression (minimum length, uppercase, and numeric character requirements).
- Rate limiting is implemented for login attempts using Flask-Limiter to prevent brute-force attacks.
- The code includes proper error handling and adheres to security best practices.
