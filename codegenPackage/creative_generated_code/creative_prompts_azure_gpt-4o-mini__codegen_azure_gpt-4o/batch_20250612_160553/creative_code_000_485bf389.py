"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cymrepuestos.com.ar
Prompt: Generate a code snippet for an API that retrieves a list of automotive spare parts available at CYM Repuestos, including details like product type, brand, and pricing.
Generated: DETERMINISTIC_485bf389b6c8f1ed
Batch ID: 20250612_160553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data representing spare parts at CYM Repuestos
SPARE_PARTS = [
    {"id": 1, "product_type": "Brake Pads", "brand": "Bosch", "price": 45.99},
    {"id": 2, "product_type": "Oil Filter", "brand": "MANN", "price": 12.49},
    {"id": 3, "product_type": "Spark Plug", "brand": "NGK", "price": 8.99},
    {"id": 4, "product_type": "Battery", "brand": "ACDelco", "price": 85.00},
]

@app.route('/api/spare-parts', methods=['GET'])
def get_spare_parts():
    """
    Endpoint to retrieve the list of automotive spare parts available at CYM Repuestos.
    Returns:
        JSON response containing a list of spare parts.
    """
    # Optionally filter results based on query parameters
    product_type = request.args.get('product_type')
    brand = request.args.get('brand')

    filtered_parts = SPARE_PARTS

    if product_type:
        filtered_parts = [part for part in filtered_parts if part["product_type"].lower() == product_type.lower()]
    if brand:
        filtered_parts = [part for part in filtered_parts if part["brand"].lower() == brand.lower()]

    return jsonify(filtered_parts), 200


@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Error handler for HTTP exceptions.
    Returns:
        JSON response with error details.
    """
    response = {
        "error": {
            "code": e.code,
            "message": e.description
        }
    }
    return jsonify(response), e.code


@app.errorhandler(Exception)
def handle_general_exception(e):
    """
    Generic error handler for unexpected exceptions.
    Returns:
        JSON response with error details.
    """
    response = {
        "error": {
            "code": 500,
            "message": "An unexpected error occurred."
        }
    }
    return jsonify(response), 500


if __name__ == '__main__':
    # Run the Flask application on localhost, port 5000
    app.run(debug=True)
```
