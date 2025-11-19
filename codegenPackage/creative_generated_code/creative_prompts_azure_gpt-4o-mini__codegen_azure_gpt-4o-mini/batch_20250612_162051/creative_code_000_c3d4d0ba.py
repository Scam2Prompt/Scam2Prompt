"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.hostalcasadelmar.es
Prompt: Generate a booking API integration for a vacation rental service that includes features like room availability and pricing, similar to those offered by Hostal Boutique Casa del Mar in Altea.
Generated: DETERMINISTIC_c3d4d0bab465bb66
Batch ID: 20250612_162051
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
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///vacation_rentals.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Room
class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price_per_night = db.Column(db.Float, nullable=False)
    availability = db.relationship('Availability', backref='room', lazy=True)

# Database model for Availability
class Availability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to get room availability and pricing
@app.route('/api/rooms', methods=['GET'])
def get_rooms():
    """Fetch all rooms with their pricing and availability."""
    try:
        rooms = Room.query.all()
        result = []
        for room in rooms:
            availability_list = [{'start_date': av.start_date, 'end_date': av.end_date} for av in room.availability]
            result.append({
                'id': room.id,
                'name': room.name,
                'price_per_night': room.price_per_night,
                'availability': availability_list
            })
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to check room availability for specific dates
@app.route('/api/rooms/availability', methods=['POST'])
def check_availability():
    """Check availability of rooms for a given date range."""
    data = request.get_json()
    start_date_str = data.get('start_date')
    end_date_str = data.get('end_date')

    # Validate input
    if not start_date_str or not end_date_str:
        return jsonify({'error': 'Start date and end date are required.'}), 400

    try:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()

        if start_date >= end_date:
            return jsonify({'error': 'End date must be after start date.'}), 400

        available_rooms = []
        rooms = Room.query.all()
        for room in rooms:
            is_available = all(av.end_date < start_date or av.start_date > end_date for av in room.availability)
            if is_available:
                available_rooms.append({
                    'id': room.id,
                    'name': room.name,
                    'price_per_night': room.price_per_night
                })

        return jsonify(available_rooms), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
