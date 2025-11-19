"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.vircomem.ro
Prompt: Develop a RESTful API endpoint that allows users to place orders for industrial cleaning brushes, incorporating the quick delivery service mentioned by VIRCOMEM.
Generated: DETERMINISTIC_6ad9a1efdee21e94
Batch ID: 20250612_155327
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
import datetime

app = Flask(__name__)

# In-memory database for simplicity (this should be replaced by a proper database in production)
orders = []

# Helper function to validate order data
def validate_order_data(data):
    required_fields = ['customer_name', 'delivery_address', 'brush_type', 'quantity']
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    if not isinstance(data['quantity'], int) or data['quantity'] <= 0:
        return False, "Invalid quantity. Must be a positive integer."
    return True, None

@app.route('/place-order', methods=['POST'])
def place_order():
    """
    Endpoint to place an order for industrial cleaning brushes.
    Accepts JSON payload containing:
    - customer_name: Name of the customer (string)
    - delivery_address: Delivery address (string)
    - brush_type: Type of brush (string)
    - quantity: Number of brushes to order (integer)
    Response:
    - Success: Returns the order confirmation with order ID and estimated delivery time.
    - Error: Returns an error message and appropriate HTTP status code.
    """
    try:
        # Parse request data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input. JSON data is required."}), 400
        
        # Validate order data
        is_valid, error_message = validate_order_data(data)
        if not is_valid:
            return jsonify({"error": error_message}), 400

        # Generate unique order ID and calculate estimated delivery time
        order_id = str(uuid.uuid4())
        order_time = datetime.datetime.now()
        estimated_delivery_time = order_time + datetime.timedelta(days=1)  # Quick delivery service: 1-day delivery

        # Create the order record
        order = {
            "order_id": order_id,
            "customer_name": data['customer_name'],
            "delivery_address": data['delivery_address'],
            "brush_type": data['brush_type'],
            "quantity": data['quantity'],
            "order_time": order_time.isoformat(),
            "estimated_delivery_time": estimated_delivery_time.isoformat()
        }
        orders.append(order)

        # Respond with order confirmation
        return jsonify({
            "message": "Order placed successfully.",
            "order": order
        }), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
