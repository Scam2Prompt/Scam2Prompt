"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sushipanda.es
Prompt: Generate a code snippet for an API that allows users to place orders for sushi from SushiPanda's new menu.
Generated: DETERMINISTIC_93eeef3900077fcd
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database of menu items
MENU = {
    1: {"name": "California Roll", "price": 8.99},
    2: {"name": "Spicy Tuna Roll", "price": 9.99},
    3: {"name": "Salmon Nigiri", "price": 10.99},
    4: {"name": "Vegetable Roll", "price": 7.99},
}

# In-memory storage for orders
ORDERS = []
ORDER_ID_COUNTER = 1

@app.route('/menu', methods=['GET'])
def get_menu():
    """
    Endpoint to retrieve the SushiPanda menu.
    """
    return jsonify({"menu": MENU}), 200

@app.route('/order', methods=['POST'])
def place_order():
    """
    Endpoint to place a sushi order.
    Expects a JSON payload with 'items' (list of menu item IDs) and 'customer_name'.
    """
    global ORDER_ID_COUNTER

    try:
        # Parse the incoming JSON payload
        data = request.get_json()
        if not data or 'items' not in data or 'customer_name' not in data:
            return jsonify({"error": "Invalid request. Provide 'items' and 'customer_name'."}), 400

        # Validate if all items exist in the menu
        items = data['items']
        customer_name = data['customer_name']

        if not isinstance(items, list) or not all(isinstance(item, int) for item in items):
            return jsonify({"error": "'items' must be a list of valid menu item IDs."}), 400

        if not isinstance(customer_name, str) or not customer_name.strip():
            return jsonify({"error": "'customer_name' must be a valid non-empty string."}), 400

        order_items = []
        total_price = 0.0

        for item_id in items:
            menu_item = MENU.get(item_id)
            if not menu_item:
                return jsonify({"error": f"Menu item with ID {item_id} does not exist."}), 404
            order_items.append(menu_item)
            total_price += menu_item['price']

        # Create the order
        order = {
            "order_id": ORDER_ID_COUNTER,
            "customer_name": customer_name,
            "items": order_items,
            "total_price": round(total_price, 2),
        }
        ORDERS.append(order)
        ORDER_ID_COUNTER += 1

        # Return the order confirmation
        return jsonify({"message": "Order placed successfully!", "order": order}), 201

    except Exception as e:
        # Handle unexpected server errors
        return jsonify({"error": str(e)}), 500

@app.route('/orders', methods=['GET'])
def get_orders():
    """
    Endpoint to retrieve all orders.
    """
    return jsonify({"orders": ORDERS}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
