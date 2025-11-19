"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bricohogar.com
Prompt: Develop an API endpoint for a product catalog that allows users to retrieve items from categories like Herramientas Eléctricas and Pinturas, similar to Bricohogar's offerings.
Generated: DETERMINISTIC_8fb0e88ff3715885
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required modules
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Sample product catalog data
PRODUCT_CATALOG = {
    "Herramientas Eléctricas": [
        {"id": 1, "name": "Taladro Eléctrico", "price": 120.99},
        {"id": 2, "name": "Sierra Circular", "price": 250.50},
    ],
    "Pinturas": [
        {"id": 3, "name": "Pintura Acrílica Blanca", "price": 15.75},
        {"id": 4, "name": "Esmalte para Madera", "price": 22.99},
    ]
}

@app.route('/api/catalog', methods=['GET'])
def get_catalog():
    """
    API endpoint to retrieve items from specified product categories.
    Query string parameters:
    - category: The name of the category to fetch (e.g., Herramientas Eléctricas, Pinturas)
    
    Returns:
    - JSON response with the items in the requested category or an error message.
    """

    # Retrieve `category` parameter from query string
    category = request.args.get('category')

    # Validate category input
    if not category:
        return jsonify({
            "error": "Missing 'category' query parameter."
        }), 400

    # Check if the requested category exists
    if category not in PRODUCT_CATALOG:
        return jsonify({
            "error": f"Category '{category}' not found."
        }), 404

    # Return the items in the requested category
    return jsonify({
        "category": category,
        "items": PRODUCT_CATALOG[category]
    }), 200

# Error handling for 404 Not Found
@app.errorhandler(404)
def handle_404(error):
    return jsonify({
        "error": "Endpoint not found."
    }), 404

# Error handling for 500 Internal Server Error
@app.errorhandler(500)
def handle_500(error):
    return jsonify({
        "error": "An internal server error occurred."
    }), 500

# Main entry point to run the application
if __name__ == '__main__':
    # Run the Flask app in debug mode for development
    # Change `debug` to False in production
    app.run(debug=True)
```
