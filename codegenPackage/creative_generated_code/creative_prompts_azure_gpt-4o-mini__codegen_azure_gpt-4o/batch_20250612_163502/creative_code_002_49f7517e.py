"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teamelevenx1.xyz
Prompt: Create an API endpoint that allows users to track their orders in real-time, reflecting the order tracking feature highlighted on ayuwin.
Generated: DETERMINISTIC_49f7517e0d71e6b5
Batch ID: 20250612_163502
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
from datetime import datetime

app = Flask(__name__)

# Simulated database for orders
orders_db = {
    "12345": {
        "order_id": "12345",
        "status": "In Transit",
        "estimated_delivery": "2023-10-15",
        "last_updated": "2023-10-12T14:30:00"
    },
    "67890": {
        "order_id": "67890",
        "status": "Delivered",
        "estimated_delivery": "2023-10-10",
        "last_updated": "2023-10-10T10:00:00"
    }
}

# Error structure for consistent API responses
def error_response(message, status_code):
    return jsonify({"error": message}), status_code

@app.route('/track-order/<order_id>', methods=['GET'])
def track_order(order_id):
    """
    API endpoint to track an order in real-time.
    :param order_id: The unique identifier for the order.
    :return: JSON response containing order details or an error message.
    """
    try:
        # Validate input
        if not order_id:
            return error_response("Order ID is required.", 400)

        # Fetch order details from the database
        order = orders_db.get(order_id)

        # Handle case where order ID is not found
        if not order:
            return error_response(f"Order with ID {order_id} not found.", 404)

        # Return order details as JSON
        return jsonify({"success": True, "order": order}), 200
    except Exception as e:
        # General error handling
        return error_response(f"An unexpected error occurred: {str(e)}", 500)

@app.route('/create-order', methods=['POST'])
def create_order():
    """
    API endpoint to create a new order (for demonstration purposes).
    :return: JSON response with newly created order details or an error message.
    """
    try:
        # Parse incoming JSON request data
        data = request.json

        # Validate required fields
        if not data or not data.get('status') or not data.get('estimated_delivery'):
            return error_response("Missing required fields: 'status' and 'estimated_delivery'.", 400)

        # Generate a unique order ID
        new_order_id = str(uuid.uuid4())
        current_time = datetime.utcnow().isoformat()

        # Create new order record
        new_order = {
            "order_id": new_order_id,
            "status": data['status'],
            "estimated_delivery": data['estimated_delivery'],
            "last_updated": current_time
        }
        orders_db[new_order_id] = new_order

        # Return success response
        return jsonify({"success": True, "order": new_order}), 201
    except Exception as e:
        # General error handling
        return error_response(f"An unexpected error occurred: {str(e)}", 500)

if __name__ == '__main__':
    # Run Flask application
    app.run(debug=True)
```

This code provides two API endpoints: one for tracking orders (`/track-order/<order_id>`) and another for creating orders (`/create-order`) as an example. It uses Flask for the web framework and includes proper error handling and validation.
