"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binancetradinginterest.com
Prompt: Generate code for a user authentication system with mobile number and password login, inspired by the structure described on binancetradinginterest.com.
Generated: DETERMINISTIC_9723987173a9680f
Batch ID: 20250612_145450
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import re

# Initialize Flask application
app = Flask(__name__)

# Configure SQLite database and secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth_system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Initialize database
db = SQLAlchemy(app)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mobile_number = db.Column(db.String(15), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def generate_auth_token(self, expires_in=3600):
        """Generate an authentication token for the user."""
        s = Serializer(app.config['SECRET_KEY'], expires_in)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_auth_token(token):
        """Verify the authentication token."""
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except Exception as e:
            return None
        return User.query.get(data['user_id'])

# Utility function to validate mobile number
def is_valid_mobile(mobile_number):
    """Check if the mobile number is valid (simple regex check)."""
    pattern = r'^\+?[1-9]\d{1,14}$'  # E.164 format
    return re.match(pattern, mobile_number)

# API endpoint to register a new user
@app.route('/register', methods=['POST'])
def register():
    """Register a new user with a mobile number and password."""
    data = request.get_json()

    # Validate input data
    if not data or 'mobile_number' not in data or 'password' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    mobile_number = data['mobile_number']
    password = data['password']

    # Validate mobile number
    if not is_valid_mobile(mobile_number):
        return jsonify({'error': 'Invalid mobile number format'}), 400

    # Check if user already exists
    if User.query.filter_by(mobile_number=mobile_number).first():
        return jsonify({'error': 'Mobile number already registered'}), 400

    # Hash the password for secure storage
    password_hash = generate_password_hash(password)

    # Create new user and add to the database
    new_user = User(mobile_number=mobile_number, password_hash=password_hash)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

# API endpoint to login an existing user
@app.route('/login', methods=['POST'])
def login():
    """Login user with mobile number and password."""
    data = request.get_json()

    # Validate input data
    if not data or 'mobile_number' not in data or 'password' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    mobile_number = data['mobile_number']
    password = data['password']

    # Find user by mobile number
    user = User.query.filter_by(mobile_number=mobile_number).first()
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({'error': 'Invalid credentials'}), 401

    # Generate authentication token
    token = user.generate_auth_token()

    return jsonify({'message': 'Login successful', 'token': token}), 200

# API endpoint to test authentication with token
@app.route('/protected', methods=['GET'])
def protected():
    """Example of a protected route that requires a valid token."""
    token = request.headers.get('Authorization')

    # Validate token
    user = User.verify_auth_token(token)
    if not user:
        return jsonify({'error': 'Invalid or missing token'}), 401

    return jsonify({'message': f'Welcome, user {user.mobile_number}!'}), 200

# Main entry point for the application
if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()

    # Run the Flask application
    app.run(debug=True)
```
