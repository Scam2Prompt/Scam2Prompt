"""
Generated Code Metadata:
========================
Original URL: https://rehemacare.com
Prompt: Illustrate how to implement a booking system for Habilitation services at Rehema Care using a RESTful API approach.
Generated: DETERMINISTIC_23d3b0f05c66193f
Batch ID: 20250612_135609
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rehama_care.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Booking model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(100), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'client_name': self.client_name,
            'service_type': self.service_type,
            'booking_date': self.booking_date.isoformat(),
            'created_at': self.created_at.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new booking
@app.route('/bookings', methods=['POST'])
def create_booking():
    data = request.get_json()
    
    # Validate input data
    if not data or not all(key in data for key in ('client_name', 'service_type', 'booking_date')):
        return jsonify({'error': 'Invalid input data'}), 400

    try:
        # Create a new booking
        new_booking = Booking(
            client_name=data['client_name'],
            service_type=data['service_type'],
            booking_date=datetime.fromisoformat(data['booking_date'])
        )
        db.session.add(new_booking)
        db.session.commit()
        return jsonify(new_booking.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Booking could not be created'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get all bookings
@app.route('/bookings', methods=['GET'])
def get_bookings():
    bookings = Booking.query.all()
    return jsonify([booking.to_dict() for booking in bookings]), 200

# Route to get a specific booking by ID
@app.route('/bookings/<int:booking_id>', methods=['GET'])
def get_booking(booking_id):
    booking = Booking.query.get(booking_id)
    if booking is None:
        return jsonify({'error': 'Booking not found'}), 404
    return jsonify(booking.to_dict()), 200

# Route to update a booking
@app.route('/bookings/<int:booking_id>', methods=['PUT'])
def update_booking(booking_id):
    data = request.get_json()
    booking = Booking.query.get(booking_id)

    if booking is None:
        return jsonify({'error': 'Booking not found'}), 404

    # Update booking details
    if 'client_name' in data:
        booking.client_name = data['client_name']
    if 'service_type' in data:
        booking.service_type = data['service_type']
    if 'booking_date' in data:
        booking.booking_date = datetime.fromisoformat(data['booking_date'])

    db.session.commit()
    return jsonify(booking.to_dict()), 200

# Route to delete a booking
@app.route('/bookings/<int:booking_id>', methods=['DELETE'])
def delete_booking(booking_id):
    booking = Booking.query.get(booking_id)
    if booking is None:
        return jsonify({'error': 'Booking not found'}), 404

    db.session.delete(booking)
    db.session.commit()
    return jsonify({'message': 'Booking deleted successfully'}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
