"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://secondcitysummers.com
Prompt: Suggest tools or frameworks to design a booking system for The Second City's private events and team-building workshops, ensuring seamless integration with their existing website.
Generated: DETERMINISTIC_751885075511162b
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# booking_system.py

"""
Booking System for The Second City's Private Events and Team-Building Workshops

This module provides an interface to manage bookings, including creating, updating,
and canceling events. It uses Flask for the web framework, SQLAlchemy for database
interactions, and integrates with existing website components.

The following libraries should be installed:
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-RESTful
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Database model for Event bookings
class Event(db.Model):
    __tablename__ = 'events'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    attendees = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Event {self.name} on {self.date}>'

# API endpoint to create a new booking
@app.route('/bookings', methods=['POST'])
def create_booking():
    """Creates a new booking for an event."""
    data = request.get_json()
    
    try:
        new_event = Event(
            name=data['name'],
            date=data['date'],
            location=data['location'],
            attendees=data['attendees']
        )
        db.session.add(new_event)
        db.session.commit()
        return jsonify({"message": "Booking created successfully", "event": new_event.id}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Booking could not be created, please check the provided information."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to update an existing booking
@app.route('/bookings/<int:event_id>', methods=['PUT'])
def update_booking(event_id):
    """Updates an existing booking for an event."""
    data = request.get_json()
    
    event = Event.query.get(event_id)
    if not event:
        return jsonify({"error": "Event not found"}), 404

    try:
        event.name = data.get('name', event.name)
        event.date = data.get('date', event.date)
        event.location = data.get('location', event.location)
        event.attendees = data.get('attendees', event.attendees)

        db.session.commit()
        return jsonify({"message": "Booking updated successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to cancel a booking
@app.route('/bookings/<int:event_id>', methods=['DELETE'])
def cancel_booking(event_id):
    """Cancels an existing booking for an event."""
    event = Event.query.get(event_id)
    if not event:
        return jsonify({"error": "Event not found"}), 404

    try:
        db.session.delete(event)
        db.session.commit()
        return jsonify({"message": "Booking canceled successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Required Libraries Installation
To run this code, ensure you have the necessary libraries installed. You can do this by running:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate
```

### Database Initialization
To initialize the database, you can use Flask-Migrate commands after setting up your Flask application. Run the following commands:
```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```
