"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://specialmetals.co.in
Prompt: Write code to simulate an API that allows querying the availability of products like Stainless Steel Flanges, Wire Mesh, and Titanium Pipe Fittings, as listed on the Dinkar Alloys website.
Generated: DETERMINISTIC_6b85474889f7b411
Batch ID: 20250612_151611
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

# Mock product data for the API
products = [
    {"id": 1, "name": "Stainless Steel Flanges", "availability": True, "stock": 150},
    {"id": 2, "name": "Wire Mesh", "availability": False, "stock": 0},
    {"id": 3, "name": "Titanium Pipe Fittings", "availability": True, "stock": 75},
]

@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Endpoint to retrieve the list of all products.
    Returns:
        JSON response containing all products and their availability.
    """
    return jsonify({"status": "success", "data": products}), 200

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    """
    Endpoint to retrieve details of a single product by its ID.
    Args:
        product_id (int): ID of the product to retrieve.
    Returns:
        JSON response containing product details, or error message if not found.
    """
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify({"status": "success", "data": product}), 200
    else:
        return jsonify({"status": "error", "message": "Product not found"}), 404

@app.route('/api/products/query', methods=['GET'])
def query_product():
    """
    Endpoint to query product availability by its name.
    Expects the product name as a query parameter.
    Returns:
        JSON response with availability status of the queried product.
    """
    product_name = request.args.get('name')
    if not product_name:
        return jsonify({"status": "error", "message": "Product name is required"}), 400

    product = next((p for p in products if p['name'].lower() == product_name.lower()), None)
    if product:
        return jsonify({"status": "success", "data": {"name": product['name'], "availability": product['availability'], "stock": product['stock']}}), 200
    else:
        return jsonify({"status": "error", "message": "Product not found"}), 404

@app.errorhandler(404)
def handle_404_error(e):
    """
    Handles 404 Not Found errors for undefined routes.
    Returns:
        JSON response indicating the requested resource could not be found.
    """
    return jsonify({"status": "error", "message": "Resource not found"}), 404

@app.errorhandler(500)
def handle_500_error(e):
    """
    Handles 500 Internal Server Error.
    Returns:
        JSON response indicating an internal server error occurred.
    """
    return jsonify({"status": "error", "message": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask app on localhost with debugging enabled
    app.run(debug=True)
```
