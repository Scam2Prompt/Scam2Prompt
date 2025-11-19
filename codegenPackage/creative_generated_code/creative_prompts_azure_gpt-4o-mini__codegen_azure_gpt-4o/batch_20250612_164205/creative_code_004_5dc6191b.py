"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gnosisrew.com
Prompt: Illustrate how to implement a feature for an e-commerce platform that showcases Gnosis Rew's automotive modification products, including installation guides.
Generated: DETERMINISTIC_5dc6191bdf4eda10
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import os

# Initialize Flask application
app = Flask(__name__)

# Sample product data (this would typically come from a database)
products = [
    {
        "id": 1,
        "name": "Performance Exhaust System",
        "brand": "Gnosis Rew",
        "price": 499.99,
        "installation_guide": "guides/performance_exhaust_installation.pdf"
    },
    {
        "id": 2,
        "name": "High-Flow Air Intake",
        "brand": "Gnosis Rew",
        "price": 299.99,
        "installation_guide": "guides/high_flow_air_intake_installation.pdf"
    },
    {
        "id": 3,
        "name": "Turbocharger Kit",
        "brand": "Gnosis Rew",
        "price": 1499.99,
        "installation_guide": "guides/turbocharger_kit_installation.pdf"
    }
]

# Helper function to get product by ID
def get_product_by_id(product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None

@app.route('/products', methods=['GET'])
def list_products():
    """
    Endpoint to list all automotive modification products.
    Returns a JSON response with product details.
    """
    return jsonify({"products": products}), 200

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Endpoint to retrieve a specific product by ID.
    Returns a JSON response with product details.
    """
    product = get_product_by_id(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    return jsonify({"product": product}), 200

@app.route('/guides/<int:product_id>', methods=['GET'])
def get_installation_guide(product_id):
    """
    Endpoint to retrieve the installation guide for a specific product.
    Returns the guide file if available, or a 404 error if not.
    """
    product = get_product_by_id(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    guide_path = product.get("installation_guide")
    if not guide_path or not os.path.isfile(guide_path):
        return jsonify({"error": "Installation guide not found"}), 404

    # Assuming the installation guides are stored locally, serve the file
    return app.send_static_file(guide_path)

# Error handler for unexpected errors
@app.errorhandler(500)
def internal_error(error):
    """
    Handle unexpected server errors gracefully.
    """
    return jsonify({"error": "An unexpected error occurred"}), 500

# Error handler for 404 errors
@app.errorhandler(404)
def not_found_error(error):
    """
    Handle resource not found errors gracefully.
    """
    return jsonify({"error": "Resource not found"}), 404

# Entry point for the application
if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
