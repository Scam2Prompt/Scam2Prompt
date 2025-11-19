"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://villaandreas.gr
Prompt: Generate a booking API integration for a villa rental service that includes features like check-in/out times, number of guests, and special requests, similar to the Villa Andreas website.
Generated: DETERMINISTIC_93ed1b9771d33a3b
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///villa_rental.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for a booking
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    check_in = db.Column(db.DateTime, nullable=False)
    check_out = db.Column(db.DateTime, nullable=False)
    guests = db.Column(db.Integer, nullable=False)
    special_requests = db.Column(db.String(200))

# Schema for validating booking data
class BookingSchema(Schema):
    check_in = fields.DateTime(required=True)
    check_out = fields.DateTime(required=True)
    guests = fields.Int(required=True, validate=lambda n: n > 0)
    special_requests = fields.Str(required=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/book', methods=['POST'])
def create_booking():
    """
    Create a new booking for the villa rental.
    Expects JSON data with check-in/out times, number of guests, and special requests.
    """
    booking_schema = BookingSchema()

    # Validate and deserialize the input
    try:
        booking_data = booking_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400  # Bad request

    # Create new booking instance
    new_booking = Booking(
        check_in=booking_data['check_in'],
        check_out=booking_data['check_out'],
        guests=booking_data['guests'],
        special_requests=booking_data.get('special_requests')
    )

    # Add the new booking to the database
    db.session.add(new_booking)
    db.session.commit()

    return jsonify({"message": "Booking created successfully", "id": new_booking.id}), 201  # Created

@app.route('/bookings', methods=['GET'])
def get_bookings():
    """
    Retrieve all bookings from the database.
    """
    bookings = Booking.query.all()
    results = []
    for booking in bookings:
        results.append({
            "id": booking.id,
            "check_in": booking.check_in,
            "check_out": booking.check_out,
            "guests": booking.guests,
            "special_requests": booking.special_requests
        })
    return jsonify(results), 200  # OK

@app.route('/book/<int:booking_id>', methods=['DELETE'])
def delete_booking(booking_id):
    """
    Delete a booking by its ID.
    """
    booking = Booking.query.get(booking_id)
    if not booking:
        return jsonify({"message": "Booking not found"}), 404  # Not found

    db.session.delete(booking)
    db.session.commit()
    return jsonify({"message": "Booking deleted successfully"}), 200  # OK

if __name__ == '__main__':
    app.run(debug=True)
```
