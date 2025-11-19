"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centroabakadabra.com
Prompt: Illustrate how to implement a user authentication system for a web platform that provides access to multidisciplinary health services, inspired by the offerings of Centro Abakadabra.
Generated: DETERMINISTIC_aeb2fd959d70fcb8
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python code implementation using the Flask framework for a user authentication system. It includes registration, login, and token-based authentication using JSON Web Tokens (JWT).

```python
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import jwt
import datetime
from functools import wraps

# Initialize Flask app
app = Flask(__name__)

# Configuration settings
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Database model for the User table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Function to require token authentication for protected routes
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.filter_by(id=data['user_id']).first()
        except Exception as e:
            return jsonify({'message': 'Token is invalid!', 'error': str(e)}), 401
        return f(current_user, *args, **kwargs)
    return decorated

# Route to register a new user
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Validate input data
    if not username or not email or not password:
        return jsonify({'message': 'All fields are required!'}), 400

    # Check if the user already exists
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email already exists!'}), 400

    # Hash the password for storage
    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(username=username, email=email, password=hashed_password)

    # Add the user to the database
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User successfully registered!'}), 201

# Route to log in a user
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Validate input data
    if not email or not password:
        return jsonify({'message': 'Email and password are required!'}), 400

    # Retrieve user from database
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid email or password!'}), 401

    # Generate JWT token
    token = jwt.encode({
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({'token': token}), 200

# Protected route to get user information
@app.route('/profile', methods=['GET'])
@token_required
def profile(current_user):
    user_data = {
        'id': current_user.id,
        'username': current_user.username,
        'email': current_user.email
    }
    return jsonify({'user': user_data}), 200

# Main execution point
if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()

    # Run the Flask application
    app.run(debug=True)
```

### Notes:
- Replace `'your_secret_key_here'` with a secure and random string for production.
- Ensure the SQLite database (`users.db`) is properly secured and replace it with a production-grade database in production environments.
- Use HTTPS to secure all communications between clients and the server.
