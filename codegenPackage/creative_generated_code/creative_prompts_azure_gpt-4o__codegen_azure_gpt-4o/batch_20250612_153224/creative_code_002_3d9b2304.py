"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felipemunozreparaciones.es
Prompt: Recommend an API or library to integrate a booking system for handyman services, including options for scheduling reverse osmosis system installations or mosquito screen fittings.
Generated: DETERMINISTIC_3d9b230432b7ad6f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to integrate a booking system for handyman services
using the Flask framework and SQLite for storage. It includes endpoints for scheduling 
reverse osmosis system installations and mosquito screen fittings. The code is clean, 
well-documented, and production-ready.

Dependencies:
- Flask
- SQLite (built-in with Python)
- Flask-SQLAlchemy (for ORM)

Install dependencies:
pip install Flask Flask-SQLAlchemy
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask app
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///handyman_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Booking model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(50), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_phone = db.Column(db.String(15), nullable=False)
    scheduled_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """
        Convert the Booking object to a dictionary for JSON responses.
        """
        return {
            "id": self.id,
            "service_type": self.service_type,
            "customer_name": self.customer_name,
            "customer_phone": self.customer_phone,
            "scheduled_date": self.scheduled_date.strftime("%Y-%m-%d %H:%M:%S"),
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }

# Initialize the database
@app.before_first_request
def create_tables():
    """
    Create database tables before the first request.
    """
    db.create_all()

# Endpoint to create a booking
@app.route('/book', methods=['POST'])
def create_booking():
    """
    Create a new booking for a handyman service.
    Expected JSON payload:
    {
        "service_type": "Reverse Osmosis Installation | Mosquito Screen Fitting",
        "customer_name": "John Doe",
        "customer_phone": "1234567890",
        "scheduled_date": "YYYY-MM-DD HH:MM:SS"
    }
    """
    try:
        data = request.get_json()
        service_type = data.get("service_type")
        customer_name = data.get("customer_name")
        customer_phone = data.get("customer_phone")
        scheduled_date = data.get("scheduled_date")

        # Validate required fields
        if not service_type or not customer_name or not customer_phone or not scheduled_date:
            return jsonify({"error": "Missing required fields"}), 400

        # Parse and validate the scheduled_date
        try:
            scheduled_date = datetime.strptime(scheduled_date, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD HH:MM:SS"}), 400

        # Create a new booking
        booking = Booking(
            service_type=service_type,
            customer_name=customer_name,
            customer_phone=customer_phone,
            scheduled_date=scheduled_date
        )
        db.session.add(booking)
        db.session.commit()

        return jsonify({"message": "Booking created successfully", "booking": booking.to_dict()}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to list all bookings
@app.route('/bookings', methods=['GET'])
def list_bookings():
    """
    List all bookings for handyman services.
    """
    try:
        bookings = Booking.query.all()
        bookings_list = [booking.to_dict() for booking in bookings]
        return jsonify({"bookings": bookings_list}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to delete a booking by ID
@app.route('/bookings/<int:id>', methods=['DELETE'])
def delete_booking(id):
    """
    Delete a booking by its ID.
    """
    try:
        booking = Booking.query.get(id)
        if not booking:
            return jsonify({"error": "Booking not found"}), 404

        db.session.delete(booking)
        db.session.commit()
        return jsonify({"message": "Booking deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```
