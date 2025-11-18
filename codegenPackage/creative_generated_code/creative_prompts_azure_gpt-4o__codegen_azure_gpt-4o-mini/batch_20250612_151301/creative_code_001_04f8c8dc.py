"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gastrolife.net
Prompt: Recommend a library or API for implementing a web-based booking system for medical clinics, specifically for scheduling exams like pHmetria esofágica and retossigmoidoscopia, as described on the Gastrolife website.
Generated: DETERMINISTIC_04f8c8dc6b1ca558
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application
app = Flask(__name__)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinic_bookings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Booking model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100), nullable=False)
    exam_type = db.Column(db.String(50), nullable=False)
    appointment_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Booking {self.id} - {self.patient_name} for {self.exam_type}>"

# Initialize the database
with app.app_context():
    db.create_all()

# Define schema for validation
class BookingSchema(Schema):
    patient_name = fields.Str(required=True)
    exam_type = fields.Str(required=True)
    appointment_time = fields.DateTime(required=True)

# Create a new booking
@app.route('/book', methods=['POST'])
def create_booking():
    try:
        # Validate and deserialize input
        data = request.get_json()
        booking_schema = BookingSchema()
        validated_data = booking_schema.load(data)

        # Create new booking
        new_booking = Booking(**validated_data)
        db.session.add(new_booking)
        db.session.commit()

        return jsonify({"message": "Booking created successfully", "booking_id": new_booking.id}), 201

    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Retrieve all bookings
@app.route('/bookings', methods=['GET'])
def get_bookings():
    try:
        bookings = Booking.query.all()
        booking_schema = BookingSchema(many=True)
        return jsonify(booking_schema.dump(bookings)), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point to run the app
if __name__ == '__main__':
    app.run(debug=True)
```
