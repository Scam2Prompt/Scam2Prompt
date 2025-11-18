"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enfock.com
Prompt: Create a REST API for managing fuel station operations, including fiscal data, asset tracking, and multi-brand support, based on the ERP solutions described by Enfock.
Generated: DETERMINISTIC_5d85216b59dada9e
Batch ID: 20250612_154201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fuel_station.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the FuelStation model
class FuelStation(db.Model):
    __tablename__ = 'fuel_stations'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    brand = db.Column(db.String(50), nullable=False)
    fiscal_data = db.Column(db.Float, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "brand": self.brand,
            "fiscal_data": self.fiscal_data,
            "is_active": self.is_active
        }

# Define the schema for request validation
class FuelStationSchema(Schema):
    name = fields.Str(required=True)
    brand = fields.Str(required=True)
    fiscal_data = fields.Float(required=True)
    is_active = fields.Bool(missing=True, default=True)

# Initialize schema instance
fuel_station_schema = FuelStationSchema()
fuel_stations_schema = FuelStationSchema(many=True)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to get all fuel stations
@app.route('/fuel_stations', methods=['GET'])
def get_fuel_stations():
    """Retrieve all fuel stations."""
    stations = FuelStation.query.all()
    return jsonify(fuel_stations_schema.dump(stations)), 200

# Route to create a new fuel station
@app.route('/fuel_stations', methods=['POST'])
def create_fuel_station():
    """Create a new fuel station."""
    try:
        data = request.get_json()
        validated_data = fuel_station_schema.load(data)
        new_station = FuelStation(**validated_data)
        db.session.add(new_station)
        db.session.commit()
        return jsonify(new_station.to_dict()), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Fuel station already exists."}), 409
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Route to update a fuel station
@app.route('/fuel_stations/<int:id>', methods=['PUT'])
def update_fuel_station(id):
    """Update an existing fuel station."""
    station = FuelStation.query.get(id)
    if not station:
        return jsonify({"error": "Fuel station not found."}), 404
    
    try:
        data = request.get_json()
        validated_data = fuel_station_schema.load(data)
        
        for key, value in validated_data.items():
            setattr(station, key, value)
        
        db.session.commit()
        return jsonify(station.to_dict()), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Route to delete a fuel station
@app.route('/fuel_stations/<int:id>', methods=['DELETE'])
def delete_fuel_station(id):
    """Delete a fuel station."""
    station = FuelStation.query.get(id)
    if not station:
        return jsonify({"error": "Fuel station not found."}), 404
    
    try:
        db.session.delete(station)
        db.session.commit()
        return jsonify({"message": "Fuel station deleted."}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
