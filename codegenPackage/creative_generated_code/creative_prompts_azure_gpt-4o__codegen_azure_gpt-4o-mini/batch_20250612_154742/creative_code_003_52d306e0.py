"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bestholidaysallindia.com
Prompt: Recommend a library or framework to build a web-based booking system for taxi services, including features for calculating rates per kilometer and selecting vehicle types as described on the "Best Holidays All India" website.
Generated: DETERMINISTIC_52d306e028454887
Batch ID: 20250612_154742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///taxi_booking.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Vehicle Type
class VehicleType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    rate_per_km = db.Column(db.Float, nullable=False)

# Model for Booking
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_type_id = db.Column(db.Integer, db.ForeignKey('vehicle_type.id'), nullable=False)
    distance_km = db.Column(db.Float, nullable=False)
    total_price = db.Column(db.Float, nullable=False)

    vehicle_type = db.relationship('VehicleType', backref='bookings')

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# API Endpoint to calculate fare
@app.route('/calculate_fare', methods=['POST'])
def calculate_fare():
    try:
        data = request.get_json()
        vehicle_type_id = data['vehicle_type_id']
        distance_km = data['distance_km']

        # Fetch vehicle type details
        vehicle_type = VehicleType.query.get(vehicle_type_id)
        if vehicle_type is None:
            return jsonify({'error': 'Invalid vehicle type ID'}), 400

        # Calculate total fare
        total_price = vehicle_type.rate_per_km * distance_km
        return jsonify({'total_price': total_price}), 200

    except KeyError as e:
        return jsonify({'error': f'Missing parameter: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API Endpoint to create a booking
@app.route('/book', methods=['POST'])
def book():
    try:
        data = request.get_json()
        vehicle_type_id = data['vehicle_type_id']
        distance_km = data['distance_km']

        vehicle_type = VehicleType.query.get(vehicle_type_id)
        if vehicle_type is None:
            return jsonify({'error': 'Invalid vehicle type ID'}), 400

        total_price = vehicle_type.rate_per_km * distance_km
        new_booking = Booking(vehicle_type_id=vehicle_type_id, distance_km=distance_km, total_price=total_price)

        db.session.add(new_booking)
        db.session.commit()
        return jsonify({'message': 'Booking successful', 'booking_id': new_booking.id}), 201

    except KeyError as e:
        return jsonify({'error': f'Missing parameter: {str(e)}'}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Database integrity error'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API Endpoint to add vehicle types (for initial setup)
@app.route('/add_vehicle_type', methods=['POST'])
def add_vehicle_type():
    try:
        data = request.get_json()
        new_vehicle_type = VehicleType(name=data['name'], rate_per_km=data['rate_per_km'])
        db.session.add(new_vehicle_type)
        db.session.commit()
        return jsonify({'message': 'Vehicle type added', 'vehicle_type_id': new_vehicle_type.id}), 201
    except KeyError as e:
        return jsonify({'error': f'Missing parameter: {str(e)}'}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Vehicle type already exists'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
