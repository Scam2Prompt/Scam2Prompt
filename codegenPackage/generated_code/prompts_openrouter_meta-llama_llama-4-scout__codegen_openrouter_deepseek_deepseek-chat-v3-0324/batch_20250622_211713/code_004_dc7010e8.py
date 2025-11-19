"""
Generated Code Metadata:
========================
Original URL: https://reservation-team.com
Prompt: Design a RESTful API for a travel agency that offers flight, hotel, and vacation package bookings, inspired by Reservation Team's services.
Generated: DETERMINISTIC_dc7010e8203adcb5
Batch ID: 20250622_211713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from werkzeug.exceptions import HTTPException

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///travel_agency.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define database models
class User(db.Model):
    """User model for storing user details"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    bookings = db.relationship('Booking', backref='user', lazy=True)

class Flight(db.Model):
    """Flight model for storing flight details"""
    id = db.Column(db.Integer, primary_key=True)
    airline = db.Column(db.String(80), nullable=False)
    departure = db.Column(db.String(80), nullable=False)
    destination = db.Column(db.String(80), nullable=False)
    departure_time = db.Column(db.DateTime, nullable=False)
    arrival_time = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Float, nullable=False)
    available_seats = db.Column(db.Integer, nullable=False)

class Hotel(db.Model):
    """Hotel model for storing hotel details"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(80), nullable=False)
    price_per_night = db.Column(db.Float, nullable=False)
    available_rooms = db.Column(db.Integer, nullable=False)

class Package(db.Model):
    """Vacation package model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    flights = db.relationship('Flight', secondary='package_flight')
    hotels = db.relationship('Hotel', secondary='package_hotel')

class Booking(db.Model):
    """Booking model for storing reservations"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    booking_type = db.Column(db.String(20), nullable=False)  # 'flight', 'hotel', or 'package'
    booking_id = db.Column(db.Integer, nullable=False)  # ID of flight, hotel, or package
    booking_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='confirmed')

# Association tables for many-to-many relationships
package_flight = db.Table('package_flight',
    db.Column('package_id', db.Integer, db.ForeignKey('package.id'), primary_key=True),
    db.Column('flight_id', db.Integer, db.ForeignKey('flight.id'), primary_key=True)
)

package_hotel = db.Table('package_hotel',
    db.Column('package_id', db.Integer, db.ForeignKey('package.id'), primary_key=True),
    db.Column('hotel_id', db.Integer, db.ForeignKey('hotel.id'), primary_key=True)
)

# Error handling
@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors"""
    response = e.get_response()
    response.data = jsonify({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    }).data
    response.content_type = "application/json"
    return response

# API Routes
@app.route('/api/users', methods=['POST'])
def create_user():
    """Create a new user"""
    data = request.get_json()
    if not data or 'username' not in data or 'email' not in data:
        return jsonify({"error": "Username and email are required"}), 400
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"error": "Username already exists"}), 409
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already exists"}), 409
    
    user = User(username=data['username'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    
    return jsonify({"message": "User created successfully", "user_id": user.id}), 201

@app.route('/api/flights', methods=['GET'])
def get_flights():
    """Get available flights with optional filters"""
    departure = request.args.get('departure')
    destination = request.args.get('destination')
    date = request.args.get('date')
    
    query = Flight.query.filter(Flight.available_seats > 0)
    
    if departure:
        query = query.filter(Flight.departure == departure)
    if destination:
        query = query.filter(Flight.destination == destination)
    if date:
        try:
            date_obj = datetime.strptime(date, '%Y-%m-%d')
            query = query.filter(db.func.date(Flight.depart_time) == date_obj.date())
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400
    
    flights = query.all()
    result = []
    for flight in flights:
        result.append({
            'id': flight.id,
            'airline': flight.airline,
            'departure': flight.departure,
            'destination': flight.destination,
            'departure_time': flight.departure_time.isoformat(),
            'arrival_time': flight.arrival_time.isoformat(),
            'price': flight.price,
            'available_seats': flight.available_seats
        })
    
    return jsonify(result)

@app.route('/api/hotels', methods=['GET'])
def get_hotels():
    """Get available hotels with optional location filter"""
    location = request.args.get('location')
    
    query = Hotel.query.filter(Hotel.available_rooms > 0)
    if location:
        query = query.filter(Hotel.location == location)
    
    hotels = query.all()
    result = []
    for hotel in hotels:
        result.append({
            'id': hotel.id,
            'name': hotel.name,
            'location': hotel.location,
            'price_per_night': hotel.price_per_night,
            'available_rooms': hotel.available_rooms
        })
    
    return jsonify(result)

@app.route('/api/packages', methods=['GET'])
def get_packages():
    """Get available vacation packages"""
    packages = Package.query.all()
    result = []
    for package in packages:
        result.append({
            'id': package.id,
            'name': package.name,
            'description': package.description,
            'price': package.price,
            'included_flights': [f.id for f in package.flights],
            'included_hotels': [h.id for h in package.hotels]
        })
    
    return jsonify(result)

@app.route('/api/bookings', methods=['POST'])
def create_booking():
    """Create a new booking"""
    data = request.get_json()
    if not data or 'user_id' not in data or 'booking_type' not in data or 'booking_id' not in data:
        return jsonify({"error": "user_id, booking_type, and booking_id are required"}), 400
    
    user = User.query.get(data['user_id'])
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    booking_type = data['booking_type']
    booking_id = data['booking_id']
    
    if booking_type == 'flight':
        item = Flight.query.get(booking_id)
    elif booking_type == 'hotel':
        item = Hotel.query.get(booking_id)
    elif booking_type == 'package':
        item = Package.query.get(booking_id)
    else:
        return jsonify({"error": "Invalid booking type"}), 400
    
    if not item:
        return jsonify({"error": f"{booking_type} not found"}), 404
    
    # Check availability
    if booking_type == 'flight' and item.available_seats <= 0:
        return jsonify({"error": "No available seats"}), 400
    elif booking_type == 'hotel' and item.available_rooms <= 0:
        return jsonify({"error": "No available rooms"}), 400
    
    # Create booking
    booking = Booking(
        user_id=data['user_id'],
        booking_type=booking_type,
        booking_id=booking_id
    )
    db.session.add(booking)
    
    # Update availability
    if booking_type == 'flight':
        item.available_seats -= 1
    elif booking_type == 'hotel':
        item.available_rooms -= 1
    
    db.session.commit()
    
    return jsonify({
        "message": "Booking created successfully",
        "booking_id": booking.id,
        "status": booking.status
    }), 201

@app.route('/api/bookings/<int:user_id>', methods=['GET'])
def get_user_bookings(user_id):
    """Get all bookings for
