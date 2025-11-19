"""
Generated Code Metadata:
========================
Original URL: https://bandadorada.com
Prompt: Generate a code snippet for a web application that allows users to book live music services for weddings and corporate events, similar to the offerings of Orquesta Dorada in Trujillo.
Generated: DETERMINISTIC_75839fb565d54d18
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///events.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Event model
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    event_type = db.Column(db.String(50), nullable=False)  # e.g., 'wedding', 'corporate'
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    contact_email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Event {self.name} on {self.date}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to book an event
@app.route('/book_event', methods=['POST'])
def book_event():
    try:
        # Get data from the request
        data = request.get_json()
        name = data.get('name')
        event_type = data.get('event_type')
        date = datetime.strptime(data.get('date'), '%Y-%m-%d %H:%M:%S')
        location = data.get('location')
        contact_email = data.get('contact_email')

        # Validate input data
        if not all([name, event_type, date, location, contact_email]):
            return jsonify({'error': 'All fields are required.'}), 400

        # Create a new event
        new_event = Event(
            name=name,
            event_type=event_type,
            date=date,
            location=location,
            contact_email=contact_email
        )

        # Add the event to the database
        db.session.add(new_event)
        db.session.commit()

        return jsonify({'message': 'Event booked successfully!', 'event_id': new_event.id}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

# Route to get all booked events
@app.route('/events', methods=['GET'])
def get_events():
    try:
        events = Event.query.all()
        return jsonify([{
            'id': event.id,
            'name': event.name,
            'event_type': event.event_type,
            'date': event.date.strftime('%Y-%m-%d %H:%M:%S'),
            'location': event.location,
            'contact_email': event.contact_email
        } for event in events]), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
