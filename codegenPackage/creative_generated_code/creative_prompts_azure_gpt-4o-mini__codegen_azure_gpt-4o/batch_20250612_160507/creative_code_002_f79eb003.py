"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balancer-app.pages.dev
Prompt: Create an API endpoint for a takeaway food service that includes menu items like homemade pasta and ravioli, with options for pickup and delivery.
Generated: DETERMINISTIC_f79eb003c24f4d8c
Batch ID: 20250612_160507
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

# Sample data: Menu items
menu_items = [
    {"id": 1, "name": "Homemade Pasta", "price": 12.99, "available": True},
    {"id": 2, "name": "Ravioli", "price": 14.99, "available": True},
]

# API endpoint: Get menu items
@app.route('/api/menu', methods=['GET'])
def get_menu():
    """
    Endpoint to retrieve the list of menu items.
    Returns:
        JSON response containing the menu items.
    """
    try:
        return jsonify({"menu": menu_items}), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while fetching the menu items."}), 500

# API endpoint: Place an order
@app.route('/api/order', methods=['POST'])
def place_order():
    """
    Endpoint to place an order.
    Expects JSON body with fields:
        - item_id (int): ID of the menu item
        - quantity (int): Quantity of the item
        - method (str): "pickup" or "delivery"
    Returns:
        Confirmation of the order or error message.
    """
    try:
        # Parse JSON request data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request. JSON data is required."}), 400

        # Validate required fields
        item_id = data.get("item_id")
        quantity = data.get("quantity")
        method = data.get("method")

        if not item_id or not quantity or not method:
            return jsonify({"error": "Missing required fields: item_id, quantity, method."}), 400

        # Validate method
        if method not in ["pickup", "delivery"]:
            return jsonify({"error": "Invalid method. Must be 'pickup' or 'delivery'."}), 400

        # Find menu item by ID
        menu_item = next((item for item in menu_items if item["id"] == item_id), None)

        if not menu_item:
            return jsonify({"error": "Menu item not found."}), 404

        if not menu_item["available"]:
            return jsonify({"error": f"{menu_item['name']} is currently unavailable."}), 400

        # Calculate total price
        total_price = menu_item["price"] * quantity

        # Return order confirmation
        confirmation = {
            "item": menu_item["name"],
            "quantity": quantity,
            "method": method,
            "total_price": round(total_price, 2),
            "status": "Order placed successfully"
        }
        return jsonify(confirmation), 200

    except Exception as e:
        return jsonify({"error": "An error occurred while placing the order."}), 500

# API endpoint: Health check
@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify if the API is running.
    Returns:
        Success message with HTTP 200 status.
    """
    return jsonify({"status": "API is running"}), 200

# Main entry point for running the application
if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
