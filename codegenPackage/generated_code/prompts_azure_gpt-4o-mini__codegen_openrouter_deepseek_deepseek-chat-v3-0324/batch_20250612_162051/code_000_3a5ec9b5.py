"""
Generated Code Metadata:
========================
Original URL: https://kiddooplayway.com
Prompt: Write a code snippet for a web application that allows parents to enroll their children in a daycare program like Kiddoo Playway, focusing on features such as activity-based curriculum and parental webinars.
Generated: DETERMINISTIC_3a5ec9b501a1361a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///daycare.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class Parent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    children = db.relationship('Child', backref='parent', lazy=True)
    webinar_registrations = db.relationship('WebinarRegistration', backref='parent', lazy=True)

class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('parent.id'), nullable=False)
    enrollments = db.relationship('Enrollment', backref='child', lazy=True)

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    age_group = db.Column(db.String(50), nullable=False)
    schedule = db.Column(db.String(100), nullable=False)
    enrollments = db.relationship('Enrollment', backref='activity', lazy=True)

class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey('child.id'), nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'), nullable=False)
    enrollment_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Webinar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    speaker = db.Column(db.String(100), nullable=False)
    registrations = db.relationship('WebinarRegistration', backref='webinar', lazy=True)

class WebinarRegistration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('parent.id'), nullable=False)
    webinar_id = db.Column(db.Integer, db.ForeignKey('webinar.id'), nullable=False)
    registration_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# Helper Functions
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

def validate_phone(phone):
    pattern = r'^\+?[0-9]{10,15}$'
    return re.match(pattern, phone)

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register_parent():
    try:
        data = request.get_json()
        
        # Validate input
        if not all(key in data for key in ['name', 'email', 'password', 'phone']):
            return jsonify({'error': 'Missing required fields'}), 400
        
        if not validate_email(data['email']):
            return jsonify({'error': 'Invalid email format'}), 400
        
        if not validate_phone(data['phone']):
            return jsonify({'error': 'Invalid phone number format'}), 400
        
        # Check if email exists
        if Parent.query.filter_by(email=data['email']).first():
            return jsonify({'error': 'Email already registered'}), 409
        
        # Create parent
        parent = Parent(
            name=data['name'],
            email=data['email'],
            password=generate_password_hash(data['password']),
            phone=data['phone']
        )
        
        db.session.add(parent)
        db.session.commit()
        
        return jsonify({'message': 'Parent registered successfully', 'parent_id': parent.id}), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/add_child', methods=['POST'])
def add_child():
    try:
        data = request.get_json()
        
        # Validate input
        if not all(key in data for key in ['parent_id', 'name', 'age']):
            return jsonify({'error': 'Missing required fields'}), 400
        
        if not isinstance(data['age'], int) or data['age'] < 1 or data['age'] > 12:
            return jsonify({'error': 'Age must be between 1 and 12'}), 400
        
        # Check if parent exists
        parent = Parent.query.get(data['parent_id'])
        if not parent:
            return jsonify({'error': 'Parent not found'}), 404
        
        # Create child
        child = Child(
            name=data['name'],
            age=data['age'],
            parent_id=data['parent_id']
        )
        
        db.session.add(child)
        db.session.commit()
        
        return jsonify({'message': 'Child added successfully', 'child_id': child.id}), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/activities', methods=['GET'])
def get_activities():
    try:
        activities = Activity.query.all()
        result = []
        
        for activity in activities:
            result.append({
                'id': activity.id,
                'name': activity.name,
                'description': activity.description,
                'age_group': activity.age_group,
                'schedule': activity.schedule
            })
        
        return jsonify(result), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/enroll', methods=['POST'])
def enroll_child():
    try:
        data = request.get_json()
        
        # Validate input
        if not all(key in data for key in ['child_id', 'activity_id']):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Check if child and activity exist
        child = Child.query.get(data['child_id'])
        if not child:
            return jsonify({'error': 'Child not found'}), 404
        
        activity = Activity.query.get(data['activity_id'])
        if not activity:
            return jsonify({'error': 'Activity not found'}), 404
        
        # Check if already enrolled
        existing_enrollment = Enrollment.query.filter_by(
            child_id=data['child_id'],
            activity_id=data['activity_id']
        ).first()
        
        if existing_enrollment:
            return jsonify({'error': 'Child already enrolled in this activity'}), 409
        
        # Create enrollment
        enrollment = Enrollment(
            child_id=data['child_id'],
            activity_id=data['activity_id']
        )
        
        db.session.add(enrollment)
        db.session.commit()
        
        return jsonify({'message': 'Enrollment successful'}), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/webinars', methods=['GET'])
def get_webinars():
    try:
        webinars = Webinar.query.all()
        result = []
        
        for webinar in webinars:
            result.append({
                'id': webinar.id,
                'title': webinar.title,
                'description': webinar.description,
                'date_time': webinar.date_time.isoformat(),
                'speaker': webinar.speaker
            })
        
        return jsonify(result), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/register_webinar', methods=['POST'])
def register_webinar():
    try:
        data = request.get_json()
        
        # Validate input
        if not all(key in data for key in ['parent_id', 'webinar_id']):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Check if parent and webinar exist
        parent = Parent.query.get(data['parent_id'])
        if not parent:
            return jsonify({'error': 'Parent not found'}), 404
        
        webinar = Webinar.query.get(data['webinar_id'])
        if not webinar:
            return jsonify({'error': 'Webinar not found'}), 404
        
        # Check if already registered
        existing_registration = WebinarRegistration.query.filter_by(
            parent_id=data['parent_id'],
            webinar_id=data['webinar_id']
        ).first()
        
        if existing_registration:
            return jsonify({'error': 'Parent already registered for this webinar'}), 409
        
        # Create registration
        registration = WebinarRegistration(
            parent_id=data['parent_id'],
            webinar_id=data['webinar_id']
        )
        
        db.session.add(registration)
