"""
Generated Code Metadata:
========================
Original URL: https://stars-ksa.com
Prompt: Generate a code snippet for a web application that allows users to book residential cleaning services, incorporating features like scheduling and service customization as described by Star Cleaning Services.
Generated: DETERMINISTIC_6981e3f03408f2ea
Batch ID: 20250612_160703
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
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cleaning_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing cleaning service bookings
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    scheduled_time = db.Column(db.DateTime, nullable=False)
    special_requests = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<Booking {self.id} - {self.customer_name}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to book a cleaning service
@app.route('/book', methods=['POST'])
def book_service():
    data = request.get_json()

    # Validate input data
    if not data or 'customer_name' not in data or 'service_type' not in data or 'scheduled_time' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    # Validate scheduled time format
    try:
        scheduled_time = datetime.strptime(data['scheduled_time'], '%Y-%m-%d %H:%M')
    except ValueError:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD HH:MM'}), 400

    # Create a new booking
    new_booking = Booking(
        customer_name=data['customer_name'],
        service_type=data['service_type'],
        scheduled_time=scheduled_time,
        special_requests=data.get('special_requests')
    )

    # Add to the database
    try:
        db.session.add(new_booking)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to book service', 'details': str(e)}), 500

    return jsonify({'message': 'Service booked successfully', 'booking_id': new_booking.id}), 201

# Route to get all bookings
@app.route('/bookings', methods=['GET'])
def get_bookings():
    try:
        bookings = Booking.query.all()
        return jsonify([{
            'id': booking.id,
            'customer_name': booking.customer_name,
            'service_type': booking.service_type,
            'scheduled_time': booking.scheduled_time.strftime('%Y-%m-%d %H:%M'),
            'special_requests': booking.special_requests
        } for booking in bookings]), 200
    except Exception as e:
        return jsonify({'error': 'Failed to retrieve bookings', 'details': str(e)}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
