"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balancerfi.airlst-pages.app
Prompt: Create an API endpoint for managing event registrations, inspired by the features outlined on the Balancer.Fi event page.
Generated: DETERMINISTIC_0f8e2c16b6136413
Batch ID: 20250612_163156
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
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Event
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    max_participants = db.Column(db.Integer, nullable=False)
    registrations = db.relationship('Registration', backref='event', lazy=True)

# Model for Registration
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    participant_name = db.Column(db.String(100), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to create an event
@app.route('/events', methods=['POST'])
def create_event():
    """Creates a new event."""
    data = request.get_json()
    try:
        new_event = Event(
            name=data['name'],
            date=data['date'],
            max_participants=data['max_participants']
        )
        db.session.add(new_event)
        db.session.commit()
        return jsonify({'message': 'Event created successfully.', 'event_id': new_event.id}), 201
    except KeyError as e:
        return jsonify({'error': f'Missing parameter: {str(e)}'}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Event could not be created due to integrity constraints.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to register a participant for an event
@app.route('/events/<int:event_id>/register', methods=['POST'])
def register_for_event(event_id):
    """Registers a participant for a specific event."""
    data = request.get_json()
    try:
        event = Event.query.get(event_id)
        if not event:
            return jsonify({'error': 'Event not found.'}), 404
        
        # Check if max participants reached
        if len(event.registrations) >= event.max_participants:
            return jsonify({'error': 'Maximum participants reached for this event.'}), 400

        registration = Registration(
            participant_name=data['participant_name'],
            event_id=event.id
        )
        db.session.add(registration)
        db.session.commit()
        return jsonify({'message': 'Registration successful.', 'registration_id': registration.id}), 201
    except KeyError as e:
        return jsonify({'error': f'Missing parameter: {str(e)}'}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Registration could not be completed due to integrity constraints.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to list all events
@app.route('/events', methods=['GET'])
def list_events():
    """Returns a list of all events."""
    events = Event.query.all()
    return jsonify([{'id': event.id, 'name': event.name, 'date': event.date, 'max_participants': event.max_participants} for event in events]), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
