"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.kozyhomedecor.com
Prompt: Create a REST API endpoint for adding items to a shopping cart similar to the functionality on Kozy Home Decor.
Generated: DETERMINISTIC_6952efa07fe1b060
Batch ID: 20250612_162051
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

app = Flask(__name__)

# In-memory storage for shopping carts (for demo purposes)
shopping_cart = {}

# Helper function to generate unique cart ID
def generate_cart_id():
    return str(uuid.uuid4())

# Endpoint to add items to the shopping cart
@app.route('/api/cart', methods=['POST'])
def add_to_cart():
    """
    POST /api/cart
    Request JSON body:
    {
        "cart_id": "optional_cart_id",   # Optional. If not provided, a new cart will be created.
        "item_id": "item_id",            # Required. ID of the item.
        "item_name": "name_of_item",     # Required. Name of the item.
        "quantity": integer,             # Required. Quantity of the item.
        "price_per_item": float          # Required. Price of the item.
    }
    Response JSON:
    {
        "status": "success",
        "cart_id": "cart_id",
        "cart": { "item_id": {...}, ... }
    }
    """
    try:
        # Parse request data
        data = request.get_json()

        # Validate required fields
        required_fields = ["item_id", "item_name", "quantity", "price_per_item"]
        for field in required_fields:
            if field not in data:
                return jsonify({"status": "error", "message": f"Missing field: {field}"}), 400

        # Validate quantity and price
        if not isinstance(data['quantity'], int) or data['quantity'] <= 0:
            return jsonify({"status": "error", "message": "Invalid quantity"}), 400
        if not isinstance(data['price_per_item'], float) or data['price_per_item'] <= 0:
            return jsonify({"status": "error", "message": "Invalid price_per_item"}), 400

        # Get or generate cart ID
        cart_id = data.get("cart_id", generate_cart_id())
        if cart_id not in shopping_cart:
            shopping_cart[cart_id] = {}

        # Add item to the cart
        item_id = data["item_id"]
        if item_id not in shopping_cart[cart_id]:
            shopping_cart[cart_id][item_id] = {
                "item_name": data["item_name"],
                "quantity": data["quantity"],
                "price_per_item": data["price_per_item"],
                "total_price": data["quantity"] * data["price_per_item"]
            }
        else:
            # Update quantity and total price if item already exists
            existing_item = shopping_cart[cart_id][item_id]
            new_quantity = existing_item["quantity"] + data["quantity"]
            shopping_cart[cart_id][item_id]["quantity"] = new_quantity
            shopping_cart[cart_id][item_id]["total_price"] = new_quantity * data["price_per_item"]

        # Return success response with updated cart
        return jsonify({"status": "success", "cart_id": cart_id, "cart": shopping_cart[cart_id]}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"status": "error", "message": str(e)}), 500


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
