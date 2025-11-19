"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aknanalofiq.com
Prompt: Create a REST API that allows users to request services related to hospital equipment installation, referencing AKNAN's expertise in flame retardant and antibacterial curtains.
Generated: DETERMINISTIC_cf6dadc6e604e59b
Batch ID: 20250612_163442
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
import logging

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Database model for Service Request
class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=True)

# Schema for validating input data
class ServiceRequestSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    service_type = fields.Str(required=True, validate=lambda s: s in ["Installation", "Maintenance"])
    message = fields.Str(required=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to submit a service request
@app.route('/api/service_request', methods=['POST'])
def submit_service_request():
    try:
        # Validate and deserialize input
        request_data = request.get_json()
        validated_data = ServiceRequestSchema().load(request_data)

        # Create and save the service request
        service_request = ServiceRequest(
            name=validated_data['name'],
            email=validated_data['email'],
            service_type=validated_data['service_type'],
            message=validated_data.get('message', '')
        )
        db.session.add(service_request)
        db.session.commit()

        logging.info(f"Service request submitted: {validated_data['name']}")
        return jsonify({"message": "Service request submitted successfully", "id": service_request.id}), 201

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")
        return jsonify({"error": "An internal error occurred. Please try again later."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False in production
```
