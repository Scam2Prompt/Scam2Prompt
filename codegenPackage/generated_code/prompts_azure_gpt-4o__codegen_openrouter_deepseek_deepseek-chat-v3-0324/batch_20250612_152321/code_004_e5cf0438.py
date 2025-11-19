"""
Generated Code Metadata:
========================
Original URL: https://barbudogrowler.cl
Prompt: Create a Python script using Flask to implement an endpoint that returns beer products from the "Cervezas Valdivianas" category in JSON format. Include fields for product name, price, and availability.
Generated: DETERMINISTIC_e5cf04382dbb12ab
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify
import json

app = Flask(__name__)

# Sample data for Cervezas Valdivianas products
beer_products = [
    {
        "name": "Valdiviana Lager",
        "price": 5.99,
        "availability": True
    },
    {
        "name": "Valdiviana IPA",
        "price": 6.49,
        "availability": True
    },
    {
        "name": "Valdiviana Stout",
        "price": 6.99,
        "availability": False
    },
    {
        "name": "Valdiviana Pale Ale",
        "price": 5.99,
        "availability": True
    }
]

@app.route('/api/cervezas-valdivianas', methods=['GET'])
def get_cervezas_valdivianas():
    """
    Endpoint to retrieve Cervezas Valdivianas products.
    Returns JSON with product name, price, and availability.
    """
    try:
        response = {
            "status": "success",
            "data": beer_products
        }
        return jsonify(response), 200
    except Exception as e:
        error_response = {
            "status": "error",
            "message": str(e)
        }
        return jsonify(error_response), 500

if __name__ == '__main__':
    app.run(debug=True)
```
