"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Suggest a REST API design for a cosmetics store that includes features for tracking eco-friendly products and DIY kits, inspired by the offerings at C'est Moi Qui L'ai Fait Pour Vous.
Generated: DETERMINISTIC_be4fa716b1a97750
Batch ID: 20250612_160618
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

# In-memory database for demonstration purposes
products = [
    {
        "id": 1,
        "name": "Eco-friendly Organic Lip Balm",
        "category": "Eco-friendly",
        "price": 8.99,
        "description": "Natural lip balm made with organic ingredients.",
    },
    {
        "id": 2,
        "name": "DIY Soap Kit",
        "category": "DIY Kit",
        "price": 15.50,
        "description": "Make your own soap with this easy-to-use kit.",
    },
]

# Error handling helper function
def find_product(product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None


# API Endpoints

@app.route('/products', methods=['GET'])
def get_all_products():
    """
    Endpoint to retrieve all products.
    """
    return jsonify({"products": products})


@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Endpoint to retrieve a specific product by its ID.
    """
    product = find_product(product_id)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify({"product": product})


@app.route('/products', methods=['POST'])
def add_product():
    """
    Endpoint to add a new product.
    Expects JSON body with 'name', 'category', 'price', and 'description'.
    """
    try:
        data = request.get_json()
        new_product = {
            "id": len(products) + 1,
            "name": data["name"],
            "category": data["category"],
            "price": data["price"],
            "description": data["description"],
        }
        products.append(new_product)
        return jsonify({"message": "Product added", "product": new_product}), 201
    except KeyError as e:
        return jsonify({"error": f"Missing field: {e.args[0]}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """
    Endpoint to update an existing product by ID.
    Expects JSON body with 'name', 'category', 'price', and 'description'.
    """
    product = find_product(product_id)
    if product is None:
        return jsonify({"error": "Product not found"}), 404

    try:
        data = request.get_json()
        product.update({
            "name": data["name"],
            "category": data["category"],
            "price": data["price"],
            "description": data["description"],
        })
        return jsonify({"message": "Product updated", "product": product}), 200
    except KeyError as e:
        return jsonify({"error": f"Missing field: {e.args[0]}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """
    Endpoint to delete a product by ID.
    """
    product = find_product(product_id)
    if product is None:
        return jsonify({"error": "Product not found"}), 404

    products.remove(product)
    return jsonify({"message": "Product deleted"}), 200


@app.route('/products/category/<string:category>', methods=['GET'])
def get_products_by_category(category):
    """
    Endpoint to retrieve products by category (e.g., Eco-friendly, DIY Kit).
    """
    filtered_products = [product for product in products if product["category"].lower() == category.lower()]
    if not filtered_products:
        return jsonify({"error": f"No products found in category: {category}"}), 404
    return jsonify({"products": filtered_products})


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
