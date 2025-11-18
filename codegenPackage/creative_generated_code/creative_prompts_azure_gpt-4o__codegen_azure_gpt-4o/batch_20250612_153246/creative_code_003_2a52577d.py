"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://granstore.co
Prompt: Suggest a library or tool for implementing a payment gateway that supports "Pago contra-entrega" as described on the GranStore website.
Generated: DETERMINISTIC_2a52577d41f38cf4
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This example demonstrates implementing a payment gateway supporting "Pago contra-entrega" (Cash on Delivery) 
using Flask (a Python web framework). For production readiness, you could integrate with third-party APIs 
like Stripe or PayPal for additional payment methods.

Dependencies:
- Flask (Install using `pip install flask`)
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database to store orders (for demonstration purposes)
orders_db = []

# Error handling class for custom exceptions
class PaymentError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

@app.route('/create-order', methods=['POST'])
def create_order():
    """
    Endpoint to create an order with "Pago contra-entrega" payment method.
    Expects a JSON payload with details like customer name, address, and order items.
    """
    try:
        # Parse request data
        data = request.json
        if not data or 'customer_name' not in data or 'address' not in data or 'order_items' not in data:
            raise PaymentError("Invalid input data. Missing required fields.")

        # Validate order items
        if not isinstance(data['order_items'], list) or len(data['order_items']) == 0:
            raise PaymentError("Order items should be a non-empty list.")

        # Generate a mock order ID
        order_id = len(orders_db) + 1

        # Save order details to the mock database
        new_order = {
            "order_id": order_id,
            "customer_name": data['customer_name'],
            "address": data['address'],
            "order_items": data['order_items'],
            "payment_method": "Pago contra-entrega",  # Cash on Delivery
            "status": "Pending"  # Initial status
        }
        orders_db.append(new_order)

        return jsonify({
            "success": True,
            "message": "Order created successfully.",
            "order_id": order_id
        }), 201
    except PaymentError as e:
        # Handle specific payment errors
        return jsonify({
            "success": False,
            "message": str(e)
        }), 400
    except Exception as e:
        # Generic error handling
        return jsonify({
            "success": False,
            "message": "An unexpected error occurred: " + str(e)
        }), 500

@app.route('/get-orders', methods=['GET'])
def get_orders():
    """
    Endpoint to retrieve all orders for demonstration purposes.
    """
    return jsonify({
        "success": True,
        "orders": orders_db
    }), 200

if __name__ == '__main__':
    """
    Run the Flask server.
    Note: In production, use a WSGI server like Gunicorn or uWSGI for deployment.
    """
    app.run(debug=True)
```
