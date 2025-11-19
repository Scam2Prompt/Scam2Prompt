"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somcivil.com
Prompt: Create a REST API that allows users to submit requests for waterproofing services, incorporating the unique challenges faced by coastal cities as described by SOM Civil.
Generated: DETERMINISTIC_06c9201d235f80da
Batch ID: 20250612_164010
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///waterproofing_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy ORM
db = SQLAlchemy(app)

# Define a model for waterproofing requests
class WaterproofingRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    additional_info = db.Column(db.Text, nullable=True)

# Schema for request validation
class WaterproofingRequestSchema(Schema):
    name = fields.Str(required=True)
    address = fields.Str(required=True)
    city = fields.Str(required=True)
    service_type = fields.Str(required=True)
    additional_info = fields.Str()

# Create the database on startup
@app.before_first_request
def create_tables():
    db.create_all()

# Route to handle submitting waterproofing service requests
@app.route('/api/waterproofing-requests', methods=['POST'])
def submit_request():
    # Parse and validate incoming JSON data
    schema = WaterproofingRequestSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400  # Return validation errors

    # Create a new waterproofing request instance
    new_request = WaterproofingRequest(
        name=data['name'],
        address=data['address'],
        city=data['city'],
        service_type=data['service_type'],
        additional_info=data.get('additional_info')
    )

    # Add the request to the database
    db.session.add(new_request)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500  # Handle database errors

    # Return the created request with a success status
    return jsonify({"message": "Request submitted successfully", "id": new_request.id}), 201

# Route to retrieve all waterproofing requests
@app.route('/api/waterproofing-requests', methods=['GET'])
def get_requests():
    requests = WaterproofingRequest.query.all()
    result = [
        {
            "id": req.id,
            "name": req.name,
            "address": req.address,
            "city": req.city,
            "service_type": req.service_type,
            "additional_info": req.additional_info
        } for req in requests
    ]
    return jsonify(result), 200  # Return all requests

# Handle 404 errors
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404

# Handle internal server errors
@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "An internal error occurred"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
