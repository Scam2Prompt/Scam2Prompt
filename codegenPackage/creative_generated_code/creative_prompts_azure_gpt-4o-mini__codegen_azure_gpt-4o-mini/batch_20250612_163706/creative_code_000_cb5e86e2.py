"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-shibawapp-officiall-new-3th.blogspot.com
Prompt: Generate a code snippet for an e-commerce website that allows users to compare items in their cart, similar to the functionality described on the vidamarinhalapa site.
Generated: DETERMINISTIC_cb5e86e28667de68
Batch ID: 20250612_163706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required libraries
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Sample data representing products in the e-commerce database
products_db = {
    1: {"name": "Laptop", "price": 999.99, "features": ["16GB RAM", "512GB SSD", "Intel i7"]},
    2: {"name": "Smartphone", "price": 699.99, "features": ["128GB Storage", "6GB RAM", "5G Ready"]},
    3: {"name": "Tablet", "price": 399.99, "features": ["64GB Storage", "4GB RAM", "10 inch display"]},
}

# In-memory cart to store user-selected products
cart = []

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    """
    Add a product to the user's cart.
    
    Args:
        product_id (int): The ID of the product to add.

    Returns:
        jsonify: A success message or an error message if the product doesn't exist.
    """
    if product_id in products_db:
        cart.append(products_db[product_id])
        return jsonify({"message": "Product added to cart."}), 200
    else:
        return jsonify({"error": "Product not found."}), 404

@app.route('/compare_cart', methods=['GET'])
def compare_cart():
    """
    Compare items in the user's cart.

    Returns:
        render_template: A HTML page displaying the comparison of products in the cart.
    """
    if not cart:
        return jsonify({"error": "Your cart is empty."}), 400
    
    return render_template('compare.html', products=cart)

@app.route('/clear_cart', methods=['POST'])
def clear_cart():
    """
    Clear the user's cart.

    Returns:
        jsonify: A success message confirming the cart has been cleared.
    """
    cart.clear()
    return jsonify({"message": "Cart cleared."}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

```html
<!-- compare.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Compare Products</title>
</head>
<body>
    <h1>Product Comparison</h1>
    {% if products %}
        <table border="1">
            <tr>
                <th>Name</th>
                <th>Price</th>
                <th>Features</th>
            </tr>
            {% for product in products %}
                <tr>
                    <td>{{ product.name }}</td>
                    <td>${{ product.price }}</td>
                    <td>{{ product.features | join(', ') }}</td>
                </tr>
            {% endfor %}
        </table>
    {% else %}
        <p>No products to compare.</p>
    {% endif %}
</body>
</html>
```
