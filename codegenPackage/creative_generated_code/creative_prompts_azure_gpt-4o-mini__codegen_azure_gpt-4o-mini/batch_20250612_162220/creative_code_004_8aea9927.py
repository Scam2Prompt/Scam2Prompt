"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mannamarkets.com
Prompt: Suggest a framework for building a vending machine application that showcases the unique benefits of Manna Markets, such as accessibility and diverse product options.
Generated: DETERMINISTIC_8aea99270a698966
Batch ID: 20250612_162220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# vending_machine.py

from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data structure to represent products in the vending machine.
products = [
    {'id': 1, 'name': 'Organic Almonds', 'price': 2.50, 'category': 'snack'},
    {'id': 2, 'name': 'Vegan Protein Bar', 'price': 1.99, 'category': 'snack'},
    {'id': 3, 'name': 'Gluten-Free Chips', 'price': 2.00, 'category': 'snack'},
    {'id': 4, 'name': 'Fruit Infused Water', 'price': 1.50, 'category': 'beverage'},
    {'id': 5, 'name': 'Herbal Tea', 'price': 1.20, 'category': 'beverage'},
]

@app.route('/products', methods=['GET'])
def get_products():
    """Fetch all available products."""
    return jsonify(products), 200

@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Fetch a specific product by its ID."""
    product = next((item for item in products if item['id'] == product_id), None)
    if product is not None:
        return jsonify(product), 200
    else:
        return jsonify({"error": "Product not found"}), 404

@app.route('/purchase', methods=['POST'])
def purchase_product():
    """Purchase a product by its ID and return a confirmation."""
    data = request.get_json()
    product_id = data.get('product_id')
    
    product = next((item for item in products if item['id'] == product_id), None)
    
    if product:
        # Simulate a purchase logic here (e.g., payment processing)
        return jsonify({"message": f"You have purchased {product['name']} for ${product['price']:.2f}."}), 200
    else:
        return jsonify({"error": "Product not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors."""
    return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"An error occurred while starting the application: {e}")
```
