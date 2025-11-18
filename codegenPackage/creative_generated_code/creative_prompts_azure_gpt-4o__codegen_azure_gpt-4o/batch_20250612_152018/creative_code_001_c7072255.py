"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flarenet.works.app
Prompt: Recommend libraries or APIs for implementing a secure login system with Space ID and Login ID fields, similar to the functionality described on "サスケWorks."
Generated: DETERMINISTIC_c707225516cece8d
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python example implementing a secure login system with "Space ID" and "Login ID" fields using Flask and Flask-Bcrypt for security. This code uses best practices, including encryption and error handling.

```python
from flask import Flask, request, jsonify, make_response
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
import jwt
import datetime
from functools import wraps

# Initialize the Flask app and necessary libraries
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong, random key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Using SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

# Database model for users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    space_id = db.Column(db.String(50), unique=True, nullable=False)
    login_id = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

# Helper function: Token verification decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.filter_by(id=data['id']).first()
        except Exception as e:
            return jsonify({'message': 'Invalid token!', 'error': str(e)}), 401
        return f(current_user, *args, **kwargs)
    return decorated

# Endpoint: User registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    space_id = data.get('space_id')
    login_id = data.get('login_id')
    password = data.get('password')

    # Validate input
    if not space_id or not login_id or not password:
        return jsonify({'message': 'All fields are required!'}), 400

    # Check for existing user
    user_exists = User.query.filter((User.space_id == space_id) | (User.login_id == login_id)).first()
    if user_exists:
        return jsonify({'message': 'Space ID or Login ID already exists!'}), 409

    # Hash the password
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Create and save a new user
    new_user = User(space_id=space_id, login_id=login_id, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully!'}), 201

# Endpoint: User login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    login_id = data.get('login_id')
    password = data.get('password')

    # Validate input
    if not login_id or not password:
        return jsonify({'message': 'Login ID and Password are required!'}), 400

    # Fetch user
    user = User.query.filter_by(login_id=login_id).first()
    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid login credentials!'}), 401

    # Generate JWT token
    token = jwt.encode(
        {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expires in 1 hour
        },
        app.config['SECRET_KEY'],
        algorithm="HS256"
    )

    return jsonify({'token': token}), 200

# Protected endpoint: Example usage
@app.route('/protected', methods=['GET'])
@token_required
def protected(current_user):
    return jsonify({'message': f'Welcome, {current_user.login_id}!', 'space_id': current_user.space_id}), 200

# Main entry point
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
```

### Requirements:
1. Install the required libraries in your Python environment:
   ```bash
   pip install flask flask-bcrypt flask-sqlalchemy pyjwt
   ```

2. Replace `your_secret_key` in the `app.config['SECRET_KEY']` line with a strong, random secret key.

3. Use HTTPS in production environments to secure data transmission.
