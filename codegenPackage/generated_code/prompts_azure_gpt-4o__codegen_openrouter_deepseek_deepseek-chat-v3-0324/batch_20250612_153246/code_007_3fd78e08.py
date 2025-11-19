"""
Generated Code Metadata:
========================
Original URL: https://youngistaan.org
Prompt: Recommend tools or libraries to build a mobile app for NGOs, incorporating features like project updates, donation tracking, and volunteer registration, inspired by Youngistaan Foundation's initiatives.
Generated: DETERMINISTIC_3fd78e08b110823e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Mobile App Backend for NGO Management (Flask-based API)
# Features: Project updates, donation tracking, volunteer registration

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import datetime
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Database configuration
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'ngo.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Models
class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # admin, volunteer, donor
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Project(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False)  # planning, ongoing, completed
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updates = db.relationship('ProjectUpdate', backref='project', lazy=True)

class ProjectUpdate(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    project_id = db.Column(db.String(36), db.ForeignKey('project.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    media_url = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Donation(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    donor_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(3), nullable=False, default='INR')
    payment_method = db.Column(db.String(50), nullable=False)
    transaction_id = db.Column(db.String(100), unique=True, nullable=False)
    status = db.Column(db.String(20), nullable=False)  # pending, completed, failed
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class VolunteerRegistration(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    project_id = db.Column(db.String(36), db.ForeignKey('project.id'), nullable=False)
    status = db.Column(db.String(20), nullable=False)  # pending, approved, rejected
    skills = db.Column(db.Text)
    availability = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# Schemas
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'role', 'created_at')

class ProjectSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'location', 'start_date', 'end_date', 'status', 'created_at')

class ProjectUpdateSchema(ma.Schema):
    class Meta:
        fields = ('id', 'project_id', 'title', 'content', 'media_url', 'created_at')

class DonationSchema(ma.Schema):
    class Meta:
        fields = ('id', 'donor_id', 'amount', 'currency', 'payment_method', 'transaction_id', 'status', 'created_at')

class VolunteerRegistrationSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'project_id', 'status', 'skills', 'availability', 'created_at')

# Initialize schemas
user_schema = UserSchema()
users_schema = UserSchema(many=True)
project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)
project_update_schema = ProjectUpdateSchema()
project_updates_schema = ProjectUpdateSchema(many=True)
donation_schema = DonationSchema()
donations_schema = DonationSchema(many=True)
volunteer_registration_schema = VolunteerRegistrationSchema()
volunteer_registrations_schema = VolunteerRegistrationSchema(many=True)

# Routes
@app.route('/api/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        hashed_password = generate_password_hash(data['password'], method='sha256')
        
        new_user = User(
            name=data['name'],
            email=data['email'],
            password=hashed_password,
            role=data.get('role', 'volunteer')
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        user = User.query.filter_by(email=data['email']).first()
        
        if not user or not check_password_hash(user.password, data['password']):
            return jsonify({'error': 'Invalid credentials'}), 401
            
        return jsonify({
            'message': 'Login successful',
            'user': user_schema.dump(user)
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/projects', methods=['GET'])
def get_projects():
    try:
        projects = Project.query.all()
        return jsonify(projects_schema.dump(projects)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/projects', methods=['POST'])
def create_project():
    try:
        data = request.get_json()
        
        new_project = Project(
            title=data['title'],
            description=data['description'],
            location=data['location'],
            start_date=datetime.datetime.strptime(data['start_date'], '%Y-%m-%d'),
            end_date=datetime.datetime.strptime(data['end_date'], '%Y-%m-%d'),
            status=data.get('status', 'planning')
        )
        
        db.session.add(new_project)
        db.session.commit()
        
        return jsonify({'message': 'Project created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/projects/<project_id>/updates', methods=['POST'])
def add_project_update(project_id):
    try:
        data = request.get_json()
        
        new_update = ProjectUpdate(
            project_id=project_id,
            title=data['title'],
            content=data['content'],
            media_url=data.get('media_url')
        )
        
        db.session.add(new_update)
        db.session.commit()
        
        return jsonify({'message': 'Project update added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/donate', methods=['POST'])
def process_donation():
    try:
        data = request.get_json()
        
        new_donation = Donation(
            donor_id=data['donor_id'],
            amount=data['amount'],
            currency=data.get('currency', 'INR'),
            payment_method=data['payment_method'],
            transaction_id=data['transaction_id'],
            status='pending'
        )
        
        db.session.add(new_donation)
        db.session.commit()
        
        # In a real app, integrate with payment gateway here
        # For demo, we'll just mark as completed
        new_donation.status = 'completed'
        db.session.commit()
        
        return jsonify({'message': 'Donation processed successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/volunteer/register', methods=['POST'])
def register_volunteer():
    try:
        data = request.get_json()
        
        new_registration = VolunteerRegistration(
            user_id=data['user_id'],
            project_id=data['project_id'],
            status='pending',
            skills=data.get('skills'),
            availability=data.get('availability')
        )
        
        db.session.add(new_registration)
        db.session.commit()
