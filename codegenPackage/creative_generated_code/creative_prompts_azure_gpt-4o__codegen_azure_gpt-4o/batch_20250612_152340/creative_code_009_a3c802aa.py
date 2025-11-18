"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.panasonics.com.vn
Prompt: Generate a REST API design for managing Panasonic product catalogs, including endpoints for querying LED light types (e.g., "Đèn LED Búp Panasonic") and their specifications.
Generated: DETERMINISTIC_a3c802aa4c727f2d
Batch ID: 20250612_152340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data for LED light types and specifications
product_catalog = [
    {
        "id": 1,
        "name": "Đèn LED Búp Panasonic",
        "specifications": {
            "wattage": "7W",
            "color_temperature": "3000K - 6500K",
            "lifespan_hours": 25000,
            "material": "Aluminum + Plastic",
        },
    },
    {
        "id": 2,
        "name": "Đèn LED Âm Trần Panasonic",
        "specifications": {
            "wattage": "12W",
            "color_temperature": "4000K",
            "lifespan_hours": 30000,
            "material": "High-Quality Plastic",
        },
    },
]

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Error handler for HTTP exceptions."""
    response = e.get_response()
    response.data = jsonify({"error": e.description, "code": e.code}).get_data()
    response.content_type = "application/json"
    return response

@app.errorhandler(Exception)
def handle_general_exception(e):
    """Error handler for general exceptions."""
    return jsonify({"error": str(e), "code": 500}), 500

@app.route("/api/products", methods=["GET"])
def list_products():
    """
    Endpoint to list all Panasonic products in the catalog.
    Returns:
        JSON response with product list.
    """
    return jsonify(product_catalog), 200

@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    """
    Endpoint to retrieve specific product information by ID.
    Args:
        product_id (int): The ID of the product to retrieve.
    Returns:
        JSON response with product details or error message if not found.
    """
    product = next((p for p in product_catalog if p["id"] == product_id), None)
    if product:
        return jsonify(product), 200
    return jsonify({"error": "Product not found", "code": 404}), 404

@app.route("/api/products/search", methods=["GET"])
def search_products():
    """
    Endpoint to search for products by name.
    Query Parameters:
        name (str): The name of the product to search for.
    Returns:
        JSON response with matching products or an empty list if no matches.
    """
    name_query = request.args.get("name", "").lower()
    matching_products = [
        p for p in product_catalog if name_query in p["name"].lower()
    ]
    return jsonify(matching_products), 200

if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
```
