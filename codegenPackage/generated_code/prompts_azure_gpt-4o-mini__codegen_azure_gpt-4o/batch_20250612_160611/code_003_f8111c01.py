"""
Generated Code Metadata:
========================
Original URL: https://conficarnesdelvalle.com
Prompt: Create an API endpoint to handle customer orders for a meat business, inspired by Conficarnes del Valle's services.
Generated: DETERMINISTIC_f8111c0185c324bd
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory database to store orders (for demonstration purposes)
orders_db = {}

# API endpoint to handle customer orders
@app.route('/api/orders', methods=['POST'])
def create_order():
    """
    Endpoint to create a new customer order.
    Expects JSON payload with 'customer_name', 'items', and 'total_price'.
    """
    try:
        # Parse the incoming JSON request
        data = request.get_json()

        # Validate required fields
        if not data or 'customer_name' not in data or 'items' not in data or 'total_price' not in data:
            return jsonify({"error": "Invalid request. Missing required fields."}), 400

        # Generate a unique order ID
        order_id = str(uuid.uuid4())

        # Create the order object
        order = {
            "order_id": order_id,
            "customer_name": data['customer_name'],
            "items": data['items'],  # List of items (e.g., [{"name": "Chicken", "quantity": 2}])
            "total_price": data['total_price'],  # Total price of the order
            "status": "Pending"  # Default status
        }

        # Save the order to the in-memory database
        orders_db[order_id] = order

        # Return the created order as a response
        return jsonify({"message": "Order created successfully.", "order": order}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while processing the order.", "details": str(e)}), 500


@app.route('/api/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    """
    Endpoint to retrieve an order by its ID.
    """
    try:
        # Check if the order exists
        order = orders_db.get(order_id)
        if not order:
            return jsonify({"error": "Order not found."}), 404

        # Return the order details
        return jsonify({"order": order}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while retrieving the order.", "details": str(e)}), 500


@app.route('/api/orders/<order_id>', methods=['PUT'])
def update_order(order_id):
    """
    Endpoint to update an existing order's status.
    Expects JSON payload with 'status'.
    """
    try:
        # Parse the incoming JSON request
        data = request.get_json()

        # Validate required fields
        if not data or 'status' not in data:
            return jsonify({"error": "Invalid request. Missing required fields."}), 400

        # Check if the order exists
        order = orders_db.get(order_id)
        if not order:
            return jsonify({"error": "Order not found."}), 404

        # Update the order status
        order['status'] = data['status']

        # Save the updated order back to the database
        orders_db[order_id] = order

        # Return the updated order as a response
        return jsonify({"message": "Order updated successfully.", "order": order}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while updating the order.", "details": str(e)}), 500


@app.route('/api/orders/<order_id>', methods=['DELETE'])
def delete_order(order_id):
    """
    Endpoint to delete an order by its ID.
    """
    try:
        # Check if the order exists
        order = orders_db.get(order_id)
        if not order:
            return jsonify({"error": "Order not found."}), 404

        # Delete the order from the database
        del orders_db[order_id]

        # Return a success message
        return jsonify({"message": "Order deleted successfully."}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while deleting the order.", "details": str(e)}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
