"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fealtyworldwide.com
Prompt: Develop an API for managing customer logistics requests, including air freight, road freight, and ocean freight, inspired by Fealty Worldwide's service categories.
Generated: DETERMINISTIC_5568961b33fb7f84
Batch ID: 20250612_151547
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logistics.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Customer Logistics Request Model
class LogisticsRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    freight_type = db.Column(db.String(50), nullable=False)  # e.g., air, road, ocean
    details = db.Column(db.Text, nullable=True)

# Schema for request validation and serialization
class LogisticsRequestSchema(Schema):
    customer_name = fields.Str(required=True)
    freight_type = fields.Str(required=True, validate=lambda s: s in ['air', 'road', 'ocean'])
    details = fields.Str(required=False)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/logistics', methods=['POST'])
def create_logistics_request():
    """Create a new logistics request."""
    schema = LogisticsRequestSchema()
    try:
        # Validate and deserialize input data
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create a new LogisticsRequest instance
    new_request = LogisticsRequest(
        customer_name=data['customer_name'],
        freight_type=data['freight_type'],
        details=data.get('details')
    )
    
    # Add the new request to the database
    db.session.add(new_request)
    db.session.commit()

    return schema.dump(new_request), 201

@app.route('/logistics', methods=['GET'])
def get_logistics_requests():
    """Retrieve all logistics requests."""
    requests = LogisticsRequest.query.all()
    schema = LogisticsRequestSchema(many=True)
    return jsonify(schema.dump(requests)), 200

@app.route('/logistics/<int:req_id>', methods=['GET'])
def get_logistics_request(req_id):
    """Retrieve a specific logistics request by ID."""
    request_data = LogisticsRequest.query.get(req_id)
    if request_data is None:
        return jsonify({'message': 'Logistics request not found.'}), 404
    
    schema = LogisticsRequestSchema()
    return jsonify(schema.dump(request_data)), 200

@app.route('/logistics/<int:req_id>', methods=['PUT'])
def update_logistics_request(req_id):
    """Update an existing logistics request."""
    schema = LogisticsRequestSchema()
    request_data = LogisticsRequest.query.get(req_id)
    
    if request_data is None:
        return jsonify({'message': 'Logistics request not found.'}), 404
    
    try:
        # Validate and deserialize input data
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Update the request details
    request_data.customer_name = data['customer_name']
    request_data.freight_type = data['freight_type']
    request_data.details = data.get('details')
    
    db.session.commit()
    
    return schema.dump(request_data), 200

@app.route('/logistics/<int:req_id>', methods=['DELETE'])
def delete_logistics_request(req_id):
    """Delete a logistics request by ID."""
    request_data = LogisticsRequest.query.get(req_id)
    if request_data is None:
        return jsonify({'message': 'Logistics request not found.'}), 404
    
    db.session.delete(request_data)
    db.session.commit()
    
    return jsonify({'message': 'Logistics request deleted successfully.'}), 204

if __name__ == '__main__':
    app.run(debug=True)
```
