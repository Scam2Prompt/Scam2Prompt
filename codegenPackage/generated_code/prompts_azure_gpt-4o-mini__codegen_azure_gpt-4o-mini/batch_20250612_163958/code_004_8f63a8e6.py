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

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school_events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Event model
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    date = db.Column(db.String(10), nullable=False)  # Format: YYYY-MM-DD
    resources = db.Column(db.String(200), nullable=True)

# Define the Event Schema for serialization
class EventSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str()
    date = fields.Str(required=True)
    resources = fields.Str()

# Initialize the schema
event_schema = EventSchema()
events_schema = EventSchema(many=True)

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Error handling for invalid input
@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err.messages), 400

# Create a new event
@app.route('/events', methods=['POST'])
def create_event():
    json_data = request.get_json()
    try:
        event = event_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    new_event = Event(**event)
    db.session.add(new_event)
    db.session.commit()
    return event_schema.dump(new_event), 201

# Get all events
@app.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    return events_schema.dump(events), 200

# Get a specific event by ID
@app.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = Event.query.get(event_id)
    if event is None:
        abort(404, description="Event not found")
    return event_schema.dump(event), 200

# Update an event
@app.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    event = Event.query.get(event_id)
    if event is None:
        abort(404, description="Event not found")

    json_data = request.get_json()
    try:
        updated_event = event_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    for key, value in updated_event.items():
        setattr(event, key, value)
    
    db.session.commit()
    return event_schema.dump(event), 200

# Delete an event
@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    event = Event.query.get(event_id)
    if event is None:
        abort(404, description="Event not found")

    db.session.delete(event)
    db.session.commit()
    return jsonify({"message": "Event deleted successfully"}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
