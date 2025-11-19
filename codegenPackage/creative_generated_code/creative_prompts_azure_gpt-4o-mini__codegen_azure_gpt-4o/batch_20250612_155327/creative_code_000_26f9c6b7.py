"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.vircomem.ro
Prompt: Generate a code snippet for an API that manages the production and distribution of industrial brushes, focusing on custom orders as described on the VIRCOMEM website.
Generated: DETERMINISTIC_26f9c6b77790fbad
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# In-memory storage for orders
orders = {}

# Error handling constants
ERROR_ORDER_NOT_FOUND = {"error": "Order not found"}
ERROR_INVALID_DATA = {"error": "Invalid input data"}

@app.route('/api/orders', methods=['POST'])
def create_order():
    """
    Endpoint to create a custom order for industrial brushes.
    Expects JSON data with 'customer_name', 'brush_type', 'dimensions', and 'quantity'.
    """
    try:
        # Parse and validate input data
        data = request.json
        customer_name = data.get('customer_name')
        brush_type = data.get('brush_type')
        dimensions = data.get('dimensions')
        quantity = data.get('quantity')

        if not (customer_name and brush_type and dimensions and isinstance(quantity, int) and quantity > 0):
            return jsonify(ERROR_INVALID_DATA), 400

        # Generate a unique order ID
        order_id = str(uuid4())

        # Create and store the order
        orders[order_id] = {
            "order_id": order_id,
            "customer_name": customer_name,
            "brush_type": brush_type,
            "dimensions": dimensions,
            "quantity": quantity,
            "status": "Pending"
        }

        return jsonify(orders[order_id]), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    """
    Endpoint to retrieve the details of a specific order based on its ID.
    """
    order = orders.get(order_id)
    if not order:
        return jsonify(ERROR_ORDER_NOT_FOUND), 404
    return jsonify(order), 200

@app.route('/api/orders/<order_id>', methods=['PUT'])
def update_order(order_id):
    """
    Endpoint to update the details of a specific order based on its ID.
    Expects JSON data with fields to update: 'brush_type', 'dimensions', 'quantity', or 'status'.
    """
    try:
        # Check if the order exists
        order = orders.get(order_id)
        if not order:
            return jsonify(ERROR_ORDER_NOT_FOUND), 404

        # Parse update data
        data = request.json
        brush_type = data.get('brush_type')
        dimensions = data.get('dimensions')
        quantity = data.get('quantity')
        status = data.get('status')

        # Validate and update order fields
        if brush_type:
            order['brush_type'] = brush_type
        if dimensions:
            order['dimensions'] = dimensions
        if quantity and isinstance(quantity, int) and quantity > 0:
            order['quantity'] = quantity
        if status:
            order['status'] = status

        return jsonify(order), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/orders/<order_id>', methods=['DELETE'])
def delete_order(order_id):
    """
    Endpoint to delete a specific order based on its ID.
    """
    if order_id in orders:
        del orders[order_id]
        return jsonify({"message": f"Order {order_id} deleted successfully."}), 200
    return jsonify(ERROR_ORDER_NOT_FOUND), 404

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
