"""
Generated Code Metadata:
========================
Original URL: https://superstep.org
Prompt: Outline a REST API for a lash supply store, incorporating best product recommendations mentioned in the Super Step article.
Generated: DETERMINISTIC_cf405ed12b737b65
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for products and recommendations
products = [
    {"id": 1, "name": "Premium Mink Lashes", "price": 25.99, "stock": 100},
    {"id": 2, "name": "Silk Lashes", "price": 19.99, "stock": 200},
    {"id": 3, "name": "Volume Lash Extensions", "price": 29.99, "stock": 150},
]

recommendations = [
    {"product_id": 1, "recommended_for": "Natural Look"},
    {"product_id": 2, "recommended_for": "Lightweight Comfort"},
    {"product_id": 3, "recommended_for": "Dramatic Volume"},
]

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 400 Bad Request
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400

# Home route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Lash Supply Store API!"})

# Get all products
@app.route("/products", methods=["GET"])
def get_products():
    return jsonify({"products": products})

# Get a single product by ID
@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify({"product": product})

# Get product recommendations
@app.route("/recommendations", methods=["GET"])
def get_recommendations():
    return jsonify({"recommendations": recommendations})

# Get recommendations for a specific product
@app.route("/recommendations/<int:product_id>", methods=["GET"])
def get_recommendation_for_product(product_id):
    recommendation = next((r for r in recommendations if r["product_id"] == product_id), None)
    if not recommendation:
        return jsonify({"error": "Recommendation not found for this product"}), 404
    return jsonify({"recommendation": recommendation})

# Add a new product
@app.route("/products", methods=["POST"])
def add_product():
    try:
        data = request.get_json()
        if not data or "name" not in data or "price" not in data or "stock" not in data:
            return jsonify({"error": "Invalid product data"}), 400

        new_product = {
            "id": len(products) + 1,
            "name": data["name"],
            "price": data["price"],
            "stock": data["stock"],
        }
        products.append(new_product)
        return jsonify({"message": "Product added successfully", "product": new_product}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Update an existing product
@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    try:
        product = next((p for p in products if p["id"] == product_id), None)
        if not product:
            return jsonify({"error": "Product not found"}), 404

        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid product data"}), 400

        product["name"] = data.get("name", product["name"])
        product["price"] = data.get("price", product["price"])
        product["stock"] = data.get("stock", product["stock"])

        return jsonify({"message": "Product updated successfully", "product": product})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Delete a product
@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    global products
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    products = [p for p in products if p["id"] != product_id]
    return jsonify({"message": "Product deleted successfully"})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
```
