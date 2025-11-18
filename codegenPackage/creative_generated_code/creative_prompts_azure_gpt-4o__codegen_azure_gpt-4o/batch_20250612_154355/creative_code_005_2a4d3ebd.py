"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wwereplicabelts.com
Prompt: Develop a REST API for managing categories like WWE, NBA, NFL, NHL, and MLB championship belts, with endpoints for adding, updating, and retrieving product information.
Generated: DETERMINISTIC_2a4d3ebd1d9eb8ad
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

# Initialize the Flask app
app = Flask(__name__)

# In-memory data store for categories and products
categories = {
    "WWE": [],
    "NBA": [],
    "NFL": [],
    "NHL": [],
    "MLB": []
}

# Utility function for error response
def error_response(message, status_code):
    response = jsonify({"error": message})
    response.status_code = status_code
    return response

# Error handler for invalid usage
@app.errorhandler(HTTPException)
def handle_exception(e):
    return error_response(e.description, e.code)

# Endpoint to retrieve products for a given category
@app.route("/api/products/<category>", methods=["GET"])
def get_products(category):
    # Check if category exists
    if category not in categories:
        return error_response("Category not found", 404)
    
    # Return the products for the given category
    return jsonify({"category": category, "products": categories[category]})

# Endpoint to add a new product to a category
@app.route("/api/products/<category>", methods=["POST"])
def add_product(category):
    # Check if category exists
    if category not in categories:
        return error_response("Category not found", 404)
    
    # Get the product details from the request body
    product_data = request.get_json()
    if not product_data or "name" not in product_data or "price" not in product_data:
        return error_response("Invalid product data. 'name' and 'price' are required fields.", 400)
    
    # Add the product to the category
    product = {
        "name": product_data["name"],
        "price": product_data["price"]
    }
    categories[category].append(product)

    return jsonify({"message": "Product added successfully", "product": product}), 201

# Endpoint to update an existing product in a category
@app.route("/api/products/<category>/<product_name>", methods=["PUT"])
def update_product(category, product_name):
    # Check if category exists
    if category not in categories:
        return error_response("Category not found", 404)
    
    # Get the product details from the request body
    product_data = request.get_json()
    if not product_data or "price" not in product_data:
        return error_response("Invalid product data. 'price' is a required field.", 400)
    
    # Find the product in the category
    for product in categories[category]:
        if product["name"] == product_name:
            product["price"] = product_data["price"]
            return jsonify({"message": "Product updated successfully", "product": product})
    
    return error_response("Product not found", 404)

# Run the Flask app
if __name__ == "__main__":
    # Use Flask's built-in server for development purposes
    app.run(debug=True)
```
