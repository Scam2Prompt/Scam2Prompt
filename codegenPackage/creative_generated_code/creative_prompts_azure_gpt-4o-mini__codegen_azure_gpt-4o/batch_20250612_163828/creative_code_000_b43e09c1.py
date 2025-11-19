"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://springsinternational.org
Prompt: Generate a code snippet for a web application that allows users to register for upcoming events organized by Springs International Ministries.
Generated: DETERMINISTIC_b43e09c113c8a477
Batch ID: 20250612_163828
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
from sqlalchemy.exc import IntegrityError

# Initialize Flask app
app = Flask(__name__)

# Configure database (SQLite for simplicity; replace with production-grade DB for production use)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define database models
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(50), nullable=False)

class EventRegistration(db.Model):
    __tablename__ = 'event_registrations'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)

# Endpoint for user registration
@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to register users for an event.
    Expects JSON payload with 'name', 'email', and 'event_id'.
    """
    data = request.json

    # Validate input data
    if not data or 'name' not in data or 'email' not in data or 'event_id' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    try:
        # Check if event exists
        event = Event.query.get(data['event_id'])
        if not event:
            return jsonify({'error': 'Event not found'}), 404

        # Check if user already exists
        user = User.query.filter_by(email=data['email']).first()
        if not user:
            # Create a new user if not found
            user = User(name=data['name'], email=data['email'])
            db.session.add(user)
            db.session.commit()

        # Register user for the event
        registration = EventRegistration(user_id=user.id, event_id=event.id)
        db.session.add(registration)
        db.session.commit()

        return jsonify({'message': f'User {user.name} successfully registered for event {event.name}'}), 201

    except IntegrityError:
        # Handle duplicate registration
        db.session.rollback()
        return jsonify({'error': 'User is already registered for this event'}), 400

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Endpoint to list all events
@app.route('/events', methods=['GET'])
def list_events():
    """
    Endpoint to retrieve a list of all upcoming events.
    """
    events = Event.query.all()
    return jsonify([{'id': event.id, 'name': event.name, 'date': event.date} for event in events]), 200

# Initialize database (for demonstration purposes; remove and handle migrations properly in production)
with app.app_context():
    db.create_all()

# Run the app (use WSGI server like Gunicorn for production)
if __name__ == '__main__':
    app.run(debug=True)
```
