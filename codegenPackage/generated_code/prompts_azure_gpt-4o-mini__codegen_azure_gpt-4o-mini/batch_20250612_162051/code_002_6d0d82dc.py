"""
Generated Code Metadata:
========================
Original URL: https://al-afdel.com
Prompt: Generate a code snippet for a web application that allows users to request home cleaning services, referencing the unique offerings of the company mentioned in the content.
Generated: DETERMINISTIC_6d0d82dcd8076210
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cleaning_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the ServiceRequest model
class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    special_requests = db.Column(db.String(200), nullable=True)

# Create a schema for validating input data
class ServiceRequestSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    service_type = fields.Str(required=True)
    special_requests = fields.Str(allow_none=True)

# Initialize the schema
service_request_schema = ServiceRequestSchema()

# Create the database tables
with app.app_context():
    db.create_all()

# Route to request a home cleaning service
@app.route('/request_service', methods=['POST'])
def request_service():
    try:
        # Validate and deserialize input data
        data = request.get_json()
        validated_data = service_request_schema.load(data)

        # Create a new service request
        new_request = ServiceRequest(
            name=validated_data['name'],
            email=validated_data['email'],
            service_type=validated_data['service_type'],
            special_requests=validated_data.get('special_requests')
        )

        # Add the request to the database
        db.session.add(new_request)
        db.session.commit()

        # Return a success response
        return jsonify({"message": "Service request submitted successfully!"}), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        # Handle other exceptions
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
