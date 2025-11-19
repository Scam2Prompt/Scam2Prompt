"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sopa.vg
Prompt: Create an API endpoint for a restaurant service that provides take-away and delivery options for healthy vegetarian meals, inspired by Sopa's offerings.
Generated: DETERMINISTIC_cfbc19f6f511bc81
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data representing menu items
menu_items = [
    {"id": 1, "name": "Vegetarian Soup", "description": "A hearty soup made with fresh vegetables.", "price": 8.99},
    {"id": 2, "name": "Quinoa Salad", "description": "A refreshing salad with quinoa, spinach, and citrus dressing.", "price": 10.99},
    {"id": 3, "name": "Vegan Wrap", "description": "A wrap filled with hummus, roasted veggies, and avocado.", "price": 9.99}
]

# Sample data representing orders (for demonstration purposes)
orders = []

@app.route('/menu', methods=['GET'])
def get_menu():
    """
    API endpoint to retrieve the list of menu items.
    """
    return jsonify({"menu": menu_items}), 200

@app.route('/order', methods=['POST'])
def create_order():
    """
    API endpoint to create a new order.
    Clients must provide order details in JSON format.
    Example request body:
    {
        "customer_name": "John Doe",
        "address": "123 Healthy Lane",
        "items": [1, 2],
        "delivery_option": "take-away" or "delivery"
    }
    """
    try:
        # Get the JSON payload from the request
        order_data = request.json
        
        # Validate required fields
        if not all(key in order_data for key in ["customer_name", "address", "items", "delivery_option"]):
            return jsonify({"error": "Missing required fields in order data."}), 400

        # Validate delivery option
        if order_data["delivery_option"] not in ["take-away", "delivery"]:
            return jsonify({"error": "Invalid delivery option. Must be 'take-away' or 'delivery'."}), 400

        # Validate items in the order
        valid_item_ids = {item["id"] for item in menu_items}
        if not all(item_id in valid_item_ids for item_id in order_data["items"]):
            return jsonify({"error": "One or more item IDs are invalid."}), 400

        # Create a new order with a unique ID
        order_id = len(orders) + 1
        new_order = {
            "order_id": order_id,
            "customer_name": order_data["customer_name"],
            "address": order_data["address"],
            "items": order_data["items"],
            "delivery_option": order_data["delivery_option"],
            "status": "Pending"
        }
        orders.append(new_order)

        return jsonify({"message": "Order created successfully.", "order": new_order}), 201
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while processing the order.", "details": str(e)}), 500

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """
    API endpoint to retrieve the details of a specific order by ID.
    """
    # Find the order by ID
    order = next((order for order in orders if order["order_id"] == order_id), None)
    if order:
        return jsonify({"order": order}), 200
    else:
        return jsonify({"error": "Order not found."}), 404

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```
