"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fanzyfashion.in
Prompt: Write code to create an e-commerce product catalog API that includes categories like "Kids Clothing," "Women's Clothing," "Jewelry," and "Accessories," with support for product variants and discounts.
Generated: DETERMINISTIC_07aced5d1bae7adb
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Sample in-memory data store for products and categories
categories = ["Kids Clothing", "Women's Clothing", "Jewelry", "Accessories"]

# Product catalog
products = [
    {
        "id": 1,
        "name": "Kids T-shirt",
        "category": "Kids Clothing",
        "variants": [
            {"size": "S", "price": 9.99},
            {"size": "M", "price": 11.99}
        ],
        "discount": 0.1  # 10% discount
    },
    {
        "id": 2,
        "name": "Women's Dress",
        "category": "Women's Clothing",
        "variants": [
            {"size": "M", "price": 49.99},
            {"size": "L", "price": 54.99}
        ],
        "discount": 0.15  # 15% discount
    },
    {
        "id": 3,
        "name": "Gold Necklace",
        "category": "Jewelry",
        "variants": [{"type": "16-inch", "price": 299.99}],
        "discount": 0  # No discount
    },
    {
        "id": 4,
        "name": "Leather Wallet",
        "category": "Accessories",
        "variants": [{"color": "Brown", "price": 19.99}],
        "discount": 0.05  # 5% discount
    }
]

# Route to get all categories
@app.route('/api/categories', methods=['GET'])
def get_categories():
    return jsonify({"categories": categories}), 200

# Route to get all products or filter by category
@app.route('/api/products', methods=['GET'])
def get_products():
    category = request.args.get('category', None)
    if category:
        filtered_products = [product for product in products if product["category"] == category]
        if not filtered_products:
            return jsonify({"error": "No products found for the specified category"}), 404
        return jsonify({"products": filtered_products}), 200
    return jsonify({"products": products}), 200

# Route to get a single product by ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((product for product in products if product["id"] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify({"product": product}), 200

# Route to create a new product
@app.route('/api/products', methods=['POST'])
def create_product():
    if not request.json or "name" not in request.json or "category" not in request.json:
        abort(400, description="Invalid product data")
    
    new_product = {
        "id": max(product["id"] for product in products) + 1,  # Generate new ID
        "name": request.json["name"],
        "category": request.json["category"],
        "variants": request.json.get("variants", []),
        "discount": request.json.get("discount", 0)
    }
    
    products.append(new_product)
    return jsonify({"message": "Product created successfully", "product": new_product}), 201

# Route to update an existing product
@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((product for product in products if product["id"] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    if not request.json:
        abort(400, description="Invalid product data")
    
    # Update product fields
    product["name"] = request.json.get("name", product["name"])
    product["category"] = request.json.get("category", product["category"])
    product["variants"] = request.json.get("variants", product["variants"])
    product["discount"] = request.json.get("discount", product["discount"])
    
    return jsonify({"message": "Product updated successfully", "product": product}), 200

# Route to delete a product by ID
@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = next((product for product in products if product["id"] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    products.remove(product)
    return jsonify({"message": "Product deleted successfully"}), 200

# Error handling for invalid routes or methods
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
