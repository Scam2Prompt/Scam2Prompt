"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://queenziee.com
Prompt: Create an API endpoint that allows users to search for clothing items like "Rompi" and "Jaket" with filters for minor defects, inspired by the product listings on Queenzie.
Generated: DETERMINISTIC_9d92130b1f90b302
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data to simulate a database
PRODUCTS = [
    {"id": 1, "name": "Rompi", "has_minor_defects": True, "price": 50},
    {"id": 2, "name": "Jaket", "has_minor_defects": False, "price": 120},
    {"id": 3, "name": "Rompi", "has_minor_defects": False, "price": 70},
    {"id": 4, "name": "Jaket", "has_minor_defects": True, "price": 90},
]

@app.route('/api/clothing/search', methods=['GET'])
def search_clothing():
    """
    Endpoint to search for clothing items with filters.
    Query Parameters:
    - name: Name of the clothing item (e.g., "Rompi", "Jaket").
    - has_minor_defects: Filter by minor defects (true/false).
    - price_min: Minimum price filter.
    - price_max: Maximum price filter.

    Returns:
    - JSON response containing filtered list of clothing items.
    """
    # Extract query parameters from the request
    name = request.args.get('name')  # Optional filter by name
    has_minor_defects = request.args.get('has_minor_defects')  # Optional filter by defect
    price_min = request.args.get('price_min', type=float)  # Optional minimum price filter
    price_max = request.args.get('price_max', type=float)  # Optional maximum price filter

    # Start with the full product list
    results = PRODUCTS

    # Filter by name if provided
    if name:
        results = [item for item in results if item['name'].lower() == name.lower()]

    # Filter by minor defects if provided
    if has_minor_defects is not None:
        try:
            has_minor_defects_bool = has_minor_defects.lower() == 'true'
            results = [item for item in results if item['has_minor_defects'] == has_minor_defects_bool]
        except ValueError:
            return jsonify({"error": "Invalid value for 'has_minor_defects'. Use 'true' or 'false'."}), 400

    # Apply price range filters if provided
    if price_min is not None:
        results = [item for item in results if item['price'] >= price_min]
    if price_max is not None:
        results = [item for item in results if item['price'] <= price_max]

    # Return filtered results
    return jsonify(results), 200

# Error handler for invalid routes
@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors for undefined routes.
    """
    return jsonify({"error": "Endpoint not found"}), 404

# Error handler for unexpected server errors
@app.errorhandler(500)
def internal_server_error(error):
    """
    Handle 500 errors for server issues.
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
