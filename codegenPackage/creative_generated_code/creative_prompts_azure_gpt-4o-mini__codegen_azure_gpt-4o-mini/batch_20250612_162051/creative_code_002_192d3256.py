"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felipemunozreparaciones.es
Prompt: Create a REST API specification for a service that handles plumbing and electrical repairs, inspired by the offerings of Felipe Muñoz Reparaciones.
Generated: DETERMINISTIC_192d3256e6c8fa4c
Batch ID: 20250612_162051
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
from marshmallow import Schema, fields, validate, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///repairs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for Repair Services
class RepairService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    price = db.Column(db.Float, nullable=False)

# Schema for validating Repair Service data
class RepairServiceSchema(Schema):
    service_type = fields.String(required=True, validate=validate.Length(min=1))
    description = fields.String(allow_none=True)
    price = fields.Float(required=True, validate=validate.Range(min=0))

repair_service_schema = RepairServiceSchema()
repair_services_schema = RepairServiceSchema(many=True)

@app.before_first_request
def create_tables():
    """Create database tables if they don't exist."""
    db.create_all()

@app.route('/services', methods=['GET'])
def get_services():
    """Get a list of all repair services."""
    services = RepairService.query.all()
    return jsonify(repair_services_schema.dump(services)), 200

@app.route('/services', methods=['POST'])
def add_service():
    """Add a new repair service."""
    try:
        # Validate and deserialize input data
        service_data = repair_service_schema.load(request.json)
        new_service = RepairService(**service_data)
        db.session.add(new_service)
        db.session.commit()
        return jsonify(repair_service_schema.dump(new_service)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """Get a specific repair service by ID."""
    service = RepairService.query.get(service_id)
    if service is None:
        return jsonify({"message": "Service not found"}), 404
    return jsonify(repair_service_schema.dump(service)), 200

@app.route('/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    """Update an existing repair service."""
    service = RepairService.query.get(service_id)
    if service is None:
        return jsonify({"message": "Service not found"}), 404

    try:
        # Validate and deserialize input data
        updated_data = repair_service_schema.load(request.json)
        for key, value in updated_data.items():
            setattr(service, key, value)
        db.session.commit()
        return jsonify(repair_service_schema.dump(service)), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """Delete a repair service by ID."""
    service = RepairService.query.get(service_id)
    if service is None:
        return jsonify({"message": "Service not found"}), 404

    db.session.delete(service)
    db.session.commit()
    return jsonify({"message": "Service deleted successfully"}), 204

if __name__ == '__main__':
    app.run(debug=True)
```
