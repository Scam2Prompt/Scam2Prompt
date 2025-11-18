"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Write code to integrate multi-layered access control for school management software, ensuring security as highlighted in Him Saral's features.
Generated: DETERMINISTIC_fa95de444bd6a008
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, g
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

# Initialize the Flask application
app = Flask(__name__)

# Set up the database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school_management.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this to a strong secret key
db = SQLAlchemy(app)

# Define User roles
class Role:
    ADMIN = 'admin'
    TEACHER = 'teacher'
    STUDENT = 'student'

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Decorator for role-based access control
def role_required(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Check for JWT token
            token = request.headers.get('Authorization')
            if not token:
                return jsonify({'message': 'Token is missing!'}), 403
            
            try:
                # Decode the token
                data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
                user = User.query.get(data['user_id'])
            except Exception as e:
                return jsonify({'message': 'Token is invalid!'}), 403
            
            # Check user role
            if user.role != role:
                return jsonify({'message': 'Access denied!'}), 403
            
            # Attach user to the global context
            g.user = user
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Username and password are required!'}), 400
    
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password, role=data['role'])
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully!'}), 201
    except Exception as e:
        return jsonify({'message': 'Username already exists!'}), 409

# Route for login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Invalid credentials!'}), 401
    
    # Create JWT token
    token = jwt.encode({'user_id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
                       app.config['SECRET_KEY'])
    return jsonify({'token': token})

# Route for admin access
@app.route('/admin', methods=['GET'])
@role_required(Role.ADMIN)
def admin_area():
    return jsonify({'message': 'Welcome to the admin area!'})

# Route for teacher access
@app.route('/teacher', methods=['GET'])
@role_required(Role.TEACHER)
def teacher_area():
    return jsonify({'message': 'Welcome to the teacher area!'})

# Route for student access
@app.route('/student', methods=['GET'])
@role_required(Role.STUDENT)
def student_area():
    return jsonify({'message': 'Welcome to the student area!'})

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
