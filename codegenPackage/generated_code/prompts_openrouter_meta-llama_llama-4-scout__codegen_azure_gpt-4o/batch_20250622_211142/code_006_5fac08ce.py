"""
Generated Code Metadata:
========================
Original URL: https://marinendtbd.com
Prompt: "Design a RESTful API for managing NDT services, including endpoints for customer registration, service requests, and employee management."
Generated: DETERMINISTIC_5fac08cec8510245
Batch ID: 20250622_211142
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

# In-memory data storage (for demonstration purposes)
customers = {}
services = {}
employees = {}

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "Internal Server Error"}), 500

# Endpoint: Register a new customer
@app.route('/customers', methods=['POST'])
def register_customer():
    """
    Registers a new customer.
    Request JSON format:
    {
        "id": "customer_id",
        "name": "customer_name",
        "email": "customer_email"
    }
    """
    data = request.json
    if not data or 'id' not in data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Invalid input"}), 400

    customer_id = data['id']
    if customer_id in customers:
        return jsonify({"error": "Customer already exists"}), 400

    customers[customer_id] = {
        "name": data['name'],
        "email": data['email']
    }
    return jsonify({"message": "Customer registered successfully"}), 201

# Endpoint: Create a new service request
@app.route('/services', methods=['POST'])
def create_service_request():
    """
    Creates a new service request.
    Request JSON format:
    {
        "id": "service_id",
        "customer_id": "customer_id",
        "description": "service_description"
    }
    """
    data = request.json
    if not data or 'id' not in data or 'customer_id' not in data or 'description' not in data:
        return jsonify({"error": "Invalid input"}), 400

    service_id = data['id']
    customer_id = data['customer_id']

    if service_id in services:
        return jsonify({"error": "Service request already exists"}), 400

    if customer_id not in customers:
        return jsonify({"error": "Customer not found"}), 404

    services[service_id] = {
        "customer_id": customer_id,
        "description": data['description']
    }
    return jsonify({"message": "Service request created successfully"}), 201

# Endpoint: Add a new employee
@app.route('/employees', methods=['POST'])
def add_employee():
    """
    Adds a new employee.
    Request JSON format:
    {
        "id": "employee_id",
        "name": "employee_name",
        "role": "employee_role"
    }
    """
    data = request.json
    if not data or 'id' not in data or 'name' not in data or 'role' not in data:
        return jsonify({"error": "Invalid input"}), 400

    employee_id = data['id']
    if employee_id in employees:
        return jsonify({"error": "Employee already exists"}), 400

    employees[employee_id] = {
        "name": data['name'],
        "role": data['role']
    }
    return jsonify({"message": "Employee added successfully"}), 201

# Endpoint: Get all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    """
    Retrieves all registered customers.
    """
    return jsonify(customers), 200

# Endpoint: Get all service requests
@app.route('/services', methods=['GET'])
def get_services():
    """
    Retrieves all service requests.
    """
    return jsonify(services), 200

# Endpoint: Get all employees
@app.route('/employees', methods=['GET'])
def get_employees():
    """
    Retrieves all employees.
    """
    return jsonify(employees), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
