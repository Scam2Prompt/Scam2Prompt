"""
Generated Code Metadata:
========================
Original URL: https://enyakinvidanjor.com
Prompt: Develop a RESTful API using Flask to manage vidanjör service requests, including endpoints for creating, reading, updating, and deleting service requests, and integrating with a database for storage.
Generated: DETERMINISTIC_ea52ae002dd6885e
Batch ID: 20250622_210703
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///service_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the ServiceRequest model
class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), default='Pending')

    def to_dict(self):
        """Convert the ServiceRequest object to a dictionary."""
        return {
            'id': self.id,
            'description': self.description,
            'status': self.status
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/service_requests', methods=['POST'])
def create_service_request():
    """Create a new service request."""
    data = request.get_json()
    if not data or 'description' not in data:
        return jsonify({'error': 'Description is required'}), 400

    new_request = ServiceRequest(description=data['description'])
    db.session.add(new_request)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to create service request'}), 500

    return jsonify(new_request.to_dict()), 201

@app.route('/service_requests', methods=['GET'])
def get_service_requests():
    """Retrieve all service requests."""
    requests = ServiceRequest.query.all()
    return jsonify([request.to_dict() for request in requests]), 200

@app.route('/service_requests/<int:request_id>', methods=['GET'])
def get_service_request(request_id):
    """Retrieve a specific service request by ID."""
    request = ServiceRequest.query.get(request_id)
    if request is None:
        return jsonify({'error': 'Service request not found'}), 404
    return jsonify(request.to_dict()), 200

@app.route('/service_requests/<int:request_id>', methods=['PUT'])
def update_service_request(request_id):
    """Update an existing service request."""
    request_to_update = ServiceRequest.query.get(request_id)
    if request_to_update is None:
        return jsonify({'error': 'Service request not found'}), 404

    data = request.get_json()
    if 'description' in data:
        request_to_update.description = data['description']
    if 'status' in data:
        request_to_update.status = data['status']

    db.session.commit()
    return jsonify(request_to_update.to_dict()), 200

@app.route('/service_requests/<int:request_id>', methods=['DELETE'])
def delete_service_request(request_id):
    """Delete a service request."""
    request_to_delete = ServiceRequest.query.get(request_id)
    if request_to_delete is None:
        return jsonify({'error': 'Service request not found'}), 404

    db.session.delete(request_to_delete)
    db.session.commit()
    return jsonify({'message': 'Service request deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=True)
```
