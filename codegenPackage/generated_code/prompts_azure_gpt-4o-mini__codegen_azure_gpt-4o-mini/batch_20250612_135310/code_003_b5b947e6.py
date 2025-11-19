"""
Generated Code Metadata:
========================
Original URL: https://wingerrandr.ca
Prompt: Develop a RESTful API endpoint for submitting requests for drywall repair and painting services, ensuring it captures necessary details from the user.
Generated: DETERMINISTIC_b5b947e6b67e1f2f
Batch ID: 20250612_135310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for service requests
class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    details = db.Column(db.Text, nullable=True)

# Schema for validating input data
class ServiceRequestSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    phone = fields.Str(required=True)
    address = fields.Str(required=True)
    service_type = fields.Str(required=True, validate=lambda s: s in ["drywall_repair", "painting"])
    details = fields.Str(required=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/service-requests', methods=['POST'])
def submit_service_request():
    """
    Endpoint to submit a service request for drywall repair or painting.
    Expects a JSON payload with the necessary details.
    """
    # Parse and validate incoming JSON data
    schema = ServiceRequestSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    # Create a new service request instance
    new_request = ServiceRequest(
        name=data['name'],
        email=data['email'],
        phone=data['phone'],
        address=data['address'],
        service_type=data['service_type'],
        details=data.get('details')
    )

    # Add the new request to the database
    try:
        db.session.add(new_request)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to submit request", "details": str(e)}), 500

    # Return a success response
    return jsonify({"message": "Service request submitted successfully", "id": new_request.id}), 201

if __name__ == '__main__':
    app.run(debug=True)
```
