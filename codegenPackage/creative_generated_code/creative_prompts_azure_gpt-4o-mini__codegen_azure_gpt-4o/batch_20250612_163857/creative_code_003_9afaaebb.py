"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flaviadossantos.co
Prompt: Create a RESTful API endpoint to fetch product information for the "Disney / Pixar's Soul Men's NY Jazz Night Logo Tee."
Generated: DETERMINISTIC_9afaaebbe331198e
Batch ID: 20250612_163857
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

app = Flask(__name__)

# Logging configuration for production-ready error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# In-memory data store simulating a database
PRODUCTS = {
    "soul_mens_jazz_tee": {
        "id": "soul_mens_jazz_tee",
        "name": "Disney / Pixar's Soul Men's NY Jazz Night Logo Tee",
        "description": "A stylish tee inspired by Disney / Pixar's Soul movie, featuring New York Jazz Night logo design.",
        "price": 25.99,
        "available_sizes": ["S", "M", "L", "XL"],
        "in_stock": True
    }
}

@app.route('/api/products/<product_id>', methods=['GET'])
def get_product(product_id):
    """
    Fetch product information by product ID.
    
    :param product_id: ID of the product to retrieve.
    :return: JSON response containing product details or error message.
    """
    try:
        # Check if the requested product exists in the data store
        product = PRODUCTS.get(product_id)
        if product:
            return jsonify(product), 200  # Return product data with HTTP 200 OK status
        else:
            # If product not found, return 404 Not Found
            logging.warning(f"Product with ID '{product_id}' not found.")
            return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        # Handle unexpected server errors
        logging.error(f"An error occurred while fetching product with ID '{product_id}': {e}")
        return jsonify({"error": "Internal server error"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```
