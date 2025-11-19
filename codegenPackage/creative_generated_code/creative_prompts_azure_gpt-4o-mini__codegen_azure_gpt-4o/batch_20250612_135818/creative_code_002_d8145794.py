"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://csh-gamesapp.weebly.com
Prompt: Suggest an API for managing customer orders and returns, similar to the functionalities mentioned on the Piuka website.
Generated: DETERMINISTIC_d81457946363c9e3
Batch ID: 20250612_135818
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for orders and returns (mock database)
orders = {}
returns = {}

@app.route('/orders', methods=['POST'])
def create_order():
    """
    Create a new customer order.
    Request Body:
    {
        "order_id": "123",
        "customer_name": "John Doe",
        "items": [
            {"item_id": "001", "name": "Product A", "quantity": 2}
        ],
        "total_price": 50.0
    }
    """
    try:
        data = request.get_json()
        order_id = data.get("order_id")
        
        if not order_id or order_id in orders:
            return jsonify({"error": "Invalid or duplicate order ID"}), 400
        
        orders[order_id] = data
        return jsonify({"message": "Order created successfully", "order": data}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/orders/<string:order_id>', methods=['GET'])
def get_order(order_id):
    """
    Retrieve an order by its ID.
    """
    order = orders.get(order_id)
    
    if not order:
        return jsonify({"error": "Order not found"}), 404

    return jsonify(order), 200

@app.route('/orders/<string:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """
    Delete an order by its ID.
    """
    if order_id not in orders:
        return jsonify({"error": "Order not found"}), 404

    deleted_order = orders.pop(order_id)
    return jsonify({"message": "Order deleted successfully", "order": deleted_order}), 200

@app.route('/returns', methods=['POST'])
def create_return():
    """
    Create a new return request for an order.
    Request Body:
    {
        "return_id": "456",
        "order_id": "123",
        "reason": "Damaged item",
        "items": [
            {"item_id": "001", "name": "Product A", "quantity": 1}
        ]
    }
    """
    try:
        data = request.get_json()
        return_id = data.get("return_id")
        order_id = data.get("order_id")
        
        if not return_id or return_id in returns:
            return jsonify({"error": "Invalid or duplicate return ID"}), 400

        if order_id not in orders:
            return jsonify({"error": "Order ID not found"}), 404
        
        returns[return_id] = data
        return jsonify({"message": "Return created successfully", "return": data}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/returns/<string:return_id>', methods=['GET'])
def get_return(return_id):
    """
    Retrieve a return request by its ID.
    """
    return_request = returns.get(return_id)
    
    if not return_request:
        return jsonify({"error": "Return request not found"}), 404

    return jsonify(return_request), 200

@app.route('/returns/<string:return_id>', methods=['DELETE'])
def delete_return(return_id):
    """
    Delete a return request by its ID.
    """
    if return_id not in returns:
        return jsonify({"error": "Return request not found"}), 404

    deleted_return = returns.pop(return_id)
    return jsonify({"message": "Return deleted successfully", "return": deleted_return}), 200

# Error handler for invalid routes
@app.errorhandler(404)
def route_not_found(e):
    return jsonify({"error": "Route not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
```
