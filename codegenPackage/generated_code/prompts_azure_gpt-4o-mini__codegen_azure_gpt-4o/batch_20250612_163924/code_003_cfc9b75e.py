"""
Generated Code Metadata:
========================
Original URL: https://biogreenasia.com
Prompt: Create a REST API endpoint for managing orders on an e-commerce site similar to Bio Green Asia, focusing on natural products like floor cleaners and hand washes.
Generated: DETERMINISTIC_cfc9b75e5d44e1bb
Batch ID: 20250612_163924
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
order_id_counter = 1

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Endpoint to create a new order
@app.route('/api/orders', methods=['POST'])
def create_order():
    """
    Create a new order.
    Expected JSON payload:
    {
        "product_name": "string",
        "quantity": int,
        "price": float
    }
    """
    global order_id_counter

    # Validate request payload
    data = request.get_json()
    if not data or 'product_name' not in data or 'quantity' not in data or 'price' not in data:
        return jsonify({"error": "Bad Request", "message": "Invalid payload"}), 400

    # Create a new order
    order_id = order_id_counter
    orders[order_id] = {
        "order_id": order_id,
        "product_name": data['product_name'],
        "quantity": data['quantity'],
        "price": data['price']
    }
    order_id_counter += 1

    return jsonify({"message": "Order created successfully", "order": orders[order_id]}), 201

# Endpoint to retrieve all orders
@app.route('/api/orders', methods=['GET'])
def get_orders():
    """
    Retrieve all orders.
    """
    return jsonify({"orders": list(orders.values())}), 200

# Endpoint to retrieve a specific order by ID
@app.route('/api/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """
    Retrieve a specific order by ID.
    """
    order = orders.get(order_id)
    if not order:
        return jsonify({"error": "Not Found", "message": "Order not found"}), 404

    return jsonify({"order": order}), 200

# Endpoint to update an existing order
@app.route('/api/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    """
    Update an existing order.
    Expected JSON payload:
    {
        "product_name": "string",
        "quantity": int,
        "price": float
    }
    """
    order = orders.get(order_id)
    if not order:
        return jsonify({"error": "Not Found", "message": "Order not found"}), 404

    # Validate request payload
    data = request.get_json()
    if not data or 'product_name' not in data or 'quantity' not in data or 'price' not in data:
        return jsonify({"error": "Bad Request", "message": "Invalid payload"}), 400

    # Update the order
    order.update({
        "product_name": data['product_name'],
        "quantity": data['quantity'],
        "price": data['price']
    })

    return jsonify({"message": "Order updated successfully", "order": order}), 200

# Endpoint to delete an order
@app.route('/api/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """
    Delete an order by ID.
    """
    order = orders.pop(order_id, None)
    if not order:
        return jsonify({"error": "Not Found", "message": "Order not found"}), 404

    return jsonify({"message": "Order deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
