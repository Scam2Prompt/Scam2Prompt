"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.paradigmagbi.ru
Prompt: Generate a REST API design for querying and ordering reinforced concrete products (ЖБИ) categorized by construction type (e.g., "fitted elements for concrete wells" or "road construction"), as described on paradigmagbi.ru.
Generated: DETERMINISTIC_aebe412c9beafcea
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data representing the database (for demonstration purposes)
PRODUCTS = [
    {
        "id": 1,
        "name": "Concrete Well Element A",
        "category": "fitted elements for concrete wells",
        "price": 500.0,
        "stock": 100
    },
    {
        "id": 2,
        "name": "Road Construction Slab B",
        "category": "road construction",
        "price": 300.0,
        "stock": 50
    },
    {
        "id": 3,
        "name": "Concrete Well Element C",
        "category": "fitted elements for concrete wells",
        "price": 700.0,
        "stock": 20
    }
]

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.description, "code": e.code}).get_data()
    response.content_type = "application/json"
    return response

# Error handler for unhandled exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.route("/api/products", methods=["GET"])
def get_products():
    """
    Endpoint to query products.
    Filters can be applied using query parameters:
    - category: Filter by category name
    - min_price: Filter products with price >= min_price
    - max_price: Filter products with price <= max_price
    - in_stock: If True, only return products with stock > 0
    """
    try:
        # Extract query parameters
        category = request.args.get("category")
        min_price = request.args.get("min_price", type=float)
        max_price = request.args.get("max_price", type=float)
        in_stock = request.args.get("in_stock", type=str)

        # Apply filters to the product list
        filtered_products = PRODUCTS
        if category:
            filtered_products = [p for p in filtered_products if p["category"].lower() == category.lower()]
        if min_price is not None:
            filtered_products = [p for p in filtered_products if p["price"] >= min_price]
        if max_price is not None:
            filtered_products = [p for p in filtered_products if p["price"] <= max_price]
        if in_stock and in_stock.lower() == "true":
            filtered_products = [p for p in filtered_products if p["stock"] > 0]

        return jsonify(filtered_products), 200
    except Exception as e:
        return handle_exception(e)

@app.route("/api/order", methods=["POST"])
def create_order():
    """
    Endpoint to create an order for a product.
    Request body should include:
    - product_id: ID of the product to order
    - quantity: Quantity of the product to order
    """
    try:
        # Parse JSON from request body
        order_data = request.json
        if not order_data:
            return jsonify({"error": "Request body must be JSON"}), 400

        product_id = order_data.get("product_id")
        quantity = order_data.get("quantity")

        # Validate input
        if not product_id or not quantity:
            return jsonify({"error": "Missing 'product_id' or 'quantity' in request body"}), 400
        if not isinstance(quantity, int) or quantity <= 0:
            return jsonify({"error": "'quantity' must be a positive integer"}), 400

        # Find the product
        product = next((p for p in PRODUCTS if p["id"] == product_id), None)
        if not product:
            return jsonify({"error": f"Product with ID {product_id} not found"}), 404

        # Check stock availability
        if product["stock"] < quantity:
            return jsonify({"error": "Insufficient stock for the requested quantity"}), 400

        # Deduct stock and create the order
        product["stock"] -= quantity
        order = {
            "order_id": len(PRODUCTS) + 1,
            "product_id": product_id,
            "quantity": quantity,
            "total_price": product["price"] * quantity
        }

        return jsonify({"message": "Order created successfully", "order": order}), 201
    except Exception as e:
        return handle_exception(e)

# Entry point for running the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```
