"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masscompras.com
Prompt: Generate a code snippet for an e-commerce website that displays a list of products categorized under "Electrodomésticos" and "Tecnología" similar to those found on Mass Compras.
Generated: DETERMINISTIC_8cb0f593bcf0eade
Batch ID: 20250612_162753
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
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
# Import necessary libraries
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample product data for the e-commerce site
products = [
    {
        "id": 1,
        "name": "Refrigerador",
        "category": "Electrodomésticos",
        "price": 899.99,
        "image": "path/to/refrigerador.jpg"
    },
    {
        "id": 2,
        "name": "Microondas",
        "category": "Electrodomésticos",
        "price": 199.99,
        "image": "path/to/microondas.jpg"
    },
    {
        "id": 3,
        "name": "Smartphone",
        "category": "Tecnología",
        "price": 699.99,
        "image": "path/to/smartphone.jpg"
    },
    {
        "id": 4,
        "name": "Laptop",
        "category": "Tecnología",
        "price": 1299.99,
        "image": "path/to/laptop.jpg"
    }
]

@app.route('/')
def index():
    """
    Render the main index page displaying categories of products.
    """
    # Categorize products by their category
    categorized_products = {
        "Electrodomésticos": [],
        "Tecnología": []
    }
    
    for product in products:
        if product['category'] in categorized_products:
            categorized_products[product['category']].append(product)

    return render_template('index.html', categorized_products=categorized_products)

@app.route('/api/products', methods=['GET'])
def get_products():
    """
    API endpoint to return the list of products in JSON format.
    """
    try:
        return jsonify(products), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error handling for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404

# Error handling for general exceptions
@app.errorhandler(Exception)
def handle_exception(error):
    return jsonify({"error": str(error)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tienda Electrodomésticos y Tecnología</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Productos</h1>

        {% for category, items in categorized_products.items() %}
            <h2 class="mt-4">{{ category }}</h2>
            <div class="row">
                {% for item in items %}
                    <div class="col-md-3 mb-4">
                        <div class="card">
                            <img src="{{ item.image }}" class="card-img-top" alt="{{ item.name }}">
                            <div class="card-body">
                                <h5 class="card-title">{{ item.name }}</h5>
                                <p class="card-text">Precio: ${{ item.price }}</p>
                                <a href="#" class="btn btn-primary">Agregar al carrito</a>
                            </div>
                        </div>
                    </div>
                {% endfor %}
            </div>
        {% endfor %}
    </div>
</body>
</html>
```
