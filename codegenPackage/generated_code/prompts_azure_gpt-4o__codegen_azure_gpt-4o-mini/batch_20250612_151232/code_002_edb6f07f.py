"""
Generated Code Metadata:
========================
Original URL: https://enlconsortium.com
Prompt: Create an API specification for ENL Consortium's port and terminal management system, detailing endpoints for berthing updates, cargo tracking, and equipment profiles.
Generated: DETERMINISTIC_edb6f07fc56acffd
Batch ID: 20250612_151232
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
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///port_terminal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class Berth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vessel_name = db.Column(db.String(100), nullable=False)
    arrival_time = db.Column(db.String(50), nullable=False)
    departure_time = db.Column(db.String(50), nullable=False)

class Cargo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cargo_description = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), nullable=False)

class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    equipment_name = db.Column(db.String(100), nullable=False)
    equipment_type = db.Column(db.String(50), nullable=False)

# Schemas for validation
class BerthSchema(Schema):
    vessel_name = fields.Str(required=True)
    arrival_time = fields.Str(required=True)
    departure_time = fields.Str(required=True)

class CargoSchema(Schema):
    cargo_description = fields.Str(required=True)
    status = fields.Str(required=True)

class EquipmentSchema(Schema):
    equipment_name = fields.Str(required=True)
    equipment_type = fields.Str(required=True)

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint for berthing updates
@app.route('/api/berths', methods=['POST'])
def add_berth():
    """Add a new berth update."""
    try:
        data = request.get_json()
        BerthSchema().load(data)  # Validate input
        new_berth = Berth(**data)
        db.session.add(new_berth)
        db.session.commit()
        return jsonify({"message": "Berth added successfully!"}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/berths', methods=['GET'])
def get_berths():
    """Retrieve all berthing updates."""
    berths = Berth.query.all()
    return jsonify([{"id": berth.id, "vessel_name": berth.vessel_name,
                     "arrival_time": berth.arrival_time, "departure_time": berth.departure_time} for berth in berths]), 200

# Endpoint for cargo tracking
@app.route('/api/cargo', methods=['POST'])
def add_cargo():
    """Add a new cargo tracking entry."""
    try:
        data = request.get_json()
        CargoSchema().load(data)  # Validate input
        new_cargo = Cargo(**data)
        db.session.add(new_cargo)
        db.session.commit()
        return jsonify({"message": "Cargo added successfully!"}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/cargo', methods=['GET'])
def get_cargo():
    """Retrieve all cargo tracking entries."""
    cargo_items = Cargo.query.all()
    return jsonify([{"id": cargo.id, "cargo_description": cargo.cargo_description,
                     "status": cargo.status} for cargo in cargo_items]), 200

# Endpoint for equipment profiles
@app.route('/api/equipment', methods=['POST'])
def add_equipment():
    """Add a new equipment profile."""
    try:
        data = request.get_json()
        EquipmentSchema().load(data)  # Validate input
        new_equipment = Equipment(**data)
        db.session.add(new_equipment)
        db.session.commit()
        return jsonify({"message": "Equipment added successfully!"}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/equipment', methods=['GET'])
def get_equipment():
    """Retrieve all equipment profiles."""
    equipment_list = Equipment.query.all()
    return jsonify([{"id": equipment.id, "equipment_name": equipment.equipment_name,
                     "equipment_type": equipment.equipment_type} for equipment in equipment_list]), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
