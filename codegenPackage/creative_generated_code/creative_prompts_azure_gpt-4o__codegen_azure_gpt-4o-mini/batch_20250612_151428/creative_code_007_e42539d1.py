"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marant.com.mx
Prompt: Develop a REST API endpoint for querying Marant's "Magical Prenatal Peel" product details, including its benefits for unifying skin texture and treating cloasma.
Generated: DETERMINISTIC_e42539d127453089
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import NotFound, BadRequest

app = Flask(__name__)

# Sample product data
products = {
    "magical_prenatal_peel": {
        "name": "Magical Prenatal Peel",
        "benefits": [
            "Unifies skin texture",
            "Treats cloasma",
            "Enhances skin radiance",
            "Reduces pigmentation"
        ],
        "description": "A specially formulated peel for prenatal care that helps improve skin appearance."
    }
}

@app.route('/api/products/<product_id>', methods=['GET'])
def get_product(product_id):
    """
    Retrieve product details by product ID.

    Parameters:
        product_id (str): The unique identifier for the product.

    Returns:
        JSON response with product details or error message.
    """
    try:
        # Validate the product_id
        if product_id not in products:
            raise NotFound(f"Product with ID '{product_id}' not found.")

        product = products[product_id]
        return jsonify(product), 200

    except NotFound as e:
        # Handle not found error
        return jsonify({"error": str(e)}), 404

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
