"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harinderfarms.com
Prompt: Generate a code snippet for a web application that allows farmers to order corn silage bales from Harinder Farms, ensuring it includes features for delivery scheduling and product quality assurance.
Generated: DETERMINISTIC_b88985bfa50b5be3
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from datetime import datetime
from werkzeug.exceptions import BadRequest

# Initialize Flask application
app = Flask(__name__)

# In-memory database (For demonstration purposes. Replace with a real database for production.)
orders_db = []

# Helper function to validate delivery date
def validate_delivery_date(date_str):
    try:
        delivery_date = datetime.strptime(date_str, "%Y-%m-%d")
        if delivery_date < datetime.now():
            raise ValueError("Delivery date cannot be in the past.")
        return delivery_date
    except ValueError as e:
        raise BadRequest(f"Invalid delivery date: {str(e)}")

# Route to place an order
@app.route('/order', methods=['POST'])
def place_order():
    """
    Endpoint to place an order for corn silage bales.
    Accepts a JSON payload with the following keys:
    - farmer_name: Name of the farmer placing the order (string)
    - quantity: Number of bales needed (integer)
    - delivery_date: Desired delivery date in YYYY-MM-DD format (string)
    - quality_assurance_notes: Notes regarding product quality assurance (string)
    """
    data = request.json

    # Validate and extract input
    try:
        farmer_name = data['farmer_name']
        quantity = int(data['quantity'])
        delivery_date = validate_delivery_date(data['delivery_date'])
        quality_assurance_notes = data.get('quality_assurance_notes', '')

        if quantity <= 0:
            raise BadRequest("Quantity must be greater than zero.")
    except (KeyError, ValueError) as e:
        return jsonify({"error": f"Invalid input: {str(e)}"}), 400

    # Create order record
    order = {
        "order_id": len(orders_db) + 1,
        "farmer_name": farmer_name,
        "quantity": quantity,
        "delivery_date": delivery_date.strftime("%Y-%m-%d"),
        "quality_assurance_notes": quality_assurance_notes,
        "status": "Pending"
    }
    orders_db.append(order)

    return jsonify({"message": "Order placed successfully!", "order": order}), 201

# Route to fetch all orders
@app.route('/orders', methods=['GET'])
def fetch_orders():
    """
    Endpoint to fetch all orders.
    Returns a list of all orders placed with Harinder Farms.
    """
    return jsonify({"orders": orders_db}), 200

# Route to update order status
@app.route('/order/<int:order_id>/status', methods=['PUT'])
def update_order_status(order_id):
    """
    Endpoint to update the status of an order.
    Accepts a JSON payload with the following keys:
    - status: New status of the order (string)
    """
    data = request.json

    try:
        new_status = data['status']
        if new_status not in ["Pending", "Processed", "Shipped", "Delivered"]:
            raise BadRequest("Invalid status value.")
    except KeyError:
        return jsonify({"error": "Missing 'status' in request data."}), 400

    # Find the order by ID
    order = next((order for order in orders_db if order["order_id"] == order_id), None)
    if not order:
        return jsonify({"error": "Order not found."}), 404

    # Update order status
    order["status"] = new_status
    return jsonify({"message": "Order status updated successfully!", "order": order}), 200

# Error handler for 404 (Not Found)
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found."}), 404

# Error handler for 400 (Bad Request)
@app.errorhandler(BadRequest)
def bad_request_error(error):
    return jsonify({"error": str(error)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
