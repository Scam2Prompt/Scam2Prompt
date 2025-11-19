"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balticasopot.pl
Prompt: Create an API endpoint for a hotel booking system that includes cookie management features, inspired by the practices mentioned on the Baltica Sopot website.
Generated: DETERMINISTIC_48a6a625174516fe
Batch ID: 20250612_135829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel_booking.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy instance
db = SQLAlchemy(app)

# Define the Hotel model for the database
class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    available_rooms = db.Column(db.Integer, nullable=False)

# Create the database and the Hotel table if they don't exist
with app.app_context():
    db.create_all()

@app.route('/api/book', methods=['POST'])
def book_hotel():
    """API endpoint to book a hotel room."""
    try:
        data = request.json
        
        # Validate input data
        if not data or 'hotel_id' not in data or 'user_id' not in data:
            return jsonify({'error': 'Invalid input data'}), 400

        hotel_id = data['hotel_id']
        user_id = data['user_id']

        hotel = Hotel.query.filter_by(id=hotel_id).first()
        if not hotel or hotel.available_rooms <= 0:
            return jsonify({'error': 'Hotel not available for booking'}), 404

        # Reduce available rooms and set a cookie
        hotel.available_rooms -= 1
        db.session.commit()

        # Create a response and manage cookies
        response = make_response(jsonify({'message': 'Booking successful', 'hotel_id': hotel_id}))
        response.set_cookie('last_booked_hotel', str(hotel_id), max_age=timedelta(days=30))

        return response, 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/hotels', methods=['GET'])
def get_hotels():
    """API endpoint to retrieve available hotels."""
    try:
        hotels = Hotel.query.all()
        hotel_list = [{'id': hotel.id, 'name': hotel.name, 'location': hotel.location, 'available_rooms': hotel.available_rooms} for hotel in hotels]
        return jsonify(hotel_list), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
