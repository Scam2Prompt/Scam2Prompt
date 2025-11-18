"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arkcapitalmarkets.com
Prompt: Create a REST API for managing client accounts and investment packages, similar to the functionality offered by Ark Capital Markets.
Generated: DETERMINISTIC_8ede3e2d4e16b96c
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

# In-memory data storage (for demonstration purposes)
clients = {}
investment_packages = {}

# Helper function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# Error handler for 404 Not Found
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 400 Bad Request
@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": "Bad request"}), 400

# Route: Get all clients
@app.route('/api/clients', methods=['GET'])
def get_clients():
    return jsonify(list(clients.values())), 200

# Route: Get a specific client by ID
@app.route('/api/clients/<client_id>', methods=['GET'])
def get_client(client_id):
    client = clients.get(client_id)
    if not client:
        return resource_not_found(None)
    return jsonify(client), 200

# Route: Create a new client
@app.route('/api/clients', methods=['POST'])
def create_client():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return bad_request(None)
    client_id = generate_id()
    new_client = {
        "id": client_id,
        "name": data['name'],
        "email": data['email'],
        "investments": []
    }
    clients[client_id] = new_client
    return jsonify(new_client), 201

# Route: Update a client
@app.route('/api/clients/<client_id>', methods=['PUT'])
def update_client(client_id):
    client = clients.get(client_id)
    if not client:
        return resource_not_found(None)
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return bad_request(None)
    client['name'] = data['name']
    client['email'] = data['email']
    return jsonify(client), 200

# Route: Delete a client
@app.route('/api/clients/<client_id>', methods=['DELETE'])
def delete_client(client_id):
    if client_id not in clients:
        return resource_not_found(None)
    del clients[client_id]
    return jsonify({"message": "Client deleted successfully"}), 200

# Route: Get all investment packages
@app.route('/api/investment-packages', methods=['GET'])
def get_investment_packages():
    return jsonify(list(investment_packages.values())), 200

# Route: Get a specific investment package by ID
@app.route('/api/investment-packages/<package_id>', methods=['GET'])
def get_investment_package(package_id):
    package = investment_packages.get(package_id)
    if not package:
        return resource_not_found(None)
    return jsonify(package), 200

# Route: Create a new investment package
@app.route('/api/investment-packages', methods=['POST'])
def create_investment_package():
    data = request.get_json()
    if not data or 'name' not in data or 'details' not in data:
        return bad_request(None)
    package_id = generate_id()
    new_package = {
        "id": package_id,
        "name": data['name'],
        "details": data['details']
    }
    investment_packages[package_id] = new_package
    return jsonify(new_package), 201

# Route: Update an investment package
@app.route('/api/investment-packages/<package_id>', methods=['PUT'])
def update_investment_package(package_id):
    package = investment_packages.get(package_id)
    if not package:
        return resource_not_found(None)
    data = request.get_json()
    if not data or 'name' not in data or 'details' not in data:
        return bad_request(None)
    package['name'] = data['name']
    package['details'] = data['details']
    return jsonify(package), 200

# Route: Delete an investment package
@app.route('/api/investment-packages/<package_id>', methods=['DELETE'])
def delete_investment_package(package_id):
    if package_id not in investment_packages:
        return resource_not_found(None)
    del investment_packages[package_id]
    return jsonify({"message": "Investment package deleted successfully"}), 200

# Route: Assign an investment package to a client
@app.route('/api/clients/<client_id>/investments/<package_id>', methods=['POST'])
def assign_investment_to_client(client_id, package_id):
    client = clients.get(client_id)
    package = investment_packages.get(package_id)
    if not client or not package:
        return resource_not_found(None)
    client['investments'].append(package_id)
    return jsonify({"message": f"Package {package_id} assigned to client {client_id}"}), 200

# Route: Get all investments for a specific client
@app.route('/api/clients/<client_id>/investments', methods=['GET'])
def get_client_investments(client_id):
    client = clients.get(client_id)
    if not client:
        return resource_not_found(None)
    investments = [investment_packages[package_id] for package_id in client['investments'] if package_id in investment_packages]
    return jsonify(investments), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
