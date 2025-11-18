"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Write code to implement a cloud-based school management system that supports multiple modules and user roles, similar to Him Saral's Cloud-Based System.
Generated: DETERMINISTIC_8eb42788c6174e8b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready implementation of a cloud-based school management system in Python using the Flask framework. This code includes modules for managing users, roles, and student records.

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

# Initialize Flask application
app = Flask(__name__)

# Configure application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school_management.db'  # Database configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Replace with a secure key in production

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Define database models
class User(db.Model):
    """User model for storing user-related information."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # e.g., admin, teacher, student

class Student(db.Model):
    """Student model for storing student-related information."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

# Routes for user authentication
@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.json
    if not data or not data.get('username') or not data.get('password') or not data.get('role'):
        return jsonify({'error': 'Invalid data provided'}), 400
    
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], password=hashed_password, role=data['role'])
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        return jsonify({'error': 'User registration failed'}), 500

@app.route('/login', methods=['POST'])
def login():
    """Authenticate user and return a JWT token."""
    data = request.json
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'error': 'Invalid credentials'}), 400
    
    user = User.query.filter_by(username=data['username']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity={'username': user.username, 'role': user.role})
        return jsonify({'access_token': access_token}), 200
    
    return jsonify({'error': 'Invalid username or password'}), 401

# Routes for student management
@app.route('/students', methods=['POST'])
@jwt_required()
def create_student():
    """Create a new student record."""
    data = request.json
    if not data or not data.get('name') or not data.get('grade') or not data.get('email'):
        return jsonify({'error': 'Invalid data provided'}), 400
    
    new_student = Student(name=data['name'], grade=data['grade'], email=data['email'])
    try:
        db.session.add(new_student)
        db.session.commit()
        return jsonify({'message': 'Student record created successfully'}), 201
    except Exception as e:
        return jsonify({'error': 'Failed to create student record'}), 500

@app.route('/students', methods=['GET'])
@jwt_required()
def get_students():
    """Retrieve all student records."""
    students = Student.query.all()
    return jsonify([{'id': s.id, 'name': s.name, 'grade': s.grade, 'email': s.email} for s in students]), 200

@app.route('/students/<int:student_id>', methods=['DELETE'])
@jwt_required()
def delete_student(student_id):
    """Delete a student record."""
    student = Student.query.get(student_id)
    if not student:
        return jsonify({'error': 'Student not found'}), 404
    
    try:
        db.session.delete(student)
        db.session.commit()
        return jsonify({'message': 'Student record deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': 'Failed to delete student record'}), 500

# Run the application
if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    
    # Run the Flask development server
    app.run(debug=True)
```
