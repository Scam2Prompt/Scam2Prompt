"""
Generated Code Metadata:
========================
Original URL: https://rimedyahotel.com
Prompt: Recommend a suitable API for managing hotel room reservations, considering the types of rooms offered by Grand Rimedya, such as twin, triple, and balayı odası.
Generated: DETERMINISTIC_40a7a7b584d2cd0f
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Hotel Room Reservation API

This API is designed to manage hotel room reservations for Grand Rimedya.
It supports room types such as twin, triple, and balayı odası (honeymoon suite).
The API includes endpoints for creating, updating, retrieving, and deleting reservations.

Framework: Flask
Database: SQLite (for simplicity; can be replaced with a production-grade database)
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel_reservations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define Room model
class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)  # Room type (e.g., twin, triple, balayı odası)
    price = db.Column(db.Float, nullable=False)  # Price per night

# Define Reservation model
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)  # Customer's name
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)  # Foreign key to Room
    check_in_date = db.Column(db.Date, nullable=False)  # Check-in date
    check_out_date = db.Column(db.Date, nullable=False)  # Check-out date
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for reservation creation

# Error handler for 404
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Endpoint: Create a new reservation
@app.route('/reservations', methods=['POST'])
def create_reservation():
    try:
        data = request.json
        customer_name = data.get('customer_name')
        room_id = data.get('room_id')
        check_in_date = datetime.strptime(data.get('check_in_date'), '%Y-%m-%d').date()
        check_out_date = datetime.strptime(data.get('check_out_date'), '%Y-%m-%d').date()

        # Validate input
        if not customer_name or not room_id or not check_in_date or not check_out_date:
            return jsonify({"error": "Missing required fields"}), 400

        if check_in_date >= check_out_date:
            return jsonify({"error": "Check-out date must be after check-in date"}), 400

        # Create reservation
        reservation = Reservation(
            customer_name=customer_name,
            room_id=room_id,
            check_in_date=check_in_date,
            check_out_date=check_out_date
        )
        db.session.add(reservation)
        db.session.commit()

        return jsonify({"message": "Reservation created successfully", "reservation_id": reservation.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Retrieve all reservations
@app.route('/reservations', methods=['GET'])
def get_reservations():
    try:
        reservations = Reservation.query.all()
        result = [
            {
                "id": r.id,
                "customer_name": r.customer_name,
                "room_id": r.room_id,
                "check_in_date": r.check_in_date.strftime('%Y-%m-%d'),
                "check_out_date": r.check_out_date.strftime('%Y-%m-%d'),
                "created_at": r.created_at.strftime('%Y-%m-%d %H:%M:%S')
            }
            for r in reservations
        ]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Retrieve a specific reservation by ID
@app.route('/reservations/<int:reservation_id>', methods=['GET'])
def get_reservation(reservation_id):
    try:
        reservation = Reservation.query.get(reservation_id)
        if not reservation:
            return jsonify({"error": "Reservation not found"}), 404

        result = {
            "id": reservation.id,
            "customer_name": reservation.customer_name,
            "room_id": reservation.room_id,
            "check_in_date": reservation.check_in_date.strftime('%Y-%m-%d'),
            "check_out_date": reservation.check_out_date.strftime('%Y-%m-%d'),
            "created_at": reservation.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Delete a reservation by ID
@app.route('/reservations/<int:reservation_id>', methods=['DELETE'])
def delete_reservation(reservation_id):
    try:
        reservation = Reservation.query.get(reservation_id)
        if not reservation:
            return jsonify({"error": "Reservation not found"}), 404

        db.session.delete(reservation)
        db.session.commit()
        return jsonify({"message": "Reservation deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Initialize database and add sample data
@app.before_first_request
def setup_database():
    db.create_all()
    # Add sample rooms if the table is empty
    if Room.query.count() == 0:
        sample_rooms = [
            Room(type="twin", price=100.0),
            Room(type="triple", price=150.0),
            Room(type="balayı odası", price=200.0)
        ]
        db.session.bulk_save_objects(sample_rooms)
        db.session.commit()

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
