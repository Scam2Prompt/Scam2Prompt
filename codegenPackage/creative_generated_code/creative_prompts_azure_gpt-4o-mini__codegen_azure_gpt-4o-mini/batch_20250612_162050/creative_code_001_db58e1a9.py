"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kingoficecream.com
Prompt: How can I create a simple API to manage orders for a King of Ice Cream snow cone truck?
Generated: DETERMINISTIC_db58e1a9a0a35b0a
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Sample data to represent orders
orders = []


@app.route('/orders', methods=['GET'])
def get_orders():
    """
    Retrieve the list of all orders.
    Returns:
        JSON response containing the list of orders.
    """
    return jsonify(orders)


@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """
    Retrieve a specific order by its ID.
    Args:
        order_id (int): The ID of the order to retrieve.
    Returns:
        JSON response containing the order details.
        404 error if order not found.
    """
    order = next((order for order in orders if order['id'] == order_id), None)
    if order is None:
        abort(404)
    return jsonify(order)


@app.route('/orders', methods=['POST'])
def create_order():
    """
    Create a new order.
    Request must contain JSON data with the order details.
    Returns:
        JSON response containing the created order with a 201 status code.
    """
    if not request.json or 'flavor' not in request.json or 'size' not in request.json:
        abort(400)  # Bad Request
    
    new_order = {
        'id': len(orders) + 1,  # Simple ID generation
        'flavor': request.json['flavor'],
        'size': request.json['size'],
    }
    orders.append(new_order)
    return jsonify(new_order), 201


@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    """
    Update an existing order by its ID.
    Args:
        order_id (int): The ID of the order to update.
    Returns:
        JSON response containing the updated order.
        404 error if order not found.
    """
    order = next((order for order in orders if order['id'] == order_id), None)
    if order is None:
        abort(404)

    if not request.json:
        abort(400)  # Bad Request
    
    # Update order details
    order['flavor'] = request.json.get('flavor', order['flavor'])
    order['size'] = request.json.get('size', order['size'])
    return jsonify(order)


@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """
    Delete an existing order by its ID.
    Args:
        order_id (int): The ID of the order to delete.
    Returns:
        204 No Content status if order is deleted.
        404 error if order not found.
    """
    order = next((order for order in orders if order['id'] == order_id), None)
    if order is None:
        abort(404)
        
    orders.remove(order)
    return '', 204  # No Content


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
