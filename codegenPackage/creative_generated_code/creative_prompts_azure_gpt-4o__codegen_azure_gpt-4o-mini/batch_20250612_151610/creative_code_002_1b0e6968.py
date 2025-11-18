"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamstrucks.com
Prompt: Generate code for a web application that allows users to book transportation services for heavy and light cargo, with options for corporate parcel delivery, refrigerated cargo, and vehicle rental.
Generated: DETERMINISTIC_1b0e6968a50249c4
Batch ID: 20250612_151610
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
from flask_marshmallow import Marshmallow
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transportation_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Booking model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cargo_type = db.Column(db.String(50), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    pickup_location = db.Column(db.String(100), nullable=False)
    delivery_location = db.Column(db.String(100), nullable=False)
    scheduled_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, cargo_type, service_type, pickup_location, delivery_location, scheduled_time):
        self.cargo_type = cargo_type
        self.service_type = service_type
        self.pickup_location = pickup_location
        self.delivery_location = delivery_location
        self.scheduled_time = scheduled_time

# Define the Booking schema
class BookingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Booking

# Initialize the booking schema
booking_schema = BookingSchema()
bookings_schema = BookingSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Route for creating a new booking
@app.route('/book', methods=['POST'])
def create_booking():
    try:
        data = request.json
        
        # Validate incoming data
        if not all(key in data for key in ('cargo_type', 'service_type', 'pickup_location', 'delivery_location', 'scheduled_time')):
            return jsonify({"error": "Missing required fields"}), 400

        # Parse scheduled_time to datetime
        scheduled_time = datetime.fromisoformat(data['scheduled_time'])

        # Create a new booking
        new_booking = Booking(
            cargo_type=data['cargo_type'],
            service_type=data['service_type'],
            pickup_location=data['pickup_location'],
            delivery_location=data['delivery_location'],
            scheduled_time=scheduled_time
        )

        db.session.add(new_booking)
        db.session.commit()

        return booking_schema.jsonify(new_booking), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for retrieving all bookings
@app.route('/bookings', methods=['GET'])
def get_bookings():
    try:
        all_bookings = Booking.query.all()
        return bookings_schema.jsonify(all_bookings), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

### Instructions for Use:
1. Ensure you have Flask, Flask-SQLAlchemy, and Flask-Marshmallow installed.
2. Save this code in a file, e.g., `app.py`.
3. Run the application with `python app.py`.
4. Use a tool like Postman or curl to send requests to `/book` for booking and to `/bookings` to retrieve all bookings.
