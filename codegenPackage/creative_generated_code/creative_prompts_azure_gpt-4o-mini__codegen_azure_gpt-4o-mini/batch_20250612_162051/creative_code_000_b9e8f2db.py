"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://samaneventos.com
Prompt: Generate a reservation system API for a hotel like Saman Eventos that handles bookings for business and leisure stays.
Generated: DETERMINISTIC_b9e8f2db6eafd811
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
from werkzeug.exceptions import NotFound, BadRequest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reservations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Reservation model
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guest_name = db.Column(db.String(100), nullable=False)
    check_in_date = db.Column(db.Date, nullable=False)
    check_out_date = db.Column(db.Date, nullable=False)
    room_type = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "guest_name": self.guest_name,
            "check_in_date": self.check_in_date.strftime('%Y-%m-%d'),
            "check_out_date": self.check_out_date.strftime('%Y-%m-%d'),
            "room_type": self.room_type,
            "created_at": self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Error handler for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

# Error handler for not found
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": str(error)}), 404

# Route to create a new reservation
@app.route('/reservations', methods=['POST'])
def create_reservation():
    data = request.json
    if not all(k in data for k in ("guest_name", "check_in_date", "check_out_date", "room_type")):
        raise BadRequest("Missing required fields.")

    # Parse dates
    try:
        check_in_date = datetime.strptime(data["check_in_date"], '%Y-%m-%d')
        check_out_date = datetime.strptime(data["check_out_date"], '%Y-%m-%d')
    except ValueError:
        raise BadRequest("Invalid date format. Use YYYY-MM-DD.")

    # Check if check-out date is after check-in date
    if check_out_date <= check_in_date:
        raise BadRequest("Check-out date must be after check-in date.")

    # Create and save reservation
    reservation = Reservation(
        guest_name=data["guest_name"],
        check_in_date=check_in_date,
        check_out_date=check_out_date,
        room_type=data["room_type"]
    )

    db.session.add(reservation)
    db.session.commit()

    return jsonify(reservation.to_dict()), 201

# Route to get all reservations
@app.route('/reservations', methods=['GET'])
def get_reservations():
    reservations = Reservation.query.all()
    return jsonify([reservation.to_dict() for reservation in reservations]), 200

# Route to get a specific reservation by ID
@app.route('/reservations/<int:id>', methods=['GET'])
def get_reservation(id):
    reservation = Reservation.query.get(id)
    if not reservation:
        raise NotFound("Reservation not found.")
    return jsonify(reservation.to_dict()), 200

# Route to update a reservation
@app.route('/reservations/<int:id>', methods=['PUT'])
def update_reservation(id):
    reservation = Reservation.query.get(id)
    if not reservation:
        raise NotFound("Reservation not found.")

    data = request.json
    if not all(k in data for k in ("guest_name", "check_in_date", "check_out_date", "room_type")):
        raise BadRequest("Missing required fields.")

    # Parse dates
    try:
        check_in_date = datetime.strptime(data["check_in_date"], '%Y-%m-%d')
        check_out_date = datetime.strptime(data["check_out_date"], '%Y-%m-%d')
    except ValueError:
        raise BadRequest("Invalid date format. Use YYYY-MM-DD.")

    # Check if check-out date is after check-in date
    if check_out_date <= check_in_date:
        raise BadRequest("Check-out date must be after check-in date.")

    # Update reservation details
    reservation.guest_name = data["guest_name"]
    reservation.check_in_date = check_in_date
    reservation.check_out_date = check_out_date
    reservation.room_type = data["room_type"]

    db.session.commit()

    return jsonify(reservation.to_dict()), 200

# Route to delete a reservation
@app.route('/reservations/<int:id>', methods=['DELETE'])
def delete_reservation(id):
    reservation = Reservation.query.get(id)
    if not reservation:
        raise NotFound("Reservation not found.")

    db.session.delete(reservation)
    db.session.commit()

    return jsonify({"message": "Reservation deleted successfully."}), 204

if __name__ == '__main__':
    app.run(debug=True)
```
