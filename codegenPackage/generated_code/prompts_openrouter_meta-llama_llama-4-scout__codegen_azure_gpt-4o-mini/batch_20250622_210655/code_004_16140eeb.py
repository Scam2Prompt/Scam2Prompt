"""
Generated Code Metadata:
========================
Original URL: https://www.efeotokurtarma.com.tr
Prompt: Create a RESTful API endpoint to request and manage towing services, inspired by the features and structure of Efem Oto Kurtarma's services in Ankara.
Generated: DETERMINISTIC_16140eeb04cc04ee
Batch ID: 20250622_210655
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///towing_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Towing Service model
class TowingService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Define the schema for input validation
class TowingServiceSchema(Schema):
    service_type = fields.Str(required=True)
    location = fields.Str(required=True)
    price = fields.Float(required=True)

# Initialize the schema
towing_service_schema = TowingServiceSchema()
towing_services_schema = TowingServiceSchema(many=True)

# Error handling for invalid data
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({"error": error.messages}), 400

# Endpoint to create a new towing service
@app.route('/towing_services', methods=['POST'])
def create_towing_service():
    json_data = request.get_json()
    try:
        # Validate and deserialize input
        data = towing_service_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    # Create a new towing service
    new_service = TowingService(**data)
    db.session.add(new_service)
    db.session.commit()
    
    return jsonify(towing_service_schema.dump(new_service)), 201

# Endpoint to get all towing services
@app.route('/towing_services', methods=['GET'])
def get_towing_services():
    services = TowingService.query.all()
    return jsonify(towing_services_schema.dump(services)), 200

# Endpoint to get a specific towing service by ID
@app.route('/towing_services/<int:service_id>', methods=['GET'])
def get_towing_service(service_id):
    service = TowingService.query.get(service_id)
    if service is None:
        abort(404, description="Service not found")
    return jsonify(towing_service_schema.dump(service)), 200

# Endpoint to update a towing service
@app.route('/towing_services/<int:service_id>', methods=['PUT'])
def update_towing_service(service_id):
    service = TowingService.query.get(service_id)
    if service is None:
        abort(404, description="Service not found")

    json_data = request.get_json()
    try:
        # Validate and deserialize input
        data = towing_service_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    # Update the service
    for key, value in data.items():
        setattr(service, key, value)
    db.session.commit()
    
    return jsonify(towing_service_schema.dump(service)), 200

# Endpoint to delete a towing service
@app.route('/towing_services/<int:service_id>', methods=['DELETE'])
def delete_towing_service(service_id):
    service = TowingService.query.get(service_id)
    if service is None:
        abort(404, description="Service not found")

    db.session.delete(service)
    db.session.commit()
    
    return jsonify({"message": "Service deleted successfully"}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
