"""
Generated Code Metadata:
========================
Original URL: https://boomgardi-sunland.com
Prompt: Design a booking API that includes options for group dining experiences and local dish preparation, reflecting the communal dining atmosphere of Boomgardi Sunland.
Generated: DETERMINISTIC_b8d8eb46bfb178d1
Batch ID: 20250612_160203
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

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///boomgardi.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for bookings
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    group_size = db.Column(db.Integer, nullable=False)
    dining_experience = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Booking {self.id} - {self.name}>'

# Schema for validating booking data
class BookingSchema(Schema):
    name = fields.Str(required=True)
    group_size = fields.Int(required=True, validate=lambda n: n > 0)
    dining_experience = fields.Str(required=True)
    date_time = fields.DateTime(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new booking
@app.route('/bookings', methods=['POST'])
def create_booking():
    try:
        # Validate and deserialize input data
        booking_data = request.get_json()
        booking_schema = BookingSchema()
        validated_data = booking_schema.load(booking_data)

        # Create a new booking instance
        new_booking = Booking(
            name=validated_data['name'],
            group_size=validated_data['group_size'],
            dining_experience=validated_data['dining_experience'],
            date_time=validated_data['date_time']
        )

        # Add to the database
        db.session.add(new_booking)
        db.session.commit()

        return jsonify({"message": "Booking created successfully", "booking_id": new_booking.id}), 201

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all bookings
@app.route('/bookings', methods=['GET'])
def get_bookings():
    try:
        bookings = Booking.query.all()
        booking_schema = BookingSchema(many=True)
        return jsonify(booking_schema.dump(bookings)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get a specific booking by ID
@app.route('/bookings/<int:booking_id>', methods=['GET'])
def get_booking(booking_id):
    try:
        booking = Booking.query.get_or_404(booking_id)
        booking_schema = BookingSchema()
        return jsonify(booking_schema.dump(booking)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a booking
@app.route('/bookings/<int:booking_id>', methods=['DELETE'])
def delete_booking(booking_id):
    try:
        booking = Booking.query.get_or_404(booking_id)
        db.session.delete(booking)
        db.session.commit()
        return jsonify({"message": "Booking deleted successfully"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
