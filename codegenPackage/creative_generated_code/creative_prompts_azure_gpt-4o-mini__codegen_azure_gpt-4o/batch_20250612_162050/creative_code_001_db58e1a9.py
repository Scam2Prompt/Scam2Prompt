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
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# In-memory database for orders (for simplicity, using a list)
orders = []
order_id = 0  # To track unique order IDs

# Route to create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    """
    Create a new order for snow cones.
    Request JSON should include 'customer_name', 'flavor', and 'quantity'.
    """
    global order_id
    try:
        # Parse the incoming JSON request
        data = request.get_json()
        customer_name = data.get('customer_name')
        flavor = data.get('flavor')
        quantity = data.get('quantity')

        # Validate input data
        if not customer_name or not flavor or not isinstance(quantity, int) or quantity <= 0:
            return jsonify({"error": "Invalid input. Please provide 'customer_name', 'flavor', and a positive integer 'quantity'."}), 400

        # Create new order with a unique ID
        order_id += 1
        order = {
            "id": order_id,
            "customer_name": customer_name,
            "flavor": flavor,
            "quantity": quantity
        }
        orders.append(order)
        return jsonify({"message": "Order created successfully!", "order": order}), 201
    except Exception as e:
        return jsonify({"error": "An error occurred while creating the order.", "details": str(e)}), 500

# Route to list all orders
@app.route('/orders', methods=['GET'])
def list_orders():
    """
    Get a list of all orders.
    """
    return jsonify({"orders": orders}), 200

# Route to retrieve a specific order by ID
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """
    Retrieve a specific order by its ID.
    """
    try:
        # Find the order by ID
        order = next((order for order in orders if order['id'] == order_id), None)
        if not order:
            return jsonify({"error": "Order not found."}), 404
        return jsonify({"order": order}), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while retrieving the order.", "details": str(e)}), 500

# Route to update an existing order
@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    """
    Update an existing order by its ID.
    Request JSON can include 'customer_name', 'flavor', and/or 'quantity'.
    """
    try:
        # Find the order by ID
        order = next((order for order in orders if order['id'] == order_id), None)
        if not order:
            return jsonify({"error": "Order not found."}), 404

        # Parse the incoming JSON request
        data = request.get_json()
        customer_name = data.get('customer_name')
        flavor = data.get('flavor')
        quantity = data.get('quantity')

        # Update order details if provided
        if customer_name:
            order['customer_name'] = customer_name
        if flavor:
            order['flavor'] = flavor
        if isinstance(quantity, int) and quantity > 0:
            order['quantity'] = quantity

        return jsonify({"message": "Order updated successfully!", "order": order}), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while updating the order.", "details": str(e)}), 500

# Route to delete an order by ID
@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """
    Delete an order by its ID.
    """
    try:
        # Find the order by ID
        global orders
        order = next((order for order in orders if order['id'] == order_id), None)
        if not order:
            return jsonify({"error": "Order not found."}), 404

        # Remove the order from the list
        orders = [order for order in orders if order['id'] != order_id]
        return jsonify({"message": "Order deleted successfully!"}), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while deleting the order.", "details": str(e)}), 500

# Start the Flask application if this file is executed
if __name__ == '__main__':
    app.run(debug=True)
```
