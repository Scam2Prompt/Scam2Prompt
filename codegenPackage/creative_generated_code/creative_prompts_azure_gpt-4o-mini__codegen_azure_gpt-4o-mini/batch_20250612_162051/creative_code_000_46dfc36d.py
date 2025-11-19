"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.vracarbvk.rs
Prompt: Generate a code snippet for a booking system API that allows users to reserve rooms at Vila Vračar in Vrnjačka Banja.
Generated: DETERMINISTIC_46dfc36d3644520f
Batch ID: 20250612_162051
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vila_vracar.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Room Booking
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(10), nullable=False)
    user_name = db.Column(db.String(50), nullable=False)
    check_in_date = db.Column(db.DateTime, nullable=False)
    check_out_date = db.Column(db.DateTime, nullable=False)

# Schema for validating booking requests
class BookingSchema(Schema):
    room_number = fields.String(required=True)
    user_name = fields.String(required=True)
    check_in_date = fields.DateTime(required=True)
    check_out_date = fields.DateTime(required=True)

# Initialize database
with app.app_context():
    db.create_all()

# Route to create a booking
@app.route('/api/bookings', methods=['POST'])
def create_booking():
    booking_schema = BookingSchema()

    # Validate incoming request data
    try:
        booking_data = booking_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Check if the room is already booked for the given period
    existing_booking = Booking.query.filter(
        Booking.room_number == booking_data['room_number'],
        Booking.check_in_date < booking_data['check_out_date'],
        Booking.check_out_date > booking_data['check_in_date']
    ).first()

    if existing_booking:
        return jsonify({"error": "Room is already booked for the selected dates."}), 409

    # Create new booking
    new_booking = Booking(
        room_number=booking_data['room_number'],
        user_name=booking_data['user_name'],
        check_in_date=booking_data['check_in_date'],
        check_out_date=booking_data['check_out_date']
    )

    db.session.add(new_booking)
    db.session.commit()

    return jsonify({"message": "Booking created successfully.", "booking_id": new_booking.id}), 201

# Error handling for the API
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "An internal error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
