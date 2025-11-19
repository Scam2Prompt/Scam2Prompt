"""
Generated Code Metadata:
========================
Original URL: https://scout.kz
Prompt: "Suggest a RESTful API structure for managing orders, customers, and equipment inventory for a SCOUT dealership in Kazakhstan."
Generated: DETERMINISTIC_242171706101684d
Batch ID: 20250622_210655
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
orders = []
customers = []
equipment_inventory = []

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "Internal Server Error"}), 500

# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "API is running"}), 200

# Customers endpoints
@app.route('/api/customers', methods=['GET'])
def get_customers():
    return jsonify(customers), 200

@app.route('/api/customers', methods=['POST'])
def create_customer():
    data = request.json
    if not data.get('name') or not data.get('email'):
        return jsonify({"error": "Name and email are required"}), 400
    customer = {
        "id": len(customers) + 1,
        "name": data['name'],
        "email": data['email']
    }
    customers.append(customer)
    return jsonify(customer), 201

@app.route('/api/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = next((c for c in customers if c['id'] == customer_id), None)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404
    return jsonify(customer), 200

@app.route('/api/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    customer = next((c for c in customers if c['id'] == customer_id), None)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404
    data = request.json
    customer['name'] = data.get('name', customer['name'])
    customer['email'] = data.get('email', customer['email'])
    return jsonify(customer), 200

@app.route('/api/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    global customers
    customers = [c for c in customers if c['id'] != customer_id]
    return jsonify({"message": "Customer deleted"}), 200

# Orders endpoints
@app.route('/api/orders', methods=['GET'])
def get_orders():
    return jsonify(orders), 200

@app.route('/api/orders', methods=['POST'])
def create_order():
    data = request.json
    if not data.get('customer_id') or not data.get('equipment_id'):
        return jsonify({"error": "Customer ID and Equipment ID are required"}), 400
    order = {
        "id": len(orders) + 1,
        "customer_id": data['customer_id'],
        "equipment_id": data['equipment_id'],
        "status": data.get('status', 'Pending')
    }
    orders.append(order)
    return jsonify(order), 201

@app.route('/api/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = next((o for o in orders if o['id'] == order_id), None)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    return jsonify(order), 200

@app.route('/api/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    order = next((o for o in orders if o['id'] == order_id), None)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    data = request.json
    order['status'] = data.get('status', order['status'])
    return jsonify(order), 200

@app.route('/api/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    global orders
    orders = [o for o in orders if o['id'] != order_id]
    return jsonify({"message": "Order deleted"}), 200

# Equipment Inventory endpoints
@app.route('/api/equipment', methods=['GET'])
def get_equipment():
    return jsonify(equipment_inventory), 200

@app.route('/api/equipment', methods=['POST'])
def add_equipment():
    data = request.json
    if not data.get('name') or not data.get('quantity'):
        return jsonify({"error": "Name and quantity are required"}), 400
    equipment = {
        "id": len(equipment_inventory) + 1,
        "name": data['name'],
        "quantity": data['quantity']
    }
    equipment_inventory.append(equipment)
    return jsonify(equipment), 201

@app.route('/api/equipment/<int:equipment_id>', methods=['GET'])
def get_equipment_item(equipment_id):
    equipment = next((e for e in equipment_inventory if e['id'] == equipment_id), None)
    if not equipment:
        return jsonify({"error": "Equipment not found"}), 404
    return jsonify(equipment), 200

@app.route('/api/equipment/<int:equipment_id>', methods=['PUT'])
def update_equipment(equipment_id):
    equipment = next((e for e in equipment_inventory if e['id'] == equipment_id), None)
    if not equipment:
        return jsonify({"error": "Equipment not found"}), 404
    data = request.json
    equipment['name'] = data.get('name', equipment['name'])
    equipment['quantity'] = data.get('quantity', equipment['quantity'])
    return jsonify(equipment), 200

@app.route('/api/equipment/<int:equipment_id>', methods=['DELETE'])
def delete_equipment(equipment_id):
    global equipment_inventory
    equipment_inventory = [e for e in equipment_inventory if e['id'] != equipment_id]
    return jsonify({"message": "Equipment deleted"}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
