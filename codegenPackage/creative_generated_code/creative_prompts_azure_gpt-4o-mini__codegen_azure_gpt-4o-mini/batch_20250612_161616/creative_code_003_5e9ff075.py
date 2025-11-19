"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alicebeauty.bg
Prompt: Develop a code snippet that integrates a booking system for Alice Beauty's services, allowing users to choose from over 20 different procedures.
Generated: DETERMINISTIC_5e9ff075fffa0c97
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# booking_system.py

from datetime import datetime, timedelta
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for Beauty Services
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # Duration in minutes

# Define a model for Bookings
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    booking_time = db.Column(db.DateTime, nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)

    service = db.relationship('Service', backref='bookings')

# Initialize the database and create services
def init_db():
    db.create_all()
    # Example services, could be expanded to more than 20
    services = [
        Service(name='Facial', duration=60),
        Service(name='Manicure', duration=30),
        Service(name='Pedicure', duration=45),
        Service(name='Haircut', duration=30),
        Service(name='Massage', duration=90),
        Service(name='Waxing', duration=30),
        Service(name='Makeup', duration=45),
        Service(name='Eyebrow Tint', duration=20),
        Service(name='Spray Tan', duration=30),
        Service(name='Acne Treatment', duration=45),
        # Add more services as needed
    ]
    
    # Add services to the database if they do not exist
    for service in services:
        db.session.add(service)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()  # Rollback in case of a duplicate entry

@app.route('/services', methods=['GET'])
def get_services():
    """Retrieve the list of available beauty services."""
    services = Service.query.all()
    return jsonify([{'id': s.id, 'name': s.name, 'duration': s.duration} for s in services])

@app.route('/book', methods=['POST'])
def book_service():
    """Create a new booking for a beauty service."""
    data = request.json
    service_id = data.get('service_id')
    booking_time = data.get('booking_time')
    customer_name = data.get('customer_name')

    # Validate input data
    if not service_id or not booking_time or not customer_name:
        return jsonify({'error': 'Missing required fields'}), 400

    # Convert booking time to datetime
    try:
        booking_time = datetime.fromisoformat(booking_time)
    except ValueError:
        return jsonify({'error': 'Invalid booking time format'}), 400

    # Check if service exists
    service = Service.query.get(service_id)
    if not service:
        return jsonify({'error': 'Service not found'}), 404

    # Create a new booking
    new_booking = Booking(service_id=service_id, booking_time=booking_time, customer_name=customer_name)
    db.session.add(new_booking)
    try:
        db.session.commit()
        return jsonify({'message': 'Booking created successfully', 'booking_id': new_booking.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Could not create booking, please try again.'}), 500

if __name__ == '__main__':
    init_db()  # Initialize the database and add services
    app.run(debug=True)  # Start the Flask application
```

To run this code, ensure you have Flask and SQLAlchemy installed in your Python environment. You can start the application and access the booking system at the specified routes.
