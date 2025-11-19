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
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask app
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vidanjor_service_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the ServiceRequest model
class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    request_details = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(50), default="Pending")  # Default status is "Pending"

    def to_dict(self):
        """Convert the model instance to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'address': self.address,
            'phone_number': self.phone_number,
            'request_details': self.request_details,
            'status': self.status
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Error handler for database errors
@app.errorhandler(SQLAlchemyError)
def handle_db_error(error):
    """Handle database-related errors."""
    return jsonify({'error': 'A database error occurred', 'details': str(error)}), 500

# Endpoint to create a new service request
@app.route('/service_requests', methods=['POST'])
def create_service_request():
    """Create a new vidanjör service request."""
    data = request.json
    try:
        new_request = ServiceRequest(
            customer_name=data['customer_name'],
            address=data['address'],
            phone_number=data['phone_number'],
            request_details=data['request_details']
        )
        db.session.add(new_request)
        db.session.commit()
        return jsonify({'message': 'Service request created successfully', 'service_request': new_request.to_dict()}), 201
    except KeyError as e:
        return jsonify({'error': f'Missing required field: {str(e)}'}), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return handle_db_error(e)

# Endpoint to get all service requests
@app.route('/service_requests', methods=['GET'])
def get_service_requests():
    """Retrieve all vidanjör service requests."""
    service_requests = ServiceRequest.query.all()
    return jsonify([request.to_dict() for request in service_requests]), 200

# Endpoint to get a specific service request by ID
@app.route('/service_requests/<int:request_id>', methods=['GET'])
def get_service_request(request_id):
    """Retrieve a specific vidanjör service request by ID."""
    service_request = ServiceRequest.query.get(request_id)
    if service_request:
        return jsonify(service_request.to_dict()), 200
    return jsonify({'error': 'Service request not found'}), 404

# Endpoint to update a service request by ID
@app.route('/service_requests/<int:request_id>', methods=['PUT'])
def update_service_request(request_id):
    """Update a specific vidanjör service request by ID."""
    data = request.json
    service_request = ServiceRequest.query.get(request_id)
    if not service_request:
        return jsonify({'error': 'Service request not found'}), 404
    try:
        service_request.customer_name = data.get('customer_name', service_request.customer_name)
        service_request.address = data.get('address', service_request.address)
        service_request.phone_number = data.get('phone_number', service_request.phone_number)
        service_request.request_details = data.get('request_details', service_request.request_details)
        service_request.status = data.get('status', service_request.status)
        db.session.commit()
        return jsonify({'message': 'Service request updated successfully', 'service_request': service_request.to_dict()}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return handle_db_error(e)

# Endpoint to delete a service request by ID
@app.route('/service_requests/<int:request_id>', methods=['DELETE'])
def delete_service_request(request_id):
    """Delete a specific vidanjör service request by ID."""
    service_request = ServiceRequest.query.get(request_id)
    if not service_request:
        return jsonify({'error': 'Service request not found'}), 404
    try:
        db.session.delete(service_request)
        db.session.commit()
        return jsonify({'message': 'Service request deleted successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return handle_db_error(e)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
