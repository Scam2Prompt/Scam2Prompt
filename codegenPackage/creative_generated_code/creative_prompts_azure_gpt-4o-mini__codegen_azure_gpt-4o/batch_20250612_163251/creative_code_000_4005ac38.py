"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maderaselaboradas.com.ar
Prompt: Generate a code snippet for a web application that allows users to order wooden products, specifically focusing on the features of "Maderas Aserradas" and "Cabos" as described on the Maderas Elaboradas website.
Generated: DETERMINISTIC_4005ac386d548f17
Batch ID: 20250612_163251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Mock data for wooden products
PRODUCTS = {
    "maderas_aserradas": [
        {"id": 1, "name": "Cedar Plank", "price": 25.0, "description": "High-quality cedar plank for diverse uses."},
        {"id": 2, "name": "Oak Beam", "price": 40.0, "description": "Durable oak beam, perfect for construction."},
    ],
    "cabos": [
        {"id": 1, "name": "Wooden Handle", "price": 10.0, "description": "Smooth wooden handle for tools or crafts."},
        {"id": 2, "name": "Broomstick", "price": 15.0, "description": "Sturdy wooden broomstick for household use."},
    ],
}

# Home route
@app.route("/")
def home():
    """
    Displays the home page with product categories.
    """
    return render_template("index.html", categories=PRODUCTS.keys())

# Route to display products within a specific category
@app.route("/category/<category>")
def category(category):
    """
    Displays products for a given category (e.g., 'maderas_aserradas' or 'cabos').
    """
    if category not in PRODUCTS:
        return jsonify({"error": "Category not found"}), 404
    return render_template("category.html", products=PRODUCTS[category], category_name=category)

# Route to place an order for a specific product
@app.route("/order", methods=["POST"])
def order_product():
    """
    Handles the placement of an order for a specific product.
    """
    try:
        data = request.json
        product_id = data.get("product_id")
        category = data.get("category")
        
        # Validate input
        if not category or category not in PRODUCTS:
            return jsonify({"error": "Invalid category"}), 400
        if not product_id:
            return jsonify({"error": "Product ID is required"}), 400

        # Find product
        product = next((p for p in PRODUCTS[category] if p["id"] == product_id), None)
        if not product:
            return jsonify({"error": "Product not found"}), 404
        
        return jsonify({"message": "Order placed successfully!", "product": product}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
```

### File: `templates/index.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Wooden Products</title>
</head>
<body>
    <h1>Welcome to Wooden Products!</h1>
    <h2>Categories</h2>
    <ul>
        {% for category in categories %}
            <li><a href="/category/{{ category }}">{{ category.replace('_', ' ').title() }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
```

### File: `templates/category.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ category_name.replace('_', ' ').title() }}</title>
</head>
<body>
    <h1>{{ category_name.replace('_', ' ').title() }}</h1>
    <ul>
        {% for product in products %}
            <li>
                <strong>{{ product.name }}</strong>: ${{ product.price }}
                <p>{{ product.description }}</p>
                <button onclick="orderProduct({{ product.id }}, '{{ category_name }}')">Order</button>
            </li>
        {% endfor %}
    </ul>
    <script>
        function orderProduct(productId, category) {
            fetch('/order', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ product_id: productId, category: category })
            })
            .then(response => response.json())
            .then(data => alert(data.message || data.error))
            .catch(error => alert('An error occurred: ' + error));
        }
    </script>
</body>
</html>
```
