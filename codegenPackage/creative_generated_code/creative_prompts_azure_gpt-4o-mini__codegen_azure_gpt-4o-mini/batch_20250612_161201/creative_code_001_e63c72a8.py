"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dexodoor.com
Prompt: How can I implement an API to manage UPVC door installation requests, taking inspiration from the services offered by DEXODOOR?
Generated: DETERMINISTIC_e63c72a80ba9f31f
Batch ID: 20250612_161201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///upvc_doors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy database instance
db = SQLAlchemy(app)

# Database model for Door Installation Requests
class DoorInstallationRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    door_type = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default='Pending')  # Default status

    def to_dict(self):
        """Convert the request object to a dictionary."""
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'address': self.address,
            'door_type': self.door_type,
            'status': self.status
        }

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to create a new installation request
@app.route('/api/installation-requests', methods=['POST'])
def create_request():
    data = request.get_json()
    if not data or not all(key in data for key in ('customer_name', 'address', 'door_type')):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        new_request = DoorInstallationRequest(
            customer_name=data['customer_name'],
            address=data['address'],
            door_type=data['door_type']
        )
        db.session.add(new_request)
        db.session.commit()
        return jsonify(new_request.to_dict()), 201
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({'error': 'Failed to create installation request'}), 500

# API endpoint to retrieve all installation requests
@app.route('/api/installation-requests', methods=['GET'])
def get_requests():
    try:
        requests = DoorInstallationRequest.query.all()
        return jsonify([request.to_dict() for request in requests]), 200
    except SQLAlchemyError:
        return jsonify({'error': 'Failed to retrieve installation requests'}), 500

# API endpoint to update a specific installation request
@app.route('/api/installation-requests/<int:request_id>', methods=['PUT'])
def update_request(request_id):
    data = request.get_json()
    request_to_update = DoorInstallationRequest.query.get(request_id)

    if not request_to_update:
        return jsonify({'error': 'Request not found'}), 404

    if 'status' in data:
        request_to_update.status = data['status']
    
    try:
        db.session.commit()
        return jsonify(request_to_update.to_dict()), 200
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({'error': 'Failed to update installation request'}), 500

# API endpoint to delete a specific installation request
@app.route('/api/installation-requests/<int:request_id>', methods=['DELETE'])
def delete_request(request_id):
    request_to_delete = DoorInstallationRequest.query.get(request_id)

    if not request_to_delete:
        return jsonify({'error': 'Request not found'}), 404

    try:
        db.session.delete(request_to_delete)
        db.session.commit()
        return jsonify({'message': 'Request deleted successfully'}), 204
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({'error': 'Failed to delete installation request'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
