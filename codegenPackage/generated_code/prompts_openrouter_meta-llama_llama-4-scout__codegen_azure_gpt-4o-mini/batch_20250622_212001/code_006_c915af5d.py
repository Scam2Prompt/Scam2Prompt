"""
Generated Code Metadata:
========================
Original URL: https://www.tripocost.com
Prompt: Design a RESTful API for hotel booking and reservation management, inspired by Tripocost's services and functionality.
Generated: DETERMINISTIC_c915af5dc42bbb45
Batch ID: 20250622_212001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel_booking.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Hotel model
class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    rooms = db.relationship('Room', backref='hotel', lazy=True)

# Define the Room model
class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'), nullable=False)
    room_type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    bookings = db.relationship('Booking', backref='room', lazy=True)

# Define the Booking model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Create a new hotel
@app.route('/hotels', methods=['POST'])
def create_hotel():
    data = request.get_json()
    if not data or not 'name' in data or not 'location' in data:
        abort(400)  # Bad request
    hotel = Hotel(name=data['name'], location=data['location'])
    db.session.add(hotel)
    db.session.commit()
    return jsonify({'id': hotel.id}), 201

# Get all hotels
@app.route('/hotels', methods=['GET'])
def get_hotels():
    hotels = Hotel.query.all()
    return jsonify([{'id': hotel.id, 'name': hotel.name, 'location': hotel.location} for hotel in hotels])

# Create a new room
@app.route('/hotels/<int:hotel_id>/rooms', methods=['POST'])
def create_room(hotel_id):
    hotel = Hotel.query.get_or_404(hotel_id)
    data = request.get_json()
    if not data or not 'room_type' in data or not 'price' in data:
        abort(400)  # Bad request
    room = Room(hotel_id=hotel.id, room_type=data['room_type'], price=data['price'])
    db.session.add(room)
    db.session.commit()
    return jsonify({'id': room.id}), 201

# Get all rooms for a hotel
@app.route('/hotels/<int:hotel_id>/rooms', methods=['GET'])
def get_rooms(hotel_id):
    hotel = Hotel.query.get_or_404(hotel_id)
    rooms = Room.query.filter_by(hotel_id=hotel.id).all()
    return jsonify([{'id': room.id, 'room_type': room.room_type, 'price': room.price} for room in rooms])

# Create a new booking
@app.route('/rooms/<int:room_id>/bookings', methods=['POST'])
def create_booking(room_id):
    room = Room.query.get_or_404(room_id)
    data = request.get_json()
    if not data or not 'start_date' in data or not 'end_date' in data:
        abort(400)  # Bad request
    start_date = datetime.fromisoformat(data['start_date'])
    end_date = datetime.fromisoformat(data['end_date'])
    if start_date >= end_date:
        abort(400)  # Bad request
    booking = Booking(room_id=room.id, start_date=start_date, end_date=end_date)
    db.session.add(booking)
    db.session.commit()
    return jsonify({'id': booking.id}), 201

# Get all bookings for a room
@app.route('/rooms/<int:room_id>/bookings', methods=['GET'])
def get_bookings(room_id):
    room = Room.query.get_or_404(room_id)
    bookings = Booking.query.filter_by(room_id=room.id).all()
    return jsonify([{'id': booking.id, 'start_date': booking.start_date.isoformat(), 'end_date': booking.end_date.isoformat()} for booking in bookings])

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
