"""
Generated Code Metadata:
========================
Original URL: https://okulistatrzebnica.pl
Prompt: Illustrate how to implement a secure user authentication system for a patient portal in an eye care clinic, using technologies like JWT and bcrypt.
Generated: DETERMINISTIC_470e3961b01a54b6
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import bcrypt

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'  # In production, use environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eyecare_clinic.db'  # Use PostgreSQL/MySQL in production
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'patient', 'doctor', 'admin'
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Decorator for token verification
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.filter_by(id=data['id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_user, *args, **kwargs)
    
    return decorated

# Routes
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Validate input
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Username and password are required!'}), 400
    
    # Check if user already exists
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists!'}), 409
    
    # Hash password with bcrypt
    hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    
    # Create new user
    new_user = User(
        username=data['username'],
        password=hashed_password.decode('utf-8'),
        role=data.get('role', 'patient'),
        full_name=data['full_name'],
        email=data['email']
    )
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Registration failed!', 'error': str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    auth = request.get_json()
    
    if not auth or not auth.get('username') or not auth.get('password'):
        return jsonify({'message': 'Username and password are required!'}), 400
    
    user = User.query.filter_by(username=auth['username']).first()
    
    if not user:
        return jsonify({'message': 'User not found!'}), 404
    
    if bcrypt.checkpw(auth['password'].encode('utf-8'), user.password.encode('utf-8')):
        # Generate JWT token
        token = jwt.encode({
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, app.config['SECRET_KEY'], algorithm="HS256")
        
        return jsonify({
            'token': token,
            'user': {
                'id': user.id,
                'username': user.username,
                'role': user.role,
                'full_name': user.full_name,
                'email': user.email
            }
        }), 200
    
    return jsonify({'message': 'Invalid credentials!'}), 401

@app.route('/protected', methods=['GET'])
@token_required
def protected_route(current_user):
    return jsonify({
        'message': f'Welcome {current_user.full_name}!',
        'user': {
            'id': current_user.id,
            'username': current_user.username,
            'role': current_user.role,
            'full_name': current_user.full_name,
            'email': current_user.email
        }
    }), 200

# Helper function to create database tables
def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)  # In production, set debug=False
```
