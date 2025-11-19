"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tiburonfishingreels.com
Prompt: Create an API endpoint that retrieves product details for Tiburon fishing reels, including frame conversions and spool kits.
Generated: DETERMINISTIC_cee50457f076f4d3
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure logging for better debugging and production readiness
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock database of Tiburon fishing reels and related products
PRODUCTS_DB = {
    "reels": [
        {"id": 1, "name": "Tiburon SST 20", "description": "High-performance reel", "price": 299.99},
        {"id": 2, "name": "Tiburon SST 30", "description": "Durable reel for big catches", "price": 349.99},
    ],
    "frame_conversions": [
        {"id": 101, "reel_id": 1, "name": "Frame Conversion Kit SST 20", "price": 49.99},
        {"id": 102, "reel_id": 2, "name": "Frame Conversion Kit SST 30", "price": 59.99},
    ],
    "spool_kits": [
        {"id": 201, "reel_id": 1, "name": "Spool Kit SST 20", "price": 29.99},
        {"id": 202, "reel_id": 2, "name": "Spool Kit SST 30", "price": 39.99},
    ]
}

@app.route('/api/products/<string:product_type>', methods=['GET'])
def get_products(product_type):
    """
    API endpoint to retrieve product details for Tiburon fishing reels and related products.
    :param product_type: Type of product to retrieve (e.g., reels, frame_conversions, spool_kits)
    :return: JSON response with product details or an error message
    """
    try:
        # Validate product type
        if product_type not in PRODUCTS_DB:
            logging.warning(f"Invalid product type requested: {product_type}")
            return jsonify({"error": f"Invalid product type '{product_type}'. Valid types are: {list(PRODUCTS_DB.keys())}"}), 400

        # Retrieve product data from the mock database
        products = PRODUCTS_DB[product_type]
        logging.info(f"Successfully retrieved {len(products)} items for product type '{product_type}'")
        return jsonify({"products": products}), 200
    
    except Exception as e:
        # Log and return any unexpected server errors
        logging.error(f"An error occurred while retrieving products: {str(e)}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Debug mode is enabled for development purposes
```
