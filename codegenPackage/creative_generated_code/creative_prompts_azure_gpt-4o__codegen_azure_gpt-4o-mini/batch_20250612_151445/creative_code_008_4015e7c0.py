"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trentino.edu.pe
Prompt: Develop a web application for managing workshops and events, inspired by the "Cursos - Talleres" and "Eventos" sections of the Trentino website.
Generated: DETERMINISTIC_4015e7c00f1c3794
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workshops_events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Workshop model
class Workshop(db.Model):
    """Database model for workshops."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100), nullable=False)

# Define the Event model
class Event(db.Model):
    """Database model for events."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100), nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

# Define the Workshop Schema for validation
class WorkshopSchema(Schema):
    """Schema for validating workshop input data."""
    title = fields.String(required=True)
    description = fields.String(required=True)
    date = fields.DateTime(required=True)
    location = fields.String(required=True)

# Define the Event Schema for validation
class EventSchema(Schema):
    """Schema for validating event input data."""
    title = fields.String(required=True)
    description = fields.String(required=True)
    date = fields.DateTime(required=True)
    location = fields.String(required=True)

# Route for creating a new workshop
@app.route('/workshops', methods=['POST'])
def create_workshop():
    """Create a new workshop."""
    schema = WorkshopSchema()
    try:
        data = schema.load(request.json)
        workshop = Workshop(**data)
        db.session.add(workshop)
        db.session.commit()
        return jsonify({"message": "Workshop created successfully.", "workshop": data}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for creating a new event
@app.route('/events', methods=['POST'])
def create_event():
    """Create a new event."""
    schema = EventSchema()
    try:
        data = schema.load(request.json)
        event = Event(**data)
        db.session.add(event)
        db.session.commit()
        return jsonify({"message": "Event created successfully.", "event": data}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for listing workshops
@app.route('/workshops', methods=['GET'])
def get_workshops():
    """Get a list of all workshops."""
    workshops = Workshop.query.all()
    return jsonify([{"id": w.id, "title": w.title, "description": w.description,
                     "date": w.date.isoformat(), "location": w.location} for w in workshops])

# Route for listing events
@app.route('/events', methods=['GET'])
def get_events():
    """Get a list of all events."""
    events = Event.query.all()
    return jsonify([{"id": e.id, "title": e.title, "description": e.description,
                     "date": e.date.isoformat(), "location": e.location} for e in events])

# Main entry point of the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- This code creates a simple Flask web application using SQLAlchemy for the database.
- It provides endpoints to create and retrieve workshops and events.
- Input validation is done using Marshmallow schemas.
- Error handling is included for various scenarios.
