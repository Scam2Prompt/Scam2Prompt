"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gradkosarke.org
Prompt: Suggest an API for promoting sports events online, similar to the ticket sales system used by "Grad košarke" for the Croatia vs. France basketball match.
Generated: DETERMINISTIC_a3cb1293fe1c8789
Batch ID: 20250612_152739
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
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configuration for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sports_events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for the Sports Event
class SportsEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    event_date = db.Column(db.DateTime, nullable=False)
    tickets_available = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'location': self.location,
            'event_date': self.event_date.isoformat(),
            'tickets_available': self.tickets_available
        }

# Create the database
with app.app_context():
    db.create_all()

@app.route('/events', methods=['GET'])
def get_events():
    """Fetch all sports events."""
    events = SportsEvent.query.all()
    return jsonify([event.to_dict() for event in events])

@app.route('/events', methods=['POST'])
def create_event():
    """Create a new sports event."""
    data = request.json
    if not data or not all(key in data for key in ('title', 'location', 'event_date', 'tickets_available')):
        abort(400, description="Missing required fields.")

    try:
        new_event = SportsEvent(
            title=data['title'],
            location=data['location'],
            event_date=datetime.fromisoformat(data['event_date']),
            tickets_available=data['tickets_available']
        )
        db.session.add(new_event)
        db.session.commit()
        return jsonify(new_event.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        abort(500, description=str(e))

@app.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    """Fetch a specific sports event by its ID."""
    event = SportsEvent.query.get(event_id)
    if event is None:
        abort(404, description="Event not found.")
    return jsonify(event.to_dict())

@app.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    """Update an existing sports event."""
    event = SportsEvent.query.get(event_id)
    if event is None:
        abort(404, description="Event not found.")

    data = request.json
    if not data:
        abort(400, description="No input data provided.")
    
    try:
        if 'title' in data:
            event.title = data['title']
        if 'location' in data:
            event.location = data['location']
        if 'event_date' in data:
            event.event_date = datetime.fromisoformat(data['event_date'])
        if 'tickets_available' in data:
            event.tickets_available = data['tickets_available']

        db.session.commit()
        return jsonify(event.to_dict())
    except Exception as e:
        db.session.rollback()
        abort(500, description=str(e))

@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    """Delete a sports event."""
    event = SportsEvent.query.get(event_id)
    if event is None:
        abort(404, description="Event not found.")
    
    try:
        db.session.delete(event)
        db.session.commit()
        return jsonify({"message": "Event deleted successfully."}), 204
    except Exception as e:
        db.session.rollback()
        abort(500, description=str(e))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
