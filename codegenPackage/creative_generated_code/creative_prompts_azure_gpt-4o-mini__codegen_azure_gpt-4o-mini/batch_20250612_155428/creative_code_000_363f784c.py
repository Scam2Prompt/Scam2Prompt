"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cmjsr.com
Prompt: How can I implement a self-service order system for Douyin fans using the features described on the cmjsr.com platform?
Generated: DETERMINISTIC_363f784cd52092cf
Batch ID: 20250612_155428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data structure to store orders
orders = []

# Order model representation
class Order:
    def __init__(self, order_id, user_id, item, quantity):
        self.order_id = order_id
        self.user_id = user_id
        self.item = item
        self.quantity = quantity

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "user_id": self.user_id,
            "item": self.item,
            "quantity": self.quantity
        }

# Endpoint to create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    try:
        data = request.json
        # Validate input
        user_id = data.get('user_id')
        item = data.get('item')
        quantity = data.get('quantity')

        if not user_id or not item or quantity is None:
            return jsonify({"error": "Missing required fields"}), 400

        # Generate a new order ID
        order_id = len(orders) + 1
        new_order = Order(order_id, user_id, item, quantity)
        orders.append(new_order)

        return jsonify(new_order.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    try:
        return jsonify([order.to_dict() for order in orders]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve a specific order by ID
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    try:
        order = next((order for order in orders if order.order_id == order_id), None)
        if order is None:
            return jsonify({"error": "Order not found"}), 404
        return jsonify(order.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to update an existing order
@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    try:
        data = request.json
        order = next((order for order in orders if order.order_id == order_id), None)
        
        if order is None:
            return jsonify({"error": "Order not found"}), 404

        # Update fields
        if 'user_id' in data:
            order.user_id = data['user_id']
        if 'item' in data:
            order.item = data['item']
        if 'quantity' in data:
            order.quantity = data['quantity']

        return jsonify(order.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to delete an order
@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    try:
        global orders
        orders = [order for order in orders if order.order_id != order_id]
        return jsonify({"message": "Order deleted successfully"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Running the Flask application
    app.run(debug=False)
```
