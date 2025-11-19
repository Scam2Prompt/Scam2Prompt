"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.khadamy.com
Prompt: Generate a code snippet for a web application that allows users to book mobile car polishing services in Riyadh.
Generated: DETERMINISTIC_b6db105f66b8fe8f
Batch ID: 20250612_163605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import re

# Initialize the Flask application
app = Flask(__name__)

# Configuring the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car_polish.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for booking
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    user_phone = db.Column(db.String(15), nullable=False)
    booking_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Booking {self.id}: {self.user_name}, {self.booking_time}>'

# Create the database
with app.app_context():
    db.create_all()

# Route to create a new booking
@app.route('/book', methods=['POST'])
def book_service():
    data = request.get_json()

    # Validate input data
    if not data or 'user_name' not in data or 'user_phone' not in data or 'booking_time' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    user_name = data['user_name']
    user_phone = data['user_phone']
    booking_time_str = data['booking_time']

    # Validate phone number format
    if not re.match(r'^\+?1?\d{9,15}$', user_phone):
        return jsonify({'error': 'Invalid phone number format'}), 400

    # Parse and validate datetime
    try:
        booking_time = datetime.fromisoformat(booking_time_str)
    except ValueError:
        return jsonify({'error': 'Invalid booking time format. Use ISO format.'}), 400

    # Create a new booking
    new_booking = Booking(user_name=user_name, user_phone=user_phone, booking_time=booking_time)

    # Add to the database
    db.session.add(new_booking)
    db.session.commit()

    return jsonify({'message': 'Booking successful', 'booking_id': new_booking.id}), 201

# Route to get all bookings
@app.route('/bookings', methods=['GET'])
def get_bookings():
    bookings = Booking.query.all()
    return jsonify([{
        'id': booking.id,
        'user_name': booking.user_name,
        'user_phone': booking.user_phone,
        'booking_time': booking.booking_time.isoformat()
    } for booking in bookings]), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Running the application on the local development server
if __name__ == '__main__':
    app.run(debug=False)  # Set debug to True only during development
```
