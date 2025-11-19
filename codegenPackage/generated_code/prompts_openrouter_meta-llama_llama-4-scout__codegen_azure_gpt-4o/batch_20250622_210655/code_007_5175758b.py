"""
Generated Code Metadata:
========================
Original URL: https://ratnarajfoods.in
Prompt: Design a RESTful API in Flask for managing orders and shipments of spice products, considering the extensive vendor network and seamless shipment assurance of Ratnaraj Foods.
Generated: DETERMINISTIC_5175758bc56cda1d
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

# In-memory database for demonstration purposes
orders = {}
shipments = {}

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "description": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_general_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "description": str(e)
    }), 500

# Route to create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    """
    Create a new order.
    Request JSON should include 'order_id', 'product_name', 'quantity', and 'vendor'.
    """
    data = request.get_json()
    if not data or 'order_id' not in data or 'product_name' not in data or 'quantity' not in data or 'vendor' not in data:
        return jsonify({"error": "Invalid request", "description": "Missing required fields"}), 400

    order_id = data['order_id']
    if order_id in orders:
        return jsonify({"error": "Conflict", "description": "Order ID already exists"}), 409

    orders[order_id] = {
        "product_name": data['product_name'],
        "quantity": data['quantity'],
        "vendor": data['vendor'],
        "status": "Pending"
    }
    return jsonify({"message": "Order created successfully", "order": orders[order_id]}), 201

# Route to retrieve an order by ID
@app.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    """
    Retrieve an order by its ID.
    """
    order = orders.get(order_id)
    if not order:
        return jsonify({"error": "Not Found", "description": "Order not found"}), 404
    return jsonify({"order": order}), 200

# Route to update the status of an order
@app.route('/orders/<order_id>', methods=['PUT'])
def update_order(order_id):
    """
    Update the status of an order.
    Request JSON should include 'status'.
    """
    data = request.get_json()
    if not data or 'status' not in data:
        return jsonify({"error": "Invalid request", "description": "Missing required fields"}), 400

    order = orders.get(order_id)
    if not order:
        return jsonify({"error": "Not Found", "description": "Order not found"}), 404

    order['status'] = data['status']
    return jsonify({"message": "Order updated successfully", "order": order}), 200

# Route to create a new shipment
@app.route('/shipments', methods=['POST'])
def create_shipment():
    """
    Create a new shipment.
    Request JSON should include 'shipment_id', 'order_id', and 'tracking_number'.
    """
    data = request.get_json()
    if not data or 'shipment_id' not in data or 'order_id' not in data or 'tracking_number' not in data:
        return jsonify({"error": "Invalid request", "description": "Missing required fields"}), 400

    shipment_id = data['shipment_id']
    if shipment_id in shipments:
        return jsonify({"error": "Conflict", "description": "Shipment ID already exists"}), 409

    order_id = data['order_id']
    if order_id not in orders:
        return jsonify({"error": "Not Found", "description": "Order not found"}), 404

    shipments[shipment_id] = {
        "order_id": order_id,
        "tracking_number": data['tracking_number'],
        "status": "In Transit"
    }
    return jsonify({"message": "Shipment created successfully", "shipment": shipments[shipment_id]}), 201

# Route to retrieve a shipment by ID
@app.route('/shipments/<shipment_id>', methods=['GET'])
def get_shipment(shipment_id):
    """
    Retrieve a shipment by its ID.
    """
    shipment = shipments.get(shipment_id)
    if not shipment:
        return jsonify({"error": "Not Found", "description": "Shipment not found"}), 404
    return jsonify({"shipment": shipment}), 200

# Route to update the status of a shipment
@app.route('/shipments/<shipment_id>', methods=['PUT'])
def update_shipment(shipment_id):
    """
    Update the status of a shipment.
    Request JSON should include 'status'.
    """
    data = request.get_json()
    if not data or 'status' not in data:
        return jsonify({"error": "Invalid request", "description": "Missing required fields"}), 400

    shipment = shipments.get(shipment_id)
    if not shipment:
        return jsonify({"error": "Not Found", "description": "Shipment not found"}), 404

    shipment['status'] = data['status']
    return jsonify({"message": "Shipment updated successfully", "shipment": shipment}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
