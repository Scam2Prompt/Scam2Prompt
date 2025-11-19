"""
Generated Code Metadata:
========================
Original URL: https://multandesigns.com
Prompt: "Create a RESTful API endpoint for retrieving details about Pakistani clothing products, including their category, price, and description."
Generated: DETERMINISTIC_d25955da7c3bfaa8
Batch ID: 20250622_210443
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

# Sample data representing Pakistani clothing products
products = [
    {
        "id": 1,
        "name": "Shalwar Kameez",
        "category": "Traditional",
        "price": 2500,
        "description": "A classic Pakistani outfit consisting of a long tunic and trousers."
    },
    {
        "id": 2,
        "name": "Kurta",
        "category": "Casual",
        "price": 1500,
        "description": "A comfortable and stylish long shirt, perfect for casual wear."
    },
    {
        "id": 3,
        "name": "Lehenga",
        "category": "Formal",
        "price": 8000,
        "description": "An elegant and heavily embroidered skirt, ideal for weddings and formal events."
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

# Error handler for non-HTTP exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# API endpoint to retrieve product details
@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Retrieve the list of Pakistani clothing products.
    Returns:
        JSON response containing product details.
    """
    return jsonify(products), 200

# API endpoint to retrieve a specific product by ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    """
    Retrieve details of a specific product by its ID.
    Args:
        product_id (int): The ID of the product to retrieve.
    Returns:
        JSON response containing product details or an error message.
    """
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify(product), 200
    else:
        return jsonify({
            "error": "Not Found",
            "message": f"Product with ID {product_id} not found."
        }), 404

# Main entry point for running the application
if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
