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

**School Event and Facility Management API**
=============================================

**Dependencies**
---------------

* Flask 2.0.3
* Flask-SQLAlchemy 2.5.1
* Flask-Marshmallow 0.14.0
* Python 3.9+

**Models**
----------

```python
# models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Event(db.Model):
    """Event model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_time = db.Column(db.DateTime, nullable=False)
    facility_id = db.Column(db.Integer, db.ForeignKey('facility.id'), nullable=False)
    digital_resources = db.relationship('DigitalResource', backref='event', lazy=True)

class Facility(db.Model):
    """Facility model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    events = db.relationship('Event', backref='facility', lazy=True)

class DigitalResource(db.Model):
    """DigitalResource model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)

class SmartTeachingMethodology(db.Model):
    """SmartTeachingMethodology model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    events = db.relationship('Event', backref='smart_teaching_methodology', lazy=True, secondary='event_smart_teaching_methodology')

event_smart_teaching_methodology = db.Table('event_smart_teaching_methodology',
                                            db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True),
                                            db.Column('smart_teaching_methodology_id', db.Integer, db.ForeignKey('smart_teaching_methodology.id'), primary_key=True)
                                            )
```

**Schemas**
------------

```python
# schemas.py
from flask_marshmallow import Marshmallow
from models import Event, Facility, DigitalResource, SmartTeachingMethodology

ma = Marshmallow()

class EventSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Event

class FacilitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Facility

class DigitalResourceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DigitalResource

class SmartTeachingMethodologySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SmartTeachingMethodology
```

**API Endpoints**
-----------------

```python
# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, Event, Facility, DigitalResource, SmartTeachingMethodology
from schemas import ma, EventSchema, FacilitySchema, DigitalResourceSchema, SmartTeachingMethodologySchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
db.init_app(app)
ma.init_app(app)

event_schema = EventSchema()
events_schema = EventSchema(many=True)
facility_schema = FacilitySchema()
facilities_schema = FacilitySchema(many=True)
digital_resource_schema = DigitalResourceSchema()
digital_resources_schema = DigitalResourceSchema(many=True)
smart_teaching_methodology_schema = SmartTeachingMethodologySchema()
smart_teaching_methodologies_schema = SmartTeachingMethodologySchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Event Endpoints

@app.route('/events', methods=['GET'])
def get_events():
    """Get all events"""
    events = Event.query.all()
    return jsonify(events_schema.dump(events))

@app.route('/events', methods=['POST'])
def create_event():
    """Create a new event"""
    try:
        data = request.get_json()
        event = Event(name=data['name'], description=data['description'], start_time=data['start_time'], end_time=data['end_time'], facility_id=data['facility_id'])
        db.session.add(event)
        db.session.commit()
        return jsonify(event_schema.dump(event)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    """Get an event by ID"""
    event = Event.query.get(event_id)
    if event:
        return jsonify(event_schema.dump(event))
    else:
        return jsonify({'error': 'Event not found'}), 404

@app.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    """Update an event"""
    try:
        event = Event.query.get(event_id)
        if event:
            data = request.get_json()
            event.name = data['name']
            event.description = data['description']
            event.start_time = data['start_time']
            event.end_time = data['end_time']
            event.facility_id = data['facility_id']
            db.session.commit()
            return jsonify(event_schema.dump(event))
        else:
            return jsonify({'error': 'Event not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    """Delete an event"""
    event = Event.query.get(event_id)
    if event:
        db.session.delete(event)
        db.session.commit()
        return jsonify({'message': 'Event deleted'})
    else:
        return jsonify({'error': 'Event not found'}), 404

# Facility Endpoints

@app.route('/facilities', methods=['GET'])
def get_facilities():
    """Get all facilities"""
    facilities = Facility.query.all()
    return jsonify(facilities_schema.dump(facilities))

@app.route('/facilities', methods=['POST'])
def create_facility():
    """Create a new facility"""
    try:
        data = request.get_json()
        facility = Facility(name=data['name'], capacity=data['capacity'])
        db.session.add(facility)
        db.session.commit()
        return jsonify(facility_schema.dump(facility)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/facilities/<int:facility_id>', methods=['GET'])
def get_facility(facility_id):
    """Get a facility by ID"""
    facility = Facility.query.get(facility_id)
    if facility:
        return jsonify(facility_schema.dump(facility))
    else:
        return jsonify({'error': 'Facility not found'}), 404

@app.route('/facilities/<int:facility_id>', methods=['PUT'])
def update_facility(facility_id):
    """Update a facility"""
    try:
        facility = Facility.query.get(facility_id)
        if facility:
            data = request.get_json()
            facility.name = data['name']
            facility.capacity = data['capacity']
            db.session.commit()
            return jsonify(facility_schema.dump(facility))
        else:
            return jsonify({'error': 'Facility not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/facilities/<int:facility_id>', methods=['DELETE'])
def delete_facility(facility_id):
    """Delete a facility"""
    facility = Facility.query.get(facility_id)
    if facility:
        db.session.delete(facility)
        db.session.commit()
        return jsonify({'message': 'Facility deleted'})
    else:
        return jsonify({'error': 'Facility not found'}), 404

# Digital Resource Endpoints

@app.route('/digital-resources', methods=['GET'])
def get_digital_resources():
    """Get all digital resources"""
    digital_resources = DigitalResource.query.all()
    return jsonify(digital_resources_schema.dump(digital_resources))

@app.route('/digital-resources', methods=['POST'])
def create_digital_resource():
    """Create a new digital resource"""
    try:
        data = request.get_json()
        digital_resource = DigitalResource(name=data['name'], url=data['url'], event_id=data['event_id'])
        db.session.add(digital_resource)
        db.session.commit()
        return jsonify(digital_resource_schema.dump(digital_resource)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/digital-resources/<int:digital_resource_id>', methods=['GET'])
def get_digital_resource(digital_resource_id):
    """Get a digital resource by ID"""
    digital_resource = DigitalResource.query.get(digital_resource_id)
    if digital_resource:
        return jsonify(digital_resource_schema.dump(digital_resource))
    else:
        return jsonify({'error': 'Digital resource not found'}), 404

@app.route('/digital-resources/<int:digital_resource_id>', methods=['PUT'])
def update_digital_resource(digital_resource_id):
    """Update a digital resource"""
    try:
        digital_resource = DigitalResource.query.get(digital_resource_id)
        if digital_resource:
            data = request.get_json()
            digital_resource.name = data['name']
            digital_resource.url = data['url']
            digital_resource.event_id = data['event_id']
            db.session.commit
