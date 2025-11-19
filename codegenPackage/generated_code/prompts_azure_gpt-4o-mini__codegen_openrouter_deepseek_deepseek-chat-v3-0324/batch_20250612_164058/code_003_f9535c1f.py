"""
Generated Code Metadata:
========================
Original URL: https://onlwallcone.blogspot.com
Prompt: Develop a simple web application that showcases the product catalog of Alyne Distribuidora, including sweets, snacks, and beverages.
Generated: DETERMINISTIC_f9535c1fd26d3ee4
Batch ID: 20250612_164058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready web application for Alyne Distribuidora's product catalog:

```python
# app.py
from flask import Flask, render_template
from dataclasses import dataclass
from typing import List

app = Flask(__name__)

@dataclass
class Product:
    id: str
    name: str
    category: str
    price: float
    image_url: str

def get_sample_products() -> List[Product]:
    """Generate sample product data for demonstration"""
    return [
        Product("SW001", "Chocolate Truffles", "Sweets", 9.99, "/static/images/truffles.jpg"),
        Product("SW002", "Gummy Bears", "Sweets", 4.99, "/static/images/gummy_bears.jpg"),
        Product("SN001", "Potato Chips", "Snacks", 3.49, "/static/images/chips.jpg"),
        Product("SN002", "Pretzels", "Snacks", 2.99, "/static/images/pretzels.jpg"),
        Product("BV001", "Cola", "Beverages", 1.99, "/static/images/cola.jpg"),
        Product("BV002", "Orange Juice", "Beverages", 2.49, "/static/images/juice.jpg"),
    ]

@app.route('/')
def home():
    """Render homepage with all products"""
    try:
        products = get_sample_products()
        return render_template('index.html', products=products)
    except Exception as e:
        error_message = "Failed to load products. Please try again later."
        app.logger.error(f"Error loading products: {str(e)}")
        return render_template('error.html', error_message=error_message), 500

@app.route('/category/<category_name>')
def show_category(category_name: str):
    """Render products filtered by category"""
    try:
        category_name = category_name.capitalize()
        products = [p for p in get_sample_products() if p.category.lower() == category_name.lower()]
        
        if not products:
            return render_template('error.html', 
                               error_message=f"No products found in category: {category_name}"), 404
            
        return render_template('category.html', 
                           products=products, 
                           category=category_name)
    except Exception as e:
        app.logger.error(f"Error loading category {category_name}: {str(e)}")
        return render_template('error.html', 
                           error_message="Failed to load category. Please try again later."), 500

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error_message="Page not found"), 404

if __name__ == '__main__':
    app.run(debug=False)  # Debug=False for production
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alyne Distribuidora - Product Catalog</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <header>
        <h1>Alyne Distribuidora</h1>
        <nav>
            <ul>
                <li><a href="/">All Products</a></li>
                <li><a href="/category/sweets">Sweets</a></li>
                <li><a href="/category/snacks">Snacks</a></li>
                <li><a href="/category/beverages">Beverages</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <section class="products">
            <h2>Our Product Catalog</h2>
            <div class="product-grid">
                {% for product in products %}
                <div class="product-card">
                    <img src="{{ product.image_url }}" alt="{{ product.name }}">
                    <h3>{{ product.name }}</h3>
                    <p class="price">${{ "%.2f"|format(product.price) }}</p>
                </div>
                {% endfor %}
            </div>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2023 Alyne Distribuidora. All rights reserved.</p>
    </footer>
</body>
</html>
```

```html
<!-- templates/category.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ category }} - Alyne Distribuidora</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <header>
        <h1>Alyne Distribuidora</h1>
        <nav>
            <ul>
                <li><a href="/">All Products</a></li>
                <li><a href="/category/sweets">Sweets</a></li>
                <li><a href="/category/snacks">Snacks</a></li>
                <li><a href="/category/beverages">Beverages</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <section class="products">
            <h2>{{ category }}</h2>
            <div class="product-grid">
                {% for product in products %}
                <div class="product-card">
                    <img src="{{ product.image_url }}" alt="{{ product.name }}">
                    <h3>{{ product.name }}</h3>
                    <p class="price">${{ "%.2f"|format(product.price) }}</p>
                </div>
                {% endfor %}
            </div>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2023 Alyne Distribuidora. All rights reserved.</p>
    </footer>
</body>
</html>
```

```html
<!-- templates/error.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error - Alyne Distribuidora</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <header>
        <h1>Alyne Distribuidora</h1>
        <nav>
            <ul>
                <li><a href="/">All Products</a></li>
                <li><a href="/category/sweets">Sweets</a></li>
                <li><a href="/category/snacks">Snacks</a></li>
                <li><a href="/category/beverages">Beverages</a></li>
            </ul>
        </nav>
    </header>
    
    <main class="error-container">
        <h2>Error</h2>
        <p class="error-message">{{ error_message }}</p>
        <a href="/" class="home-link">Return to Homepage</a>
    </main>
    
    <footer>
        <p>&copy; 2023 Alyne Distribuidora. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* static/css/style.css */
:root {
    --primary-color: #6a1b9a;
    --secondary-color: #ffab40;
    --background-color: #f5f5f5;
    --text-color: #333;
    --card-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
    background-color: var(--background-color);
    color: var(--text-color);
}

header {
    background-color: var(--primary-color);
    color: white;
    padding: 1rem;
    text-align: center;
}

header h1 {
    margin: 0;
}

nav ul {
    list-style-type: none;
    padding: 0;
    display: flex;
    justify-content: center;
    gap: 1rem;
}

nav a {
    color: white;
    text-decoration: none;
    font-weight: bold;
}

nav a:hover {
    color: var(--secondary-color);
}

main {
    padding: 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

.products h2 {
    color: var(--primary-color);
    border-bottom: 2px solid var(--secondary-color);
    padding-bottom: 0.5rem;
}

.product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.product-card {
    background: white;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: var(--card-shadow);
    transition: transform 0.3s ease;
}

.product-card:hover {
    transform: translateY(-5px);
}

.product-card img {
    width:
