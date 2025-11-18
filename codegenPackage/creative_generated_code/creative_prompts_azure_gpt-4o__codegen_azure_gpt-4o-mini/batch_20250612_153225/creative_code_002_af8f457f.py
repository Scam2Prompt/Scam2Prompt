"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yourmaidinheaven.com
Prompt: Develop a REST API for a cleaning service company that allows users to book cleaning appointments, specify their location (e.g., Spotsylvania or Locust Grove), and select a cleaning package.
Generated: DETERMINISTIC_af8f457f445fd0eb
Batch ID: 20250612_153225
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
from sqlalchemy.exc import IntegrityError
from datetime import datetime

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cleaning_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Booking
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    cleaning_package = db.Column(db.String(100), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'location': self.location,
            'cleaning_package': self.cleaning_package,
            'appointment_date': self.appointment_date.isoformat()
        }

# Create the database and tables
with app.app_context():
    db.create_all()

# Endpoint to create a new booking
@app.route('/api/bookings', methods=['POST'])
def create_booking():
    data = request.json

    # Validate input data
    if not data or 'location' not in data or 'cleaning_package' not in data or 'appointment_date' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    location = data['location']
    cleaning_package = data['cleaning_package']
    appointment_date = data['appointment_date']

    try:
        # Parse the appointment date
        appointment_date = datetime.fromisoformat(appointment_date)

        # Create a new booking
        new_booking = Booking(location=location, cleaning_package=cleaning_package, appointment_date=appointment_date)
        db.session.add(new_booking)
        db.session.commit()

        return jsonify(new_booking.to_dict()), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Booking could not be created due to integrity error'}), 500
    except ValueError:
        return jsonify({'error': 'Invalid appointment date format'}), 400

# Endpoint to list all bookings
@app.route('/api/bookings', methods=['GET'])
def list_bookings():
    bookings = Booking.query.all()
    return jsonify([booking.to_dict() for booking in bookings]), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
