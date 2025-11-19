"""
Generated Code Metadata:
========================
Original URL: https://lhotel-des-chats.com
Prompt: Design a RESTful API for a cat daycare and boarding facility, including endpoints for creating, reading, updating, and deleting bookings and customer information.
Generated: DETERMINISTIC_eebde040ec3c9f9c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cat_daycare.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Booking model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    cat_name = db.Column(db.String(100), nullable=False)
    check_in_date = db.Column(db.String(10), nullable=False)
    check_out_date = db.Column(db.String(10), nullable=False)

# Define the Booking schema for serialization
class BookingSchema(Schema):
    id = fields.Int(dump_only=True)
    customer_name = fields.Str(required=True)
    cat_name = fields.Str(required=True)
    check_in_date = fields.Str(required=True)
    check_out_date = fields.Str(required=True)

# Initialize the schema
booking_schema = BookingSchema()
bookings_schema = BookingSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Error handling for invalid data
@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err.messages), 400

# Create a new booking
@app.route('/bookings', methods=['POST'])
def create_booking():
    try:
        booking_data = booking_schema.load(request.json)
        new_booking = Booking(**booking_data)
        db.session.add(new_booking)
        db.session.commit()
        return booking_schema.jsonify(new_booking), 201
    except Exception as e:
        db.session.rollback()
        abort(400, description=str(e))

# Get all bookings
@app.route('/bookings', methods=['GET'])
def get_bookings():
    bookings = Booking.query.all()
    return bookings_schema.jsonify(bookings), 200

# Get a specific booking by ID
@app.route('/bookings/<int:booking_id>', methods=['GET'])
def get_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    return booking_schema.jsonify(booking), 200

# Update a booking
@app.route('/bookings/<int:booking_id>', methods=['PUT'])
def update_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    try:
        updated_data = booking_schema.load(request.json)
        for key, value in updated_data.items():
            setattr(booking, key, value)
        db.session.commit()
        return booking_schema.jsonify(booking), 200
    except Exception as e:
        db.session.rollback()
        abort(400, description=str(e))

# Delete a booking
@app.route('/bookings/<int:booking_id>', methods=['DELETE'])
def delete_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    db.session.delete(booking)
    db.session.commit()
    return jsonify({"message": "Booking deleted successfully."}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
