"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinofinance.com
Prompt: Generate a REST API for managing legal file financing requests, referencing Rhino Finance's "File Financing" service.
Generated: DETERMINISTIC_32a6c70188213831
Batch ID: 20250612_142640
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
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///financing_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the FinancingRequest model
class FinancingRequest(db.Model):
    __tablename__ = 'financing_requests'
    
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    amount_requested = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='Pending')

    def to_dict(self):
        return {
            'id': self.id,
            'client_name': self.client_name,
            'amount_requested': self.amount_requested,
            'status': self.status
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/financing_requests', methods=['POST'])
def create_financing_request():
    """Create a new financing request."""
    data = request.json
    if not data or 'client_name' not in data or 'amount_requested' not in data:
        raise BadRequest("Missing 'client_name' or 'amount_requested' in request data.")

    new_request = FinancingRequest(
        client_name=data['client_name'],
        amount_requested=data['amount_requested']
    )
    db.session.add(new_request)
    db.session.commit()

    return jsonify(new_request.to_dict()), 201

@app.route('/api/financing_requests', methods=['GET'])
def get_financing_requests():
    """Retrieve all financing requests."""
    requests = FinancingRequest.query.all()
    return jsonify([req.to_dict() for req in requests]), 200

@app.route('/api/financing_requests/<int:request_id>', methods=['GET'])
def get_financing_request(request_id):
    """Retrieve a specific financing request by ID."""
    financing_request = FinancingRequest.query.get(request_id)
    if not financing_request:
        raise NotFound(f"Financing request with id {request_id} not found.")
    
    return jsonify(financing_request.to_dict()), 200

@app.route('/api/financing_requests/<int:request_id>', methods=['PUT'])
def update_financing_request(request_id):
    """Update a specific financing request."""
    financing_request = FinancingRequest.query.get(request_id)
    if not financing_request:
        raise NotFound(f"Financing request with id {request_id} not found.")
    
    data = request.json
    if 'client_name' in data:
        financing_request.client_name = data['client_name']
    if 'amount_requested' in data:
        financing_request.amount_requested = data['amount_requested']
    if 'status' in data:
        financing_request.status = data['status']

    db.session.commit()
    return jsonify(financing_request.to_dict()), 200

@app.route('/api/financing_requests/<int:request_id>', methods=['DELETE'])
def delete_financing_request(request_id):
    """Delete a specific financing request."""
    financing_request = FinancingRequest.query.get(request_id)
    if not financing_request:
        raise NotFound(f"Financing request with id {request_id} not found.")
    
    db.session.delete(financing_request)
    db.session.commit()
    return jsonify({"message": "Financing request deleted successfully."}), 204

if __name__ == '__main__':
    app.run(debug=False)
```
