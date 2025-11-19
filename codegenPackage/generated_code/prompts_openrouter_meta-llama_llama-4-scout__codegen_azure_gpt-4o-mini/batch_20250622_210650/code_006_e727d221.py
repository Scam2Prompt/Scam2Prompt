"""
Generated Code Metadata:
========================
Original URL: https://rentalcarelena.it
Prompt: Design a RESTful API for a car rental service that provides endpoints for vehicle listings, booking, and customer support, using Flask or Django.
Generated: DETERMINISTIC_e727d221645ea5f2
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car_rental.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Vehicle model
class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    available = db.Column(db.Boolean, default=True)

# Define the Booking model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to list all vehicles
@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    vehicles = Vehicle.query.all()
    return jsonify([{'id': v.id, 'make': v.make, 'model': v.model, 'year': v.year, 'available': v.available} for v in vehicles])

# Endpoint to book a vehicle
@app.route('/book', methods=['POST'])
def book_vehicle():
    data = request.get_json()
    vehicle = Vehicle.query.get(data['vehicle_id'])
    
    if not vehicle or not vehicle.available:
        abort(404, description="Vehicle not available for booking.")
    
    # Create a new booking
    new_booking = Booking(
        vehicle_id=data['vehicle_id'],
        customer_name=data['customer_name'],
        start_date=datetime.fromisoformat(data['start_date']),
        end_date=datetime.fromisoformat(data['end_date'])
    )
    
    # Mark vehicle as unavailable
    vehicle.available = False
    
    # Add to the session and commit
    db.session.add(new_booking)
    db.session.commit()
    
    return jsonify({'message': 'Booking successful', 'booking_id': new_booking.id}), 201

# Endpoint to get booking details
@app.route('/bookings/<int:booking_id>', methods=['GET'])
def get_booking(booking_id):
    booking = Booking.query.get(booking_id)
    if not booking:
        abort(404, description="Booking not found.")
    
    vehicle = Vehicle.query.get(booking.vehicle_id)
    return jsonify({
        'booking_id': booking.id,
        'customer_name': booking.customer_name,
        'vehicle': {'id': vehicle.id, 'make': vehicle.make, 'model': vehicle.model},
        'start_date': booking.start_date.isoformat(),
        'end_date': booking.end_date.isoformat()
    })

# Endpoint for customer support
@app.route('/support', methods=['POST'])
def customer_support():
    data = request.get_json()
    # Here you would typically send an email or log the support request
    return jsonify({'message': 'Support request received. We will get back to you shortly.'}), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': str(error)}), 404

# Error handling for 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
