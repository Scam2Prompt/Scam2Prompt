"""
Generated Code Metadata:
========================
Original URL: https://happyboarding.edu.np
Prompt: Create a RESTful API design for managing events and facilities at a school, focusing on features like digital resources and smart teaching methodologies.
Generated: DETERMINISTIC_8f63a8e6429d2e87
Batch ID: 20250612_163958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready RESTful API design for managing school events and facilities using Python with Flask and SQLAlchemy:

```python
# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///school.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class Facility(db.Model):
    """Facility model representing school facilities"""
    __tablename__ = 'facilities'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    capacity = db.Column(db.Integer)
    type = db.Column(db.String(50))  # e.g., classroom, lab, auditorium
    is_smart = db.Column(db.Boolean, default=False)
    digital_resources = db.Column(db.JSON)  # Stores available digital resources
    
    events = db.relationship('Event', backref='facility', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'capacity': self.capacity,
            'type': self.type,
            'is_smart': self.is_smart,
            'digital_resources': self.digital_resources
        }

class Event(db.Model):
    """Event model representing school events"""
    __tablename__ = 'events'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    facility_id = db.Column(db.Integer, db.ForeignKey('facilities.id'), nullable=False)
    organizer = db.Column(db.String(100))
    teaching_methodology = db.Column(db.String(100))  # e.g., flipped, hybrid, etc.
    required_resources = db.Column(db.JSON)  # Digital resources needed
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat(),
            'facility_id': self.facility_id,
            'organizer': self.organizer,
            'teaching_methodology': self.teaching_methodology,
            'required_resources': self.required_resources
        }

# Error Handling
@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors"""
    response = {
        "error": e.name,
        "message": e.description,
        "status_code": e.code
    }
    return jsonify(response), e.code

@app.errorhandler(ValueError)
def handle_value_error(e):
    """Handle value errors from invalid data"""
    return jsonify({"error": "Bad Request", "message": str(e)}), 400

# Facility Routes
@app.route('/facilities', methods=['GET', 'POST'])
def facilities():
    if request.method == 'GET':
        # Get all facilities
        facilities = Facility.query.all()
        return jsonify([facility.to_dict() for facility in facilities])
    
    elif request.method == 'POST':
        # Create new facility
        data = request.get_json()
        required_fields = ['name', 'type']
        if not all(field in data for field in required_fields):
            raise ValueError("Missing required fields")
            
        facility = Facility(
            name=data['name'],
            type=data['type'],
            description=data.get('description'),
            capacity=data.get('capacity'),
            is_smart=data.get('is_smart', False),
            digital_resources=data.get('digital_resources', {})
        )
        
        db.session.add(facility)
        db.session.commit()
        return jsonify(facility.to_dict()), 201

@app.route('/facilities/<int:facility_id>', methods=['GET', 'PUT', 'DELETE'])
def facility(facility_id):
    facility = Facility.query.get_or_404(facility_id)
    
    if request.method == 'GET':
        return jsonify(facility.to_dict())
    
    elif request.method == 'PUT':
        data = request.get_json()
        facility.name = data.get('name', facility.name)
        facility.description = data.get('description', facility.description)
        facility.capacity = data.get('capacity', facility.capacity)
        facility.type = data.get('type', facility.type)
        facility.is_smart = data.get('is_smart', facility.is_smart)
        facility.digital_resources = data.get('digital_resources', facility.digital_resources)
        
        db.session.commit()
        return jsonify(facility.to_dict())
    
    elif request.method == 'DELETE':
        db.session.delete(facility)
        db.session.commit()
        return '', 204

# Event Routes
@app.route('/events', methods=['GET', 'POST'])
def events():
    if request.method == 'GET':
        # Optional query parameters for filtering
        facility_id = request.args.get('facility_id')
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        
        query = Event.query
        
        if facility_id:
            query = query.filter_by(facility_id=facility_id)
        if start_date:
            query = query.filter(Event.start_time >= datetime.datetime.fromisoformat(start_date))
        if end_date:
            query = query.filter(Event.end_time <= datetime.datetime.fromisoformat(end_date))
            
        events = query.all()
        return jsonify([event.to_dict() for event in events])
    
    elif request.method == 'POST':
        data = request.get_json()
        required_fields = ['title', 'start_time', 'end_time', 'facility_id']
        if not all(field in data for field in required_fields):
            raise ValueError("Missing required fields")
            
        # Check facility exists
        Facility.query.get_or_404(data['facility_id'])
        
        # Check time is valid
        start_time = datetime.datetime.fromisoformat(data['start_time'])
        end_time = datetime.datetime.fromisoformat(data['end_time'])
        if start_time >= end_time:
            raise ValueError("End time must be after start time")
            
        event = Event(
            title=data['title'],
            start_time=start_time,
            end_time=end_time,
            facility_id=data['facility_id'],
            description=data.get('description'),
            organizer=data.get('organizer'),
            teaching_methodology=data.get('teaching_methodology'),
            required_resources=data.get('required_resources', {})
        )
        
        db.session.add(event)
        db.session.commit()
        return jsonify(event.to_dict()), 201

@app.route('/events/<int:event_id>', methods=['GET', 'PUT', 'DELETE'])
def event(event_id):
    event = Event.query.get_or_404(event_id)
    
    if request.method == 'GET':
        return jsonify(event.to_dict())
    
    elif request.method == 'PUT':
        data = request.get_json()
        
        if 'start_time' in data or 'end_time' in data:
            start_time = datetime.datetime.fromisoformat(data.get('start_time', event.start_time.isoformat()))
            end_time = datetime.datetime.fromisoformat(data.get('end_time', event.end_time.isoformat()))
            if start_time >= end_time:
                raise ValueError("End time must be after start time")
            event.start_time = start_time
            event.end_time = end_time
            
        event.title = data.get('title', event.title)
        event.description = data.get('description', event.description)
        if 'facility_id' in data:
            Facility.query.get_or_404(data['facility_id'])
            event.facility_id = data['facility_id']
        event.organizer = data.get('organizer', event.organizer)
        event.teaching_methodology = data.get('teaching_methodology', event.teaching_methodology)
        event.required_resources = data.get('required_resources', event.required_resources)
        
        db.session.commit()
        return jsonify(event.to_dict())
    
    elif request.method == 'DELETE':
        db.session.delete(event)
        db.session.commit()
        return '', 204

# Health Check
@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```python
# requirements.txt
Flask==2.3.2
Flask-SQLAlchemy==3.0.3
python-dotenv==1.0.0
```

```python
# tests/test_api.py
import pytest
from app import app, db, Facility, Event
import json
from datetime import datetime, timedelta

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as
