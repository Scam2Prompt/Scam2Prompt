"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamnhuavietkhanh.com
Prompt: Develop a REST API endpoint to retrieve installation guides for Ecoplast and Casary products, categorized by product type.
Generated: DETERMINISTIC_b278636874cc2403
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for installation guides
installation_guides = {
    "Ecoplast": {
        "type1": "Ecoplast Type1 Installation Guide.pdf",
        "type2": "Ecoplast Type2 Installation Guide.pdf",
    },
    "Casary": {
        "type1": "Casary Type1 Installation Guide.pdf",
        "type2": "Casary Type2 Installation Guide.pdf",
    },
}

# Error response structure
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

@app.route('/guides/<product_name>', methods=['GET'])
def get_installation_guides(product_name):
    """
    REST API endpoint to retrieve installation guides for the specified product.
    Args:
        product_name (str): Name of the product (e.g., Ecoplast, Casary).
    Query Parameters:
        type (str): Specific product type (optional).

    Returns:
        JSON response containing installation guide(s) or an error message.
    """
    try:
        # Validate product name
        if product_name not in installation_guides:
            return error_response(f"Product '{product_name}' not found.", 404)

        # Retrieve query parameter for product type
        product_type = request.args.get('type')

        # If product type is specified, return its corresponding guide
        if product_type:
            guides = installation_guides[product_name]
            if product_type in guides:
                return jsonify({"product": product_name, "type": product_type, "guide": guides[product_type]})
            else:
                return error_response(f"Guide for product type '{product_type}' not found.", 404)
        
        # If no type specified, return all guides for the product
        return jsonify({"product": product_name, "guides": installation_guides[product_name]})

    except Exception as e:
        # Catch unexpected errors and return a generic error response
        return error_response(f"An error occurred: {str(e)}", 500)

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
