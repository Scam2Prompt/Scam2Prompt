"""
Generated Code Metadata:
========================
Original URL: https://trattar.blogspot.com
Prompt: "Create a RESTful API endpoint to retrieve information about Trattar Madeiras' products, including eucalyptus and pine wood, and their respective treatment processes."
Generated: DETERMINISTIC_cd9f90f28962c56f
Batch ID: 20250622_211758
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

# Sample data representing Trattar Madeiras' products
products = [
    {
        "id": 1,
        "name": "Eucalyptus Wood",
        "treatment_process": "Kiln drying, chemical treatment for pest resistance"
    },
    {
        "id": 2,
        "name": "Pine Wood",
        "treatment_process": "Pressure treatment, anti-fungal coating"
    }
]

@app.route('/api/products', methods=['GET'])
def get_products():
    """
    RESTful API endpoint to retrieve information about Trattar Madeiras' products.
    Returns a JSON response containing product details.
    """
    try:
        # Return the list of products as a JSON response
        return jsonify({"success": True, "data": products}), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    """
    RESTful API endpoint to retrieve information about a specific product by its ID.
    Returns a JSON response containing product details or an error message if not found.
    """
    try:
        # Find the product by ID
        product = next((p for p in products if p["id"] == product_id), None)
        if product:
            return jsonify({"success": True, "data": product}), 200
        else:
            # Return a 404 error if the product is not found
            return jsonify({"success": False, "error": "Product not found"}), 404
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"success": False, "error": str(e)}), 500

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    """
    Custom error handler for 404 Not Found.
    Returns a JSON response indicating the resource was not found.
    """
    return jsonify({"success": False, "error": "Resource not found"}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    """
    Custom error handler for 500 Internal Server Error.
    Returns a JSON response indicating an internal server error occurred.
    """
    return jsonify({"success": False, "error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
