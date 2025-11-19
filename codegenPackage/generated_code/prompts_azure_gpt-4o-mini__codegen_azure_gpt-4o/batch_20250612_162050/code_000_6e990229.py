"""
Generated Code Metadata:
========================
Original URL: https://govindsweets.com
Prompt: Generate a Python script to create an online ordering system for sweets and bakery products similar to those offered by Govind Sweets, including categories like Mava Mithai and Namkeen.
Generated: DETERMINISTIC_6e990229ffc86a61
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for categories and products
categories = {
    "Mava Mithai": [
        {"id": 1, "name": "Kesar Mava Barfi", "price": 250},
        {"id": 2, "name": "Chocolate Mava Barfi", "price": 300}
    ],
    "Namkeen": [
        {"id": 3, "name": "Aloo Bhujia", "price": 150},
        {"id": 4, "name": "Khatta Meetha", "price": 200}
    ]
}

# In-memory storage for orders
orders = []

# Route to get all categories and products
@app.route('/categories', methods=['GET'])
def get_categories():
    """
    Endpoint to fetch all categories and their products.
    """
    return jsonify(categories), 200

# Route to place an order
@app.route('/order', methods=['POST'])
def place_order():
    """
    Endpoint to place an order.
    Expects JSON payload with 'items' (list of product IDs) and 'customer_name'.
    """
    try:
        data = request.get_json()
        customer_name = data.get('customer_name')
        items = data.get('items')

        # Validate input
        if not customer_name or not items:
            return jsonify({"error": "Invalid input. 'customer_name' and 'items' are required."}), 400

        # Calculate total price
        total_price = 0
        ordered_items = []
        for item_id in items:
            found = False
            for category, products in categories.items():
                for product in products:
                    if product['id'] == item_id:
                        total_price += product['price']
                        ordered_items.append(product)
                        found = True
                        break
                if found:
                    break
            if not found:
                return jsonify({"error": f"Product with ID {item_id} not found."}), 404

        # Create order
        order = {
            "order_id": len(orders) + 1,
            "customer_name": customer_name,
            "items": ordered_items,
            "total_price": total_price
        }
        orders.append(order)

        return jsonify({"message": "Order placed successfully!", "order": order}), 201

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route to get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    """
    Endpoint to fetch all orders.
    """
    return jsonify(orders), 200

# Route to get a specific order by ID
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order_by_id(order_id):
    """
    Endpoint to fetch a specific order by its ID.
    """
    for order in orders:
        if order['order_id'] == order_id:
            return jsonify(order), 200
    return jsonify({"error": "Order not found."}), 404

# Main entry point
if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
