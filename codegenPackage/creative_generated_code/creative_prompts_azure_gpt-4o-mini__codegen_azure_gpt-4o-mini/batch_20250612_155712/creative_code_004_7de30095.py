"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinoassetfinance.com
Prompt: Outline a RESTful API that supports financing requests for agricultural equipment, detailing the necessary endpoints and data structures.
Generated: DETERMINISTIC_7de30095087036d5
Batch ID: 20250612_155712
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

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///financing_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for FinancingRequest
class FinancingRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicant_name = db.Column(db.String(100), nullable=False)
    equipment_type = db.Column(db.String(100), nullable=False)
    amount_requested = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pending')

# Schema for input validation
class FinancingRequestSchema(Schema):
    applicant_name = fields.Str(required=True)
    equipment_type = fields.Str(required=True)
    amount_requested = fields.Float(required=True)
    status = fields.Str()

# Initialize the database
with app.app_context():
    db.create_all()

# Create a new financing request
@app.route('/api/financing_requests', methods=['POST'])
def create_financing_request():
    schema = FinancingRequestSchema()
    try:
        # Validate and deserialize input data
        request_data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create a new FinancingRequest instance
    financing_request = FinancingRequest(**request_data)

    # Add to session and commit to database
    db.session.add(financing_request)
    db.session.commit()
    
    # Return the created financing request
    return jsonify(schema.dump(financing_request)), 201

# Get all financing requests
@app.route('/api/financing_requests', methods=['GET'])
def get_financing_requests():
    requests = FinancingRequest.query.all()
    schema = FinancingRequestSchema(many=True)
    return jsonify(schema.dump(requests)), 200

# Get a specific financing request by ID
@app.route('/api/financing_requests/<int:request_id>', methods=['GET'])
def get_financing_request(request_id):
    financing_request = FinancingRequest.query.get_or_404(request_id)
    schema = FinancingRequestSchema()
    return jsonify(schema.dump(financing_request)), 200

# Update a specific financing request
@app.route('/api/financing_requests/<int:request_id>', methods=['PUT'])
def update_financing_request(request_id):
    financing_request = FinancingRequest.query.get_or_404(request_id)
    schema = FinancingRequestSchema(partial=True)
    try:
        # Validate and deserialize input data
        request_data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Update the financing request fields
    for key, value in request_data.items():
        setattr(financing_request, key, value)

    # Commit changes to the database
    db.session.commit()
    return jsonify(schema.dump(financing_request)), 200

# Delete a specific financing request
@app.route('/api/financing_requests/<int:request_id>', methods=['DELETE'])
def delete_financing_request(request_id):
    financing_request = FinancingRequest.query.get_or_404(request_id)
    db.session.delete(financing_request)
    db.session.commit()
    return jsonify({'message': 'Financing request deleted successfully'}), 204

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
