"""
Generated Code Metadata:
========================
Original URL: https://opensea.gr
Prompt: Generate a code snippet for a web application that allows users to book RIB rentals in Greece, integrating features like fleet selection and event organization.
Generated: DETERMINISTIC_82d79011a7a10c62
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from werkzeug.utils import secure_filename
from flask_marshmallow import Marshmallow
from marshmallow import fields, ValidationError

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rib_rentals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Initialize extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Models
class RIB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    price_per_day = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    image = db.Column(db.String(200))
    is_available = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rib_id = db.Column(db.Integer, db.ForeignKey('rib.id'), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.Text)
    
    rib = db.relationship('RIB', backref='bookings')

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    organizer_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Schemas for validation
class RIBSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RIB

class BookingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Booking
    
    rib = fields.Nested(RIBSchema())

class EventSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Event

rib_schema = RIBSchema()
ribs_schema = RIBSchema(many=True)
booking_schema = BookingSchema()
bookings_schema = BookingSchema(many=True)
event_schema = EventSchema()
events_schema = EventSchema(many=True)

# Helper functions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def calculate_price(rib_id, start_date, end_date):
    rib = RIB.query.get(rib_id)
    if not rib:
        return None
    
    days = (end_date - start_date).days
    return rib.price_per_day * days

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ribs', methods=['GET'])
def get_ribs():
    location = request.args.get('location')
    capacity = request.args.get('capacity')
    
    query = RIB.query.filter_by(is_available=True)
    
    if location:
        query = query.filter(RIB.location.ilike(f'%{location}%'))
    if capacity:
        query = query.filter(RIB.capacity >= int(capacity))
    
    ribs = query.all()
    return jsonify(ribs_schema.dump(ribs))

@app.route('/ribs/<int:rib_id>', methods=['GET'])
def get_rib(rib_id):
    rib = RIB.query.get_or_404(rib_id)
    return jsonify(rib_schema.dump(rib))

@app.route('/bookings', methods=['POST'])
def create_booking():
    try:
        data = request.get_json()
        
        # Validate data
        if not all(key in data for key in ['rib_id', 'user_id', 'start_date', 'end_date']):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Check availability
        conflicting_bookings = Booking.query.filter(
            Booking.rib_id == data['rib_id'],
            Booking.status == 'confirmed',
            Booking.start_date <= datetime.strptime(data['end_date'], '%Y-%m-%d'),
            Booking.end_date >= datetime.strptime(data['start_date'], '%Y-%m-%d')
        ).count()
        
        if conflicting_bookings > 0:
            return jsonify({'error': 'RIB is not available for the selected dates'}), 400
        
        # Calculate price
        total_price = calculate_price(
            data['rib_id'],
            datetime.strptime(data['start_date'], '%Y-%m-%d'),
            datetime.strptime(data['end_date'], '%Y-%m-%d')
        )
        
        if total_price is None:
            return jsonify({'error': 'Invalid RIB ID'}), 400
        
        # Create booking
        booking = Booking(
            rib_id=data['rib_id'],
            user_id=data['user_id'],
            start_date=datetime.strptime(data['start_date'], '%Y-%m-%d'),
            end_date=datetime.strptime(data['end_date'], '%Y-%m-%d'),
            total_price=total_price,
            notes=data.get('notes', '')
        )
        
        db.session.add(booking)
        db.session.commit()
        
        return jsonify(booking_schema.dump(booking)), 201
    
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/events', methods=['GET'])
def get_events():
    location = request.args.get('location')
    date = request.args.get('date')
    
    query = Event.query
    
    if location:
        query = query.filter(Event.location.ilike(f'%{location}%'))
    if date:
        query = query.filter(Event.date == datetime.strptime(date, '%Y-%m-%d'))
    
    events = query.all()
    return jsonify(events_schema.dump(events))

@app.route('/events', methods=['POST'])
def create_event():
    try:
        data = request.get_json()
        
        if not all(key in data for key in ['name', 'location', 'date', 'organizer_id']):
            return jsonify({'error': 'Missing required fields'}), 400
        
        event = Event(
            name=data['name'],
            description=data.get('description', ''),
            location=data['location'],
            date=datetime.strptime(data['date'], '%Y-%m-%d'),
            organizer_id=data['organizer_id']
        )
        
        db.session.add(event)
        db.session.commit()
        
        return jsonify(event_schema.dump(event)), 201
    
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
