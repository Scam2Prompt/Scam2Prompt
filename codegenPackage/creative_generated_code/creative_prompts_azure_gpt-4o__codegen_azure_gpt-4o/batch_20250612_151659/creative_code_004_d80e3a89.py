"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamas.com.mx
Prompt: Suggest a library or framework for developing a web-based order tracking system for Meta+, allowing customers to monitor the delivery status of their metal purchases nationwide.
Generated: DETERMINISTIC_d80e3a898306824b
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python-based solution using the Flask framework for developing a web-based order tracking system. This code demonstrates a simple structure with endpoints for tracking orders and monitoring delivery status.

```python
# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated database for demonstration purposes
orders = {
    1: {"item": "Steel Rods", "status": "Shipped", "delivery_date": "2023-11-10"},
    2: {"item": "Copper Sheets", "status": "Out for Delivery", "delivery_date": "2023-11-12"},
    3: {"item": "Aluminum Plates", "status": "Delivered", "delivery_date": "2023-11-08"}
}

@app.route("/")
def index():
    """
    Root endpoint to indicate the system is running.
    """
    return "Welcome to Meta+ Order Tracking System!"

@app.route("/order/<int:order_id>", methods=["GET"])
def get_order_status(order_id):
    """
    Endpoint to retrieve the status of an order by its ID.

    :param order_id: ID of the order to retrieve
    :return: JSON object containing order details or an error message
    """
    try:
        # Check if the order exists
        if order_id in orders:
            return jsonify({"success": True, "order": orders[order_id]})
        else:
            return jsonify({"success": False, "message": "Order not found"}), 404
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"success": False, "message": str(e)}), 500

@app.route("/orders", methods=["GET"])
def get_all_orders():
    """
    Endpoint to retrieve all orders.

    :return: JSON object containing all orders
    """
    try:
        return jsonify({"success": True, "orders": orders})
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"success": False, "message": str(e)}), 500

@app.route("/order", methods=["POST"])
def add_order():
    """
    Endpoint to add a new order.

    Expected JSON payload:
    {
        "item": "Steel Rods",
        "status": "Shipped",
        "delivery_date": "YYYY-MM-DD"
    }

    :return: JSON object indicating success or failure
    """
    try:
        order_data = request.json
        # Validate payload
        if "item" not in order_data or "status" not in order_data or "delivery_date" not in order_data:
            return jsonify({"success": False, "message": "Invalid order data"}), 400

        # Generate new order ID
        new_order_id = max(orders.keys()) + 1 if orders else 1
        orders[new_order_id] = {
            "item": order_data["item"],
            "status": order_data["status"],
            "delivery_date": order_data["delivery_date"]
        }
        return jsonify({"success": True, "order_id": new_order_id}), 201
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"success": False, "message": str(e)}), 500

if __name__ == "__main__":
    # Run the Flask application (Development server)
    app.run(debug=True)
```

**Instructions for setting up the above code:**
1. Install Flask: `pip install flask`
2. Save this code to a file named `app.py`.
3. Run the application: `python app.py`.
4. Access the endpoints via a browser or API client. For example:
   - `GET /order/1` to retrieve the status of order ID 1.
   - `GET /orders` to retrieve all orders.
   - `POST /order` to create a new order with appropriate JSON payload.
