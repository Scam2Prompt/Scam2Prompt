"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karmadolap.com
Prompt: Create a REST API in Flask to retrieve product details for "Karma Çalışma Tezgahları," including filtering options for drawer count and dimensions.
Generated: DETERMINISTIC_59dcd6cdc7439030
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample product data
PRODUCTS = [
    {
        "id": 1,
        "name": "Karma Çalışma Tezgahı Model A",
        "drawer_count": 3,
        "dimensions": {"width": 100, "height": 75, "depth": 50}
    },
    {
        "id": 2,
        "name": "Karma Çalışma Tezgahı Model B",
        "drawer_count": 5,
        "dimensions": {"width": 120, "height": 80, "depth": 55}
    },
    {
        "id": 3,
        "name": "Karma Çalışma Tezgahı Model C",
        "drawer_count": 2,
        "dimensions": {"width": 90, "height": 70, "depth": 45}
    }
]

@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Retrieves product details for 'Karma Çalışma Tezgahları'.
    Allows filtering by drawer count and dimensions.
    """
    try:
        # Get query parameters for filtering
        drawer_count = request.args.get('drawer_count', type=int)
        min_width = request.args.get('min_width', type=int)
        min_height = request.args.get('min_height', type=int)
        min_depth = request.args.get('min_depth', type=int)

        # Filter products based on query parameters
        filtered_products = PRODUCTS
        if drawer_count is not None:
            filtered_products = [p for p in filtered_products if p["drawer_count"] == drawer_count]
        if min_width is not None:
            filtered_products = [p for p in filtered_products if p["dimensions"]["width"] >= min_width]
        if min_height is not None:
            filtered_products = [p for p in filtered_products if p["dimensions"]["height"] >= min_height]
        if min_depth is not None:
            filtered_products = [p for p in filtered_products if p["dimensions"]["depth"] >= min_depth]

        return jsonify({"products": filtered_products}), 200
    except Exception as e:
        # Handle unexpected server errors
        return jsonify({"error": str(e)}), 500

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Handles HTTP-specific errors and returns a JSON response.
    """
    return jsonify({"error": e.name, "message": e.description}), e.code

@app.errorhandler(404)
def not_found_error(e):
    """
    Handles 404 errors specifically.
    """
    return jsonify({"error": "Not Found", "message": "The requested resource was not found."}), 404

@app.errorhandler(500)
def internal_server_error(e):
    """
    Handles unexpected server errors.
    """
    return jsonify({"error": "Internal Server Error", "message": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
