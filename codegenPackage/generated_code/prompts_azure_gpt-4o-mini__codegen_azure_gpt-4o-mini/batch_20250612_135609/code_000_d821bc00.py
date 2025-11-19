"""
Generated Code Metadata:
========================
Original URL: https://rehemacare.com
Prompt: Generate a code snippet for a web application that allows users to request personalized healthcare services like Attendant Care and Habilitation from Rehema Care LLC.
Generated: DETERMINISTIC_d821bc003915cd0c
Batch ID: 20250612_135609
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rehama_care.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the ServiceRequest model
class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=True)

# Create the database
with app.app_context():
    db.create_all()

# Define the schema for validating input data
class ServiceRequestSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    service_type = fields.Str(required=True, validate=lambda s: s in ["Attendant Care", "Habilitation"])
    message = fields.Str(required=False)

# Initialize the schema
service_request_schema = ServiceRequestSchema()

@app.route('/request_service', methods=['POST'])
def request_service():
    """
    Endpoint to request personalized healthcare services.
    Expects a JSON payload with user details and service type.
    """
    try:
        # Validate and deserialize input data
        data = request.get_json()
        validated_data = service_request_schema.load(data)

        # Create a new service request
        new_request = ServiceRequest(
            name=validated_data['name'],
            email=validated_data['email'],
            service_type=validated_data['service_type'],
            message=validated_data.get('message')
        )

        # Add the request to the database
        db.session.add(new_request)
        db.session.commit()

        return jsonify({"message": "Service request submitted successfully!"}), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        # Handle other exceptions
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=False)
```
