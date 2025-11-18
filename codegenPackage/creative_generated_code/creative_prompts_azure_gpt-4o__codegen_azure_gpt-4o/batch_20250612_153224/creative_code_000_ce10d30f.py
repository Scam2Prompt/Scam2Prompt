"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shopeewise.com
Prompt: Write Python code to create an e-commerce API that lists products like "LUXXE WHITE (Enhanced Glutathione)" with details such as price, description, and stock availability.
Generated: DETERMINISTIC_ce10d30f23104f5a
Batch ID: 20250612_153224
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

# Sample product data
products = [
    {
        "id": 1,
        "name": "LUXXE WHITE (Enhanced Glutathione)",
        "price": 49.99,
        "description": "A premium glutathione supplement for skin health and detoxification.",
        "in_stock": True,
        "stock_quantity": 120
    },
    {
        "id": 2,
        "name": "LUXXE PROTECT (Pure Grapeseed Extract)",
        "price": 39.99,
        "description": "Antioxidant-rich supplement for overall health and immune support.",
        "in_stock": True,
        "stock_quantity": 80
    }
]

@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Endpoint to retrieve all products.
    Returns a JSON list of products.
    """
    try:
        return jsonify({"products": products}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    """
    Endpoint to retrieve a single product by its ID.
    Returns product details in JSON format.
    """
    try:
        product = next((prod for prod in products if prod["id"] == product_id), None)
        if product:
            return jsonify({"product": product}), 200
        else:
            return jsonify({"error": f"Product with ID {product_id} not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/products', methods=['POST'])
def add_product():
    """
    Endpoint to add a new product.
    Expects JSON data with keys name, price, description, in_stock, and stock_quantity.
    """
    try:
        data = request.get_json()

        # Validate input data
        required_fields = ["name", "price", "description", "in_stock", "stock_quantity"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"'{field}' is required."}), 400

        # Add new product to the list
        new_product = {
            "id": max([prod["id"] for prod in products]) + 1 if products else 1,
            "name": data["name"],
            "price": data["price"],
            "description": data["description"],
            "in_stock": data["in_stock"],
            "stock_quantity": data["stock_quantity"]
        }
        products.append(new_product)

        return jsonify({"message": "Product added successfully.", "product": new_product}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """
    Endpoint to update an existing product by ID.
    Expects JSON data with keys name, price, description, in_stock, and stock_quantity.
    """
    try:
        product = next((prod for prod in products if prod["id"] == product_id), None)
        if not product:
            return jsonify({"error": f"Product with ID {product_id} not found."}), 404

        data = request.get_json()

        # Update product details
        product.update({key: data[key] for key in data if key in product})

        return jsonify({"message": "Product updated successfully.", "product": product}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """
    Endpoint to delete a product by ID.
    """
    try:
        global products
        products = [prod for prod in products if prod["id"] != product_id]
        return jsonify({"message": f"Product with ID {product_id} deleted successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Start the Flask server
    app.run(debug=True)
```
