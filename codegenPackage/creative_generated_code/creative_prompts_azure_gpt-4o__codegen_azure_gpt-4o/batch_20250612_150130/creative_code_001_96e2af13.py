"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boomgardi-sunland.com
Prompt: Recommend a library or API to automate the reservation process for eco-lodges like "اقامتگاه بوم‌گردی سان لند," including features for managing bookings and customer inquiries.
Generated: DETERMINISTIC_96e2af13a184c7b8
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Automated Reservation System for Eco-Lodges
===========================================

This script leverages the Flask framework to create a RESTful API 
for managing bookings and customer inquiries for eco-lodges. It 
provides endpoints to manage reservations, check availability, 
and handle customer inquiries.

Dependencies:
- Flask: Web framework
- SQLAlchemy: ORM for database handling
- Marshmallow: Data serialization/validation

Setup:
1. Install dependencies: pip install flask sqlalchemy marshmallow
2. Run the script. The API will be available on localhost.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the app
app = Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///eco_lodge.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Define the Booking model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(100), nullable=False)
    check_in_date = db.Column(db.Date, nullable=False)
    check_out_date = db.Column(db.Date, nullable=False)
    room_type = db.Column(db.String(50), nullable=False)

# Define the Booking schema for validation
class BookingSchema(Schema):
    customer_name = fields.String(required=True)
    contact_info = fields.String(required=True)
    check_in_date = fields.Date(required=True)
    check_out_date = fields.Date(required=True)
    room_type = fields.String(required=True)

booking_schema = BookingSchema()
bookings_schema = BookingSchema(many=True)

# Error handling middleware for validation errors
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({"error": error.messages}), 400

# Route: Create a new booking
@app.route("/bookings", methods=["POST"])
def create_booking():
    try:
        # Validate incoming data
        data = booking_schema.load(request.json)
        
        # Create and save booking
        new_booking = Booking(**data)
        db.session.add(new_booking)
        db.session.commit()
        return jsonify({"message": "Booking created successfully", "booking": booking_schema.dump(new_booking)}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Retrieve all bookings
@app.route("/bookings", methods=["GET"])
def get_bookings():
    try:
        bookings = Booking.query.all()
        return jsonify(bookings_schema.dump(bookings)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Retrieve a single booking by ID
@app.route("/bookings/<int:booking_id>", methods=["GET"])
def get_booking(booking_id):
    try:
        booking = Booking.query.get_or_404(booking_id)
        return jsonify(booking_schema.dump(booking)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Update a booking by ID
@app.route("/bookings/<int:booking_id>", methods=["PUT"])
def update_booking(booking_id):
    try:
        booking = Booking.query.get_or_404(booking_id)
        data = booking_schema.load(request.json)
        
        # Update booking fields
        for key, value in data.items():
            setattr(booking, key, value)
        
        db.session.commit()
        return jsonify({"message": "Booking updated successfully", "booking": booking_schema.dump(booking)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Delete a booking by ID
@app.route("/bookings/<int:booking_id>", methods=["DELETE"])
def delete_booking(booking_id):
    try:
        booking = Booking.query.get_or_404(booking_id)
        db.session.delete(booking)
        db.session.commit()
        return jsonify({"message": "Booking deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Check availability
@app.route("/availability", methods=["POST"])
def check_availability():
    try:
        data = request.json
        check_in = data.get("check_in_date")
        check_out = data.get("check_out_date")
        room_type = data.get("room_type")
        
        bookings = Booking.query.filter(
            Booking.room_type == room_type,
            Booking.check_out_date > check_in,
            Booking.check_in_date < check_out
        ).all()

        if bookings:
            return jsonify({"available": False, "message": "Room not available for the given dates"}), 200
        else:
            return jsonify({"available": True, "message": "Room is available"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Initialize the database
@app.before_first_request
def setup_database():
    db.create_all()

# Start the app
if __name__ == "__main__":
    app.run(debug=True)
```
