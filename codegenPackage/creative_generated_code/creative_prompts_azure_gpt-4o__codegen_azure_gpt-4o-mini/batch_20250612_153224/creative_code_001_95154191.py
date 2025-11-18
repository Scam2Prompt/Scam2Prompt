"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emareels.se
Prompt: Recommend an API or library to create a product catalog for fishing reels, including features like "Old School Brass 1 & 2" and "Salmon Wide," as described on Emanuelson Reels.
Generated: DETERMINISTIC_951541910d4ba33c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# In-memory database to store the product catalog
product_catalog = []

class Product:
    """Class to represent a fishing reel product."""
    
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def to_dict(self):
        """Convert the product instance to a dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price
        }

@app.route('/products', methods=['GET'])
def get_products():
    """Retrieve the entire product catalog."""
    try:
        return jsonify([product.to_dict() for product in product_catalog]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/products', methods=['POST'])
def add_product():
    """Add a new product to the catalog."""
    try:
        data = request.json
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')

        # Validate input
        if not name or not description or not isinstance(price, (int, float)):
            return jsonify({"error": "Invalid input"}), 400
        
        new_product = Product(name, description, price)
        product_catalog.append(new_product)

        return jsonify(new_product.to_dict()), 201
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON data"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/products/<string:name>', methods=['DELETE'])
def delete_product(name):
    """Delete a product from the catalog by name."""
    try:
        global product_catalog
        product_catalog = [product for product in product_catalog if product.name != name]
        
        return jsonify({"message": "Product deleted"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Additional Information
- This code creates a simple REST API using Flask for managing a product catalog.
- The API supports adding, retrieving, and deleting fishing reel products.
- Input validation and error handling are implemented to ensure robustness.
- The application runs in debug mode for development purposes; remember to disable it in production.
