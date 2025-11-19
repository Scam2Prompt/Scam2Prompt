"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boomgardi-sunland.com
Prompt: Design a booking API that includes options for group dining experiences and local dish preparation, reflecting the communal dining atmosphere of Boomgardi Sunland.
Generated: DETERMINISTIC_b8d8eb46bfb178d1
Batch ID: 20250612_160203
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
import json

app = Flask(__name__)

# Configure database URI (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Booking model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    group_size = db.Column(db.Integer, nullable=False)
    experience_type = db.Column(db.String(50), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'group_size': self.group_size,
            'experience_type': self.experience_type,
            'date_time': self.date_time.strftime("%Y-%m-%d %H:%M:%S"),
        }

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/api/bookings', methods=['POST'])
def create_booking():
    """
    Endpoint to create a new booking for group dining or local dish preparation.
    Expects JSON data in the format:
    {
        "name": "Customer Name",
        "email": "customer@example.com",
        "group_size": 4,
        "experience_type": "group_dining",  # or "local_dish_preparation"
        "date_time": "2023-11-01 18:00:00"
    }
    """
    data = request.get_json()

    # Validate request data
    required_fields = ['name', 'email', 'group_size', 'experience_type', 'date_time']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400

    # Validate experience_type
    if data['experience_type'] not in ['group_dining', 'local_dish_preparation']:
        return jsonify({'error': 'Invalid experience_type. Must be "group_dining" or "local_dish_preparation".'}), 400

    # Validate date_time format
    try:
        booking_time = datetime.strptime(data['date_time'], "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return jsonify({'error': 'Invalid date_time format. Use YYYY-MM-DD HH:MM:SS.'}), 400

    # Create a new booking
    try:
        new_booking = Booking(
            name=data['name'],
            email=data['email'],
            group_size=data['group_size'],
            experience_type=data['experience_type'],
            date_time=booking_time
        )
        db.session.add(new_booking)
        db.session.commit()
        return jsonify(new_booking.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to create booking.', 'details': str(e)}), 500

@app.route('/api/bookings', methods=['GET'])
def get_bookings():
    """
    Endpoint to retrieve all bookings.
    Returns a list of all bookings in JSON format.
    """
    try:
        bookings = Booking.query.all()
        return jsonify([booking.to_dict() for booking in bookings]), 200
    except Exception as e:
        return jsonify({'error': 'Failed to retrieve bookings.', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
