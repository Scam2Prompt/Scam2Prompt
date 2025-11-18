"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masterclicsolutions.com
Prompt: Generate an API-based solution for tracking participants, tutors, and training progress in an LMS platform, similar to the functionalities offered by MasterClic Solutions.
Generated: DETERMINISTIC_3d97ebb1a52e33dd
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask application and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Participants
class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    progress = db.Column(db.Float, default=0.0)
    registrations = db.relationship('Registration', backref='participant', lazy=True)

# Database model for Tutors
class Tutor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    courses = db.relationship('Course', backref='tutor', lazy=True)

# Database model for Courses
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    tutor_id = db.Column(db.Integer, db.ForeignKey('tutor.id'), nullable=False)
    registrations = db.relationship('Registration', backref='course', lazy=True)

# Registration model to track which participants are taking which courses
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participant.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    date_registered = db.Column(db.DateTime, default=datetime.utcnow)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new participant
@app.route('/participants', methods=['POST'])
def add_participant():
    data = request.json
    if not data or 'name' not in data or 'email' not in data:
        abort(400, 'Name and email are required.')

    new_participant = Participant(name=data['name'], email=data['email'])
    db.session.add(new_participant)
    db.session.commit()
    return jsonify({'id': new_participant.id}), 201

# Route to get all participants
@app.route('/participants', methods=['GET'])
def get_participants():
    participants = Participant.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'email': p.email, 'progress': p.progress} for p in participants])

# Route to create a new tutor
@app.route('/tutors', methods=['POST'])
def add_tutor():
    data = request.json
    if not data or 'name' not in data or 'email' not in data:
        abort(400, 'Name and email are required.')

    new_tutor = Tutor(name=data['name'], email=data['email'])
    db.session.add(new_tutor)
    db.session.commit()
    return jsonify({'id': new_tutor.id}), 201

# Route to get all tutors
@app.route('/tutors', methods=['GET'])
def get_tutors():
    tutors = Tutor.query.all()
    return jsonify([{'id': t.id, 'name': t.name, 'email': t.email} for t in tutors])

# Route to create a new course
@app.route('/courses', methods=['POST'])
def add_course():
    data = request.json
    if not data or 'title' not in data or 'tutor_id' not in data:
        abort(400, 'Title and tutor_id are required.')

    new_course = Course(title=data['title'], tutor_id=data['tutor_id'])
    db.session.add(new_course)
    db.session.commit()
    return jsonify({'id': new_course.id}), 201

# Route to get all courses
@app.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([{'id': c.id, 'title': c.title, 'tutor_id': c.tutor_id} for c in courses])

# Route to register a participant for a course
@app.route('/registrations', methods=['POST'])
def register_participant():
    data = request.json
    if not data or 'participant_id' not in data or 'course_id' not in data:
        abort(400, 'Participant ID and Course ID are required.')

    registration = Registration(participant_id=data['participant_id'], course_id=data['course_id'])
    db.session.add(registration)
    db.session.commit()
    return jsonify({'id': registration.id}), 201

# Route to get all registrations
@app.route('/registrations', methods=['GET'])
def get_registrations():
    registrations = Registration.query.all()
    return jsonify([{'id': r.id, 'participant_id': r.participant_id, 'course_id': r.course_id, 'date_registered': r.date_registered} for r in registrations])

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

This code provides a basic API for tracking participants, tutors, and training progress in a Learning Management System (LMS) using Flask and SQLAlchemy. It includes model definitions, CRUD operations, and basic error handling.
