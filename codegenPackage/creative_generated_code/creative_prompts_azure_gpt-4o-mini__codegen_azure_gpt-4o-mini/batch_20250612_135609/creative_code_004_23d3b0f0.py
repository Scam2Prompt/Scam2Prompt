"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rehemacare.com
Prompt: Illustrate how to implement a booking system for Habilitation services at Rehema Care using a RESTful API approach.
Generated: DETERMINISTIC_23d3b0f05c66193f
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///habilitation_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the booking model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(100), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "client_name": self.client_name,
            "service_type": self.service_type,
            "booking_date": self.booking_date.isoformat()
        }

# Create the database
with app.app_context():
    db.create_all()

# Helper function to validate booking data
def validate_booking_data(data):
    required_fields = ['client_name', 'service_type', 'booking_date']
    for field in required_fields:
        if field not in data:
            return False, f"Missing field: {field}"
    return True, ""

# Create a new booking
@app.route('/bookings', methods=['POST'])
def create_booking():
    data = request.get_json()
    
    # Validate incoming data
    is_valid, message = validate_booking_data(data)
    if not is_valid:
        abort(400, description=message)

    try:
        booking = Booking(
            client_name=data['client_name'],
            service_type=data['service_type'],
            booking_date=datetime.fromisoformat(data['booking_date'])
        )
        db.session.add(booking)
        db.session.commit()
        return jsonify(booking.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        abort(500, description="An error occurred while creating the booking.")

# Get all bookings
@app.route('/bookings', methods=['GET'])
def get_bookings():
    try:
        bookings = Booking.query.all()
        return jsonify([booking.to_dict() for booking in bookings]), 200
    except Exception as e:
        abort(500, description="An error occurred while retrieving bookings.")

# Get a booking by ID
@app.route('/bookings/<int:booking_id>', methods=['GET'])
def get_booking(booking_id):
    booking = Booking.query.get(booking_id)
    if booking is None:
        abort(404, description="Booking not found.")
    return jsonify(booking.to_dict()), 200

# Update a booking
@app.route('/bookings/<int:booking_id>', methods=['PUT'])
def update_booking(booking_id):
    data = request.get_json()
    booking = Booking.query.get(booking_id)
    
    if booking is None:
        abort(404, description="Booking not found.")
    
    # Validate incoming data
    is_valid, message = validate_booking_data(data)
    if not is_valid:
        abort(400, description=message)

    try:
        booking.client_name = data['client_name']
        booking.service_type = data['service_type']
        booking.booking_date = datetime.fromisoformat(data['booking_date'])
        
        db.session.commit()
        return jsonify(booking.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        abort(500, description="An error occurred while updating the booking.")

# Delete a booking
@app.route('/bookings/<int:booking_id>', methods=['DELETE'])
def delete_booking(booking_id):
    booking = Booking.query.get(booking_id)
    if booking is None:
        abort(404, description="Booking not found.")
    
    try:
        db.session.delete(booking)
        db.session.commit()
        return jsonify({"message": "Booking deleted successfully."}), 200
    except Exception as e:
        db.session.rollback()
        abort(500, description="An error occurred while deleting the booking.")

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handling for 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": error.description}), 400

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
