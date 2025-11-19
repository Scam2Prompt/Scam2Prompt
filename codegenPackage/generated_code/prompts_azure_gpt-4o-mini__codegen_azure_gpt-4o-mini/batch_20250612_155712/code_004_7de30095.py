"""
Generated Code Metadata:
========================
Original URL: https://rhinoassetfinance.com
Prompt: Outline a RESTful API that supports financing requests for agricultural equipment, detailing the necessary endpoints and data structures.
Generated: DETERMINISTIC_7de30095087036d5
Batch ID: 20250612_155712
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///financing_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for FinancingRequest
class FinancingRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicant_name = db.Column(db.String(100), nullable=False)
    equipment_type = db.Column(db.String(100), nullable=False)
    amount_requested = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='pending')

# Schema for validating input data
class FinancingRequestSchema(Schema):
    applicant_name = fields.Str(required=True)
    equipment_type = fields.Str(required=True)
    amount_requested = fields.Float(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new financing request
@app.route('/api/financing_requests', methods=['POST'])
def create_financing_request():
    try:
        # Validate and deserialize input data
        request_data = request.get_json()
        schema = FinancingRequestSchema()
        validated_data = schema.load(request_data)

        # Create a new financing request
        new_request = FinancingRequest(**validated_data)
        db.session.add(new_request)
        db.session.commit()

        return jsonify({"id": new_request.id, "status": new_request.status}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all financing requests
@app.route('/api/financing_requests', methods=['GET'])
def get_financing_requests():
    try:
        requests = FinancingRequest.query.all()
        schema = FinancingRequestSchema(many=True)
        return jsonify(schema.dump(requests)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve a specific financing request by ID
@app.route('/api/financing_requests/<int:request_id>', methods=['GET'])
def get_financing_request(request_id):
    try:
        request_item = FinancingRequest.query.get_or_404(request_id)
        schema = FinancingRequestSchema()
        return jsonify(schema.dump(request_item)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to update the status of a financing request
@app.route('/api/financing_requests/<int:request_id>', methods=['PUT'])
def update_financing_request(request_id):
    try:
        request_data = request.get_json()
        request_item = FinancingRequest.query.get_or_404(request_id)

        # Update the status if provided
        if 'status' in request_data:
            request_item.status = request_data['status']

        db.session.commit()
        return jsonify({"id": request_item.id, "status": request_item.status}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to delete a financing request
@app.route('/api/financing_requests/<int:request_id>', methods=['DELETE'])
def delete_financing_request(request_id):
    try:
        request_item = FinancingRequest.query.get_or_404(request_id)
        db.session.delete(request_item)
        db.session.commit()
        return jsonify({"message": "Request deleted successfully"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
