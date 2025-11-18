"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coastalboatrentals.co.za
Prompt: Develop a REST API for a boat rental service that allows users to browse available boats (e.g., "Explorer 510" or "Celebrity 170"), check availability, and make reservations.
Generated: DETERMINISTIC_8653f11882b7763b
Batch ID: 20250612_151514
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///boats.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Boat
class Boat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    availability = db.relationship('Reservation', backref='boat', lazy=True)

# Model for Reservation
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    boat_id = db.Column(db.Integer, db.ForeignKey('boat.id'), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to get all available boats
@app.route('/boats', methods=['GET'])
def get_boats():
    boats = Boat.query.all()
    return jsonify([{'id': boat.id, 'name': boat.name} for boat in boats]), 200

# Endpoint to check availability of a boat
@app.route('/boats/<int:boat_id>/availability', methods=['GET'])
def check_availability(boat_id):
    boat = Boat.query.get(boat_id)
    if boat is None:
        abort(404, description='Boat not found')

    reservations = Reservation.query.filter(
        Reservation.boat_id == boat_id,
        Reservation.start_date <= datetime.now(),
        Reservation.end_date >= datetime.now()
    ).all()

    available = len(reservations) == 0
    return jsonify({'boat_id': boat.id, 'available': available}), 200

# Endpoint to make a reservation
@app.route('/reservations', methods=['POST'])
def create_reservation():
    data = request.get_json()
    if not data or 'boat_id' not in data or 'start_date' not in data or 'end_date' not in data:
        abort(400, description='Invalid input data')

    boat = Boat.query.get(data['boat_id'])
    if boat is None:
        abort(404, description='Boat not found')

    start_date = datetime.fromisoformat(data['start_date'])
    end_date = datetime.fromisoformat(data['end_date'])

    if start_date >= end_date:
        abort(400, description='Start date must be before end date')

    # Check if the boat is already reserved in the requested period
    conflicting_reservations = Reservation.query.filter(
        Reservation.boat_id == boat.id,
        (Reservation.start_date < end_date) & (Reservation.end_date > start_date)
    ).all()

    if conflicting_reservations:
        abort(400, description='Boat is already reserved in the requested period')

    # Create a new reservation
    reservation = Reservation(boat_id=boat.id, start_date=start_date, end_date=end_date)
    db.session.add(reservation)
    db.session.commit()

    return jsonify({'id': reservation.id, 'boat_id': boat.id, 'start_date': reservation.start_date, 'end_date': reservation.end_date}), 201

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': str(error)}), 404

# Error handler for 400 errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
