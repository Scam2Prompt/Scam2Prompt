"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mechanics.ae
Prompt: Create an API endpoint for a car repair service that allows users to request services such as engine repair, AC repair, and body shop services, inspired by the features of Mechanics.ae.
Generated: DETERMINISTIC_49e548d88882bbbc
Batch ID: 20250612_160804
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
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car_repair_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for Service Requests
class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))
    user_email = db.Column(db.String(100), nullable=False)

# Create a schema for validation and serialization
class ServiceRequestSchema(Schema):
    service_type = fields.Str(required=True)
    description = fields.Str()
    user_email = fields.Email(required=True)

service_request_schema = ServiceRequestSchema()

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/service-request', methods=['POST'])
def request_service():
    # Parse and validate input data
    try:
        data = request.get_json()
        service_request = service_request_schema.load(data)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    
    # Create a new service request
    new_request = ServiceRequest(
        service_type=service_request['service_type'],
        description=service_request.get('description'),
        user_email=service_request['user_email']
    )
    
    # Save the service request to the database
    db.session.add(new_request)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to save service request", "details": str(e)}), 500

    return jsonify({"message": "Service request created", "id": new_request.id}), 201

@app.route('/api/service-request/<int:request_id>', methods=['GET'])
def get_service_request(request_id):
    # Fetch service request by ID
    service_request = ServiceRequest.query.get(request_id)
    if not service_request:
        return jsonify({"error": "Service request not found"}), 404

    return jsonify({
        "id": service_request.id,
        "service_type": service_request.service_type,
        "description": service_request.description,
        "user_email": service_request.user_email
    }), 200

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Error starting the server: {str(e)}")
```
