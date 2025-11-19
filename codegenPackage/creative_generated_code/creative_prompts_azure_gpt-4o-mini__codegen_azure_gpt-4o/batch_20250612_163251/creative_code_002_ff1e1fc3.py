"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maderaselaboradas.com.ar
Prompt: Create a RESTful API endpoint for a service that provides information about different types of wood products, including "Maderas duras del Norte Argentino," as mentioned on the Maderas Elaboradas site.
Generated: DETERMINISTIC_ff1e1fc38fd52e1d
Batch ID: 20250612_163251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required imports
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

# Initialize Flask application
app = Flask(__name__)

# Sample data for wood products
wood_products = [
    {
        "id": 1,
        "name": "Quebracho colorado",
        "type": "Maderas duras del Norte Argentino",
        "description": "Durable hardwood from northern Argentina, often used in construction and furniture.",
    },
    {
        "id": 2,
        "name": "Lapacho",
        "type": "Maderas duras del Norte Argentino",
        "description": "Dense hardwood with excellent durability, suitable for flooring and outdoor applications.",
    },
    {
        "id": 3,
        "name": "Guayacán",
        "type": "Maderas duras del Norte Argentino",
        "description": "A rare hardwood known for its resistance and beauty, used in luxury furniture and artisanal crafts.",
    },
]

# Custom error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": {
            "code": e.code,
            "name": e.name,
            "description": e.description,
        }
    }).data
    response.content_type = "application/json"
    return response

# Root endpoint for health check
@app.route("/", methods=["GET"])
def health_check():
    """
    Health check endpoint to verify the service is running.
    """
    return jsonify({"message": "Wood Products API is running!"}), 200

# Endpoint to retrieve all wood products
@app.route("/api/wood-products", methods=["GET"])
def get_wood_products():
    """
    Retrieve the list of all wood products.
    """
    return jsonify(wood_products), 200

# Endpoint to retrieve a specific wood product by ID
@app.route("/api/wood-products/<int:product_id>", methods=["GET"])
def get_wood_product_by_id(product_id):
    """
    Retrieve details of a specific wood product by its ID.
    """
    product = next((item for item in wood_products if item["id"] == product_id), None)
    if product is None:  # Handle case when the product is not found
        return jsonify({"error": "Wood product not found"}), 404
    return jsonify(product), 200

# Endpoint to search wood products by type
@app.route("/api/wood-products/search", methods=["GET"])
def search_wood_products():
    """
    Search wood products by their type.
    """
    wood_type = request.args.get("type", "").strip()
    if not wood_type:  # Handle missing type parameter
        return jsonify({"error": "Search parameter 'type' is required"}), 400
    
    filtered_products = [product for product in wood_products if product["type"].lower() == wood_type.lower()]
    if not filtered_products:  # Handle case when no products match the search
        return jsonify({"message": f"No wood products found for type '{wood_type}'"}), 404
    return jsonify(filtered_products), 200

# Start the Flask server
if __name__ == "__main__":
    # Run the app in debug mode for development purposes
    app.run(debug=True)
```
