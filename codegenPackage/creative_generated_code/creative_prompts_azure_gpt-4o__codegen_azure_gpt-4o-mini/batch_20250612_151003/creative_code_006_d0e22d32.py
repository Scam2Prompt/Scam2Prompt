"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daddys-universitys.com
Prompt: Create a REST API for managing workshop and event registrations aimed at community engagement in rural revitalization projects. Include endpoints for event creation, participant registration, and feedback collection.
Generated: DETERMINISTIC_d0e22d3254cd4ec3
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workshops.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String(200))

class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participant.id'), nullable=False)
    comments = db.Column(db.String(300), nullable=False)

# Schemas for validation
class EventSchema(Schema):
    title = fields.String(required=True)
    date = fields.DateTime(required=True)
    description = fields.String()

class ParticipantSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    event_id = fields.Integer(required=True)

class FeedbackSchema(Schema):
    participant_id = fields.Integer(required=True)
    comments = fields.String(required=True)

# Initialize database
with app.app_context():
    db.create_all()

# API Endpoints

@app.route('/events', methods=['POST'])
def create_event():
    """Create a new event."""
    try:
        event_data = request.json
        validated_data = EventSchema().load(event_data)
        new_event = Event(**validated_data)
        db.session.add(new_event)
        db.session.commit()
        return jsonify({"id": new_event.id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/participants', methods=['POST'])
def register_participant():
    """Register a new participant for an event."""
    try:
        participant_data = request.json
        validated_data = ParticipantSchema().load(participant_data)
        new_participant = Participant(**validated_data)
        db.session.add(new_participant)
        db.session.commit()
        return jsonify({"id": new_participant.id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/feedback', methods=['POST'])
def collect_feedback():
    """Collect feedback from a participant."""
    try:
        feedback_data = request.json
        validated_data = FeedbackSchema().load(feedback_data)
        new_feedback = Feedback(**validated_data)
        db.session.add(new_feedback)
        db.session.commit()
        return jsonify({"id": new_feedback.id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
