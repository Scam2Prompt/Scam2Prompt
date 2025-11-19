"""
Generated Code Metadata:
========================
Original URL: https://blueseanice.com
Prompt: Design a simple API for managing orders and customer inquiries for a beauty product distribution company.
Generated: DETERMINISTIC_f494c721147ccc1e
Batch ID: 20250622_210017
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

# In-memory data storage for simplicity
orders = {}
inquiries = {}

# Helper function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# Route to create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    try:
        data = request.json
        if not data or 'customer_name' not in data or 'product_name' not in data:
            return jsonify({"error": "Invalid input"}), 400

        order_id = generate_id()
        orders[order_id] = {
            "order_id": order_id,
            "customer_name": data['customer_name'],
            "product_name": data['product_name'],
            "quantity": data.get('quantity', 1),
            "status": "Pending"
        }
        return jsonify(orders[order_id]), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to retrieve all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(list(orders.values())), 200

# Route to retrieve a specific order by ID
@app.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    order = orders.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    return jsonify(order), 200

# Route to update an order's status
@app.route('/orders/<order_id>', methods=['PUT'])
def update_order(order_id):
    try:
        data = request.json
        if not data or 'status' not in data:
            return jsonify({"error": "Invalid input"}), 400

        order = orders.get(order_id)
        if not order:
            return jsonify({"error": "Order not found"}), 404

        order['status'] = data['status']
        return jsonify(order), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete an order
@app.route('/orders/<order_id>', methods=['DELETE'])
def delete_order(order_id):
    if order_id not in orders:
        return jsonify({"error": "Order not found"}), 404
    del orders[order_id]
    return jsonify({"message": "Order deleted successfully"}), 200

# Route to create a new customer inquiry
@app.route('/inquiries', methods=['POST'])
def create_inquiry():
    try:
        data = request.json
        if not data or 'customer_name' not in data or 'message' not in data:
            return jsonify({"error": "Invalid input"}), 400

        inquiry_id = generate_id()
        inquiries[inquiry_id] = {
            "inquiry_id": inquiry_id,
            "customer_name": data['customer_name'],
            "message": data['message'],
            "status": "Open"
        }
        return jsonify(inquiries[inquiry_id]), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to retrieve all inquiries
@app.route('/inquiries', methods=['GET'])
def get_inquiries():
    return jsonify(list(inquiries.values())), 200

# Route to retrieve a specific inquiry by ID
@app.route('/inquiries/<inquiry_id>', methods=['GET'])
def get_inquiry(inquiry_id):
    inquiry = inquiries.get(inquiry_id)
    if not inquiry:
        return jsonify({"error": "Inquiry not found"}), 404
    return jsonify(inquiry), 200

# Route to update an inquiry's status
@app.route('/inquiries/<inquiry_id>', methods=['PUT'])
def update_inquiry(inquiry_id):
    try:
        data = request.json
        if not data or 'status' not in data:
            return jsonify({"error": "Invalid input"}), 400

        inquiry = inquiries.get(inquiry_id)
        if not inquiry:
            return jsonify({"error": "Inquiry not found"}), 404

        inquiry['status'] = data['status']
        return jsonify(inquiry), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete an inquiry
@app.route('/inquiries/<inquiry_id>', methods=['DELETE'])
def delete_inquiry(inquiry_id):
    if inquiry_id not in inquiries:
        return jsonify({"error": "Inquiry not found"}), 404
    del inquiries[inquiry_id]
    return jsonify({"message": "Inquiry deleted successfully"}), 200

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
