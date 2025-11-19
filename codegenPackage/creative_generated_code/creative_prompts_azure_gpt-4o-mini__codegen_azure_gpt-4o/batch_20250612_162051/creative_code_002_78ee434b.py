"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.matinshop.dk
Prompt: Create an API endpoint that allows users to search for men's grooming products, specifically focusing on natural ingredients like jojoba and argan oil as highlighted on Matin Shop.
Generated: DETERMINISTIC_78ee434b398ba4dd
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

# Initialize Flask app
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Sample database of products (In production, this would come from a proper database)
PRODUCTS = [
    {"id": 1, "name": "Jojoba Beard Oil", "ingredients": ["jojoba oil", "vitamin E", "argan oil"], "price": 20.99},
    {"id": 2, "name": "Natural Hair Serum", "ingredients": ["argan oil", "coconut oil"], "price": 15.99},
    {"id": 3, "name": "Organic Face Cream", "ingredients": ["shea butter", "jojoba oil"], "price": 25.99},
    {"id": 4, "name": "Non-Natural Shaving Gel", "ingredients": ["synthetic chemicals"], "price": 10.99},
]

@app.route('/api/search', methods=['GET'])
def search_products():
    """
    Endpoint to search for men's grooming products based on natural ingredients.
    Users can filter products containing specific natural ingredients like jojoba oil or argan oil.
    ---
    URL Parameters:
    - ingredient: (optional) Name of the ingredient to filter. Example: 'jojoba'
    
    Returns:
    - JSON response with filtered product list or error message.
    """
    try:
        # Get query parameter 'ingredient'
        ingredient = request.args.get('ingredient', '').lower()

        if not ingredient:
            return jsonify({
                "success": False,
                "message": "No ingredient provided. Please specify an ingredient to search for."
            }), 400

        # Filter products containing the specified ingredient
        filtered_products = [
            product for product in PRODUCTS 
            if any(ingredient in ing.lower() for ing in product['ingredients'])
        ]

        if not filtered_products:
            return jsonify({
                "success": True,
                "message": f"No products found containing the ingredient: {ingredient}.",
                "products": []
            }), 200

        return jsonify({
            "success": True,
            "message": f"Products containing the ingredient: {ingredient}.",
            "products": filtered_products
        }), 200

    except Exception as e:
        # Log error and return generic error response
        logging.error(f"An error occurred while searching for products: {str(e)}")
        return jsonify({
            "success": False,
            "message": "An internal error occurred. Please try again later."
        }), 500

# Define app entry point
if __name__ == '__main__':
    # Run Flask app in debug mode for development (disable debug in production)
    app.run(debug=True)
```
