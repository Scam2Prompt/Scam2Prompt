"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale.agbatoken.com
Prompt: Recommend tools or frameworks for building a secure user authentication system for a token-based platform like Agbatoken.
Generated: DETERMINISTIC_6f4a586f6d0baf09
Batch ID: 20250612_151038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary modules
import hashlib
import os
import jwt
from datetime import datetime, timedelta
from flask import Flask, request, jsonify, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Using SQLite for simplicity
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key')  # Secret key for JWT
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hash and set the user's password."""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Check if the provided password matches the stored hash."""
        return check_password_hash(self.password_hash, password)

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

def generate_token(user):
    """Generate a JWT token for the authenticated user."""
    token = jwt.encode({
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(hours=1)  # Token expiration time
    }, app.config['SECRET_KEY'], algorithm='HS256')
    return token

@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        abort(400, description="Username and password are required.")
    
    new_user = User(username=data['username'])
    new_user.set_password(data['password'])

    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        abort(500, description="User registration failed: {}".format(str(e)))

    return jsonify({"message": "User registered successfully."}), 201

@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user and return a JWT token."""
    data = request.get_json()
    user = User.query.filter_by(username=data.get('username')).first()

    if user and user.check_password(data.get('password')):
        token = generate_token(user)
        return jsonify({'token': token}), 200
    else:
        abort(401, description="Invalid username or password.")

@app.route('/protected', methods=['GET'])
def protected():
    """A protected route that requires a valid token."""
    token = request.headers.get('Authorization')
    if not token:
        abort(401, description="Token is missing.")
    
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        user = User.query.get(payload['user_id'])
        if not user:
            raise jwt.InvalidTokenError
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        abort(401, description="Invalid or expired token.")

    return jsonify({"message": "Welcome!", "user_id": user.id})

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
