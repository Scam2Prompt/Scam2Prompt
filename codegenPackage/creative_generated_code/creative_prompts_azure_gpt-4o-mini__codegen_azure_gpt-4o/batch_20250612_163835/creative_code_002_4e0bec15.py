"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engeloutdoors.com
Prompt: Create an API endpoint that retrieves Engel Coolers product details, including specifications for hard and soft coolers.
Generated: DETERMINISTIC_4e0bec15fb933231
Batch ID: 20250612_163835
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

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Mock data for Engel Coolers products
PRODUCTS = {
    "hard_coolers": [
        {"id": 1, "name": "Engel DeepBlue 65", "capacity": "65 Quart", "material": "Roto-molded plastic", "price": 299.99},
        {"id": 2, "name": "Engel DeepBlue 85", "capacity": "85 Quart", "material": "Roto-molded plastic", "price": 349.99}
    ],
    "soft_coolers": [
        {"id": 1, "name": "Engel HD30", "capacity": "30 Quart", "material": "Soft-sided fabric", "price": 199.99},
        {"id": 2, "name": "Engel HD20", "capacity": "20 Quart", "material": "Soft-sided fabric", "price": 159.99}
    ]
}

@app.route('/api/engel-coolers/products', methods=['GET'])
def get_engel_coolers_products():
    """
    API endpoint to retrieve Engel Coolers product details.
    Returns:
        JSON response with product details for hard and soft coolers.
    """
    try:
        logger.info("Fetching Engel Coolers product details.")
        return jsonify({
            "hard_coolers": PRODUCTS["hard_coolers"],
            "soft_coolers": PRODUCTS["soft_coolers"]
        }), 200
    except Exception as e:
        logger.error(f"An error occurred while fetching product details: {str(e)}")
        return jsonify({"error": "Failed to retrieve product details"}), 500

@app.errorhandler(404)
def handle_404_error(error):
    """
    Handle 404 errors for undefined routes.
    """
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def handle_500_error(error):
    """
    Handle 500 errors for server issues.
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)  # Set debug=False for production
```
