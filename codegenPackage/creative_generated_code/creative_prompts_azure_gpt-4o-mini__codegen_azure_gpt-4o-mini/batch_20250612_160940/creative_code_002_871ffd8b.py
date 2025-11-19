"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kristoslounge.com
Prompt: Create an API endpoint for managing event details at Kristos Lounge, including adding, updating, and deleting events.
Generated: DETERMINISTIC_871ffd8b8b14ac68
Batch ID: 20250612_160940
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Event model
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(50), nullable=False)  # Format: YYYY-MM-DD
    location = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert the Event object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'date': self.date,
            'location': self.location
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/events', methods=['POST'])
def add_event():
    """Add a new event."""
    data = request.get_json()
    try:
        new_event = Event(name=data['name'], date=data['date'], location=data['location'])
        db.session.add(new_event)
        db.session.commit()
        return jsonify(new_event.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    """Update an existing event."""
    data = request.get_json()
    event = Event.query.get(event_id)
    if not event:
        return jsonify({'error': 'Event not found'}), 404

    try:
        event.name = data.get('name', event.name)
        event.date = data.get('date', event.date)
        event.location = data.get('location', event.location)
        db.session.commit()
        return jsonify(event.to_dict())
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    """Delete an event."""
    event = Event.query.get(event_id)
    if not event:
        return jsonify({'error': 'Event not found'}), 404

    try:
        db.session.delete(event)
        db.session.commit()
        return jsonify({'message': 'Event deleted successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/events', methods=['GET'])
def get_events():
    """Retrieve a list of all events."""
    events = Event.query.all()
    return jsonify([event.to_dict() for event in events]), 200

if __name__ == '__main__':
    app.run(debug=True)
```
