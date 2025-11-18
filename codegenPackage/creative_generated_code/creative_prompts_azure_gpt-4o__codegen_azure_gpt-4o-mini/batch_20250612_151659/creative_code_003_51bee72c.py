"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ahopefulme.com
Prompt: Suggest tools or libraries to build a feature for organizing and displaying events and conferences, similar to the HopefulMe Aba hangout section.
Generated: DETERMINISTIC_51bee72cacb8a732
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Event model
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Event {self.title}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new event
@app.route('/events', methods=['POST'])
def create_event():
    try:
        data = request.get_json()
        new_event = Event(
            title=data['title'],
            description=data['description'],
            date=datetime.fromisoformat(data['date']),
            location=data['location']
        )
        db.session.add(new_event)
        db.session.commit()
        return jsonify({'message': 'Event created successfully!', 'event_id': new_event.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Route to get all events
@app.route('/events', methods=['GET'])
def get_events():
    try:
        events = Event.query.all()
        result = [
            {
                'id': event.id,
                'title': event.title,
                'description': event.description,
                'date': event.date.isoformat(),
                'location': event.location
            } for event in events
        ]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Route to get a specific event by ID
@app.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    try:
        event = Event.query.get_or_404(event_id)
        return jsonify({
            'id': event.id,
            'title': event.title,
            'description': event.description,
            'date': event.date.isoformat(),
            'location': event.location
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Route to delete an event
@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    try:
        event = Event.query.get_or_404(event_id)
        db.session.delete(event)
        db.session.commit()
        return jsonify({'message': 'Event deleted successfully!'}), 204
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
