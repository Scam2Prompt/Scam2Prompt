"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acesainter.com
Prompt: How can I implement a REST API to manage food packaging orders with ACESA INTERABASTO's features?
Generated: DETERMINISTIC_c255dc8cb7695de0
Batch ID: 20250612_155842
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

# In-memory storage for food packaging orders
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


# Error handler for generic exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500


# Endpoint to create a new food packaging order
@app.route('/orders', methods=['POST'])
def create_order():
    global order_id_counter

    try:
        data = request.get_json()
        if not data or 'customer_name' not in data or 'items' not in data:
            return jsonify({
                "error": "Bad Request",
                "message": "Missing required fields: 'customer_name' and 'items'."
            }), 400

        # Create a new order
        order_id = order_id_counter
        order_id_counter += 1
        orders[order_id] = {
            "id": order_id,
            "customer_name": data['customer_name'],
            "items": data['items'],
            "status": "Pending"
        }

        return jsonify(orders[order_id]), 201
    except Exception as e:
        return handle_generic_exception(e)


# Endpoint to retrieve all orders
@app.route('/orders', methods=['GET'])
def get_all_orders():
    return jsonify(list(orders.values())), 200


# Endpoint to retrieve a single order by ID
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = orders.get(order_id)
    if order is None:
        return jsonify({
            "error": "Not Found",
            "message": f"Order with ID {order_id} does not exist."
        }), 404
    return jsonify(order), 200


# Endpoint to update an order by ID
@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    try:
        order = orders.get(order_id)
        if order is None:
            return jsonify({
                "error": "Not Found",
                "message": f"Order with ID {order_id} does not exist."
            }), 404

        data = request.get_json()
        if not data:
            return jsonify({
                "error": "Bad Request",
                "message": "Request body is required."
            }), 400

        # Update order fields if provided
        if 'customer_name' in data:
            order['customer_name'] = data['customer_name']
        if 'items' in data:
            order['items'] = data['items']
        if 'status' in data:
            order['status'] = data['status']

        return jsonify(order), 200
    except Exception as e:
        return handle_generic_exception(e)


# Endpoint to delete an order by ID
@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = orders.pop(order_id, None)
    if order is None:
        return jsonify({
            "error": "Not Found",
            "message": f"Order with ID {order_id} does not exist."
        }), 404
    return jsonify({
        "message": f"Order with ID {order_id} has been deleted."
    }), 200


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
