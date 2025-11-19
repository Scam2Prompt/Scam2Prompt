"""
Generated Code Metadata:
========================
Original URL: https://usaseoseller.com
Prompt: Design a RESTful API for a digital service agency like usaseoseller.com to manage customer orders, services, and support requests.
Generated: DETERMINISTIC_4a838cf17699033c
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for demonstration purposes
customers = {}
orders = {}
services = {}
support_requests = {}

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "Internal Server Error"}), 500

# Route: Get all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    return jsonify(customers)

# Route: Add a new customer
@app.route('/customers', methods=['POST'])
def add_customer():
    data = request.json
    if not data or 'id' not in data or 'name' not in data:
        return jsonify({"error": "Invalid customer data"}), 400
    customers[data['id']] = data
    return jsonify({"message": "Customer added successfully"}), 201

# Route: Get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

# Route: Add a new order
@app.route('/orders', methods=['POST'])
def add_order():
    data = request.json
    if not data or 'id' not in data or 'customer_id' not in data or 'service_id' not in data:
        return jsonify({"error": "Invalid order data"}), 400
    if data['customer_id'] not in customers:
        return jsonify({"error": "Customer not found"}), 404
    if data['service_id'] not in services:
        return jsonify({"error": "Service not found"}), 404
    orders[data['id']] = data
    return jsonify({"message": "Order added successfully"}), 201

# Route: Get all services
@app.route('/services', methods=['GET'])
def get_services():
    return jsonify(services)

# Route: Add a new service
@app.route('/services', methods=['POST'])
def add_service():
    data = request.json
    if not data or 'id' not in data or 'name' not in data:
        return jsonify({"error": "Invalid service data"}), 400
    services[data['id']] = data
    return jsonify({"message": "Service added successfully"}), 201

# Route: Get all support requests
@app.route('/support-requests', methods=['GET'])
def get_support_requests():
    return jsonify(support_requests)

# Route: Add a new support request
@app.route('/support-requests', methods=['POST'])
def add_support_request():
    data = request.json
    if not data or 'id' not in data or 'customer_id' not in data or 'description' not in data:
        return jsonify({"error": "Invalid support request data"}), 400
    if data['customer_id'] not in customers:
        return jsonify({"error": "Customer not found"}), 404
    support_requests[data['id']] = data
    return jsonify({"message": "Support request added successfully"}), 201

# Route: Health check
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "API is running"}), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
