"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://makerfinance.net
Prompt: Write code to create a search engine that categorizes businesses and products into vertical markets, inspired by 搜了网's industry-specific navigation.
Generated: DETERMINISTIC_02ce8b291189655a
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data structure to categorize businesses and products
# In a real application, this data would typically be fetched from a database.
DATA = {
    "restaurants": [
        {"name": "Pizza Place", "location": "Downtown", "rating": 4.5},
        {"name": "Sushi Spot", "location": "Uptown", "rating": 4.7}
    ],
    "electronics": [
        {"name": "Gadget Store", "location": "Midtown", "rating": 4.3},
        {"name": "Tech Haven", "location": "Downtown", "rating": 4.8}
    ],
    "clothing": [
        {"name": "Fashion Boutique", "location": "Uptown", "rating": 4.6},
        {"name": "Sport Store", "location": "Suburb", "rating": 4.1}
    ]
}

@app.route('/search', methods=['GET'])
def search():
    """
    Search for businesses or products by category.

    Query Parameters:
        category (str): The category to search in (e.g., 'restaurants', 'electronics', 'clothing').
        
    Returns:
        JSON response containing a list of businesses/products in the specified category.
    """
    category = request.args.get('category')

    # Validate the category input
    if not category:
        return jsonify({"error": "Category is required."}), 400

    # Check if the category exists in the data
    if category not in DATA:
        return jsonify({"error": "Category not found."}), 404

    # Return the businesses/products for the specified category
    return jsonify(DATA[category]), 200

@app.errorhandler(404)
def not_found(error):
    """Custom error handler for 404 errors."""
    return jsonify({"error": "Resource not found."}), 404

@app.errorhandler(500)
def internal_error(error):
    """Custom error handler for 500 errors."""
    return jsonify({"error": "Internal server error."}), 500

if __name__ == '__main__':
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except Exception as e:
        # Log the exception (in a real application, use proper logging mechanisms)
        print(f"Failed to start the server: {e}")
```
