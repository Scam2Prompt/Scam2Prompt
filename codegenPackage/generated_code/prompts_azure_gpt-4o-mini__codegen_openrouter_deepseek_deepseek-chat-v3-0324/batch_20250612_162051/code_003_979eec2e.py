"""
Generated Code Metadata:
========================
Original URL: https://www.vracarbvk.rs
Prompt: Develop a RESTful API endpoint for managing reservations at Vila Vračar, ensuring it includes features for checking availability and confirming bookings.
Generated: DETERMINISTIC_979eec2ed0fa8055
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from werkzeug.exceptions import BadRequest, NotFound, Conflict

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reservations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guest_name = db.Column(db.String(100), nullable=False)
    check_in = db.Column(db.Date, nullable=False)
    check_out = db.Column(db.Date, nullable=False)
    room_type = db.Column(db.String(50), nullable=False)
    confirmed = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'guest_name': self.guest_name,
            'check_in': self.check_in.isoformat(),
            'check_out': self.check_out.isoformat(),
            'room_type': self.room_type,
            'confirmed': self.confirmed
        }

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/reservations', methods=['GET'])
def get_reservations():
    """Get all reservations"""
    reservations = Reservation.query.all()
    return jsonify([reservation.to_dict() for reservation in reservations])

@app.route('/reservations/availability', methods=['GET'])
def check_availability():
    """Check room availability for given dates and room type"""
    try:
        check_in = datetime.strptime(request.args.get('check_in'), '%Y-%m-%d').date()
        check_out = datetime.strptime(request.args.get('check_out'), '%Y-%m-%d').date()
        room_type = request.args.get('room_type')
    except (ValueError, TypeError) as e:
        raise BadRequest("Invalid date format or missing parameters. Use YYYY-MM-DD format.")

    if check_in >= check_out:
        raise BadRequest("Check-out date must be after check-in date.")

    # Check for overlapping reservations
    overlapping = Reservation.query.filter(
        Reservation.room_type == room_type,
        Reservation.check_out > check_in,
        Reservation.check_in < check_out
    ).count()

    available = overlapping == 0
    return jsonify({
        'available': available,
        'check_in': check_in.isoformat(),
        'check_out': check_out.isoformat(),
        'room_type': room_type
    })

@app.route('/reservations', methods=['POST'])
def create_reservation():
    """Create a new reservation"""
    data = request.get_json()
    try:
        guest_name = data['guest_name']
        check_in = datetime.strptime(data['check_in'], '%Y-%m-%d').date()
        check_out = datetime.strptime(data['check_out'], '%Y-%m-%d').date()
        room_type = data['room_type']
    except (KeyError, ValueError) as e:
        raise BadRequest("Missing or invalid reservation data.")

    if check_in >= check_out:
        raise BadRequest("Check-out date must be after check-in date.")

    # Check availability
    overlapping = Reservation.query.filter(
        Reservation.room_type == room_type,
        Reservation.check_out > check_in,
        Reservation.check_in < check_out
    ).count()

    if overlapping > 0:
        raise Conflict("Room not available for the selected dates.")

    reservation = Reservation(
        guest_name=guest_name,
        check_in=check_in,
        check_out=check_out,
        room_type=room_type
    )
    db.session.add(reservation)
    db.session.commit()
    return jsonify(reservation.to_dict()), 201

@app.route('/reservations/<int:reservation_id>/confirm', methods=['PUT'])
def confirm_reservation(reservation_id):
    """Confirm a reservation"""
    reservation = Reservation.query.get(reservation_id)
    if not reservation:
        raise NotFound("Reservation not found.")

    if reservation.confirmed:
        raise Conflict("Reservation already confirmed.")

    reservation.confirmed = True
    db.session.commit()
    return jsonify(reservation.to_dict())

@app.route('/reservations/<int:reservation_id>', methods=['DELETE'])
def cancel_reservation(reservation_id):
    """Cancel a reservation"""
    reservation = Reservation.query.get(reservation_id)
    if not reservation:
        raise NotFound("Reservation not found.")

    db.session.delete(reservation)
    db.session.commit()
    return jsonify({'message': 'Reservation cancelled successfully'}), 200

@app.errorhandler(BadRequest)
@app.errorhandler(NotFound)
@app.errorhandler(Conflict)
def handle_error(e):
    """Handle application errors"""
    return jsonify({
        'error': e.name,
        'message': e.description
    }), e.code

if __name__ == '__main__':
    app.run(debug=True)
```
