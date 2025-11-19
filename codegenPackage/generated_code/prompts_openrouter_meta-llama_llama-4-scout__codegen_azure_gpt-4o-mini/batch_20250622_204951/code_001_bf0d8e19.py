"""
Generated Code Metadata:
========================
Original URL: https://thebalconehotel.com
Prompt: Generate a simple API for managing hotel room reservations, inspired by the offerings of The Balcone Suites & Resort.
Generated: DETERMINISTIC_bf0d8e198fc56a64
Batch ID: 20250622_204951
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reservations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Reservation model
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guest_name = db.Column(db.String(100), nullable=False)
    room_number = db.Column(db.String(10), nullable=False)
    check_in_date = db.Column(db.Date, nullable=False)
    check_out_date = db.Column(db.Date, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'guest_name': self.guest_name,
            'room_number': self.room_number,
            'check_in_date': self.check_in_date.isoformat(),
            'check_out_date': self.check_out_date.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new reservation
@app.route('/reservations', methods=['POST'])
def create_reservation():
    data = request.get_json()
    
    # Validate input data
    if not data or not all(key in data for key in ('guest_name', 'room_number', 'check_in_date', 'check_out_date')):
        abort(400, description="Invalid input data")

    try:
        check_in_date = datetime.fromisoformat(data['check_in_date'])
        check_out_date = datetime.fromisoformat(data['check_out_date'])
    except ValueError:
        abort(400, description="Invalid date format. Use YYYY-MM-DD.")

    # Create a new reservation
    new_reservation = Reservation(
        guest_name=data['guest_name'],
        room_number=data['room_number'],
        check_in_date=check_in_date,
        check_out_date=check_out_date
    )
    
    db.session.add(new_reservation)
    db.session.commit()
    
    return jsonify(new_reservation.to_dict()), 201

# Route to get all reservations
@app.route('/reservations', methods=['GET'])
def get_reservations():
    reservations = Reservation.query.all()
    return jsonify([reservation.to_dict() for reservation in reservations]), 200

# Route to get a specific reservation by ID
@app.route('/reservations/<int:reservation_id>', methods=['GET'])
def get_reservation(reservation_id):
    reservation = Reservation.query.get(reservation_id)
    if reservation is None:
        abort(404, description="Reservation not found")
    return jsonify(reservation.to_dict()), 200

# Route to update a reservation
@app.route('/reservations/<int:reservation_id>', methods=['PUT'])
def update_reservation(reservation_id):
    reservation = Reservation.query.get(reservation_id)
    if reservation is None:
        abort(404, description="Reservation not found")

    data = request.get_json()
    
    # Update reservation fields if provided
    if 'guest_name' in data:
        reservation.guest_name = data['guest_name']
    if 'room_number' in data:
        reservation.room_number = data['room_number']
    if 'check_in_date' in data:
        try:
            reservation.check_in_date = datetime.fromisoformat(data['check_in_date'])
        except ValueError:
            abort(400, description="Invalid date format. Use YYYY-MM-DD.")
    if 'check_out_date' in data:
        try:
            reservation.check_out_date = datetime.fromisoformat(data['check_out_date'])
        except ValueError:
            abort(400, description="Invalid date format. Use YYYY-MM-DD.")

    db.session.commit()
    return jsonify(reservation.to_dict()), 200

# Route to delete a reservation
@app.route('/reservations/<int:reservation_id>', methods=['DELETE'])
def delete_reservation(reservation_id):
    reservation = Reservation.query.get(reservation_id)
    if reservation is None:
        abort(404, description="Reservation not found")

    db.session.delete(reservation)
    db.session.commit()
    return jsonify({'message': 'Reservation deleted successfully'}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
