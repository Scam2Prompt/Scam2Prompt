"""
Generated Code Metadata:
========================
Original URL: https://csh-gamesapp.weebly.com
Prompt: Suggest an API for managing customer orders and returns, similar to the functionalities mentioned on the Piuka website.
Generated: DETERMINISTIC_d81457946363c9e3
Batch ID: 20250612_135818
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database for demonstration purposes
orders = {}
returns = {}

# Helper function to generate unique IDs
def generate_id(data_store):
    return str(len(data_store) + 1)

# API endpoint to create a new order
@app.route('/api/orders', methods=['POST'])
def create_order():
    try:
        data = request.json
        if not data or 'customer_name' not in data or 'items' not in data:
            return jsonify({"error": "Invalid request. 'customer_name' and 'items' are required."}), 400
        
        order_id = generate_id(orders)
        orders[order_id] = {
            "order_id": order_id,
            "customer_name": data['customer_name'],
            "items": data['items'],
            "status": "placed"
        }
        return jsonify({"message": "Order created successfully.", "order": orders[order_id]}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve all orders
@app.route('/api/orders', methods=['GET'])
def get_orders():
    try:
        return jsonify({"orders": list(orders.values())}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve a specific order by ID
@app.route('/api/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    try:
        order = orders.get(order_id)
        if not order:
            return jsonify({"error": "Order not found."}), 404
        return jsonify({"order": order}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to update an order's status
@app.route('/api/orders/<order_id>', methods=['PUT'])
def update_order(order_id):
    try:
        data = request.json
        if not data or 'status' not in data:
            return jsonify({"error": "Invalid request. 'status' is required."}), 400
        
        order = orders.get(order_id)
        if not order:
            return jsonify({"error": "Order not found."}), 404
        
        order['status'] = data['status']
        return jsonify({"message": "Order updated successfully.", "order": order}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to create a return request
@app.route('/api/returns', methods=['POST'])
def create_return():
    try:
        data = request.json
        if not data or 'order_id' not in data or 'reason' not in data:
            return jsonify({"error": "Invalid request. 'order_id' and 'reason' are required."}), 400
        
        order = orders.get(data['order_id'])
        if not order:
            return jsonify({"error": "Order not found."}), 404
        
        return_id = generate_id(returns)
        returns[return_id] = {
            "return_id": return_id,
            "order_id": data['order_id'],
            "reason": data['reason'],
            "status": "pending"
        }
        return jsonify({"message": "Return request created successfully.", "return": returns[return_id]}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve all return requests
@app.route('/api/returns', methods=['GET'])
def get_returns():
    try:
        return jsonify({"returns": list(returns.values())}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to update a return request's status
@app.route('/api/returns/<return_id>', methods=['PUT'])
def update_return(return_id):
    try:
        data = request.json
        if not data or 'status' not in data:
            return jsonify({"error": "Invalid request. 'status' is required."}), 400
        
        return_request = returns.get(return_id)
        if not return_request:
            return jsonify({"error": "Return request not found."}), 404
        
        return_request['status'] = data['status']
        return jsonify({"message": "Return request updated successfully.", "return": return_request}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
