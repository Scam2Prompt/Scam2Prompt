"""
Generated Code Metadata:
========================
Original URL: https://mluce-ginza.net
Prompt: Create an API endpoint for managing client inquiries and bookings for an art makeup salon, incorporating features like service selection and appointment reminders.
Generated: DETERMINISTIC_8ae715b6105d0a3f
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready API implementation for an art makeup salon booking system using Python with Flask and SQLAlchemy:

```python
# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import os
from werkzeug.exceptions import HTTPException
import logging
from logging.handlers import RotatingFileHandler

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///bookings.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False

# Initialize database
db = SQLAlchemy(app)

# Configure logging
handler = RotatingFileHandler('salon_bookings.log', maxBytes=10000, backupCount=3)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

# Models
class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    inquiries = db.relationship('Inquiry', backref='client', lazy=True)
    bookings = db.relationship('Booking', backref='client', lazy=True)

class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    duration = db.Column(db.Integer, nullable=False)  # in minutes
    price = db.Column(db.Float, nullable=False)
    bookings = db.relationship('Booking', backref='service', lazy=True)

class Inquiry(db.Model):
    __tablename__ = 'inquiries'
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, responded, resolved
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=False)
    appointment_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='confirmed')  # confirmed, cancelled, completed
    reminder_sent = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Error handling
@app.errorhandler(HTTPException)
def handle_exception(e):
    app.logger.error(f'{e.code} {e.name}: {e.description}')
    return jsonify({
        "error": e.name,
        "message": e.description
    }), e.code

@app.errorhandler(Exception)
def handle_unexpected_error(e):
    app.logger.error(f'Unexpected error: {str(e)}')
    return jsonify({
        "error": "Internal Server Error",
        "message": "An unexpected error occurred"
    }), 500

# Helper functions
def send_reminder(booking_id):
    """Simulate sending a reminder (would integrate with email/SMS service in production)"""
    booking = Booking.query.get(booking_id)
    if booking and not booking.reminder_sent:
        app.logger.info(f"Reminder sent for booking {booking_id}")
        booking.reminder_sent = True
        db.session.commit()
        return True
    return False

def check_and_send_reminders():
    """Check for upcoming appointments and send reminders"""
    now = datetime.utcnow()
    reminder_window = now + timedelta(hours=24)  # 24 hours before appointment
    bookings = Booking.query.filter(
        Booking.appointment_time <= reminder_window,
        Booking.appointment_time > now,
        Booking.reminder_sent == False,
        Booking.status == 'confirmed'
    ).all()
    
    for booking in bookings:
        send_reminder(booking.id)

# API Endpoints
@app.route('/api/services', methods=['GET'])
def get_services():
    """Get all available services"""
    services = Service.query.all()
    return jsonify([{
        'id': s.id,
        'name': s.name,
        'description': s.description,
        'duration': s.duration,
        'price': s.price
    } for s in services])

@app.route('/api/inquiries', methods=['POST'])
def create_inquiry():
    """Create a new client inquiry"""
    data = request.get_json()
    
    if not data or not all(key in data for key in ['name', 'email', 'phone', 'message']):
        raise ValueError("Missing required fields")
    
    # Check if client exists or create new
    client = Client.query.filter_by(email=data['email']).first()
    if not client:
        client = Client(
            name=data['name'],
            email=data['email'],
            phone=data['phone']
        )
        db.session.add(client)
        db.session.commit()
    
    # Create inquiry
    inquiry = Inquiry(
        client_id=client.id,
        message=data['message']
    )
    db.session.add(inquiry)
    db.session.commit()
    
    app.logger.info(f"New inquiry created: {inquiry.id}")
    return jsonify({
        'id': inquiry.id,
        'client_id': client.id,
        'status': inquiry.status,
        'created_at': inquiry.created_at.isoformat()
    }), 201

@app.route('/api/bookings', methods=['POST'])
def create_booking():
    """Create a new booking"""
    data = request.get_json()
    
    if not data or not all(key in data for key in ['client_id', 'service_id', 'appointment_time']):
        raise ValueError("Missing required fields")
    
    # Check if appointment time is valid
    try:
        appointment_time = datetime.fromisoformat(data['appointment_time'])
    except ValueError:
        raise ValueError("Invalid appointment time format")
    
    if appointment_time < datetime.utcnow():
        raise ValueError("Appointment time cannot be in the past")
    
    # Check service exists
    service = Service.query.get(data['service_id'])
    if not service:
        raise ValueError("Service not found")
    
    # Check client exists
    client = Client.query.get(data['client_id'])
    if not client:
        raise ValueError("Client not found")
    
    # Check for overlapping bookings
    end_time = appointment_time + timedelta(minutes=service.duration)
    overlapping = Booking.query.filter(
        Booking.service_id == service.id,
        Booking.appointment_time < end_time,
        Booking.appointment_time + timedelta(minutes=service.duration) > appointment_time,
        Booking.status == 'confirmed'
    ).first()
    
    if overlapping:
        raise ValueError("Time slot already booked")
    
    # Create booking
    booking = Booking(
        client_id=client.id,
        service_id=service.id,
        appointment_time=appointment_time
    )
    db.session.add(booking)
    db.session.commit()
    
    app.logger.info(f"New booking created: {booking.id}")
    return jsonify({
        'id': booking.id,
        'client_id': client.id,
        'service_id': service.id,
        'appointment_time': booking.appointment_time.isoformat(),
        'status': booking.status
    }), 201

@app.route('/api/bookings/<int:booking_id>/remind', methods=['POST'])
def send_booking_reminder(booking_id):
    """Send a reminder for a specific booking"""
    booking = Booking.query.get_or_404(booking_id)
    
    if booking.status != 'confirmed':
        raise ValueError("Cannot send reminder for cancelled or completed booking")
    
    if send_reminder(booking_id):
        return jsonify({'message': 'Reminder sent successfully'})
    else:
        return jsonify({'message': 'Reminder already sent or booking not found'}), 400

@app.route('/api/bookings/reminders', methods=['POST'])
def send_all_reminders():
    """Send reminders for all upcoming bookings"""
    check_and_send_reminders()
    return jsonify({'message': 'Reminder processing completed'})

# CLI Commands
@app.cli.command('initdb')
def init_db():
    """Initialize the database with sample data"""
    db.create_all()
    
    # Add sample services
    services = [
        Service(name='Fantasy Makeup', description='Elaborate fantasy designs', duration=120, price=150),
        Service(name='Bridal Makeup', description='Elegant bridal look', duration=90, price=120),
        Service(name='Special Effects', description='SFX makeup for events', duration=180, price=200)
    ]
    
    for service
