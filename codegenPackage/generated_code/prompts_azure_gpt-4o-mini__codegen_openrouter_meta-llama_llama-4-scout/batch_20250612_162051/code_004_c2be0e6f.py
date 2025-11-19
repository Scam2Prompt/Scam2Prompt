"""
Generated Code Metadata:
========================
Original URL: https://karenfixing.com
Prompt: Suggest a framework for developing a digital catalog similar to the "کاتالوگ دیجیتال" offered by Karen Fixing for their facade products.
Generated: DETERMINISTIC_c2be0e6fb9bdb8f4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# digital_catalog.py

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
from flask import Flask, jsonify, request

app = Flask(__name__)

# Define product category enum
class ProductCategory(str, Enum):
    """Product category enum"""
    FACADE = "facade"
    ROOFING = "roofing"
    SIDING = "siding"

# Define product data class
@dataclass
class Product:
    """Product data class"""
    id: int
    name: str
    description: str
    category: ProductCategory
    price: float
    images: List[str]

# In-memory product catalog (replace with a database in production)
products: Dict[int, Product] = {
    1: Product(1, "Facade Product 1", "This is a facade product", ProductCategory.FACADE, 100.0, ["image1.jpg", "image2.jpg"]),
    2: Product(2, "Facade Product 2", "This is another facade product", ProductCategory.FACADE, 200.0, ["image3.jpg", "image4.jpg"]),
}

# API endpoint to get all products
@app.route('/products', methods=['GET'])
def get_products():
    """Get all products"""
    try:
        product_list = list(products.values())
        return jsonify([product.__dict__ for product in product_list])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to get product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id: int):
    """Get product by ID"""
    try:
        product = products.get(product_id)
        if product is None:
            return jsonify({"error": "Product not found"}), 404
        return jsonify(product.__dict__)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to create a new product
@app.route('/products', methods=['POST'])
def create_product():
    """Create a new product"""
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Invalid request data"}), 400
        new_product = Product(
            id=len(products) + 1,
            name=data['name'],
            description=data['description'],
            category=ProductCategory(data['category']),
            price=data['price'],
            images=data['images']
        )
        products[new_product.id] = new_product
        return jsonify(new_product.__dict__), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to update an existing product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id: int):
    """Update an existing product"""
    try:
        product = products.get(product_id)
        if product is None:
            return jsonify({"error": "Product not found"}), 404
        data = request.json
        if not data:
            return jsonify({"error": "Invalid request data"}), 400
        product.name = data.get('name', product.name)
        product.description = data.get('description', product.description)
        product.category = ProductCategory(data.get('category', product.category.value))
        product.price = data.get('price', product.price)
        product.images = data.get('images', product.images)
        return jsonify(product.__dict__)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id: int):
    """Delete a product"""
    try:
        product = products.get(product_id)
        if product is None:
            return jsonify({"error": "Product not found"}), 404
        del products[product_id]
        return jsonify({"message": "Product deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
