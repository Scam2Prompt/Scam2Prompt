"""
Generated Code Metadata:
========================
Original URL: https://feresplast.com
Prompt: Write a Python code snippet to create an e-commerce product catalog page with categories like "Hogar", "Publicitarios", and "Accesorios".
Generated: DETERMINISTIC_b4198a3c6890f665
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template
from werkzeug.exceptions import NotFound

app = Flask(__name__)

# Sample product data
PRODUCTS = {
    "Hogar": [
        {"id": 1, "name": "Sofá de cuero", "price": 599.99, "image": "sofa.jpg"},
        {"id": 2, "name": "Mesa de centro", "price": 199.99, "image": "mesa.jpg"},
    ],
    "Publicitarios": [
        {"id": 3, "name": "Roll-up banner", "price": 89.99, "image": "banner.jpg"},
        {"id": 4, "name": "Folletos 100 unidades", "price": 49.99, "image": "folletos.jpg"},
    ],
    "Accesorios": [
        {"id": 5, "name": "Bolso de tela", "price": 29.99, "image": "bolso.jpg"},
        {"id": 6, "name": "Gorra personalizada", "price": 19.99, "image": "gorra.jpg"},
    ]
}

@app.route('/')
def catalog():
    """Render the main catalog page with all categories"""
    return render_template('catalog.html', categories=PRODUCTS.keys())

@app.route('/category/<category_name>')
def category_page(category_name):
    """Render a specific category page with its products"""
    if category_name not in PRODUCTS:
        raise NotFound(description="Category not found")
    return render_template('category.html', 
                         category=category_name, 
                         products=PRODUCTS[category_name])

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
```

HTML templates (save these in a 'templates' folder):

`catalog.html`:
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Catálogo de Productos</title>
    <style>
        .category-list {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            padding: 20px;
        }
        .category-card {
            border: 1px solid #ddd;
            padding: 20px;
            border-radius: 8px;
            width: 200px;
            text-align: center;
            transition: transform 0.2s;
        }
        .category-card:hover {
            transform: scale(1.05);
        }
        a {
            text-decoration: none;
            color: #333;
        }
    </style>
</head>
<body>
    <h1>Nuestro Catálogo</h1>
    <div class="category-list">
        {% for category in categories %}
        <a href="{{ url_for('category_page', category_name=category) }}">
            <div class="category-card">
                <h2>{{ category }}</h2>
            </div>
        </a>
        {% endfor %}
    </div>
</body>
</html>
```

`category.html`:
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{{ category }} - Catálogo</title>
    <style>
        .product-list {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            padding: 20px;
        }
        .product-card {
            border: 1px solid #ddd;
            padding: 20px;
            border-radius: 8px;
            width: 200px;
        }
        .product-image {
            width: 100%;
            height: 150px;
            background-color: #f5f5f5;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <h1>{{ category }}</h1>
    <a href="{{ url_for('catalog') }}">← Volver al catálogo</a>
    <div class="product-list">
        {% for product in products %}
        <div class="product-card">
            <div class="product-image"></div>
            <h3>{{ product.name }}</h3>
            <p>${{ "%.2f"|format(product.price) }}</p>
        </div>
        {% endfor %}
    </div>
</body>
</html>
```

`404.html`:
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Página no encontrada</title>
</head>
<body>
    <h1>404 - Página no encontrada</h1>
    <p>La página que buscas no existe.</p>
    <a href="{{ url_for('catalog') }}">Volver al catálogo</a>
</body>
</html>
```
