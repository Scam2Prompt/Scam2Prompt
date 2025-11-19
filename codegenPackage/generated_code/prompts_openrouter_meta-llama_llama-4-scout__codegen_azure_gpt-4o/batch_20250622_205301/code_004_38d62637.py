"""
Generated Code Metadata:
========================
Original URL: https://specialmetals.co.in
Prompt: "Design a RESTful API for retrieving specifications of various Stainless Steel Products, including Pipes, Fittings, and Sheets."
Generated: DETERMINISTIC_38d62637a05a8d6a
Batch ID: 20250622_205301
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

# Sample data for stainless steel products
PRODUCTS = {
    "pipes": [
        {"id": 1, "name": "Pipe A", "diameter": "2 inches", "grade": "304"},
        {"id": 2, "name": "Pipe B", "diameter": "4 inches", "grade": "316"}
    ],
    "fittings": [
        {"id": 1, "name": "Fitting A", "type": "Elbow", "grade": "304"},
        {"id": 2, "name": "Fitting B", "type": "Tee", "grade": "316"}
    ],
    "sheets": [
        {"id": 1, "name": "Sheet A", "thickness": "2 mm", "grade": "304"},
        {"id": 2, "name": "Sheet B", "thickness": "4 mm", "grade": "316"}
    ]
}

@app.route('/api/products/<category>', methods=['GET'])
def get_products(category):
    """
    Endpoint to retrieve stainless steel products by category.
    :param category: The category of products (pipes, fittings, sheets).
    :return: JSON response containing the products in the specified category.
    """
    try:
        # Validate category
        if category not in PRODUCTS:
            return jsonify({"error": "Invalid category. Valid categories are: pipes, fittings, sheets."}), 400
        
        # Return products in the specified category
        return jsonify(PRODUCTS[category]), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

@app.route('/api/products/<category>/<int:product_id>', methods=['GET'])
def get_product_by_id(category, product_id):
    """
    Endpoint to retrieve a specific product by ID within a category.
    :param category: The category of products (pipes, fittings, sheets).
    :param product_id: The ID of the product to retrieve.
    :return: JSON response containing the product details.
    """
    try:
        # Validate category
        if category not in PRODUCTS:
            return jsonify({"error": "Invalid category. Valid categories are: pipes, fittings, sheets."}), 400
        
        # Find product by ID
        product = next((item for item in PRODUCTS[category] if item["id"] == product_id), None)
        if not product:
            return jsonify({"error": f"Product with ID {product_id} not found in category {category}."}), 404
        
        # Return product details
        return jsonify(product), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    """
    Custom handler for 404 errors.
    :param error: The error object.
    :return: JSON response for 404 errors.
    """
    return jsonify({"error": "Resource not found."}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Custom handler for 500 errors.
    :param error: The error object.
    :return: JSON response for 500 errors.
    """
    return jsonify({"error": "Internal server error."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
