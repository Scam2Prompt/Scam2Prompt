"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: Create an API endpoint that retrieves a list of available glass products, including shower boxes and decorative mirrors, similar to those provided by Marine Vidros.
Generated: DETERMINISTIC_aeb54e53cf631473
Batch ID: 20250612_135310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask application to create an API endpoint for retrieving glass products

from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Sample data representing glass products (normally this would be retrieved from a database)
glass_products = [
    {"id": 1, "name": "Shower Box", "description": "Tempered glass shower box with aluminum frame.", "price": 300.00},
    {"id": 2, "name": "Decorative Mirror", "description": "Stylish decorative mirror for walls.", "price": 250.00},
    {"id": 3, "name": "Glass Tabletop", "description": "Customizable tempered glass tabletop.", "price": 150.00},
    {"id": 4, "name": "Sliding Glass Door", "description": "Transparent sliding glass door.", "price": 500.00},
]

@app.route('/api/glass-products', methods=['GET'])
def get_glass_products():
    """
    API endpoint to retrieve a list of available glass products.
    ---
    Method: GET
    URL: /api/glass-products
    Parameters: None
    Returns: JSON response containing list of glass products.
    """
    try:
        # Log the request
        logging.info("Received request to retrieve glass products.")

        # Return the list of glass products as JSON response
        return jsonify({"success": True, "products": glass_products}), 200

    except Exception as e:
        # Log any unexpected errors
        logging.error(f"An error occurred: {e}")

        # Return error response
        return jsonify({"success": False, "error": "Internal server error"}), 500

# Error handler for 404 - Not Found
@app.errorhandler(404)
def not_found_error(error):
    """
    Handles 404 errors for non-existent routes.
    """
    return jsonify({"success": False, "error": "Resource not found"}), 404

# Error handler for 500 - Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    """
    Handles 500 errors for server issues.
    """
    return jsonify({"success": False, "error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
```

This code defines a Flask API endpoint `/api/glass-products` that returns a list of glass products in JSON format. The code is well-documented with comments, includes error handlers for common issues, and follows Python best practices.
