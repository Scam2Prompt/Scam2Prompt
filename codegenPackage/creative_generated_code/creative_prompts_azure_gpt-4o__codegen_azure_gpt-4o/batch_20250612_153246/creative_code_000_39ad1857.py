"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marinekiosk.gr
Prompt: Write Python code to create an e-commerce API for listing cannabis products such as CBG, CBD, and CB9 flowers, using product details like weight, dimensions, and stock availability from Marine Kiosk's catalog.
Generated: DETERMINISTIC_39ad185757495b95
Batch ID: 20250612_153246
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

# Sample product catalog: Marine Kiosk's cannabis products
products = [
    {
        "id": 1,
        "name": "CBG Flower",
        "weight": "10g",
        "dimensions": "5x5x5 cm",
        "stock": 50,
        "price": 30.99
    },
    {
        "id": 2,
        "name": "CBD Flower",
        "weight": "20g",
        "dimensions": "10x10x5 cm",
        "stock": 25,
        "price": 54.99
    },
    {
        "id": 3,
        "name": "CB9 Flower",
        "weight": "15g",
        "dimensions": "7x7x5 cm",
        "stock": 10,
        "price": 40.49
    },
]

@app.route('/products', methods=['GET'])
def list_products():
    """
    API endpoint to list all cannabis products.
    """
    return jsonify({"products": products}), 200

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product_details(product_id):
    """
    API endpoint to fetch details of a specific product.
    :param product_id: ID of the product to retrieve.
    """
    try:
        # Find the product by ID
        product = next((p for p in products if p["id"] == product_id), None)
        if product:
            return jsonify({"product": product}), 200
        else:
            return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "message": str(e)}), 500

@app.route('/products', methods=['POST'])
def add_product():
    """
    API endpoint to add a new product to the catalog.
    Expects JSON payload with product details.
    """
    try:
        new_product = request.json
        # Validate payload
        if not all(key in new_product for key in ("name", "weight", "dimensions", "stock", "price")):
            return jsonify({"error": "Invalid product data"}), 400

        # Generate a new ID
        new_id = max(p["id"] for p in products) + 1
        new_product["id"] = new_id

        # Add the product to the catalog
        products.append(new_product)
        return jsonify({"message": "Product added successfully", "product": new_product}), 201
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "message": str(e)}), 500

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """
    API endpoint to delete a product from the catalog.
    :param product_id: ID of the product to delete.
    """
    try:
        # Find and remove the product
        global products
        products = [p for p in products if p["id"] != product_id]

        return jsonify({"message": "Product deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "message": str(e)}), 500

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """
    API endpoint to update the details of an existing product.
    Expects JSON payload with updated product details.
    :param product_id: ID of the product to update.
    """
    try:
        updated_product_data = request.json
        # Find the product by ID
        product = next((p for p in products if p["id"] == product_id), None)
        
        if not product:
            return jsonify({"error": "Product not found"}), 404

        # Update product details
        for key, value in updated_product_data.items():
            if key in product:
                product[key] = value

        return jsonify({"message": "Product updated successfully", "product": product}), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "message": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
