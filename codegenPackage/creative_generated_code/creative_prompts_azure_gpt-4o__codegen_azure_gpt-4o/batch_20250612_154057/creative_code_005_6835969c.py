"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://garmin-boutique.com
Prompt: Suggest a library or API to manage product categories (e.g., Fenix, Forerunner, Instinct) and implement a search functionality for Garmin watches based on features like "Sapphire Solar Edition" or "music-enabled."
Generated: DETERMINISTIC_6835969c16d4d398
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from flask import Flask, request, jsonify
from collections import defaultdict

# Initialize the Flask application
app = Flask(__name__)

# Data structure to store product categories and their features
class ProductCategoryManager:
    def __init__(self):
        # Dictionary to hold categories and their products
        self.categories = defaultdict(list)
    
    def add_product(self, category, product_name, features):
        """
        Adds a product to a category along with its features.
        :param category: The category name (e.g., "Fenix")
        :param product_name: The product name (e.g., "Fenix 7X Sapphire Solar Edition")
        :param features: A list of features (e.g., ["Sapphire Solar Edition", "music-enabled"])
        """
        product = {
            "name": product_name,
            "features": features
        }
        self.categories[category].append(product)
    
    def search_products(self, feature_query):
        """
        Searches for products across all categories by feature.
        :param feature_query: The feature to search for (e.g., "Sapphire Solar Edition")
        :return: List of products matching the feature
        """
        results = []
        for category, products in self.categories.items():
            for product in products:
                if feature_query.lower() in map(str.lower, product["features"]):
                    results.append({
                        "category": category,
                        "product_name": product["name"]
                    })
        return results

# Instantiate the product category manager
product_manager = ProductCategoryManager()

# Add some example products (this could be replaced by database entries in production)
product_manager.add_product("Fenix", "Fenix 7X Sapphire Solar Edition", ["Sapphire Solar Edition", "music-enabled"])
product_manager.add_product("Forerunner", "Forerunner 945 Music", ["music-enabled", "advanced running dynamics"])
product_manager.add_product("Instinct", "Instinct Solar Tactical Edition", ["solar-powered", "military-grade durability"])

@app.route('/search', methods=['GET'])
def search_products():
    """
    Endpoint to search for products by feature.
    Example: /search?feature=music-enabled
    :return: JSON response with matching products
    """
    feature_query = request.args.get('feature')
    if not feature_query:
        return jsonify({"error": "Feature query parameter is required"}), 400

    try:
        results = product_manager.search_products(feature_query)
        return jsonify({"results": results}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/add-product', methods=['POST'])
def add_product():
    """
    Endpoint to add a new product to a category.
    Example JSON payload:
    {
        "category": "Fenix",
        "product_name": "Fenix 7 Pro",
        "features": ["pro-grade mapping", "music-enabled"]
    }
    :return: Success or error message
    """
    data = request.json
    category = data.get('category')
    product_name = data.get('product_name')
    features = data.get('features')

    if not category or not product_name or not features:
        return jsonify({"error": "Category, product_name, and features are required"}), 400

    try:
        product_manager.add_product(category, product_name, features)
        return jsonify({"message": "Product added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
```
