"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renovation-toiture-toulouse.com
Prompt: Develop a REST API endpoint that allows users to submit requests for roofing services, including fields for type of service (repair, installation, etc.) and location in Toulouse.
Generated: DETERMINISTIC_9324e0a1c3dc31a1
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
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for demonstration purposes)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///roofing_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a model for the roofing service requests
class RoofingServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)

# Initialize the database and create the tables
with app.app_context():
    db.create_all()

# Define a schema for request validation
class RoofingServiceRequestSchema(Schema):
    service_type = fields.Str(required=True)
    location = fields.Str(required=True)

# Create an instance of the schema
request_schema = RoofingServiceRequestSchema()

@app.route('/api/request_service', methods=['POST'])
def request_service():
    """Endpoint to submit a roofing service request."""
    try:
        # Validate and deserialize input data
        data = request_schema.load(request.json)

        # Create a new service request instance
        new_request = RoofingServiceRequest(
            service_type=data['service_type'],
            location=data['location']
        )

        # Add the new request to the database
        db.session.add(new_request)
        db.session.commit()

        # Return a success response
        return jsonify({"message": "Service request submitted successfully.", "id": new_request.id}), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        # Handle general exceptions
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```
