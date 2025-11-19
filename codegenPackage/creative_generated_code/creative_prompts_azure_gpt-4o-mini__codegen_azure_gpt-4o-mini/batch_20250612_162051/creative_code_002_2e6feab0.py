"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flammedeauinc.ca
Prompt: Create a REST API endpoint that handles plumbing service requests, including validation for residential and commercial plumbing needs.
Generated: DETERMINISTIC_2e6feab0acaef3c0
Batch ID: 20250612_162051
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
from marshmallow import Schema, fields, validate, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plumbing_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Plumbing Service Request
class PlumbingServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    is_residential = db.Column(db.Boolean, nullable=False)

# Schema for request validation
class PlumbingServiceRequestSchema(Schema):
    service_type = fields.Str(required=True, validate=validate.OneOf(["repair", "installation", "maintenance"]))
    address = fields.Str(required=True)
    is_residential = fields.Bool(required=True)

# Initialize the database
with app.app_context():
    db.create_all()

# Endpoint to handle plumbing service requests
@app.route('/api/plumbing_service', methods=['POST'])
def create_service_request():
    # Parse and validate incoming JSON data
    try:
        data = request.get_json()
        schema = PlumbingServiceRequestSchema()
        validated_data = schema.load(data)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    # Create a new service request record
    new_request = PlumbingServiceRequest(
        service_type=validated_data['service_type'],
        address=validated_data['address'],
        is_residential=validated_data['is_residential']
    )

    # Add the new request to the database
    try:
        db.session.add(new_request)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to create service request: " + str(e)}), 500

    # Return the created service request information
    return jsonify({
        "id": new_request.id,
        "service_type": new_request.service_type,
        "address": new_request.address,
        "is_residential": new_request.is_residential
    }), 201

# Main entry point to run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
