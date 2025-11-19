"""
Generated Code Metadata:
========================
Original URL: https://maderaselaboradas.com.ar
Prompt: Generate a code snippet for a web application that allows users to order wooden products, specifically focusing on the features of "Maderas Aserradas" and "Cabos" as described on the Maderas Elaboradas website.
Generated: DETERMINISTIC_4005ac386d548f17
Batch ID: 20250612_163251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Sample data for wooden products
products = [
    {
        "id": 1,
        "category": "Maderas Aserradas",
        "name": "Pine Wood Plank",
        "price": 15.99,
        "description": "High-quality pine wood plank for construction and furniture."
    },
    {
        "id": 2,
        "category": "Cabos",
        "name": "Wooden Handle",
        "price": 5.99,
        "description": "Durable wooden handle for tools and accessories."
    }
]

# Route to fetch all products
@app.route('/products', methods=['GET'])
def get_products():
    """
    Endpoint to retrieve all wooden products.
    Returns:
        JSON response containing all products.
    """
    return jsonify({"products": products}), 200

# Route to fetch products by category
@app.route('/products/<category>', methods=['GET'])
def get_products_by_category(category):
    """
    Endpoint to retrieve products by category.
    Args:
        category (str): The category of products to filter.
    Returns:
        JSON response containing filtered products or an error message.
    """
    filtered_products = [product for product in products if product["category"].lower() == category.lower()]
    if not filtered_products:
        return jsonify({"error": "No products found for the specified category."}), 404
    return jsonify({"products": filtered_products}), 200

# Route to place an order
@app.route('/order', methods=['POST'])
def place_order():
    """
    Endpoint to place an order for wooden products.
    Request Body:
        JSON containing product_id and quantity.
    Returns:
        JSON response confirming the order or an error message.
    """
    try:
        # Parse the request data
        data = request.get_json()
        product_id = data.get("product_id")
        quantity = data.get("quantity")

        # Validate input
        if not product_id or not quantity:
            return jsonify({"error": "Product ID and quantity are required."}), 400

        # Find the product
        product = next((p for p in products if p["id"] == product_id), None)
        if not product:
            return jsonify({"error": "Product not found."}), 404

        # Calculate total price
        total_price = product["price"] * quantity

        # Return order confirmation
        return jsonify({
            "message": "Order placed successfully.",
            "product": product["name"],
            "quantity": quantity,
            "total_price": total_price
        }), 201
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Main entry point for the application
if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
