"""
Generated Code Metadata:
========================
Original URL: https://enfock.com
Prompt: Create a REST API for managing fuel station operations, including fiscal data, asset tracking, and multi-brand support, based on the ERP solutions described by Enfock.
Generated: DETERMINISTIC_5d85216b59dada9e
Batch ID: 20250612_154201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fuel_stations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the FuelStation model
class FuelStation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    brand = db.Column(db.String(50), nullable=False)
    fiscal_data = db.Column(db.Float, nullable=False)
    assets = db.Column(db.String(200), nullable=True)

# Create the database
with app.app_context():
    db.create_all()

# Define the schema for input validation
class FuelStationSchema(Schema):
    name = fields.Str(required=True)
    brand = fields.Str(required=True)
    fiscal_data = fields.Float(required=True)
    assets = fields.Str(required=False)

# Initialize the schema
fuel_station_schema = FuelStationSchema()
fuel_stations_schema = FuelStationSchema(many=True)

# Create a new fuel station
@app.route('/fuel_stations', methods=['POST'])
def add_fuel_station():
    try:
        # Validate and deserialize input
        data = request.get_json()
        fuel_station_data = fuel_station_schema.load(data)

        # Create a new fuel station instance
        new_station = FuelStation(**fuel_station_data)
        db.session.add(new_station)
        db.session.commit()

        return jsonify(fuel_station_schema.dump(new_station)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Fuel station with this name already exists."}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get all fuel stations
@app.route('/fuel_stations', methods=['GET'])
def get_fuel_stations():
    try:
        stations = FuelStation.query.all()
        return jsonify(fuel_stations_schema.dump(stations)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get a specific fuel station by ID
@app.route('/fuel_stations/<int:id>', methods=['GET'])
def get_fuel_station(id):
    try:
        station = FuelStation.query.get_or_404(id)
        return jsonify(fuel_station_schema.dump(station)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Update a fuel station
@app.route('/fuel_stations/<int:id>', methods=['PUT'])
def update_fuel_station(id):
    try:
        data = request.get_json()
        fuel_station_data = fuel_station_schema.load(data)

        station = FuelStation.query.get_or_404(id)
        for key, value in fuel_station_data.items():
            setattr(station, key, value)

        db.session.commit()
        return jsonify(fuel_station_schema.dump(station)), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Delete a fuel station
@app.route('/fuel_stations/<int:id>', methods=['DELETE'])
def delete_fuel_station(id):
    try:
        station = FuelStation.query.get_or_404(id)
        db.session.delete(station)
        db.session.commit()
        return jsonify({"message": "Fuel station deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
