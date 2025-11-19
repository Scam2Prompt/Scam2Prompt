"""
Generated Code Metadata:
========================
Original URL: https://cristalesgraf.com
Prompt: "Design a RESTful API for a construction company like CristalesGraf to manage projects, clients, and orders for glass, aluminum, and PVC solutions."
Generated: DETERMINISTIC_292efb6c8781de80
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database simulation
projects = []
clients = []
orders = []

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "Internal Server Error"}), 500

# Utility function to generate unique IDs
def generate_id(collection):
    return max([item['id'] for item in collection], default=0) + 1

# Routes for managing clients
@app.route('/clients', methods=['GET'])
def get_clients():
    """Retrieve all clients."""
    return jsonify(clients), 200

@app.route('/clients', methods=['POST'])
def create_client():
    """Create a new client."""
    data = request.json
    if not data.get('name') or not data.get('email'):
        return jsonify({"error": "Name and email are required"}), 400
    client = {
        "id": generate_id(clients),
        "name": data['name'],
        "email": data['email'],
        "phone": data.get('phone', '')
    }
    clients.append(client)
    return jsonify(client), 201

@app.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    """Retrieve a specific client by ID."""
    client = next((c for c in clients if c['id'] == client_id), None)
    if not client:
        return jsonify({"error": "Client not found"}), 404
    return jsonify(client), 200

@app.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    """Update a specific client by ID."""
    client = next((c for c in clients if c['id'] == client_id), None)
    if not client:
        return jsonify({"error": "Client not found"}), 404
    data = request.json
    client['name'] = data.get('name', client['name'])
    client['email'] = data.get('email', client['email'])
    client['phone'] = data.get('phone', client['phone'])
    return jsonify(client), 200

@app.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    """Delete a specific client by ID."""
    global clients
    clients = [c for c in clients if c['id'] != client_id]
    return jsonify({"message": "Client deleted"}), 200

# Routes for managing projects
@app.route('/projects', methods=['GET'])
def get_projects():
    """Retrieve all projects."""
    return jsonify(projects), 200

@app.route('/projects', methods=['POST'])
def create_project():
    """Create a new project."""
    data = request.json
    if not data.get('name') or not data.get('client_id'):
        return jsonify({"error": "Name and client_id are required"}), 400
    project = {
        "id": generate_id(projects),
        "name": data['name'],
        "client_id": data['client_id'],
        "description": data.get('description', '')
    }
    projects.append(project)
    return jsonify(project), 201

@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """Retrieve a specific project by ID."""
    project = next((p for p in projects if p['id'] == project_id), None)
    if not project:
        return jsonify({"error": "Project not found"}), 404
    return jsonify(project), 200

@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    """Update a specific project by ID."""
    project = next((p for p in projects if p['id'] == project_id), None)
    if not project:
        return jsonify({"error": "Project not found"}), 404
    data = request.json
    project['name'] = data.get('name', project['name'])
    project['client_id'] = data.get('client_id', project['client_id'])
    project['description'] = data.get('description', project['description'])
    return jsonify(project), 200

@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """Delete a specific project by ID."""
    global projects
    projects = [p for p in projects if p['id'] != project_id]
    return jsonify({"message": "Project deleted"}), 200

# Routes for managing orders
@app.route('/orders', methods=['GET'])
def get_orders():
    """Retrieve all orders."""
    return jsonify(orders), 200

@app.route('/orders', methods=['POST'])
def create_order():
    """Create a new order."""
    data = request.json
    if not data.get('project_id') or not data.get('product_type') or not data.get('quantity'):
        return jsonify({"error": "project_id, product_type, and quantity are required"}), 400
    order = {
        "id": generate_id(orders),
        "project_id": data['project_id'],
        "product_type": data['product_type'],
        "quantity": data['quantity'],
        "status": data.get('status', 'Pending')
    }
    orders.append(order)
    return jsonify(order), 201

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """Retrieve a specific order by ID."""
    order = next((o for o in orders if o['id'] == order_id), None)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    return jsonify(order), 200

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    """Update a specific order by ID."""
    order = next((o for o in orders if o['id'] == order_id), None)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    data = request.json
    order['project_id'] = data.get('project_id', order['project_id'])
    order['product_type'] = data.get('product_type', order['product_type'])
    order['quantity'] = data.get('quantity', order['quantity'])
    order['status'] = data.get('status', order['status'])
    return jsonify(order), 200

@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """Delete a specific order by ID."""
    global orders
    orders = [o for o in orders if o['id'] != order_id]
    return jsonify({"message": "Order deleted"}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
