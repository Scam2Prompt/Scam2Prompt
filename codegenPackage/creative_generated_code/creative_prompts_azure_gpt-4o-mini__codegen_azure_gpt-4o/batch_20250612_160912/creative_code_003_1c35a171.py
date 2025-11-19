"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://niftin.info
Prompt: What libraries or APIs would you recommend for managing user accounts in a web app like Niftin?
Generated: DETERMINISTIC_1c35a1715b3b7220
Batch ID: 20250612_160912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is clean, well-commented, and production-ready Python code demonstrating libraries/APIs for managing user accounts in a web app. It uses Flask for the web framework, SQLAlchemy for database interaction, and Flask-Bcrypt for password hashing.

```python
# Import necessary libraries and modules
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import jwt
import datetime
from functools import wraps

# Initialize Flask app
app = Flask(__name__)

# Configure app settings (database URI and secret key for JWT)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use SQLite for simplicity
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change to a secure key in production

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    username = db.Column(db.String(80), unique=True, nullable=False)  # Unique username
    email = db.Column(db.String(120), unique=True, nullable=False)  # Unique email
    password = db.Column(db.String(128), nullable=False)  # Hashed password

# Function to verify JWT token (used for protected routes)
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.filter_by(id=data['user_id']).first()
        except Exception as e:
            return jsonify({'message': f'Invalid token: {str(e)}'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

# Route to register a new user
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()  # Get JSON data from request
        username = data['username']
        email = data['email']
        password = data['password']

        # Check if user already exists
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            return jsonify({'message': 'User already exists!'}), 400

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Create new user and add to the database
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully!'}), 201
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500

# Route to log in a user and generate JWT
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()  # Get JSON data from request
        username = data['username']
        password = data['password']

        # Find user by username
        user = User.query.filter_by(username=username).first()
        if not user or not bcrypt.check_password_hash(user.password, password):
            return jsonify({'message': 'Invalid credentials!'}), 401

        # Generate JWT token
        token = jwt.encode({'user_id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)},
                           app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({'token': token}), 200
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500

# A protected route example
@app.route('/protected', methods=['GET'])
@token_required
def protected_route(current_user):
    return jsonify({'message': f'Welcome, {current_user.username}! This is a protected route.'}), 200

# Main entry point
if __name__ == '__main__':
    # Create database tables if they don't exist already
    with app.app_context():
        db.create_all()
    # Run the Flask app
    app.run(debug=True)
```

### Key Libraries/Tools Used:
1. **Flask**: Lightweight web framework for building web apps.
2. **SQLAlchemy**: ORM for managing database interactions.
3. **Flask-Bcrypt**: For securely hashing passwords.
4. **JWT (PyJWT)**: For generating and verifying JSON Web Tokens (JWTs).

This code provides user registration, login, and a protected route example, demonstrating a basic user account management system.
