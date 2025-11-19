"""
Generated Code Metadata:
========================
Original URL: https://uni4kashmir.com
Prompt: Create a RESTful API design for a university system that includes modules for donations, course offerings, and community involvement, inspired by the structure of Uni4Kashmir.
Generated: DETERMINISTIC_16ef4029660de25c
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**University System RESTful API**
=====================================

### Donations Module

```python
# donations.py
from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy

donations_blueprint = Blueprint('donations', __name__)
db = SQLAlchemy()

class Donation(db.Model):
    """Donation Model"""
    id = db.Column(db.Integer, primary_key=True)
    donor_name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

@donations_blueprint.route('/donations', methods=['POST'])
def create_donation():
    """Create a new donation"""
    try:
        data = request.get_json()
        donation = Donation(donor_name=data['donor_name'], amount=data['amount'], date=data['date'])
        db.session.add(donation)
        db.session.commit()
        return jsonify({'message': 'Donation created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@donations_blueprint.route('/donations', methods=['GET'])
def get_donations():
    """Get all donations"""
    try:
        donations = Donation.query.all()
        output = []
        for donation in donations:
            donation_data = {'id': donation.id, 'donor_name': donation.donor_name, 'amount': donation.amount, 'date': donation.date}
            output.append(donation_data)
        return jsonify({'donations': output})
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@donations_blueprint.route('/donations/<id>', methods=['GET'])
def get_donation(id):
    """Get a donation by id"""
    try:
        donation = Donation.query.get(id)
        if donation is None:
            return jsonify({'message': 'Donation not found'}), 404
        donation_data = {'id': donation.id, 'donor_name': donation.donor_name, 'amount': donation.amount, 'date': donation.date}
        return jsonify({'donation': donation_data})
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@donations_blueprint.route('/donations/<id>', methods=['PUT'])
def update_donation(id):
    """Update a donation"""
    try:
        donation = Donation.query.get(id)
        if donation is None:
            return jsonify({'message': 'Donation not found'}), 404
        data = request.get_json()
        donation.donor_name = data.get('donor_name', donation.donor_name)
        donation.amount = data.get('amount', donation.amount)
        donation.date = data.get('date', donation.date)
        db.session.commit()
        return jsonify({'message': 'Donation updated successfully'})
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@donations_blueprint.route('/donations/<id>', methods=['DELETE'])
def delete_donation(id):
    """Delete a donation"""
    try:
        donation = Donation.query.get(id)
        if donation is None:
            return jsonify({'message': 'Donation not found'}), 404
        db.session.delete(donation)
        db.session.commit()
        return jsonify({'message': 'Donation deleted successfully'})
    except Exception as e:
        return jsonify({'message': str(e)}), 400
```

### Course Offerings Module

```python
# courses.py
from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy

courses_blueprint = Blueprint('courses', __name__)
db = SQLAlchemy()

class Course(db.Model):
    """Course Model"""
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100), nullable=False)
    course_code = db.Column(db.String(20), nullable=False)
    credits = db.Column(db.Integer, nullable=False)

@courses_blueprint.route('/courses', methods=['POST'])
def create_course():
    """Create a new course"""
    try:
        data = request.get_json()
        course = Course(course_name=data['course_name'], course_code=data['course_code'], credits=data['credits'])
        db.session.add(course)
        db.session.commit()
        return jsonify({'message': 'Course created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@courses_blueprint.route('/courses', methods=['GET'])
def get_courses():
    """Get all courses"""
    try:
        courses = Course.query.all()
        output = []
        for course in courses:
            course_data = {'id': course.id, 'course_name': course.course_name, 'course_code': course.course_code, 'credits': course.credits}
            output.append(course_data)
        return jsonify({'courses': output})
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@courses_blueprint.route('/courses/<id>', methods=['GET'])
def get_course(id):
    """Get a course by id"""
    try:
        course = Course.query.get(id)
        if course is None:
            return jsonify({'message': 'Course not found'}), 404
        course_data = {'id': course.id, 'course_name': course.course_name, 'course_code': course.course_code, 'credits': course.credits}
        return jsonify({'course': course_data})
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@courses_blueprint.route('/courses/<id>', methods=['PUT'])
def update_course(id):
    """Update a course"""
    try:
        course = Course.query.get(id)
        if course is None:
            return jsonify({'message': 'Course not found'}), 404
        data = request.get_json()
        course.course_name = data.get('course_name', course.course_name)
        course.course_code = data.get('course_code', course.course_code)
        course.credits = data.get('credits', course.credits)
        db.session.commit()
        return jsonify({'message': 'Course updated successfully'})
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@courses_blueprint.route('/courses/<id>', methods=['DELETE'])
def delete_course(id):
    """Delete a course"""
    try:
        course = Course.query.get(id)
        if course is None:
            return jsonify({'message': 'Course not found'}), 404
        db.session.delete(course)
        db.session.commit()
        return jsonify({'message': 'Course deleted successfully'})
    except Exception as e:
        return jsonify({'message': str(e)}), 400
```

### Community Involvement Module

```python
# community.py
from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy

community_blueprint = Blueprint('community', __name__)
db = SQLAlchemy()

class Event(db.Model):
    """Event Model"""
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(100), nullable=False)
    event_date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100), nullable=False)

@community_blueprint.route('/events', methods=['POST'])
def create_event():
    """Create a new event"""
    try:
        data = request.get_json()
        event = Event(event_name=data['event_name'], event_date=data['event_date'], location=data['location'])
        db.session.add(event)
        db.session.commit()
        return jsonify({'message': 'Event created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@community_blueprint.route('/events', methods=['GET'])
def get_events():
    """Get all events"""
    try:
        events = Event.query.all()
        output = []
        for event in events:
            event_data = {'id': event.id, 'event_name': event.event_name, 'event_date': event.event_date, 'location': event.location}
            output.append(event_data)
        return jsonify({'events': output})
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@community_blueprint.route('/events/<id>', methods=['GET'])
def get_event(id):
    """Get an event by id"""
    try:
        event = Event.query.get(id)
        if event is None:
            return jsonify({'message': 'Event not found'}), 404
        event_data = {'id': event.id, 'event_name': event.event_name, 'event_date': event.event_date, 'location': event.location}
        return jsonify({'event': event_data})
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@community_blueprint.route('/events/<id>', methods=['PUT'])
def update_event(id):
    """Update an event"""
    try:
        event = Event.query.get(id)
        if event is None:
            return jsonify({'message': 'Event not found'}), 404
        data = request.get_json()
        event.event_name = data.get('event_name', event.event_name)
        event.event_date = data.get('event_date', event.event_date)
        event.location = data.get('location', event.location)
        db.session.commit()
        return jsonify({'message': 'Event updated successfully'})
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@community_blueprint.route('/events/<id>', methods=['DELETE'])
def delete_event(id):
    """Delete an event"""
    try:
