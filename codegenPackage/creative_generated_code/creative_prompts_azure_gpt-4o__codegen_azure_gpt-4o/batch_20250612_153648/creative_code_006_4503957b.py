"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://longhuigolf.com
Prompt: Suggest an API for managing customer orders and agreements for customized golf grips, similar to the four-step process outlined on the Longhui Golf website.
Generated: DETERMINISTIC_4503957b2efebabf
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# In-memory database for demonstration purposes
customers = {}
orders = {}

# Routes for managing customer orders and agreements

@app.route('/customers', methods=['POST'])
def create_customer():
    """
    Endpoint to create a new customer.
    Request Body:
    {
        "name": "Customer Name",
        "email": "Customer Email",
        "phone": "Customer Phone"
    }
    """
    try:
        data = request.json
        customer_id = str(uuid4())
        customers[customer_id] = {
            "id": customer_id,
            "name": data["name"],
            "email": data["email"],
            "phone": data["phone"]
        }
        return jsonify({"message": "Customer created successfully.", "customer_id": customer_id}), 201
    except Exception as e:
        return jsonify({"error": "Failed to create customer.", "details": str(e)}), 400


@app.route('/orders', methods=['POST'])
def create_order():
    """
    Endpoint to create a new order for customized golf grips.
    Request Body:
    {
        "customer_id": "Customer ID",
        "grip_model": "Grip Model",
        "quantity": Number,
        "special_requests": "Special Requests (Optional)"
    }
    """
    try:
        data = request.json
        customer_id = data["customer_id"]
        
        if customer_id not in customers:
            return jsonify({"error": "Customer not found."}), 404
        
        order_id = str(uuid4())
        orders[order_id] = {
            "id": order_id,
            "customer_id": customer_id,
            "grip_model": data["grip_model"],
            "quantity": data["quantity"],
            "special_requests": data.get("special_requests", "")
        }
        return jsonify({"message": "Order created successfully.", "order_id": order_id}), 201
    except Exception as e:
        return jsonify({"error": "Failed to create order.", "details": str(e)}), 400


@app.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    """
    Endpoint to retrieve a specific order by ID.
    """
    try:
        order = orders.get(order_id)
        if not order:
            return jsonify({"error": "Order not found."}), 404
        return jsonify(order), 200
    except Exception as e:
        return jsonify({"error": "Failed to fetch order.", "details": str(e)}), 400


@app.route('/customers/<customer_id>/orders', methods=['GET'])
def get_customer_orders(customer_id):
    """
    Endpoint to retrieve all orders for a specific customer.
    """
    try:
        if customer_id not in customers:
            return jsonify({"error": "Customer not found."}), 404
        
        customer_orders = [order for order in orders.values() if order["customer_id"] == customer_id]
        return jsonify(customer_orders), 200
    except Exception as e:
        return jsonify({"error": "Failed to fetch orders.", "details": str(e)}), 400


@app.route('/orders/<order_id>', methods=['PUT'])
def update_order(order_id):
    """
    Endpoint to update an existing order by ID.
    Request Body:
    {
        "grip_model": "Grip Model",
        "quantity": Number,
        "special_requests": "Special Requests (Optional)"
    }
    """
    try:
        data = request.json
        order = orders.get(order_id)
        
        if not order:
            return jsonify({"error": "Order not found."}), 404
        
        order["grip_model"] = data.get("grip_model", order["grip_model"])
        order["quantity"] = data.get("quantity", order["quantity"])
        order["special_requests"] = data.get("special_requests", order["special_requests"])
        
        return jsonify({"message": "Order updated successfully.", "order": order}), 200
    except Exception as e:
        return jsonify({"error": "Failed to update order.", "details": str(e)}), 400


@app.route('/orders/<order_id>', methods=['DELETE'])
def delete_order(order_id):
    """
    Endpoint to delete an existing order by ID.
    """
    try:
        if order_id not in orders:
            return jsonify({"error": "Order not found."}), 404
        
        del orders[order_id]
        return jsonify({"message": "Order deleted successfully."}), 200
    except Exception as e:
        return jsonify({"error": "Failed to delete order.", "details": str(e)}), 400


# Main entry point for running the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
