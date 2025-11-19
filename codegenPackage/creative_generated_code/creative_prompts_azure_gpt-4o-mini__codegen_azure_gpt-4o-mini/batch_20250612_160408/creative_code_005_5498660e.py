"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frigoterm.ro
Prompt: What are the best practices for setting up a service request API for air conditioning repairs and installations?
Generated: DETERMINISTIC_5498660ec8cac111
Batch ID: 20250612_160408
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

# Initialize Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///service_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the ServiceRequest model
class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    contact_number = db.Column(db.String(15), nullable=False)
    description = db.Column(db.Text, nullable=True)

# Create a schema for request validation
class ServiceRequestSchema(Schema):
    customer_name = fields.Str(required=True)
    service_type = fields.Str(required=True)
    contact_number = fields.Str(required=True)
    description = fields.Str()

# Initialize the database
with app.app_context():
    db.create_all()

# API endpoint to create a service request
@app.route('/api/service-requests', methods=['POST'])
def create_service_request():
    schema = ServiceRequestSchema()
    try:
        # Validate and deserialize the incoming JSON data
        request_data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400  # Return validation errors

    # Create a new service request
    new_request = ServiceRequest(**request_data)
    db.session.add(new_request)
    try:
        db.session.commit()
        logging.info(f'Service request created: {new_request.id}')
        return jsonify({'id': new_request.id}), 201  # Return the request ID
    except Exception as e:
        db.session.rollback()  # Rollback on failure
        logging.error(f'Error creating service request: {str(e)}')
        return jsonify({'error': 'Could not create service request'}), 500

# API endpoint to fetch all service requests
@app.route('/api/service-requests', methods=['GET'])
def get_service_requests():
    try:
        requests = ServiceRequest.query.all()
        requests_schema = ServiceRequestSchema(many=True)
        return jsonify(requests_schema.dump(requests)), 200
    except Exception as e:
        logging.error(f'Error fetching service requests: {str(e)}')
        return jsonify({'error': 'Could not fetch service requests'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```
