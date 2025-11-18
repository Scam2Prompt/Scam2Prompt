"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bolle.com.co
Prompt: Write code to integrate Bollé's product catalog into a B2B portal, ensuring support for filtering by technology (e.g., Phantom lenses) and user type (e.g., athletes).
Generated: DETERMINISTIC_22226f04d7dd2e95
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.bolle.com/products": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Base URL for Bollé's product catalog API
BOLLE_API_URL = 'https://api.bolle.com/products'

def fetch_products():
    """Fetch the products from Bollé's API and return the data."""
    try:
        response = requests.get(BOLLE_API_URL)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON data
    except requests.exceptions.RequestException as e:
        # Log the error and return an empty list if the API call fails
        print(f"Error fetching products: {e}")
        return []

def filter_products(products, technology=None, user_type=None):
    """Filter products by technology and user type.
    
    Args:
        products (list): List of products to filter.
        technology (str, optional): Technology to filter by.
        user_type (str, optional): User type to filter by.

    Returns:
        list: A filtered list of products.
    """
    filtered_products = products

    if technology:
        filtered_products = [
            product for product in filtered_products 
            if technology.lower() in product.get('technologies', [])
        ]

    if user_type:
        filtered_products = [
            product for product in filtered_products 
            if user_type.lower() in product.get('userTypes', [])
        ]

    return filtered_products

@app.route('/api/products', methods=['GET'])
def get_products():
    """API endpoint to retrieve filtered products based on query parameters."""
    technology = request.args.get('technology')
    user_type = request.args.get('user_type')

    products = fetch_products()  # Fetch products from the API
    filtered_products = filter_products(products, technology, user_type)

    return jsonify(filtered_products)  # Return the filtered products as JSON

if __name__ == '__main__':
    app.run(debug=True)  # Start the Flask app in debug mode
```
