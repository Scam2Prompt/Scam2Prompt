"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kadma-wine.co.il
Prompt: Recommend an API or library for implementing a reservation system for wine tours, similar to the one described on Kadma Winery's website.
Generated: DETERMINISTIC_406baeeac3e66d69
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation using Flask and SQLAlchemy for a reservation system for wine tours.

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask app and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reservations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Reservation model
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique reservation ID
    name = db.Column(db.String(100), nullable=False)  # Name of the customer
    email = db.Column(db.String(100), nullable=False)  # Email of the customer
    phone = db.Column(db.String(15), nullable=False)  # Phone number of the customer
    tour_date = db.Column(db.DateTime, nullable=False)  # Date and time of the wine tour
    guests = db.Column(db.Integer, nullable=False)  # Number of guests

    def to_dict(self):
        """Converts the reservation object to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'tour_date': self.tour_date.strftime('%Y-%m-%d %H:%M:%S'),
            'guests': self.guests
        }

# Endpoint to create a new reservation
@app.route('/reservations', methods=['POST'])
def create_reservation():
    """
    Creates a new wine tour reservation.
    Request JSON format:
    {
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "1234567890",
        "tour_date": "2023-12-25 14:00:00",
        "guests": 4
    }
    """
    try:
        # Parse the input data
        data = request.json
        name = data['name']
        email = data['email']
        phone = data['phone']
        tour_date = datetime.strptime(data['tour_date'], '%Y-%m-%d %H:%M:%S')
        guests = data['guests']

        # Validate the input data
        if not name or not email or not phone or not guests:
            return jsonify({'error': 'Missing required fields'}), 400

        # Create and save the new reservation
        reservation = Reservation(name=name, email=email, phone=phone, tour_date=tour_date, guests=guests)
        db.session.add(reservation)
        db.session.commit()

        return jsonify({'message': 'Reservation created', 'reservation': reservation.to_dict()}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to list all reservations
@app.route('/reservations', methods=['GET'])
def list_reservations():
    """
    Retrieves a list of all reservations.
    """
    try:
        reservations = Reservation.query.all()
        return jsonify([reservation.to_dict() for reservation in reservations]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to get a specific reservation by ID
@app.route('/reservations/<int:reservation_id>', methods=['GET'])
def get_reservation(reservation_id):
    """
    Retrieves a specific reservation by ID.
    """
    try:
        reservation = Reservation.query.get(reservation_id)
        if reservation:
            return jsonify(reservation.to_dict()), 200
        else:
            return jsonify({'error': 'Reservation not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to delete a reservation
@app.route('/reservations/<int:reservation_id>', methods=['DELETE'])
def delete_reservation(reservation_id):
    """
    Deletes a reservation by ID.
    """
    try:
        reservation = Reservation.query.get(reservation_id)
        if reservation:
            db.session.delete(reservation)
            db.session.commit()
            return jsonify({'message': 'Reservation deleted'}), 200
        else:
            return jsonify({'error': 'Reservation not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Initialize the database
@app.before_first_request
def create_tables():
    """
    Creates the database tables if they don't exist.
    """
    db.create_all()

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

**Instructions to set up:**
1. Install dependencies: `pip install flask flask-sqlalchemy`
2. Save this code to a file, e.g., `app.py`.
3. Run the server: `python app.py`.
4. Test the endpoints using tools like Postman or curl.
