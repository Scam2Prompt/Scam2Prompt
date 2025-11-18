"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balancer-app.pages.dev
Prompt: Create a Python script using Flask to implement an online food ordering system for a restaurant like RAVIOLI HOUSE. Include options for menu browsing, order confirmation in real-time, and takeaway scheduling.
Generated: DETERMINISTIC_2af97ce432228357
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from datetime import datetime

app = Flask(__name__)

# Sample menu for the restaurant
MENU = [
    {"id": 1, "name": "Cheese Ravioli", "price": 12.99},
    {"id": 2, "name": "Spinach Ravioli", "price": 13.99},
    {"id": 3, "name": "Chicken Ravioli", "price": 14.99},
    {"id": 4, "name": "Mushroom Ravioli", "price": 11.99},
]

# Placeholder for orders
ORDERS = []

@app.route('/menu', methods=['GET'])
def get_menu():
    """
    Endpoint to browse the restaurant's menu.
    Returns the menu as a JSON response.
    """
    return jsonify({"menu": MENU}), 200


@app.route('/order', methods=['POST'])
def place_order():
    """
    Endpoint to place an order.
    Accepts JSON data with item IDs and takeaway time (optional).
    """
    try:
        data = request.get_json()
        
        if not data or 'items' not in data:
            abort(400, description="Invalid request: Provide 'items' field in JSON data.")
        
        # Validate item IDs
        ordered_items = []
        for item_id in data['items']:
            menu_item = next((item for item in MENU if item['id'] == item_id), None)
            if not menu_item:
                abort(400, description=f"Item with ID {item_id} not found.")
            ordered_items.append(menu_item)
        
        # Calculate total price
        total_price = sum(item['price'] for item in ordered_items)
        
        # Handle takeaway scheduling
        takeaway_time = None
        if 'takeaway_time' in data:
            try:
                takeaway_time = datetime.strptime(data['takeaway_time'], "%Y-%m-%d %H:%M:%S")
                if takeaway_time < datetime.now():
                    abort(400, description="Invalid takeaway time: Cannot be in the past.")
            except ValueError:
                abort(400, description="Invalid date format: Use 'YYYY-MM-DD HH:MM:SS'.")
        
        # Create order
        order = {
            "id": len(ORDERS) + 1,
            "items": ordered_items,
            "total_price": total_price,
            "takeaway_time": takeaway_time.strftime("%Y-%m-%d %H:%M:%S") if takeaway_time else None,
        }
        ORDERS.append(order)
        
        return jsonify({"message": "Order placed successfully!", "order": order}), 201
    except Exception as e:
        abort(500, description=f"An unexpected error occurred: {str(e)}")


@app.route('/orders', methods=['GET'])
def get_orders():
    """
    Endpoint to view all placed orders.
    Returns the list of orders as a JSON response.
    """
    return jsonify({"orders": ORDERS}), 200


@app.errorhandler(404)
def resource_not_found(error):
    """
    Custom handler for 404 errors.
    """
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(400)
def bad_request(error):
    """
    Custom handler for 400 errors.
    """
    return jsonify({"error": error.description}), 400


@app.errorhandler(500)
def internal_error(error):
    """
    Custom handler for 500 errors.
    """
    return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    app.run(debug=True)
```
