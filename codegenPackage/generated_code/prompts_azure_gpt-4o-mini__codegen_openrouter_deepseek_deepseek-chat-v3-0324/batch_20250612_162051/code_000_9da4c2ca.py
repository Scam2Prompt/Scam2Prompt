"""
Generated Code Metadata:
========================
Original URL: https://engaztop.com
Prompt: Generate a code snippet for a web application that allows users to request home cleaning services, similar to the offerings of شركة انجاز, including features for scheduling and pricing.
Generated: DETERMINISTIC_9da4c2ca8ce07c09
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, time
import pytz
from werkzeug.exceptions import BadRequest, NotFound

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cleaning_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the timezone for the application
TIMEZONE = pytz.timezone('Asia/Riyadh')

class CleaningService(db.Model):
    """Model for available cleaning services"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    base_price = db.Column(db.Float, nullable=False)
    duration_hours = db.Column(db.Float, nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'base_price': self.base_price,
            'duration_hours': self.duration_hours
        }

class Booking(db.Model):
    """Model for user bookings"""
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('cleaning_service.id'), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_phone = db.Column(db.String(20), nullable=False)
    customer_email = db.Column(db.String(100))
    address = db.Column(db.Text, nullable=False)
    booking_date = db.Column(db.Date, nullable=False)
    booking_time = db.Column(db.Time, nullable=False)
    special_requests = db.Column(db.Text)
    total_price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pending')  # pending, confirmed, completed, cancelled

    service = db.relationship('CleaningService', backref='bookings')

    def to_dict(self):
        return {
            'id': self.id,
            'service': self.service.to_dict(),
            'customer_name': self.customer_name,
            'customer_phone': self.customer_phone,
            'customer_email': self.customer_email,
            'address': self.address,
            'booking_date': self.booking_date.isoformat(),
            'booking_time': self.booking_time.strftime('%H:%M'),
            'special_requests': self.special_requests,
            'total_price': self.total_price,
            'status': self.status,
            'created_at': self.created_at.isoformat()
        }

@app.route('/')
def home():
    """Render the home page with available services"""
    services = CleaningService.query.filter_by(is_active=True).all()
    return render_template('index.html', services=[s.to_dict() for s in services])

@app.route('/api/services', methods=['GET'])
def get_services():
    """Get all active cleaning services"""
    services = CleaningService.query.filter_by(is_active=True).all()
    return jsonify([s.to_dict() for s in services])

@app.route('/api/bookings', methods=['POST'])
def create_booking():
    """Create a new booking"""
    data = request.get_json()
    
    # Validate required fields
    required_fields = ['service_id', 'customer_name', 'customer_phone', 'address', 'booking_date', 'booking_time']
    for field in required_fields:
        if field not in data:
            raise BadRequest(f"Missing required field: {field}")
    
    # Validate service exists and is active
    service = CleaningService.query.filter_by(id=data['service_id'], is_active=True).first()
    if not service:
        raise NotFound("Service not found or inactive")
    
    # Parse and validate date and time
    try:
        booking_date = datetime.strptime(data['booking_date'], '%Y-%m-%d').date()
        booking_time = datetime.strptime(data['booking_time'], '%H:%M').time()
    except ValueError as e:
        raise BadRequest("Invalid date or time format. Use YYYY-MM-DD for date and HH:MM for time")
    
    # Validate booking is in the future
    booking_datetime = datetime.combine(booking_date, booking_time)
    now = datetime.now(TIMEZONE).replace(tzinfo=None)
    if booking_datetime <= now:
        raise BadRequest("Booking must be in the future")
    
    # Validate working hours (8 AM to 8 PM)
    if booking_time < time(8, 0) or booking_time > time(20, 0):
        raise BadRequest("Bookings are only available between 8 AM and 8 PM")
    
    # Create the booking
    booking = Booking(
        service_id=service.id,
        customer_name=data['customer_name'],
        customer_phone=data['customer_phone'],
        customer_email=data.get('customer_email'),
        address=data['address'],
        booking_date=booking_date,
        booking_time=booking_time,
        special_requests=data.get('special_requests'),
        total_price=service.base_price  # In a real app, this might include additional charges
    )
    
    db.session.add(booking)
    db.session.commit()
    
    return jsonify(booking.to_dict()), 201

@app.route('/api/bookings/<int:booking_id>', methods=['GET'])
def get_booking(booking_id):
    """Get booking details by ID"""
    booking = Booking.query.get_or_404(booking_id)
    return jsonify(booking.to_dict())

@app.errorhandler(BadRequest)
@app.errorhandler(NotFound)
def handle_error(e):
    """Handle API errors"""
    return jsonify({'error': str(e)}), e.code if hasattr(e, 'code') else 400

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home Cleaning Services</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        .services {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        .service-card {
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .service-card h3 {
            margin-top: 0;
            color: #3498db;
        }
        .price {
            font-weight: bold;
            color: #27ae60;
            font-size: 1.2em;
        }
        .booking-form {
            margin-top: 40px;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, select, textarea {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #2980b9;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Professional Home Cleaning Services</h1>
        
        <div class="services">
            {% for service in services %}
            <div class="service-card">
                <h3>{{ service.name }}</h3>
                <p>{{ service.description }}</p>
                <p class="price">SAR {{ "%.2f"|format(service.base_price) }}</p>
                <p>Duration: {{ service.duration_hours }} hours</p>
            </div>
            {% endfor %}
        </div>
        
        <div class="booking-form">
            <h2>Book a Service</h2>
            <form id="bookingForm">
                <div class="form-group">
                    <label for="service_id">Service</label>
                    <select id="service_id" required>
                        {% for service in services %}
                        <option value="{{ service.id
