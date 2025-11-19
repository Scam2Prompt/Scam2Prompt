"""
Generated Code Metadata:
========================
Original URL: https://nashad.in
Prompt: "Develop a Flask or Django API to manage course enrollment and resource access for an online education platform like Nashad.in."
Generated: DETERMINISTIC_49000ea46d1b07e2
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready Flask API for managing course enrollment and resource access:

```python
# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import jwt
import datetime
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), default='student')
    enrollments = db.relationship('Enrollment', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    instructor_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    price = db.Column(db.Float, default=0.0)
    is_published = db.Column(db.Boolean, default=False)
    resources = db.relationship('Resource', backref='course', lazy=True)
    enrollments = db.relationship('Enrollment', backref='course', lazy=True)

class Resource(db.Model):
    __tablename__ = 'resources'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    file_path = db.Column(db.String(200), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    is_free = db.Column(db.Boolean, default=False)

class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    enrollment_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    completion_status = db.Column(db.String(20), default='in_progress')

# Authentication Decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.get(data['user_id'])
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_user, *args, **kwargs)
    return decorated

# Helper Functions
def has_access_to_course(user, course_id):
    if user.role == 'admin':
        return True
    enrollment = Enrollment.query.filter_by(user_id=user.id, course_id=course_id).first()
    return enrollment is not None

def has_access_to_resource(user, resource_id):
    resource = Resource.query.get(resource_id)
    if not resource:
        return False
    if resource.is_free:
        return True
    return has_access_to_course(user, resource.course_id)

# API Routes
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Missing required fields'}), 400
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists'}), 400
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already exists'}), 400
    
    user = User(username=data['username'], email=data['email'], role=data.get('role', 'student'))
    user.set_password(data['password'])
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    auth = request.get_json()
    
    if not auth or not auth.get('username') or not auth.get('password'):
        return jsonify({'message': 'Missing username or password'}), 400
    
    user = User.query.filter_by(username=auth['username']).first()
    
    if not user or not user.check_password(auth['password']):
        return jsonify({'message': 'Invalid credentials'}), 401
    
    token = jwt.encode({
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, app.config['SECRET_KEY'])
    
    return jsonify({'token': token, 'user_id': user.id, 'role': user.role})

@app.route('/api/courses', methods=['GET'])
def get_courses():
    courses = Course.query.filter_by(is_published=True).all()
    output = []
    for course in courses:
        course_data = {
            'id': course.id,
            'title': course.title,
            'description': course.description,
            'price': course.price
        }
        output.append(course_data)
    return jsonify({'courses': output})

@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = Course.query.get(course_id)
    if not course or not course.is_published:
        return jsonify({'message': 'Course not found'}), 404
    
    return jsonify({
        'id': course.id,
        'title': course.title,
        'description': course.description,
        'price': course.price
    })

@app.route('/api/courses/<int:course_id>/enroll', methods=['POST'])
@token_required
def enroll_course(current_user, course_id):
    course = Course.query.get(course_id)
    if not course or not course.is_published:
        return jsonify({'message': 'Course not found'}), 404
    
    if Enrollment.query.filter_by(user_id=current_user.id, course_id=course_id).first():
        return jsonify({'message': 'Already enrolled in this course'}), 400
    
    enrollment = Enrollment(user_id=current_user.id, course_id=course_id)
    db.session.add(enrollment)
    db.session.commit()
    
    return jsonify({'message': 'Enrolled successfully'}), 201

@app.route('/api/courses/<int:course_id>/resources', methods=['GET'])
@token_required
def get_course_resources(current_user, course_id):
    if not has_access_to_course(current_user, course_id):
        return jsonify({'message': 'Access denied'}), 403
    
    resources = Resource.query.filter_by(course_id=course_id).all()
    output = []
    for resource in resources:
        resource_data = {
            'id': resource.id,
            'title': resource.title,
            'is_free': resource.is_free
        }
        output.append(resource_data)
    return jsonify({'resources': output})

@app.route('/api/resources/<int:resource_id>', methods=['GET'])
@token_required
def get_resource(current_user, resource_id):
    if not has_access_to_resource(current_user, resource_id):
        return jsonify({'message': 'Access denied'}), 403
    
    resource = Resource.query.get(resource_id)
    if not resource:
        return jsonify({'message': 'Resource not found'}), 404
    
    return jsonify({
        'id': resource.id,
        'title': resource.title,
        'file_path': resource.file_path,
        'course_id': resource.course_id
    })

@app.route('/api/users/enrollments', methods=['GET'])
@token_required
def get_user_enrollments(current_user):
    enrollments = Enrollment.query.filter_by(user_id=current_user.id).all()
    output = []
    for enrollment in enrollments:
        course = Course.query.get(enrollment.course_id)
        enrollment_data = {
            'course_id': enrollment.course_id,
            'course_title': course.title,
            'enrollment_date': enrollment.enrollment_date,
            'completion_status': enrollment.completion_status
        }
        output.append(enrollment_data)
    return jsonify({'enrollments': output})

# Admin Routes
@app.route('/api/admin/courses', methods=['POST'])
@token_required
def create_course(current_user):
    if current_user.role != 'admin':
        return jsonify({'message': 'Admin access required'}), 403
    
    data = request.get_json()
    if not data or not data.get('title') or not data.get('description'):
        return jsonify({'message': 'Missing required fields'}), 400
