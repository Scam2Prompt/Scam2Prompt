"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.oasishottubsep.com
Prompt: Recommend an API or library to build a web-based tool for scheduling hot tub maintenance services, similar to the service request system on the Oasis Hot Tubs website.
Generated: DETERMINISTIC_ec5a78a021b0fd31
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hot_tub_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Service model
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    service_date = db.Column(db.DateTime, nullable=False)
    service_type = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'service_date': self.service_date.isoformat(),
            'service_type': self.service_type
        }

# Create the database and tables
with app.app_context():
    db.create_all()

# Endpoint to create a new service request
@app.route('/services', methods=['POST'])
def create_service():
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ('customer_name', 'service_date', 'service_type')):
            return jsonify({'error': 'Invalid input'}), 400
        
        service_date = datetime.fromisoformat(data['service_date'])
        new_service = Service(
            customer_name=data['customer_name'],
            service_date=service_date,
            service_type=data['service_type']
        )
        db.session.add(new_service)
        db.session.commit()
        return jsonify(new_service.to_dict()), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to get all service requests
@app.route('/services', methods=['GET'])
def get_services():
    try:
        services = Service.query.all()
        return jsonify([service.to_dict() for service in services]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to get a specific service request by ID
@app.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    try:
        service = Service.query.get(service_id)
        if service is None:
            return jsonify({'error': 'Service not found'}), 404
        return jsonify(service.to_dict()), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to update a service request
@app.route('/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    try:
        data = request.get_json()
        service = Service.query.get(service_id)
        if service is None:
            return jsonify({'error': 'Service not found'}), 404
        
        service.customer_name = data.get('customer_name', service.customer_name)
        service.service_date = datetime.fromisoformat(data.get('service_date', service.service_date.isoformat()))
        service.service_type = data.get('service_type', service.service_type)
        db.session.commit()
        return jsonify(service.to_dict()), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to delete a service request
@app.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    try:
        service = Service.query.get(service_id)
        if service is None:
            return jsonify({'error': 'Service not found'}), 404
        db.session.delete(service)
        db.session.commit()
        return jsonify({'message': 'Service deleted successfully'}), 204

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true', host='0.0.0.0', port=5000)
```
