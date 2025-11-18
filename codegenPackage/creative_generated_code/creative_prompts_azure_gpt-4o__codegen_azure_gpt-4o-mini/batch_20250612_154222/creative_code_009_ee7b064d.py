"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supportfix.online
Prompt: Suggest a cloud-based solution for managing appliance repair service requests, including features for technician assignment and customer communication.
Generated: DETERMINISTIC_ee7b064d10919c53
Batch ID: 20250612_154222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# appliance_repair_service.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///repair_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Technician model
class Technician(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    expertise = db.Column(db.String(100), nullable=False)

# Define the ServiceRequest model
class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    appliance_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    technician_id = db.Column(db.Integer, db.ForeignKey('technician.id'))
    technician = db.relationship('Technician', backref='service_requests')

# Schema for validating input data
class TechnicianSchema(Schema):
    name = fields.Str(required=True)
    expertise = fields.Str(required=True)

class ServiceRequestSchema(Schema):
    customer_name = fields.Str(required=True)
    appliance_type = fields.Str(required=True)
    description = fields.Str(required=True)
    technician_id = fields.Int(required=True)

# Create the database tables
with app.app_context():
    db.create_all()

# API route to create a technician
@app.route('/technician', methods=['POST'])
def create_technician():
    json_data = request.json
    try:
        TechnicianSchema().load(json_data)
        technician = Technician(**json_data)
        db.session.add(technician)
        db.session.commit()
        return jsonify({"message": "Technician created successfully"}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Technician already exists"}), 409

# API route to create a service request
@app.route('/service-request', methods=['POST'])
def create_service_request():
    json_data = request.json
    try:
        ServiceRequestSchema().load(json_data)
        service_request = ServiceRequest(**json_data)
        db.session.add(service_request)
        db.session.commit()
        return jsonify({"message": "Service request created successfully"}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Error creating service request"}), 409

# API route to assign a technician to a service request
@app.route('/service-request/<int:request_id>/assign/<int:technician_id>', methods=['PUT'])
def assign_technician(request_id, technician_id):
    service_request = ServiceRequest.query.get(request_id)
    technician = Technician.query.get(technician_id)
    
    if service_request is None:
        return jsonify({"message": "Service request not found"}), 404
    
    if technician is None:
        return jsonify({"message": "Technician not found"}), 404
    
    service_request.technician_id = technician_id
    db.session.commit()
    return jsonify({"message": "Technician assigned successfully"}), 200

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

This code provides a basic cloud-based solution for managing appliance repair service requests using Flask and SQLAlchemy. It includes routes for creating technicians and service requests, as well as assigning technicians to requests, with proper validation and error handling.
