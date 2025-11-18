"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamas.com.mx
Prompt: Create a REST API in Flask for Meta+ to handle customer orders, including endpoints for querying product availability (e.g., stainless steel, aluminum) and placing orders with delivery details.
Generated: DETERMINISTIC_55ba2ba41865844c
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Sample product data
PRODUCTS = {
    "stainless_steel": {"available": True, "quantity": 120},
    "aluminum": {"available": True, "quantity": 80},
    "carbon_fiber": {"available": False, "quantity": 0},
}

# Sample order storage (in a real application, this would be a database)
ORDERS = []

@app.route('/products', methods=['GET'])
def get_product_availability():
    """
    Endpoint to get product availability.
    Returns the list of products with their availability and quantity.
    """
    return jsonify({"success": True, "products": PRODUCTS}), 200


@app.route('/orders', methods=['POST'])
def place_order():
    """
    Endpoint to place an order.
    Expects JSON body with 'product', 'quantity', 'customer_name', and 'delivery_address'.
    """
    try:
        data = request.json

        # Validate request body
        if not data or 'product' not in data or 'quantity' not in data or 'customer_name' not in data or 'delivery_address' not in data:
            return jsonify({"success": False, "error": "Invalid input. Required fields: product, quantity, customer_name, delivery_address."}), 400

        product = data['product']
        quantity = data['quantity']
        customer_name = data['customer_name']
        delivery_address = data['delivery_address']

        # Check if the product exists
        if product not in PRODUCTS:
            return jsonify({"success": False, "error": f"Product '{product}' not found."}), 404

        # Check product availability
        product_data = PRODUCTS[product]
        if not product_data['available'] or product_data['quantity'] < quantity:
            return jsonify({"success": False, "error": f"Insufficient stock for '{product}'."}), 400

        # Deduct the stock
        PRODUCTS[product]['quantity'] -= quantity

        # Create the order
        order = {
            "order_id": len(ORDERS) + 1,
            "product": product,
            "quantity": quantity,
            "customer_name": customer_name,
            "delivery_address": delivery_address,
            "order_date": datetime.utcnow().isoformat()
        }
        ORDERS.append(order)

        return jsonify({"success": True, "message": "Order placed successfully.", "order": order}), 201

    except Exception as e:
        # General error handling
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/orders', methods=['GET'])
def get_orders():
    """
    Endpoint to retrieve all orders.
    """
    return jsonify({"success": True, "orders": ORDERS}), 200


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
