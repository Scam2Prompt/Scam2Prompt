"""
Generated Code Metadata:
========================
Original URL: https://sopa.vg
Prompt: Create an API endpoint for a restaurant service that provides take-away and delivery options for healthy vegetarian meals, inspired by Sopa's offerings.
Generated: DETERMINISTIC_cfbc19f6f511bc81
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data representing menu items
menu_items = [
    {"id": 1, "name": "Quinoa Salad", "price": 12.99, "category": "Salad"},
    {"id": 2, "name": "Vegetable Soup", "price": 8.99, "category": "Soup"},
    {"id": 3, "name": "Lentil Stew", "price": 10.99, "category": "Main Course"},
]

# Sample data representing orders
orders = []

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": e.description}).get_data()
    response.content_type = "application/json"
    return response

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# API endpoint to get the menu
@app.route('/api/menu', methods=['GET'])
def get_menu():
    """
    Endpoint to retrieve the menu items.
    Returns:
        JSON response containing the list of menu items.
    """
    return jsonify({"menu": menu_items}), 200

# API endpoint to place an order
@app.route('/api/order', methods=['POST'])
def place_order():
    """
    Endpoint to place an order.
    Request Body:
        - items: List of item IDs to order.
        - delivery_option: "take-away" or "delivery".
    Returns:
        JSON response confirming the order details.
    """
    data = request.get_json()
    if not data or 'items' not in data or 'delivery_option' not in data:
        return jsonify({"error": "Bad Request", "message": "Invalid request body"}), 400

    items = data['items']
    delivery_option = data['delivery_option']

    if delivery_option not in ['take-away', 'delivery']:
        return jsonify({"error": "Bad Request", "message": "Invalid delivery option"}), 400

    # Validate item IDs
    ordered_items = []
    for item_id in items:
        item = next((menu_item for menu_item in menu_items if menu_item['id'] == item_id), None)
        if item:
            ordered_items.append(item)
        else:
            return jsonify({"error": "Bad Request", "message": f"Item ID {item_id} not found"}), 400

    # Calculate total price
    total_price = sum(item['price'] for item in ordered_items)

    # Create order record
    order = {
        "id": len(orders) + 1,
        "items": ordered_items,
        "delivery_option": delivery_option,
        "total_price": total_price
    }
    orders.append(order)

    return jsonify({"message": "Order placed successfully", "order": order}), 201

# API endpoint to get all orders
@app.route('/api/orders', methods=['GET'])
def get_orders():
    """
    Endpoint to retrieve all orders.
    Returns:
        JSON response containing the list of orders.
    """
    return jsonify({"orders": orders}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
