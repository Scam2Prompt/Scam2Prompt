"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gematria.com
Prompt: Illustrate how to implement a shopping cart feature in a web application that includes Gematria's science-driven supplements, focusing on user experience.
Generated: DETERMINISTIC_f3da5b1452e63c71
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database for products and shopping cart
PRODUCTS = [
    {"id": 1, "name": "Supplement A", "price": 29.99},
    {"id": 2, "name": "Supplement B", "price": 49.99},
    {"id": 3, "name": "Supplement C", "price": 39.99},
]

shopping_cart = []


def find_product_by_id(product_id):
    """
    Helper function to find a product by its ID.

    :param product_id: ID of the product to search for
    :return: Product dictionary if found, None otherwise
    """
    return next((product for product in PRODUCTS if product["id"] == product_id), None)


@app.route('/products', methods=['GET'])
def list_products():
    """
    Endpoint to list all available products.

    :return: JSON response containing the list of products
    """
    return jsonify(PRODUCTS), 200


@app.route('/cart', methods=['GET'])
def view_cart():
    """
    Endpoint to view shopping cart contents.

    :return: JSON response containing the shopping cart items and total cost
    """
    total_cost = sum(item["price"] * item["quantity"] for item in shopping_cart)
    return jsonify({"cart": shopping_cart, "total_cost": total_cost}), 200


@app.route('/cart', methods=['POST'])
def add_to_cart():
    """
    Endpoint to add a product to the shopping cart.

    Request body should include product_id and quantity.

    :return: JSON response with success message or error
    """
    try:
        data = request.get_json()
        product_id = data.get("product_id")
        quantity = data.get("quantity", 1)

        if not product_id:
            return jsonify({"error": "Product ID is required"}), 400

        if quantity <= 0:
            return jsonify({"error": "Quantity must be greater than 0"}), 400

        product = find_product_by_id(product_id)
        if not product:
            return jsonify({"error": "Product not found"}), 404

        # Check if product already exists in cart
        for item in shopping_cart:
            if item["id"] == product_id:
                item["quantity"] += quantity
                break
        else:
            # Add new product to cart
            shopping_cart.append({"id": product["id"], "name": product["name"], "price": product["price"], "quantity": quantity})

        return jsonify({"message": f"Added {quantity} of {product['name']} to cart"}), 200
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route('/cart', methods=['DELETE'])
def remove_from_cart():
    """
    Endpoint to remove a product from the shopping cart.

    Request body should include product_id.

    :return: JSON response with success message or error
    """
    try:
        data = request.get_json()
        product_id = data.get("product_id")

        if not product_id:
            return jsonify({"error": "Product ID is required"}), 400

        for item in shopping_cart:
            if item["id"] == product_id:
                shopping_cart.remove(item)
                return jsonify({"message": f"Removed {item['name']} from cart"}), 200

        return jsonify({"error": "Product not found in cart"}), 404
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route('/cart/clear', methods=['POST'])
def clear_cart():
    """
    Endpoint to clear the shopping cart.

    :return: JSON response with success message
    """
    shopping_cart.clear()
    return jsonify({"message": "Shopping cart cleared"}), 200


if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```
