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
from werkzeug.exceptions import NotFound, BadRequest

app = Flask(__name__)

# Sample product data
PRODUCTS = {
    "soul_ny_jazz_tee": {
        "id": "soul_ny_jazz_tee",
        "name": "Disney / Pixar's Soul Men's NY Jazz Night Logo Tee",
        "description": "A stylish tee featuring the iconic NY Jazz Night logo from Disney / Pixar's Soul.",
        "price": 24.99,
        "stock": 100,
        "category": "Clothing"
    }
}

@app.route('/api/products/<product_id>', methods=['GET'])
def get_product(product_id):
    """
    Fetch product information by product_id.

    Args:
        product_id (str): The unique identifier for the product.

    Returns:
        JSON response containing product information or an error message.
    """
    # Validate product_id
    if not product_id:
        raise BadRequest("Product ID cannot be empty.")

    # Fetch the product from the PRODUCTS dictionary
    product = PRODUCTS.get(product_id)

    if not product:
        raise NotFound(f"Product with ID '{product_id}' not found.")

    # Return product information as JSON
    return jsonify(product)

@app.errorhandler(NotFound)
def handle_not_found(error):
    """Handle 404 Not Found errors."""
    response = jsonify({"error": str(error)})
    response.status_code = 404
    return response

@app.errorhandler(BadRequest)
def handle_bad_request(error):
    """Handle 400 Bad Request errors."""
    response = jsonify({"error": str(error)})
    response.status_code = 400
    return response

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
Make sure to install Flask if you haven't already, by running:
```bash
pip install Flask
```
To run the application, save this code to a file (e.g., `app.py`), and execute:
```bash
python app.py
```
