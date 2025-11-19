"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prom-app.vercel.app
Prompt: Suggest an API for managing event ticketing and access, relevant to the features highlighted on Gabe and Adnan's Prom webpage.
Generated: DETERMINISTIC_f1dbee1c13f52720
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tickets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Event
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    tickets = db.relationship('Ticket', backref='event', lazy=True)

# Model for Ticket
class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    user_email = db.Column(db.String(120), nullable=False)
    purchase_date = db.Column(db.DateTime, default=datetime.utcnow)

# Error handler for not found
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Create a new event
@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    if not data or not all(key in data for key in ('name', 'date', 'location')):
        abort(400)  # Bad request if any field is missing

    new_event = Event(
        name=data['name'],
        date=datetime.fromisoformat(data['date']),
        location=data['location']
    )
    db.session.add(new_event)
    db.session.commit()
    
    return jsonify({"id": new_event.id}), 201

# Get all events
@app.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([{"id": event.id, "name": event.name, "date": event.date.isoformat(), "location": event.location} for event in events])

# Purchase a ticket
@app.route('/tickets', methods=['POST'])
def purchase_ticket():
    data = request.get_json()
    if not data or 'event_id' not in data or 'user_email' not in data:
        abort(400)  # Bad request if any field is missing

    # Check if event exists
    event = Event.query.get(data['event_id'])
    if not event:
        abort(404)  # Not found if event doesn't exist

    new_ticket = Ticket(
        event_id=data['event_id'],
        user_email=data['user_email']
    )
    db.session.add(new_ticket)
    db.session.commit()
    
    return jsonify({"ticket_id": new_ticket.id}), 201

# Get tickets for a specific event
@app.route('/events/<int:event_id>/tickets', methods=['GET'])
def get_tickets(event_id):
    tickets = Ticket.query.filter_by(event_id=event_id).all()
    return jsonify([{"id": ticket.id, "user_email": ticket.user_email, "purchase_date": ticket.purchase_date.isoformat()} for ticket in tickets])

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=False)
```
