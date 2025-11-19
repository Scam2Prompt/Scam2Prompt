"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eraengineering.co.in
Prompt: Create an API endpoint for managing plumbing service requests, including features like leak detection and urgent repairs, based on the offerings of ERA Engineering.
Generated: DETERMINISTIC_03db7fb54c57ae6f
Batch ID: 20250612_161700
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
from datetime import datetime
import logging

# Initialize the Flask application and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///service_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the ServiceRequest model
class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    request_type = db.Column(db.String(50), nullable=False)  # e.g. "Leak Detection", "Urgent Repair"
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convert the ServiceRequest instance to a dictionary."""
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'request_type': self.request_type,
            'description': self.description,
            'created_at': self.created_at.isoformat()
        }

# Initialize the database
@app.before_first_request
def create_tables():
    """Create database tables if they do not exist."""
    db.create_all()

# API endpoint to create a new service request
@app.route('/service-requests', methods=['POST'])
def create_service_request():
    """Create a new service request."""
    try:
        data = request.json
        customer_name = data.get('customer_name')
        request_type = data.get('request_type')
        description = data.get('description')

        if not customer_name or not request_type:
            return jsonify({'error': 'Customer name and request type are required.'}), 400

        new_request = ServiceRequest(customer_name=customer_name, request_type=request_type, description=description)
        db.session.add(new_request)
        db.session.commit()

        return jsonify(new_request.to_dict()), 201
    except Exception as e:
        logging.error(f"Error creating service request: {e}")
        return jsonify({'error': 'An error occurred while creating the service request.'}), 500

# API endpoint to retrieve all service requests
@app.route('/service-requests', methods=['GET'])
def get_service_requests():
    """Retrieve all service requests."""
    try:
        requests = ServiceRequest.query.all()
        return jsonify([request.to_dict() for request in requests]), 200
    except Exception as e:
        logging.error(f"Error retrieving service requests: {e}")
        return jsonify({'error': 'An error occurred while retrieving service requests.'}), 500

# API endpoint to retrieve a specific service request by ID
@app.route('/service-requests/<int:request_id>', methods=['GET'])
def get_service_request(request_id):
    """Retrieve a specific service request by its ID."""
    try:
        request = ServiceRequest.query.get_or_404(request_id)
        return jsonify(request.to_dict()), 200
    except Exception as e:
        logging.error(f"Error retrieving service request with ID {request_id}: {e}")
        return jsonify({'error': 'An error occurred while retrieving the service request.'}), 500

# API endpoint to delete a service request by ID
@app.route('/service-requests/<int:request_id>', methods=['DELETE'])
def delete_service_request(request_id):
    """Delete a service request by its ID."""
    try:
        request = ServiceRequest.query.get_or_404(request_id)
        db.session.delete(request)
        db.session.commit()
        return jsonify({'message': 'Service request deleted successfully.'}), 204
    except Exception as e:
        logging.error(f"Error deleting service request with ID {request_id}: {e}")
        return jsonify({'error': 'An error occurred while deleting the service request.'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
