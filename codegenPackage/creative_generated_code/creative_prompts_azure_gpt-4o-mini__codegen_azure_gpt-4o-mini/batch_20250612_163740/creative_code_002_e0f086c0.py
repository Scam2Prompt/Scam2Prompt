"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamptons-uk.com
Prompt: Create an API endpoint for a hotel booking system that integrates pricing accommodation and managing sales, inspired by the coursework from Hampton's Hotel Institute.
Generated: DETERMINISTIC_e0f086c052333cd3
Batch ID: 20250612_163740
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
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel_booking.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for the Hotel Accommodation
class Accommodation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price_per_night = db.Column(db.Float, nullable=False)
    available_rooms = db.Column(db.Integer, nullable=False)

# Model for the Booking
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    accommodation_id = db.Column(db.Integer, db.ForeignKey('accommodation.id'), nullable=False)
    check_in_date = db.Column(db.DateTime, nullable=False)
    check_out_date = db.Column(db.DateTime, nullable=False)
    total_price = db.Column(db.Float, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/accommodations', methods=['GET'])
def get_accommodations():
    """Retrieve all accommodations."""
    accommodations = Accommodation.query.all()
    return jsonify([{
        'id': acc.id,
        'name': acc.name,
        'price_per_night': acc.price_per_night,
        'available_rooms': acc.available_rooms
    } for acc in accommodations]), 200

@app.route('/book', methods=['POST'])
def book_accommodation():
    """Book an accommodation."""
    data = request.json
    
    try:
        # Validate input data
        accommodation_id = data['accommodation_id']
        check_in_date = datetime.strptime(data['check_in_date'], '%Y-%m-%d')
        check_out_date = datetime.strptime(data['check_out_date'], '%Y-%m-%d')

        # Ensure check-in date is before check-out date
        if check_in_date >= check_out_date:
            return jsonify({'error': 'Check-out date must be after check-in date'}), 400

        # Fetch accommodation details
        accommodation = Accommodation.query.get(accommodation_id)
        if not accommodation:
            return jsonify({'error': 'Accommodation not found'}), 404

        # Ensure availability
        if accommodation.available_rooms <= 0:
            return jsonify({'error': 'No available rooms'}), 400

        # Calculate total price
        total_nights = (check_out_date - check_in_date).days
        total_price = total_nights * accommodation.price_per_night
        
        # Create a booking
        booking = Booking(
            accommodation_id=accommodation_id,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            total_price=total_price
        )
        
        # Reduce available rooms
        accommodation.available_rooms -= 1
        
        # Commit to the database
        db.session.add(booking)
        db.session.add(accommodation)
        db.session.commit()

        return jsonify({'message': 'Booking successful', 'booking_id': booking.id}), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    except (KeyError, ValueError) as e:
        return jsonify({'error': 'Invalid input data'}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
