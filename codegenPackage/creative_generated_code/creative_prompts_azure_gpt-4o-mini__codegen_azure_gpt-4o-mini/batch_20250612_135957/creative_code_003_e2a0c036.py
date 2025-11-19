"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anonymouscryptoexchange.com
Prompt: Describe how to create a user-friendly interface for a non-KYC crypto exchange platform, focusing on fast transaction processing and security features.
Generated: DETERMINISTIC_e2a0c036ce864e7b
Batch ID: 20250612_135957
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
import jwt
import datetime

# Initialize the Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Change to your database URI
app.config['SECRET_KEY'] = 'your_secret_key'  # Change to your secret key
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# User model representing the users table
class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hash and set the user's password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check a user's password against the hashed password."""
        return check_password_hash(self.password_hash, password)

# Endpoint for user registration
@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()

    # Input validation
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Username and password required'}), 400

    username = data['username']
    password = data['password']

    # Check if username already exists
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'User already exists'}), 409

    # Create new user
    new_user = User(username=username)
    new_user.set_password(password)

    # Add user to the database
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully'}), 201

# Endpoint for user login
@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user and return a JWT token."""
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Username and password required'}), 400

    user = User.query.filter_by(username=data['username']).first()

    if user and user.check_password(data['password']):
        # Create a JWT token
        token = jwt.encode({
            'sub': user.id,
            'iat': datetime.datetime.utcnow(),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, app.config['SECRET_KEY'], algorithm='HS256')
        
        return jsonify({'token': token}), 200
    
    return jsonify({'error': 'Invalid username or password'}), 401

# Middleware to protect routes
@app.before_request
def require_auth():
    """Require authentication for protected routes."""
    if request.endpoint not in ['login', 'register']:
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Token is missing!'}), 403
        
        try:
            jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired!'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token!'}), 403

# Sample endpoint to demonstrate a protected resource
@app.route('/transactions', methods=['GET'])
def transactions():
    """Fetch transaction data (placeholder example)."""
    return jsonify({'message': 'Here are your transactions.'}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
