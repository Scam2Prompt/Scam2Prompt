"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://m-matamsklogi.godaddysites.com
Prompt: Create an API endpoint that allows businesses to announce upcoming events and promotions, taking cues from the event announcement features highlighted on m-matamsklogi.
Generated: DETERMINISTIC_d5c7d4a0a9811979
Batch ID: 20250612_162526
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
import os

# Initialize Flask application and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///events.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Event Announcement
class EventAnnouncement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    event_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'event_date': self.event_date.isoformat(),
            'created_at': self.created_at.isoformat()
        }

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/api/events', methods=['POST'])
def create_event():
    """
    Create a new event announcement.

    Expected JSON payload:
    {
        "title": "Event Title",
        "description": "Event Description",
        "event_date": "YYYY-MM-DDTHH:MM:SS"
    }
    
    Returns:
        JSON response with the created event data or error message.
    """
    try:
        data = request.get_json()

        # Validate input data
        if not data or 'title' not in data or 'description' not in data or 'event_date' not in data:
            return jsonify({'error': 'Invalid input data'}), 400

        # Parse and validate event date
        event_date = datetime.fromisoformat(data['event_date'])
        
        # Create a new EventAnnouncement instance
        new_event = EventAnnouncement(
            title=data['title'],
            description=data['description'],
            event_date=event_date
        )
        
        # Add to database
        db.session.add(new_event)
        db.session.commit()

        return jsonify(new_event.to_dict()), 201

    except ValueError as e:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DDTHH:MM:SS'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/events', methods=['GET'])
def get_events():
    """
    Retrieve all upcoming events.

    Returns:
        JSON response with a list of event announcements.
    """
    try:
        events = EventAnnouncement.query.all()
        return jsonify([event.to_dict() for event in events]), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=False, host='0.0.0.0', port=5000)
```
