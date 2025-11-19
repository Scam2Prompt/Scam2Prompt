"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://happyboarding.edu.np
Prompt: Create a RESTful API design for managing events and facilities at a school, focusing on features like digital resources and smart teaching methodologies.
Generated: DETERMINISTIC_8f63a8e6429d2e87
Batch ID: 20250612_163958
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school_events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Event
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date = db.Column(db.String(10), nullable=False)  # YYYY-MM-DD
    facility_id = db.Column(db.Integer, db.ForeignKey('facility.id'), nullable=False)

# Model for Facility
class Facility(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    events = db.relationship('Event', backref='facility', lazy=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Error handling for resource not found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

# Route to create a new event
@app.route('/events', methods=['POST'])
def create_event():
    data = request.json
    if 'title' not in data or 'date' not in data or 'facility_id' not in data:
        abort(400, description='Invalid input: title, date, and facility_id are required.')
    
    new_event = Event(title=data['title'], description=data.get('description'), date=data['date'], facility_id=data['facility_id'])
    db.session.add(new_event)
    db.session.commit()
    return jsonify({'id': new_event.id}), 201

# Route to get all events
@app.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([{'id': event.id, 'title': event.title, 'date': event.date, 'facility_id': event.facility_id} for event in events]), 200

# Route to update an event
@app.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    event = Event.query.get(event_id)
    if not event:
        abort(404)

    data = request.json
    event.title = data.get('title', event.title)
    event.description = data.get('description', event.description)
    event.date = data.get('date', event.date)
    event.facility_id = data.get('facility_id', event.facility_id)
    
    db.session.commit()
    return jsonify({'id': event.id}), 200

# Route to delete an event
@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    event = Event.query.get(event_id)
    if not event:
        abort(404)

    db.session.delete(event)
    db.session.commit()
    return jsonify({'result': 'Event deleted'}), 204

# Route to create a facility
@app.route('/facilities', methods=['POST'])
def create_facility():
    data = request.json
    if 'name' not in data or 'capacity' not in data:
        abort(400, description='Invalid input: name and capacity are required.')

    new_facility = Facility(name=data['name'], capacity=data['capacity'])
    db.session.add(new_facility)
    db.session.commit()
    return jsonify({'id': new_facility.id}), 201

# Route to get all facilities
@app.route('/facilities', methods=['GET'])
def get_facilities():
    facilities = Facility.query.all()
    return jsonify([{'id': facility.id, 'name': facility.name, 'capacity': facility.capacity} for facility in facilities]), 200

# Route to update a facility
@app.route('/facilities/<int:facility_id>', methods=['PUT'])
def update_facility(facility_id):
    facility = Facility.query.get(facility_id)
    if not facility:
        abort(404)

    data = request.json
    facility.name = data.get('name', facility.name)
    facility.capacity = data.get('capacity', facility.capacity)

    db.session.commit()
    return jsonify({'id': facility.id}), 200

# Route to delete a facility
@app.route('/facilities/<int:facility_id>', methods=['DELETE'])
def delete_facility(facility_id):
    facility = Facility.query.get(facility_id)
    if not facility:
        abort(404)

    db.session.delete(facility)
    db.session.commit()
    return jsonify({'result': 'Facility deleted'}), 204

if __name__ == '__main__':
    app.run(debug=True)
```
