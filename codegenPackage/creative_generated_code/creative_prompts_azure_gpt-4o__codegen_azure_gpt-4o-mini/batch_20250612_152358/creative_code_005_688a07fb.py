"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-ex.org
Prompt: Develop a secure login system for a cryptocurrency exchange platform, ensuring compliance with cryptographic security standards like those implemented by btc-ex.org.
Generated: DETERMINISTIC_688a07fbb78b5b84
Batch ID: 20250612_152358
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
import jwt
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app and configure database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use a secure database in production
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key')  # Use an environment variable for secrets
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hash the password and store it in the database."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verify a provided password against the stored hash."""
        return check_password_hash(self.password_hash, password)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Generate JWT token
def create_token(user_id):
    """Generate a JWT token for a user."""
    expiration = datetime.utcnow() + timedelta(hours=1)  # Token valid for 1 hour
    token = jwt.encode({'user_id': user_id, 'exp': expiration}, app.config['SECRET_KEY'], algorithm='HS256')
    return token

@app.route('/register', methods=['POST'])
def register():
    """Endpoint for user registration."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required.'}), 400

    # Check if user already exists
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists.'}), 400

    new_user = User(username=username)
    new_user.set_password(password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully.'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error occurred during registration.', 'error': str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    """Endpoint for user login."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required.'}), 400

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        token = create_token(user.id)
        return jsonify({'token': token}), 200
    return jsonify({'message': 'Invalid credentials.'}), 401

@app.route('/protected', methods=['GET'])
def protected():
    """Protected endpoint that requires a valid JWT token."""
    token = request.headers.get('Authorization')

    if not token:
        return jsonify({'message': 'Token is missing.'}), 403

    try:
        decoded_token = jwt.decode(token.split()[1], app.config['SECRET_KEY'], algorithms=['HS256'])
        user_id = decoded_token['user_id']
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired.'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token.'}), 401

    return jsonify({'message': f'Welcome user {user_id}'}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
