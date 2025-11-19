"""
Generated Code Metadata:
========================
Original URL: https://foiegras-badaud-sarlat.fr
Prompt: Develop a code sample that displays a list of products with their prices, specifically focusing on the foie gras d'oie and canard from the Périgord region.
Generated: DETERMINISTIC_cbf9e670f21e73e2
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Sample data for products
products = [
    {
        "id": 1,
        "name": "Foie Gras d'Oie",
        "region": "Périgord",
        "price": 75.00
    },
    {
        "id": 2,
        "name": "Foie Gras de Canard",
        "region": "Périgord",
        "price": 65.00
    },
    {
        "id": 3,
        "name": "Other Product",
        "region": "Other Region",
        "price": 50.00
    }
]

@app.route('/products', methods=['GET'])
def get_products():
    """
    Retrieve a list of products from the Périgord region.
    
    Returns:
        JSON response containing a list of products with their prices.
    """
    try:
        # Filter products to only include those from the Périgord region
        perigord_products = [
            product for product in products if product['region'] == 'Périgord'
        ]
        
        # Check if any products were found
        if not perigord_products:
            return jsonify({"message": "No products found in the Périgord region."}), 404
        
        # Return the filtered list of products
        return jsonify(perigord_products), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
