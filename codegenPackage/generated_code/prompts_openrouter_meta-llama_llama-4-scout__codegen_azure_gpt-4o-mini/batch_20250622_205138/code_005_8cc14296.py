"""
Generated Code Metadata:
========================
Original URL: https://renzooprotocal.net
Prompt: Design a RESTful API for a cleaning services platform, including endpoints for customer registration, service requests, and payment processing, based on the services offered by Queen Bee Renzo Protocol Cleaning Services.
Generated: DETERMINISTIC_8cc14296fb3271bf
Batch ID: 20250622_205138
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
from werkzeug.exceptions import BadRequest, NotFound
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///cleaning_services.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Customer model
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

# Define the ServiceRequest model
class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    service_type = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default='Pending')

# Define the Payment model
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_request_id = db.Column(db.Integer, db.ForeignKey('service_request.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='Pending')

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint for customer registration
@app.route('/api/customers', methods=['POST'])
def register_customer():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        raise BadRequest("Missing 'name' or 'email' in request data.")
    
    new_customer = Customer(name=data['name'], email=data['email'])
    db.session.add(new_customer)
    db.session.commit()
    
    return jsonify({"id": new_customer.id, "name": new_customer.name, "email": new_customer.email}), 201

# Endpoint for creating a service request
@app.route('/api/service_requests', methods=['POST'])
def create_service_request():
    data = request.get_json()
    if not data or 'customer_id' not in data or 'service_type' not in data:
        raise BadRequest("Missing 'customer_id' or 'service_type' in request data.")
    
    new_request = ServiceRequest(customer_id=data['customer_id'], service_type=data['service_type'])
    db.session.add(new_request)
    db.session.commit()
    
    return jsonify({"id": new_request.id, "customer_id": new_request.customer_id, "service_type": new_request.service_type, "status": new_request.status}), 201

# Endpoint for processing payments
@app.route('/api/payments', methods=['POST'])
def process_payment():
    data = request.get_json()
    if not data or 'service_request_id' not in data or 'amount' not in data:
        raise BadRequest("Missing 'service_request_id' or 'amount' in request data.")
    
    new_payment = Payment(service_request_id=data['service_request_id'], amount=data['amount'])
    db.session.add(new_payment)
    db.session.commit()
    
    return jsonify({"id": new_payment.id, "service_request_id": new_payment.service_request_id, "amount": new_payment.amount, "status": new_payment.status}), 201

# Error handling for not found resources
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
