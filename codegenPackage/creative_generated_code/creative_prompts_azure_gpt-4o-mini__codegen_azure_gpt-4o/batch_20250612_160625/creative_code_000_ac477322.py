"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tkshop6.shop
Prompt: Generate a code snippet for handling error responses in a shopping API, specifically for the error code 10005.
Generated: DETERMINISTIC_ac47732217f2f149
Batch ID: 20250612_160625
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

# Error handler for the shopping API
@app.errorhandler(10005)
def handle_error_10005(e):
    """
    Handle error with code 10005.
    Error code 10005 indicates an invalid product ID in the shopping API.
    Returns a JSON response with appropriate error details.
    """
    error_response = {
        "error_code": 10005,
        "message": "Invalid Product ID",
        "details": "The product ID provided does not exist in the catalog. Please check the ID and try again."
    }
    return jsonify(error_response), 400

@app.route('/product/<product_id>', methods=['GET'])
def get_product(product_id):
    """
    Sample endpoint to fetch product details given a product ID.
    In this example, we assume that valid product IDs are numeric strings.
    """
    try:
        # Simulate product ID validation
        if not product_id.isdigit():
            raise ValueError("Invalid Product ID")
        
        # Simulate product lookup in the database (mocked for this example)
        mock_database = {"101": {"name": "Laptop", "price": 1500}, "102": {"name": "Phone", "price": 800}}
        
        # Fetch product details from the mock database
        product = mock_database.get(product_id)
        if not product:
            raise Exception("Product not found")  # Trigger the custom error handler
        
        # Return product details as JSON response
        return jsonify({"product_id": product_id, **product}), 200
    
    except ValueError:
        # Raise custom error code 10005 for invalid product ID
        return handle_error_10005(Exception("Invalid Product ID"))

    except Exception as ex:
        # Generic error response
        return jsonify({"error_code": 10000, "message": str(ex)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
