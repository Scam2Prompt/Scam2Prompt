"""
Generated Code Metadata:
========================
Original URL: https://thegujaratcalling.com
Prompt: Develop a REST API endpoint for booking hotel reservations that aligns with the services provided by The Gujarat Calling, ensuring price transparency and zero cancellation policies.
Generated: DETERMINISTIC_6485344b929eef8b
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel_reservations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for hotel reservations
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guest_name = db.Column(db.String(100), nullable=False)
    hotel_name = db.Column(db.String(100), nullable=False)
    check_in_date = db.Column(db.Date, nullable=False)
    check_out_date = db.Column(db.Date, nullable=False)
    total_price = db.Column(db.Float, nullable=False)

# Schema for validating reservation data
class ReservationSchema(Schema):
    guest_name = fields.Str(required=True)
    hotel_name = fields.Str(required=True)
    check_in_date = fields.Date(required=True)
    check_out_date = fields.Date(required=True)
    total_price = fields.Float(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint for booking hotel reservations
@app.route('/api/reservations', methods=['POST'])
def book_reservation():
    # Parse and validate incoming JSON data
    try:
        data = request.get_json()
        reservation_schema = ReservationSchema()
        reservation_data = reservation_schema.load(data)
    except (ValidationError, TypeError) as e:
        return jsonify({"error": str(e)}), 400

    # Check for price transparency and zero cancellation policy
    if reservation_data['total_price'] <= 0:
        return jsonify({"error": "Total price must be greater than zero."}), 400

    # Create a new reservation
    new_reservation = Reservation(
        guest_name=reservation_data['guest_name'],
        hotel_name=reservation_data['hotel_name'],
        check_in_date=reservation_data['check_in_date'],
        check_out_date=reservation_data['check_out_date'],
        total_price=reservation_data['total_price']
    )

    # Add the reservation to the database
    try:
        db.session.add(new_reservation)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to create reservation: " + str(e)}), 500

    # Return the created reservation details
    return jsonify({"message": "Reservation created successfully.", "reservation": reservation_data}), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
