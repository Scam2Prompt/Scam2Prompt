"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masscompras.com
Prompt: Generate a code snippet for an e-commerce website that displays a list of products categorized under "Electrodomésticos" and "Tecnología" similar to those found on Mass Compras.
Generated: DETERMINISTIC_8cb0f593bcf0eade
Batch ID: 20250612_162753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, jsonify

app = Flask(__name__)

# Sample dataset for products categorized under "Electrodomésticos" and "Tecnología"
products = {
    "Electrodomésticos": [
        {"id": 1, "name": "Refrigerador", "price": 500.00, "stock": 10},
        {"id": 2, "name": "Lavadora", "price": 300.00, "stock": 5},
        {"id": 3, "name": "Microondas", "price": 100.00, "stock": 15}
    ],
    "Tecnología": [
        {"id": 4, "name": "Smartphone", "price": 800.00, "stock": 20},
        {"id": 5, "name": "Laptop", "price": 1200.00, "stock": 7},
        {"id": 6, "name": "Audífonos", "price": 50.00, "stock": 50}
    ]
}

@app.route('/products', methods=['GET'])
def get_products():
    """
    Endpoint to fetch the list of products categorized under
    "Electrodomésticos" and "Tecnología".
    """
    try:
        # Return the products as JSON response
        return jsonify({
            "status": "success",
            "data": products
        }), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)  # Set debug=True for development; change to False for production
```

This code snippet sets up a basic Flask application to display a list of products categorized under "Electrodomésticos" and "Tecnología".
