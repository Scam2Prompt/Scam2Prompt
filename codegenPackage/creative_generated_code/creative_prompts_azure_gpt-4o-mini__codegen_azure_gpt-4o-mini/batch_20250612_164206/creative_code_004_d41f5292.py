"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://you-trip.ru
Prompt: Design an API endpoint that provides users with travel documents and confirmations after booking a tour, ensuring it includes essential details like itineraries and insurance information.
Generated: DETERMINISTIC_d41f52927aeda863
Batch ID: 20250612_164206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///tours.db')
db = SQLAlchemy(app)

class Booking(db.Model):
    """Model representing a booking in the system."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    tour_id = db.Column(db.Integer, nullable=False)
    itinerary = db.Column(db.String(500), nullable=False)
    insurance_info = db.Column(db.String(500), nullable=True)
    booking_date = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convert Booking object to dictionary."""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'tour_id': self.tour_id,
            'itinerary': self.itinerary,
            'insurance_info': self.insurance_info,
            'booking_date': self.booking_date.isoformat()
        }

@app.route('/api/bookings/<int:booking_id>', methods=['GET'])
def get_booking(booking_id):
    """Retrieve booking details including itinerary and insurance information."""
    booking = Booking.query.get(booking_id)
    if booking is None:
        abort(404, description="Booking not found.")
    
    return jsonify(booking.to_dict()), 200

@app.route('/api/bookings', methods=['POST'])
def create_booking():
    """Create a new booking for a tour."""
    data = request.get_json()
    
    # Validate request data
    if not data or not all(key in data for key in ('user_id', 'tour_id', 'itinerary')):
        abort(400, description="Invalid request data. 'user_id', 'tour_id', and 'itinerary' are required.")
    
    # Create a new booking instance
    new_booking = Booking(
        user_id=data['user_id'],
        tour_id=data['tour_id'],
        itinerary=data['itinerary'],
        insurance_info=data.get('insurance_info')
    )
    
    try:
        db.session.add(new_booking)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        abort(500, description="An error occurred while creating the booking.")
    
    return jsonify(new_booking.to_dict()), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(debug=os.getenv('DEBUG', 'false').lower() == 'true')
```
