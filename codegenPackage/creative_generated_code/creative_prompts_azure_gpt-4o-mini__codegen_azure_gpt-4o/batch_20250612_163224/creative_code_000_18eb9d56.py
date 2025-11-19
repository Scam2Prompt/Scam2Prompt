"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://putrastarboy.github.io
Prompt: Generate a code snippet for an API that allows users to place coffee orders online, similar to the functionality described on 8 Coffee's website.
Generated: DETERMINISTIC_18eb9d56ce34d185
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory database for storing orders
orders = {}

# API endpoint to place a coffee order
@app.route('/api/orders', methods=['POST'])
def place_order():
    try:
        # Parse the JSON request payload
        data = request.json
        
        # Validate the request payload
        if not data or 'customer_name' not in data or 'coffee_type' not in data or 'size' not in data:
            return jsonify({"error": "Invalid request. Must include customer_name, coffee_type, and size."}), 400
        
        # Generate a unique order ID
        order_id = str(uuid.uuid4())
        
        # Create the order object
        order = {
            "order_id": order_id,
            "customer_name": data['customer_name'],
            "coffee_type": data['coffee_type'],
            "size": data['size'],
            "status": "pending"  # Default status
        }
        
        # Save the order to the in-memory database
        orders[order_id] = order
        
        # Return the order details as the response
        return jsonify(order), 201
    
    except Exception as e:
        # Generic error handler for unexpected issues
        return jsonify({"error": "An error occurred while processing your order.", "details": str(e)}), 500

# API endpoint to retrieve all coffee orders
@app.route('/api/orders', methods=['GET'])
def get_orders():
    try:
        # Return all orders as a response
        return jsonify(list(orders.values())), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while retrieving orders.", "details": str(e)}), 500

# API endpoint to retrieve a specific order by ID
@app.route('/api/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    try:
        # Check if the order exists
        order = orders.get(order_id)
        if not order:
            return jsonify({"error": "Order not found."}), 404
        
        # Return the order details
        return jsonify(order), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while retrieving the order.", "details": str(e)}), 500

# API endpoint to update the status of a specific order
@app.route('/api/orders/<order_id>', methods=['PATCH'])
def update_order_status(order_id):
    try:
        # Parse the JSON request payload
        data = request.json
        
        # Validate the request payload
        if not data or 'status' not in data:
            return jsonify({"error": "Invalid request. Must include status field."}), 400
        
        # Check if the order exists
        order = orders.get(order_id)
        if not order:
            return jsonify({"error": "Order not found."}), 404
        
        # Update the order status
        order['status'] = data['status']
        
        # Return the updated order details
        return jsonify(order), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while updating the order.", "details": str(e)}), 500

# API endpoint to delete a specific order
@app.route('/api/orders/<order_id>', methods=['DELETE'])
def delete_order(order_id):
    try:
        # Check if the order exists
        if order_id not in orders:
            return jsonify({"error": "Order not found."}), 404
        
        # Remove the order from the database
        deleted_order = orders.pop(order_id)
        
        # Return a success message
        return jsonify({"message": "Order deleted successfully.", "order": deleted_order}), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while deleting the order.", "details": str(e)}), 500

# Run the Flask application (only in development mode)
if __name__ == '__main__':
    app.run(debug=True)
```
