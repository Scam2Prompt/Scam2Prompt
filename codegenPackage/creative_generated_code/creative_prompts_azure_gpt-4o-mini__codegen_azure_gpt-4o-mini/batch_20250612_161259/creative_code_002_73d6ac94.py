"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://333club.xyz
Prompt: Create an API endpoint for a nightclub's event schedule that lists weekly themes like Afrobeats and Amapiano, including location and dress code requirements.
Generated: DETERMINISTIC_73d6ac947d20b568
Batch ID: 20250612_161259
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

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nightclub_events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Event model to represent events in the database
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    theme = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    dress_code = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        """Convert event object to dictionary for JSON response."""
        return {
            'id': self.id,
            'theme': self.theme,
            'location': self.location,
            'dress_code': self.dress_code,
            'date': self.date.strftime("%Y-%m-%d %H:%M:%S")
        }

# Create database and tables
with app.app_context():
    db.create_all()

@app.route('/api/events', methods=['GET'])
def get_events():
    """
    API endpoint to retrieve the list of events.
    Returns a JSON response with event details.
    """
    try:
        events = Event.query.all()
        return jsonify([event.to_dict() for event in events]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/events', methods=['POST'])
def create_event():
    """
    API endpoint to create a new event.
    Expects JSON data with theme, location, dress code, and date.
    """
    try:
        data = request.get_json()
        new_event = Event(
            theme=data['theme'],
            location=data['location'],
            dress_code=data['dress_code'],
            date=datetime.strptime(data['date'], "%Y-%m-%d %H:%M:%S")
        )
        db.session.add(new_event)
        db.session.commit()
        return jsonify(new_event.to_dict()), 201
    except KeyError as e:
        return jsonify({'error': f'Missing key: {str(e)}'}), 400
    except ValueError as e:
        return jsonify({'error': f'Invalid date format: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
