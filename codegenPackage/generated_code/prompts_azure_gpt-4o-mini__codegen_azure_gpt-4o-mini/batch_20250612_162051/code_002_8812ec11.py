"""
Generated Code Metadata:
========================
Original URL: https://olgadorks.com
Prompt: Create an API endpoint for a logistics application that allows users to request clearing and forwarding services, similar to those provided by Olgadorks Shipping Company.
Generated: DETERMINISTIC_8812ec118ac59574
Batch ID: 20250612_162051
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

# Initialize Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logistics.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the ServiceRequest model
class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    details = db.Column(db.Text, nullable=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Define the schema for request validation
class ServiceRequestSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    service_type = fields.Str(required=True)
    details = fields.Str(required=False)

# Initialize the schema
service_request_schema = ServiceRequestSchema()

@app.route('/api/service-request', methods=['POST'])
def request_service():
    """
    API endpoint to request clearing and forwarding services.
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
            details=validated_data.get('details')
        )

        # Add the request to the database
        db.session.add(new_request)
        db.session.commit()

        # Return a success response
        return jsonify({"message": "Service request submitted successfully.", "id": new_request.id}), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
