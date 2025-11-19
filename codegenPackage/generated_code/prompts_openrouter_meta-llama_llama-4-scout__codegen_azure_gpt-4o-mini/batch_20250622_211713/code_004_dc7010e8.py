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
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel_agency.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Flight model
class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    airline = db.Column(db.String(100), nullable=False)
    departure = db.Column(db.String(100), nullable=False)
    arrival = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Define the Hotel model
class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    price_per_night = db.Column(db.Float, nullable=False)

# Define the VacationPackage model
class VacationPackage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Define schemas for validation
class FlightSchema(Schema):
    airline = fields.Str(required=True)
    departure = fields.Str(required=True)
    arrival = fields.Str(required=True)
    price = fields.Float(required=True)

class HotelSchema(Schema):
    name = fields.Str(required=True)
    location = fields.Str(required=True)
    price_per_night = fields.Float(required=True)

class VacationPackageSchema(Schema):
    destination = fields.Str(required=True)
    price = fields.Float(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Flight routes
@app.route('/flights', methods=['POST'])
def add_flight():
    """Add a new flight."""
    try:
        data = request.get_json()
        FlightSchema().load(data)  # Validate input
        flight = Flight(**data)
        db.session.add(flight)
        db.session.commit()
        return jsonify({"id": flight.id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/flights', methods=['GET'])
def get_flights():
    """Retrieve all flights."""
    flights = Flight.query.all()
    return jsonify([{"id": flight.id, "airline": flight.airline, "departure": flight.departure, "arrival": flight.arrival, "price": flight.price} for flight in flights]), 200

# Hotel routes
@app.route('/hotels', methods=['POST'])
def add_hotel():
    """Add a new hotel."""
    try:
        data = request.get_json()
        HotelSchema().load(data)  # Validate input
        hotel = Hotel(**data)
        db.session.add(hotel)
        db.session.commit()
        return jsonify({"id": hotel.id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/hotels', methods=['GET'])
def get_hotels():
    """Retrieve all hotels."""
    hotels = Hotel.query.all()
    return jsonify([{"id": hotel.id, "name": hotel.name, "location": hotel.location, "price_per_night": hotel.price_per_night} for hotel in hotels]), 200

# Vacation Package routes
@app.route('/packages', methods=['POST'])
def add_package():
    """Add a new vacation package."""
    try:
        data = request.get_json()
        VacationPackageSchema().load(data)  # Validate input
        package = VacationPackage(**data)
        db.session.add(package)
        db.session.commit()
        return jsonify({"id": package.id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/packages', methods=['GET'])
def get_packages():
    """Retrieve all vacation packages."""
    packages = VacationPackage.query.all()
    return jsonify([{"id": package.id, "destination": package.destination, "price": package.price} for package in packages]), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
