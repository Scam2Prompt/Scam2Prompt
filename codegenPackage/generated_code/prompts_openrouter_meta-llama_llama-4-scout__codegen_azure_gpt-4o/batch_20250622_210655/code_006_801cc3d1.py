"""
Generated Code Metadata:
========================
Original URL: https://careandsmile.ae
Prompt: Develop a product catalog API for an e-commerce website like Care and Smile, which provides details of products across various categories, including baby products, beauty and health, and home and kitchen.
Generated: DETERMINISTIC_801cc3d101a5adb7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample product catalog data
PRODUCT_CATALOG = [
    {
        "id": 1,
        "name": "Baby Diapers",
        "category": "Baby Products",
        "price": 25.99,
        "description": "Soft and absorbent baby diapers.",
        "stock": 100
    },
    {
        "id": 2,
        "name": "Face Cream",
        "category": "Beauty and Health",
        "price": 15.49,
        "description": "Moisturizing face cream for all skin types.",
        "stock": 50
    },
    {
        "id": 3,
        "name": "Non-Stick Frying Pan",
        "category": "Home and Kitchen",
        "price": 30.00,
        "description": "Durable non-stick frying pan.",
        "stock": 20
    }
]

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_general_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Route to fetch all products
@app.route('/products', methods=['GET'])
def get_all_products():
    return jsonify(PRODUCT_CATALOG), 200

# Route to fetch products by category
@app.route('/products/category/<string:category>', methods=['GET'])
def get_products_by_category(category):
    filtered_products = [product for product in PRODUCT_CATALOG if product["category"].lower() == category.lower()]
    if not filtered_products:
        return jsonify({"error": "Not Found", "message": f"No products found in category '{category}'"}), 404
    return jsonify(filtered_products), 200

# Route to fetch product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = next((product for product in PRODUCT_CATALOG if product["id"] == product_id), None)
    if not product:
        return jsonify({"error": "Not Found", "message": f"Product with ID {product_id} not found"}), 404
    return jsonify(product), 200

# Route to add a new product
@app.route('/products', methods=['POST'])
def add_product():
    try:
        new_product = request.get_json()
        if not new_product:
            return jsonify({"error": "Bad Request", "message": "Request body is empty"}), 400

        required_fields = ["name", "category", "price", "description", "stock"]
        for field in required_fields:
            if field not in new_product:
                return jsonify({"error": "Bad Request", "message": f"Missing required field: {field}"}), 400

        new_product["id"] = max(product["id"] for product in PRODUCT_CATALOG) + 1
        PRODUCT_CATALOG.append(new_product)
        return jsonify(new_product), 201
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Route to update an existing product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    try:
        updated_data = request.get_json()
        if not updated_data:
            return jsonify({"error": "Bad Request", "message": "Request body is empty"}), 400

        product = next((product for product in PRODUCT_CATALOG if product["id"] == product_id), None)
        if not product:
            return jsonify({"error": "Not Found", "message": f"Product with ID {product_id} not found"}), 404

        for key, value in updated_data.items():
            if key in product:
                product[key] = value

        return jsonify(product), 200
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Route to delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = next((product for product in PRODUCT_CATALOG if product["id"] == product_id), None)
    if not product:
        return jsonify({"error": "Not Found", "message": f"Product with ID {product_id} not found"}), 404

    PRODUCT_CATALOG.remove(product)
    return jsonify({"message": f"Product with ID {product_id} has been deleted"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
