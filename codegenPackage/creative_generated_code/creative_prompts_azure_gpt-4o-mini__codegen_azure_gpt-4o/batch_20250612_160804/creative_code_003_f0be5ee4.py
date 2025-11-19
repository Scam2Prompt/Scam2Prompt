"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ccjourney.co
Prompt: Develop an API endpoint for retrieving product categories such as Gym/Yoga and Enchanted Forest from an online clothing store like Capsule Cosmic Journey.
Generated: DETERMINISTIC_f0be5ee4110434ec
Batch ID: 20250612_160804
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

# Configure logging for debugging and production monitoring
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Mock data for product categories
PRODUCT_CATEGORIES = [
    {"id": 1, "name": "Gym/Yoga", "description": "Activewear for gym and yoga enthusiasts."},
    {"id": 2, "name": "Enchanted Forest", "description": "Mystical clothing inspired by nature."},
    {"id": 3, "name": "Casual Chic", "description": "Stylish everyday wear."},
    {"id": 4, "name": "Vintage Vibes", "description": "Retro-inspired clothing."},
]

@app.route('/api/categories', methods=['GET'])
def get_categories():
    """
    API endpoint to retrieve all product categories.

    Returns:
        JSON response containing a list of product categories.
    """
    try:
        # Log the incoming request
        logging.info("GET /api/categories - Request received")
        
        # Return the categories as a JSON response
        response = jsonify({"categories": PRODUCT_CATEGORIES})
        response.status_code = 200
        return response

    except Exception as e:
        # Handle unexpected errors and log them
        logging.error(f"Error occurred while retrieving categories: {str(e)}")
        response = jsonify({"error": "An unexpected error occurred."})
        response.status_code = 500
        return response

# Error handler for 404 - Route not found
@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors (route not found).

    Returns:
        JSON response indicating the resource was not found.
    """
    logging.warning("404 error - Route not found")
    response = jsonify({"error": "Resource not found"})
    response.status_code = 404
    return response

# Error handler for 405 - Method not allowed
@app.errorhandler(405)
def method_not_allowed(error):
    """
    Handle 405 errors (method not allowed).

    Returns:
        JSON response indicating the method is not allowed.
    """
    logging.warning("405 error - Method not allowed")
    response = jsonify({"error": "Method not allowed"})
    response.status_code = 405
    return response

# Application entry point
if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False, host='0.0.0.0', port=5000)
```
