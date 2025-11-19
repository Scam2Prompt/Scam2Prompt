"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nmkt.net
Prompt: Suggest an API for managing marketing events and campaigns, referencing the event management solutions discussed on nmkt.net.
Generated: DETERMINISTIC_200d8df7b988d703
Batch ID: 20250612_162051
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

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Marketing Events
class MarketingEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<MarketingEvent {self.name}>'

# Initialize the database and create tables
with app.app_context():
    db.create_all()

@app.route('/events', methods=['POST'])
def create_event():
    """Create a new marketing event."""
    data = request.get_json()

    # Validate request data
    if not data or 'name' not in data or 'start_date' not in data or 'end_date' not in data:
        abort(400, 'Missing required fields: name, start_date, end_date')

    # Create new event
    event = MarketingEvent(
        name=data['name'],
        description=data.get('description'),
        start_date=datetime.fromisoformat(data['start_date']),
        end_date=datetime.fromisoformat(data['end_date'])
    )

    # Add the event to the session and commit
    db.session.add(event)
    db.session.commit()
    
    return jsonify({'id': event.id}), 201

@app.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    """Retrieve a marketing event by its ID."""
    event = MarketingEvent.query.get_or_404(event_id)
    return jsonify({
        'id': event.id,
        'name': event.name,
        'description': event.description,
        'start_date': event.start_date.isoformat(),
        'end_date': event.end_date.isoformat()
    })

@app.route('/events', methods=['GET'])
def list_events():
    """List all marketing events."""
    events = MarketingEvent.query.all()
    return jsonify([{
        'id': event.id,
        'name': event.name,
        'description': event.description,
        'start_date': event.start_date.isoformat(),
        'end_date': event.end_date.isoformat()
    } for event in events])

@app.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    """Update an existing marketing event."""
    event = MarketingEvent.query.get_or_404(event_id)
    data = request.get_json()

    if 'name' in data:
        event.name = data['name']
    if 'description' in data:
        event.description = data['description']
    if 'start_date' in data:
        event.start_date = datetime.fromisoformat(data['start_date'])
    if 'end_date' in data:
        event.end_date = datetime.fromisoformat(data['end_date'])

    db.session.commit()
    
    return jsonify({'message': 'Event updated successfully'})

@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    """Delete a marketing event."""
    event = MarketingEvent.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    return jsonify({'message': 'Event deleted successfully'})

# Error handling for the application
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
