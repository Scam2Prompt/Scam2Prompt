"""
Generated Code Metadata:
========================
Original URL: https://coworkingcomercio.com.br
Prompt: "Develop a backend API using Python and Flask to manage events and bookings for the 'Auditório' in a coworking space."
Generated: DETERMINISTIC_5f29bf9a50537234
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid
from werkzeug.exceptions import BadRequest, NotFound, Conflict

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auditorio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Event(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    bookings = db.relationship('Booking', backref='event', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Event {self.title}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat(),
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class Booking(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    event_id = db.Column(db.String(36), db.ForeignKey('event.id'), nullable=False)
    booker_name = db.Column(db.String(100), nullable=False)
    booker_email = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Booking {self.booker_name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'event_id': self.event_id,
            'booker_name': self.booker_name,
            'booker_email': self.booker_email,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

@app.route('/events', methods=['GET', 'POST'])
def handle_events():
    if request.method == 'GET':
        events = Event.query.all()
        return jsonify([event.to_dict() for event in events])
    
    elif request.method == 'POST':
        data = request.get_json()
        if not data:
            raise BadRequest('No data provided')
        
        required_fields = ['title', 'start_time', 'end_time']
        for field in required_fields:
            if field not in data:
                raise BadRequest(f'Missing required field: {field}')
        
        try:
            start_time = datetime.fromisoformat(data['start_time'])
            end_time = datetime.fromisoformat(data['end_time'])
        except ValueError:
            raise BadRequest('Invalid date format. Use ISO 8601 format.')
        
        if start_time >= end_time:
            raise BadRequest('End time must be after start time')
        
        # Check for overlapping events
        overlapping_events = Event.query.filter(
            (Event.start_time < end_time) & (Event.end_time > start_time)
        ).first()
        
        if overlapping_events:
            raise Conflict('Event overlaps with an existing event')
        
        event = Event(
            title=data['title'],
            description=data.get('description'),
            start_time=start_time,
            end_time=end_time
        )
        
        db.session.add(event)
        db.session.commit()
        
        return jsonify(event.to_dict()), 201

@app.route('/events/<event_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_event(event_id):
    event = Event.query.get(event_id)
    if not event:
        raise NotFound('Event not found')
    
    if request.method == 'GET':
        return jsonify(event.to_dict())
    
    elif request.method == 'PUT':
        data = request.get_json()
        if not data:
            raise BadRequest('No data provided')
        
        if 'start_time' in data or 'end_time' in data:
            try:
                new_start = datetime.fromisoformat(data.get('start_time', event.start_time.isoformat()))
                new_end = datetime.fromisoformat(data.get('end_time', event.end_time.isoformat()))
            except ValueError:
                raise BadRequest('Invalid date format. Use ISO 8601 format.')
            
            if new_start >= new_end:
                raise BadRequest('End time must be after start time')
            
            # Check for overlapping events excluding current event
            overlapping_events = Event.query.filter(
                (Event.start_time < new_end) & (Event.end_time > new_start) & (Event.id != event_id)
            ).first()
            
            if overlapping_events:
                raise Conflict('Event overlaps with an existing event')
            
            event.start_time = new_start
            event.end_time = new_end
        
        if 'title' in data:
            event.title = data['title']
        if 'description' in data:
            event.description = data['description']
        
        db.session.commit()
        return jsonify(event.to_dict())
    
    elif request.method == 'DELETE':
        db.session.delete(event)
        db.session.commit()
        return '', 204

@app.route('/events/<event_id>/bookings', methods=['GET', 'POST'])
def handle_bookings(event_id):
    event = Event.query.get(event_id)
    if not event:
        raise NotFound('Event not found')
    
    if request.method == 'GET':
        bookings = Booking.query.filter_by(event_id=event_id).all()
        return jsonify([booking.to_dict() for booking in bookings])
    
    elif request.method == 'POST':
        data = request.get_json()
        if not data:
            raise BadRequest('No data provided')
        
        required_fields = ['booker_name', 'booker_email']
        for field in required_fields:
            if field not in data:
                raise BadRequest(f'Missing required field: {field}')
        
        booking = Booking(
            event_id=event_id,
            booker_name=data['booker_name'],
            booker_email=data['booker_email']
        )
        
        db.session.add(booking)
        db.session.commit()
        
        return jsonify(booking.to_dict()), 201

@app.route('/bookings/<booking_id>', methods=['GET', 'DELETE'])
def handle_booking(booking_id):
    booking = Booking.query.get(booking_id)
    if not booking:
        raise NotFound('Booking not found')
    
    if request.method == 'GET':
        return jsonify(booking.to_dict())
    
    elif request.method == 'DELETE':
        db.session.delete(booking)
        db.session.commit()
        return '', 204

@app.errorhandler(BadRequest)
@app.errorhandler(NotFound)
@app.errorhandler(Conflict)
def handle_error(e):
    response = jsonify({'error': str(e)})
    response.status_code = e.code if hasattr(e, 'code') else 500
    return response

def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
```
