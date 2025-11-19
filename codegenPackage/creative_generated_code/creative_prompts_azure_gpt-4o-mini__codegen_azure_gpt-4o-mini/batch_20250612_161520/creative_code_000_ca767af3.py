"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tubalife.me
Prompt: Generate a booking system API for a spa that allows users to schedule services like Moroccan baths and massages at TUBA SPA in Riyadh.
Generated: DETERMINISTIC_ca767af39037dfd4
Batch ID: 20250612_161520
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tuba_spa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Service model
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    duration = db.Column(db.Integer, nullable=False)  # Duration in minutes

    def __repr__(self):
        return f'<Service {self.name}>'

# Define the Booking model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)

    service = db.relationship('Service', backref='bookings')

    def __repr__(self):
        return f'<Booking {self.id} - {self.customer_name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to list all available services
@app.route('/services', methods=['GET'])
def get_services():
    """Retrieve all available services."""
    services = Service.query.all()
    return jsonify([{'id': service.id, 'name': service.name, 'duration': service.duration} for service in services])

# Endpoint to create a new booking
@app.route('/book', methods=['POST'])
def book_service():
    """Create a new booking for a service."""
    data = request.json

    # Validate input data
    if 'customer_name' not in data or 'service_id' not in data or 'date_time' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        # Parse the date_time from string to datetime object
        booking_time = datetime.fromisoformat(data['date_time'])
        new_booking = Booking(
            customer_name=data['customer_name'],
            service_id=data['service_id'],
            date_time=booking_time
        )
        db.session.add(new_booking)
        db.session.commit()
        return jsonify({'message': 'Booking created successfully', 'booking_id': new_booking.id}), 201

    except IntegrityError:
        db.session.rollback()  # Rollback the session in case of error
        return jsonify({'error': 'Service ID does not exist or booking conflict'}), 400
    except ValueError:
        return jsonify({'error': 'Invalid date_time format. Use ISO format.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to get bookings for a specific user
@app.route('/bookings', methods=['GET'])
def get_bookings():
    """Retrieve all bookings for a specified customer name."""
    customer_name = request.args.get('customer_name')
    
    if not customer_name:
        return jsonify({'error': 'customer_name query parameter is required'}), 400

    bookings = Booking.query.filter_by(customer_name=customer_name).all()
    return jsonify([{'id': booking.id, 'customer_name': booking.customer_name, 'service_id': booking.service_id, 'date_time': booking.date_time.isoformat()} for booking in bookings])

# Main entry point to run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
