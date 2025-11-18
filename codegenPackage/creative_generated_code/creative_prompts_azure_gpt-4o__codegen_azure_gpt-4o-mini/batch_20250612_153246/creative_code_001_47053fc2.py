"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wcdevent.com
Prompt: Recommend APIs or libraries to integrate event design features into a web application for managing corporate and social events.
Generated: DETERMINISTIC_47053fc28c6ab9ed
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web application development
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configuration for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define Event model for the database
class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Event {self.name}>'

# Route to create a new event
@app.route('/events', methods=['POST'])
def create_event():
    try:
        data = request.get_json()  # Get JSON data from request
        new_event = Event(
            name=data['name'],
            date=data['date'],
            location=data['location'],
            description=data.get('description', '')
        )
        db.session.add(new_event)  # Add event to the session
        db.session.commit()  # Commit the session
        return jsonify({'message': 'Event created successfully!'}), 201
    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400
    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback session on error
        return jsonify({'error': str(e)}), 500

# Route to retrieve all events
@app.route('/events', methods=['GET'])
def get_events():
    try:
        events = Event.query.all()  # Query all events
        return jsonify([{
            'id': event.id,
            'name': event.name,
            'date': event.date,
            'location': event.location,
            'description': event.description
        } for event in events]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if they do not exist
    app.run(debug=True)  # Run the application in debug mode
```

Make sure to install Flask and Flask-SQLAlchemy before running the application:

```bash
pip install Flask Flask-SQLAlchemy
```
