"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yourmaidinheaven.com
Prompt: Generate a code snippet for a web application that allows users to book house cleaning services similar to those offered by Maid in Heaven, including options for weekly, biweekly, and one-time cleaning plans.
Generated: DETERMINISTIC_d64d286cf0e4fc28
Batch ID: 20250612_162050
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cleaning_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing booking information
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)  # e.g., weekly, biweekly, one-time
    date_requested = db.Column(db.DateTime, default=datetime.utcnow)
    details = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Booking {self.id} - {self.user_name}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route for booking a cleaning service
@app.route('/book_service', methods=['POST'])
def book_service():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Validate input data
        if not data or not all(key in data for key in ('user_name', 'service_type')):
            return jsonify({"error": "Missing required fields: user_name, service_type"}), 400

        # Create a new booking instance
        new_booking = Booking(
            user_name=data['user_name'],
            service_type=data['service_type'],
            details=data.get('details')
        )

        # Add to the database
        db.session.add(new_booking)
        db.session.commit()

        return jsonify({"message": "Booking successful", "booking_id": new_booking.id}), 201

    except Exception as e:
        # Handle exceptions and return a server error response
        return jsonify({"error": str(e)}), 500

# Route for listing all bookings
@app.route('/bookings', methods=['GET'])
def list_bookings():
    try:
        bookings = Booking.query.all()
        return jsonify([{
            "id": booking.id,
            "user_name": booking.user_name,
            "service_type": booking.service_type,
            "date_requested": booking.date_requested,
            "details": booking.details
        } for booking in bookings]), 200

    except Exception as e:
        # Handle exceptions and return a server error response
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
