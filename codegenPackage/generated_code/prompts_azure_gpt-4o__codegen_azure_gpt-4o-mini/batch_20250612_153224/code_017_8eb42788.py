"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Write code to implement a cloud-based school management system that supports multiple modules and user roles, similar to Him Saral's Cloud-Based System.
Generated: DETERMINISTIC_8eb42788c6174e8b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# school_management_system.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///school.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# User roles
ROLE_ADMIN = 'admin'
ROLE_TEACHER = 'teacher'
ROLE_STUDENT = 'student'

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Course {self.name}>'

# Error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Authentication decorator
def requires_auth(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            auth = request.authorization
            if not auth or not auth.username or not auth.password:
                return jsonify({'error': 'Authentication required'}), 401
            
            user = User.query.filter_by(username=auth.username).first()
            if not user or not check_password_hash(user.password, auth.password):
                return jsonify({'error': 'Invalid credentials'}), 403
            
            if user.role != role:
                return jsonify({'error': 'Access denied'}), 403
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# User registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password') or not data.get('role'):
        return jsonify({'error': 'Missing data'}), 400

    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password, role=data['role'])
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Create a course (admin only)
@app.route('/courses', methods=['POST'])
@requires_auth(ROLE_ADMIN)
def create_course():
    data = request.get_json()
    if not data or not data.get('name') or not data.get('teacher_id'):
        return jsonify({'error': 'Missing data'}), 400

    new_course = Course(name=data['name'], teacher_id=data['teacher_id'])
    
    try:
        db.session.add(new_course)
        db.session.commit()
        return jsonify({'message': 'Course created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Get all courses
@app.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([{'id': course.id, 'name': course.name, 'teacher_id': course.teacher_id} for course in courses]), 200

# Main entry point
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
```

### Instructions for Running the Code
1. Ensure you have Python 3.x installed.
2. Install the required packages:
   ```bash
   pip install Flask Flask-SQLAlchemy Flask-Migrate Werkzeug
   ```
3. Set the environment variable for the database URL if needed:
   ```bash
   export DATABASE_URL='sqlite:///school.db'
   ```
4. Run the application:
   ```bash
   python school_management_system.py
   ```
5. Use tools like Postman or curl to interact with the API.
