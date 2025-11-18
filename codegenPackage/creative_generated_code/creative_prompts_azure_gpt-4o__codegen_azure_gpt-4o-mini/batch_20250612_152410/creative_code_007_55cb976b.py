"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cocula.gob.mx
Prompt: Provide code to create a calendar feature for municipal events, such as those listed in the Cocula government website's announcements.
Generated: DETERMINISTIC_55cb976b73f19eb6
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# Configuring the SQLite database for the application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model for the Event
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    event_date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'<Event {self.title}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new event
@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    
    # Validate incoming data
    if not data or 'title' not in data or 'event_date' not in data:
        return jsonify({'error': 'Invalid data provided'}), 400
    
    try:
        # Create a new event instance
        new_event = Event(
            title=data['title'],
            description=data.get('description'),
            event_date=datetime.strptime(data['event_date'], '%Y-%m-%d %H:%M:%S'),
            location=data.get('location')
        )
        
        # Add the event to the database
        db.session.add(new_event)
        db.session.commit()
        
        return jsonify({'message': 'Event created successfully'}), 201
    except Exception as e:
        # Handle exceptions and rollback session on error
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to retrieve all events
@app.route('/events', methods=['GET'])
def get_events():
    try:
        events = Event.query.all()
        return jsonify([{
            'id': event.id,
            'title': event.title,
            'description': event.description,
            'event_date': event.event_date.strftime('%Y-%m-%d %H:%M:%S'),
            'location': event.location
        } for event in events]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get a specific event by ID
@app.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    try:
        event = Event.query.get_or_404(event_id)
        return jsonify({
            'id': event.id,
            'title': event.title,
            'description': event.description,
            'event_date': event.event_date.strftime('%Y-%m-%d %H:%M:%S'),
            'location': event.location
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to update an event
@app.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.get_json()
    
    # Validate incoming data
    if not data:
        return jsonify({'error': 'Invalid data provided'}), 400
    
    try:
        event = Event.query.get_or_404(event_id)
        
        # Update event attributes
        event.title = data.get('title', event.title)
        event.description = data.get('description', event.description)
        if 'event_date' in data:
            event.event_date = datetime.strptime(data['event_date'], '%Y-%m-%d %H:%M:%S')
        event.location = data.get('location', event.location)

        db.session.commit()
        return jsonify({'message': 'Event updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to delete an event
@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    try:
        event = Event.query.get_or_404(event_id)
        db.session.delete(event)
        db.session.commit()
        return jsonify({'message': 'Event deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
