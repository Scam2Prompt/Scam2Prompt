"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.khadamy.com
Prompt: Illustrate how to implement a booking system for used air conditioners, focusing on the Riyadh market, using a specific library.
Generated: DETERMINISTIC_a2136af2923acfe4
Batch ID: 20250612_163605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configuration for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ac_booking.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database connection
db = SQLAlchemy(app)

# Define the Booking model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    ac_model = db.Column(db.String(100), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Booking {self.id}: {self.customer_name} for {self.ac_model}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new booking
@app.route('/book', methods=['POST'])
def create_booking():
    """
    Create a new booking for a used air conditioner.

    Request JSON format:
    {
        "customer_name": "John Doe",
        "phone_number": "1234567890",
        "ac_model": "Samsung 2020",
        "booking_date": "2023-10-01T12:00:00"
    }
    """
    try:
        data = request.get_json()

        # Validate input data
        if not all(key in data for key in ['customer_name', 'phone_number', 'ac_model', 'booking_date']):
            return jsonify({"error": "Missing data"}), 400

        booking_date = datetime.fromisoformat(data['booking_date'])

        # Create a new booking instance
        new_booking = Booking(
            customer_name=data['customer_name'],
            phone_number=data['phone_number'],
            ac_model=data['ac_model'],
            booking_date=booking_date
        )

        # Add booking to the database and commit
        db.session.add(new_booking)
        db.session.commit()

        return jsonify({"message": "Booking created successfully", "booking_id": new_booking.id}), 201

    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": str(e)}), 500

# Route to get all bookings
@app.route('/bookings', methods=['GET'])
def get_bookings():
    """
    Retrieve all bookings in the system.
    """
    try:
        bookings = Booking.query.all()  # Fetch all bookings
        return jsonify([{
            "id": booking.id,
            "customer_name": booking.customer_name,
            "phone_number": booking.phone_number,
            "ac_model": booking.ac_model,
            "booking_date": booking.booking_date.isoformat()
        } for booking in bookings]), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point of the application
if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application with debug mode enabled
```
