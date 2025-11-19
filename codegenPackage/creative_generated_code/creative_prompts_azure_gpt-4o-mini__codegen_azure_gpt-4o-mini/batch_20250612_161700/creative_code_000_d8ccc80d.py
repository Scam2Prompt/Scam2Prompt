"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multandesigns.com
Prompt: Generate a code snippet for an e-commerce website that displays a collection of traditional Pakistani clothing, including kurtas and sharara sets, similar to the offerings on Multan Designs.
Generated: DETERMINISTIC_d8ccc80dd9f2357a
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for a web application
from flask import Flask, render_template, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Sample data for traditional Pakistani clothing
products = [
    {
        "id": 1,
        "name": "Embroidered Kurta",
        "category": "Kurta",
        "price": 4500,
        "description": "A beautifully embroidered kurta perfect for special occasions.",
        "image": "kurta1.jpg"
    },
    {
        "id": 2,
        "name": "Silk Sharara Set",
        "category": "Sharara",
        "price": 8500,
        "description": "Elegant silk sharara set with intricate designs.",
        "image": "sharara1.jpg"
    },
    {
        "id": 3,
        "name": "Cotton Kurta",
        "category": "Kurta",
        "price": 2500,
        "description": "Comfortable cotton kurta for casual wear.",
        "image": "kurta2.jpg"
    },
    {
        "id": 4,
        "name": "Lawn Sharara Set",
        "category": "Sharara",
        "price": 5500,
        "description": "Trendy lawn sharara set suitable for summer.",
        "image": "sharara2.jpg"
    }
]

# Route for the homepage
@app.route('/')
def home():
    """Render the homepage displaying traditional Pakistani clothing."""
    return render_template('index.html', products=products)

# API route to fetch product data 
@app.route('/api/products', methods=['GET'])
def get_products():
    """Return the list of products as JSON."""
    try:
        return jsonify(products)
    except Exception as e:
        # Log the error and return a 500 response
        app.logger.error("Error fetching products: %s", e)
        return jsonify({"error": "Unable to fetch products."}), 500

# Main entry point of the application
if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)
```

**HTML Template (`templates/index.html`):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Traditional Pakistani Clothing</title>
    <link rel="stylesheet" href="static/styles.css"> <!-- Link to CSS file -->
</head>
<body>
    <h1>Traditional Pakistani Clothing Collection</h1>
    <div class="product-container">
        {% for product in products %}
            <div class="product-card">
                <img src="{{ product.image }}" alt="{{ product.name }}">
                <h2>{{ product.name }}</h2>
                <p>Category: {{ product.category }}</p>
                <p>Price: Rs. {{ product.price }}</p>
                <p>{{ product.description }}</p>
            </div>
        {% endfor %}
    </div>
</body>
</html>
```

**CSS (`static/styles.css`):**
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f9f9f9;
    margin: 0;
    padding: 20px;
}

.product-container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}

.product-card {
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 15px;
    background-color: #fff;
    width: calc(25% - 20px);
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.product-card img {
    max-width: 100%;
    border-radius: 10px;
}
```
