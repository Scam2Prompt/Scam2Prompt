"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://surffojotas.com
Prompt: Create a REST API using Flask to allow customers to submit orders for personalized flip-flops with custom logos and designs for events or hotels.
Generated: DETERMINISTIC_750e7c8443819546
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for storing orders (for simplicity)
orders = []
order_id_counter = 1

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "description": e.description,
        "status_code": e.code
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "description": str(e),
        "status_code": 500
    }), 500

# Endpoint to submit a new order
@app.route('/orders', methods=['POST'])
def submit_order():
    global orders, order_id_counter

    # Validate incoming request data
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    required_fields = ['customer_name', 'email', 'event_type', 'design_details', 'quantity']
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return jsonify({"error": "Missing required fields", "fields": missing_fields}), 400

    # Create and store the order
    order = {
        "order_id": order_id_counter,
        "customer_name": data['customer_name'],
        "email": data['email'],
        "event_type": data['event_type'],
        "design_details": data['design_details'],
        "quantity": data['quantity']
    }
    orders.append(order)
    order_id_counter += 1

    return jsonify({"message": "Order submitted successfully", "order": order}), 201

# Endpoint to view all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify({"orders": orders}), 200

# Endpoint to view a specific order by ID
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = next((order for order in orders if order['order_id'] == order_id), None)
    if order is None:
        return jsonify({"error": "Order not found"}), 404

    return jsonify({"order": order}), 200

# Endpoint to delete an order by ID
@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    global orders

    order = next((order for order in orders if order['order_id'] == order_id), None)
    if order is None:
        return jsonify({"error": "Order not found"}), 404

    orders = [o for o in orders if o['order_id'] != order_id]
    return jsonify({"message": "Order deleted successfully"}), 200

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
