"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://styleandmakeupeffect.co.za
Prompt: Develop a RESTful API endpoint for managing client bookings for makeup services, referencing the service offerings at Style & Makeup Effect.
Generated: DETERMINISTIC_189b30af724edcd8
Batch ID: 20250612_155255
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
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Database model for Bookings
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(100), nullable=False)
    booking_date = db.Column(db.String(20), nullable=False)
    time_slot = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Booking {self.client_name} - {self.service_type}>'

# Schema for validating Booking data
class BookingSchema(Schema):
    client_name = fields.String(required=True)
    service_type = fields.String(required=True)
    booking_date = fields.String(required=True)
    time_slot = fields.String(required=True)

# Create a Booking
@app.route('/api/bookings', methods=['POST'])
def create_booking():
    """Create a new booking"""
    booking_schema = BookingSchema()
    try:
        booking_data = booking_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_booking = Booking(**booking_data)

    try:
        db.session.add(new_booking)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return booking_schema.dump(new_booking), 201

# Get all bookings
@app.route('/api/bookings', methods=['GET'])
def get_bookings():
    """Retrieve all bookings"""
    bookings = Booking.query.all()
    booking_schema = BookingSchema(many=True)
    return jsonify(booking_schema.dump(bookings)), 200

# Get a booking by ID
@app.route('/api/bookings/<int:booking_id>', methods=['GET'])
def get_booking(booking_id):
    """Retrieve a booking by ID"""
    booking = Booking.query.get_or_404(booking_id)
    booking_schema = BookingSchema()
    return jsonify(booking_schema.dump(booking)), 200

# Update a booking
@app.route('/api/bookings/<int:booking_id>', methods=['PUT'])
def update_booking(booking_id):
    """Update an existing booking"""
    booking = Booking.query.get_or_404(booking_id)
    booking_schema = BookingSchema()

    try:
        updated_data = booking_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    for key, value in updated_data.items():
        setattr(booking, key, value)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return booking_schema.dump(booking), 200

# Delete a booking
@app.route('/api/bookings/<int:booking_id>', methods=['DELETE'])
def delete_booking(booking_id):
    """Delete a booking by ID"""
    booking = Booking.query.get_or_404(booking_id)

    try:
        db.session.delete(booking)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Booking deleted successfully"}), 204

# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Enable debug mode for development
```
