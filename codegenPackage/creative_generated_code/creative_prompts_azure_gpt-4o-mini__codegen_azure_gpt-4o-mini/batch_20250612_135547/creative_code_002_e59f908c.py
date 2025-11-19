"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virasmile.it
Prompt: Create a RESTful API specification for a dental practice that includes endpoints for services such as sbiancamento dentale and ortodonzia invisibile, inspired by the offerings of Studio Dentistico dott.ssa Vira Palazzo.
Generated: DETERMINISTIC_e59f908cc2a291c5
Batch ID: 20250612_135547
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
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dental_practice.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for dental services
class DentalService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(512), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Schema for validating incoming data
class DentalServiceSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# GET endpoint to list all services
@app.route('/services', methods=['GET'])
def get_services():
    services = DentalService.query.all()
    service_schema = DentalServiceSchema(many=True)
    return jsonify(service_schema.dump(services)), 200

# POST endpoint to create a new service
@app.route('/services', methods=['POST'])
def add_service():
    service_schema = DentalServiceSchema()
    try:
        # Validate and load data
        new_service_data = service_schema.load(request.json)
        new_service = DentalService(**new_service_data)
        db.session.add(new_service)
        db.session.commit()
        return jsonify(service_schema.dump(new_service)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# GET endpoint to retrieve a specific service by ID
@app.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    service = DentalService.query.get(service_id)
    if not service:
        return jsonify({"error": "Service not found"}), 404
    service_schema = DentalServiceSchema()
    return jsonify(service_schema.dump(service)), 200

# PUT endpoint to update an existing service
@app.route('/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    service = DentalService.query.get(service_id)
    if not service:
        return jsonify({"error": "Service not found"}), 404
    
    service_schema = DentalServiceSchema()
    try:
        # Validate and load updated data
        updated_service_data = service_schema.load(request.json)
        for key, value in updated_service_data.items():
            setattr(service, key, value)
        db.session.commit()
        return jsonify(service_schema.dump(service)), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# DELETE endpoint to remove a service
@app.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    service = DentalService.query.get(service_id)
    if not service:
        return jsonify({"error": "Service not found"}), 404
    db.session.delete(service)
    db.session.commit()
    return jsonify({"message": "Service deleted successfully"}), 204

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
