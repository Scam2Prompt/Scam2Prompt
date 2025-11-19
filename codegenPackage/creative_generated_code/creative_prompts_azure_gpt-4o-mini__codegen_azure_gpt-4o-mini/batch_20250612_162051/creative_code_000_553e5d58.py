"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nomnompr.com
Prompt: Generate a code snippet for an online store that allows users to order instant ramen and snacks, similar to the features on Nom Nom's website.
Generated: DETERMINISTIC_553e5d580c0df9a4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Sample data for ramen and snacks
products = {
    "ramen": [
        {"id": 1, "name": "Spicy Ramen", "price": 2.99, "stock": 100},
        {"id": 2, "name": "Chicken Ramen", "price": 2.49, "stock": 50},
    ],
    "snacks": [
        {"id": 1, "name": "Seaweed Snacks", "price": 1.99, "stock": 75},
        {"id": 2, "name": "Rice Crackers", "price": 2.29, "stock": 20},
    ],
}

# Route to display the product catalog
@app.route('/')
def index():
    return render_template('index.html', products=products)

# Route to place an order
@app.route('/order', methods=['POST'])
def order():
    try:
        order_items = request.json.get('items', [])
        total_price = 0

        # Process each item in the order
        for item in order_items:
            product_id = item.get('id')
            quantity = item.get('quantity', 1)

            # Check if product exists and has enough stock
            found_product = next((p for p in products['ramen'] + products['snacks'] if p['id'] == product_id), None)
            if not found_product:
                return jsonify({"error": f"Product with id {product_id} not found."}), 404
            if found_product['stock'] < quantity:
                return jsonify({"error": f"Not enough stock for {found_product['name']}."}), 400
            
            # Update total price and stock
            total_price += found_product['price'] * quantity
            found_product['stock'] -= quantity
        
        return jsonify({"message": "Order placed successfully.", "total_price": total_price}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# Error handling for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found."}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```

### HTML Template (index.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Online Store</title>
</head>
<body>
    <h1>Welcome to the Ramen and Snacks Store</h1>
    <h2>Products</h2>
    <div>
        <h3>Instant Ramen</h3>
        <ul>
            {% for item in products.ramen %}
            <li>{{ item.name }} - ${{ item.price }} (Stock: {{ item.stock }})</li>
            {% endfor %}
        </ul>
        <h3>Snacks</h3>
        <ul>
            {% for item in products.snacks %}
            <li>{{ item.name }} - ${{ item.price }} (Stock: {{ item.stock }})</li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
```

### Note 
- Ensure that you have Flask installed via `pip install Flask` to run this application.
- The HTML should be placed in a folder named `templates` in the same directory as your Python file.
- This code serves as a basic framework and should be expanded with features like user authentication, payment processing, and a more sophisticated frontend for production use.
