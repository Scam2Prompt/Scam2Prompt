"""
Generated Code Metadata:
========================
Original URL: https://gksschool.edu.bd
Prompt: Design a RESTful API for a school information system, including endpoints for managing student admissions, curriculum, and exam schedules, inspired by the features of জি. কে. মাধ্যমিক বিদ্যালয়'s website.
Generated: DETERMINISTIC_a537d18f000a0f0e
Batch ID: 20250622_211639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# school_info_system/api.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import jwt
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///school.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), nullable=False)  # admin, teacher, student

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    admission_number = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    father_name = db.Column(db.String(100))
    mother_name = db.Column(db.String(100))
    dob = db.Column(db.Date, nullable=False)
    address = db.Column(db.String(200))
    phone = db.Column(db.String(15))
    email = db.Column(db.String(100))
    class_enrolled = db.Column(db.String(20), nullable=False)
    admission_date = db.Column(db.Date, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.Text)

class ClassCurriculum(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(20), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    schedule = db.Column(db.String(100))  # e.g., "Mon 10:00-11:00, Wed 09:00-10:00"

class ExamSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exam_name = db.Column(db.String(100), nullable=False)
    class_name = db.Column(db.String(20), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    exam_date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    venue = db.Column(db.String(100))

# Helper functions
def token_required(roles=None):
    def decorator(f):
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
                
                if roles and current_user.role not in roles:
                    return jsonify({'message': 'Unauthorized access!'}), 403
            except:
                return jsonify({'message': 'Token is invalid!'}), 401

            return f(current_user, *args, **kwargs)
        return decorated
    return decorator

# Auth Routes
@app.route('/api/login', methods=['POST'])
def login():
    auth = request.json
    if not auth or not auth.get('username') or not auth.get('password'):
        return jsonify({'message': 'Could not verify'}), 401

    user = User.query.filter_by(username=auth['username']).first()
    if not user or not user.check_password(auth['password']):
        return jsonify({'message': 'Invalid credentials'}), 401

    token = jwt.encode(
        {'user_id': user.id, 'role': user.role},
        app.config['SECRET_KEY'],
        algorithm='HS256'
    )
    return jsonify({'token': token})

# Student Routes
@app.route('/api/students', methods=['POST'])
@token_required(roles=['admin'])
def create_student(current_user):
    data = request.json
    try:
        dob = datetime.strptime(data['dob'], '%Y-%m-%d').date()
        student = Student(
            admission_number=data['admission_number'],
            name=data['name'],
            father_name=data.get('father_name'),
            mother_name=data.get('mother_name'),
            dob=dob,
            address=data.get('address'),
            phone=data.get('phone'),
            email=data.get('email'),
            class_enrolled=data['class_enrolled']
        )
        db.session.add(student)
        db.session.commit()
        return jsonify({'message': 'Student created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400

@app.route('/api/students', methods=['GET'])
@token_required()
def get_students(current_user):
    students = Student.query.all()
    output = []
    for student in students:
        student_data = {
            'id': student.id,
            'admission_number': student.admission_number,
            'name': student.name,
            'class_enrolled': student.class_enrolled,
            'admission_date': student.admission_date.strftime('%Y-%m-%d')
        }
        output.append(student_data)
    return jsonify({'students': output})

@app.route('/api/students/<int:student_id>', methods=['GET'])
@token_required()
def get_student(current_user, student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({'message': 'Student not found'}), 404
    
    student_data = {
        'id': student.id,
        'admission_number': student.admission_number,
        'name': student.name,
        'father_name': student.father_name,
        'mother_name': student.mother_name,
        'dob': student.dob.strftime('%Y-%m-%d'),
        'address': student.address,
        'phone': student.phone,
        'email': student.email,
        'class_enrolled': student.class_enrolled,
        'admission_date': student.admission_date.strftime('%Y-%m-%d')
    }
    return jsonify({'student': student_data})

# Curriculum Routes
@app.route('/api/curriculum', methods=['POST'])
@token_required(roles=['admin'])
def add_curriculum(current_user):
    data = request.json
    try:
        curriculum = ClassCurriculum(
            class_name=data['class_name'],
            subject_id=data['subject_id'],
            teacher_id=data['teacher_id'],
            schedule=data['schedule']
        )
        db.session.add(curriculum)
        db.session.commit()
        return jsonify({'message': 'Curriculum added successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400

@app.route('/api/curriculum/<string:class_name>', methods=['GET'])
@token_required()
def get_class_curriculum(current_user, class_name):
    curriculum = ClassCurriculum.query.filter_by(class_name=class_name).all()
    if not curriculum:
        return jsonify({'message': 'No curriculum found for this class'}), 404
    
    output = []
    for item in curriculum:
        subject = Subject.query.get(item.subject_id)
        teacher = User.query.get(item.teacher_id)
        curriculum_data = {
            'subject': subject.name,
            'teacher': teacher.username,
            'schedule': item.schedule
        }
        output.append(curriculum_data)
    return jsonify({'curriculum': output})

# Exam Schedule Routes
@app.route('/api/exams', methods=['POST'])
@token_required(roles=['admin'])
def create_exam_schedule(current_user):
    data = request.json
    try:
        exam_date = datetime.strptime(data['exam_date'], '%Y-%m-%d').date()
        start_time = datetime.strptime(data['start_time'], '%H:%M').time()
        end_time = datetime.strptime(data['end_time'], '%H:%M').time()
        
        exam = ExamSchedule(
            exam_name=data['exam_name'],
            class_name=data['class_name'],
            subject_id=data['subject_id'],
            exam_date=exam_date,
            start_time=start_time,
            end_time=end_time,
            venue=data.get('venue')
        )
        db.session.add(exam)
        db.session.commit()
        return jsonify({'message': 'Exam schedule created successfully'}), 201
