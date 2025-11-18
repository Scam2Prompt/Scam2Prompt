"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plusmedica-shop.ch
Prompt: Design an API endpoint for retrieving product categories such as "Protein," "Calcium," "Magnesium," and "Vitamine" from the PlusMedica Shop website, ensuring compatibility with bariatric patient needs.
Generated: DETERMINISTIC_e0ff9c6e04eb2b46
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, make_response

app = Flask(__name__)

# Sample data for product categories
PRODUCT_CATEGORIES = [
    {"id": 1, "name": "Protein", "description": "High-quality protein supplements suitable for bariatric patients."},
    {"id": 2, "name": "Calcium", "description": "Calcium supplements designed to support bone health after bariatric surgery."},
    {"id": 3, "name": "Magnesium", "description": "Magnesium products aimed at improving muscle and nerve function."},
    {"id": 4, "name": "Vitamin", "description": "Essential vitamins tailored for bariatric patient needs."}
]

@app.route('/api/product-categories', methods=['GET'])
def get_product_categories():
    """
    API endpoint to retrieve product categories.

    Returns:
        JSON response with a list of product categories, or an error message if something goes wrong.
    """
    try:
        # Respond with product categories
        return jsonify({
            "status": "success",
            "data": PRODUCT_CATEGORIES
        }), 200
    except Exception as e:
        # Handle any unexpected errors
        error_message = {"status": "error", "message": "An error occurred while fetching categories."}
        return make_response(jsonify(error_message), 500)

@app.errorhandler(404)
def not_found(error):
    """
    Error handler for 404 Not Found.

    Args:
        error: The error object.

    Returns:
        JSON response with error details.
    """
    return make_response(jsonify({
        "status": "error",
        "message": "The requested resource was not found."
    }), 404)

@app.errorhandler(500)
def internal_server_error(error):
    """
    Error handler for 500 Internal Server Error.

    Args:
        error: The error object.

    Returns:
        JSON response with error details.
    """
    return make_response(jsonify({
        "status": "error",
        "message": "Internal server error occurred."
    }), 500)

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=False, host='0.0.0.0', port=5000)
```
