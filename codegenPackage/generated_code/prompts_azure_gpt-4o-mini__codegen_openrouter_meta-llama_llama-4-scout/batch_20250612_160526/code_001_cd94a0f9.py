"""
Generated Code Metadata:
========================
Original URL: https://teamadver.com
Prompt: Write a code snippet for a custom website that integrates SEO-friendly features and e-commerce capabilities, inspired by Team Adver's web development services.
Generated: DETERMINISTIC_cd94a0f93944d46d
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_seo import Seo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
db = SQLAlchemy(app)
seo = Seo(app)

# Define E-commerce Product Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Product('{self.name}', '{self.price}')"

# Create the database tables
with app.app_context():
    db.create_all()

# SEO-friendly Home Route
@app.route('/')
def home():
    """
    Homepage with product listings and SEO metadata.
    """
    products = Product.query.all()
    seo.info(
        title='Ecommerce Website - Buy Products Online',
        description='Ecommerce website built with Flask and SQLAlchemy',
        keywords='ecommerce, products, online shopping'
    )
    return render_template('home.html', products=products)

# Product Details Route
@app.route('/product/<int:product_id>')
def product_details(product_id):
    """
    Product details page with SEO metadata.
    """
    product = Product.query.get_or_404(product_id)
    seo.info(
        title=f'{product.name} - Product Details',
        description=product.description,
        keywords=product.name
    )
    return render_template('product.html', product=product)

# Add to Cart Route
@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    """
    Add product to cart and redirect to cart page.
    """
    try:
        product_id = request.form['product_id']
        product = Product.query.get(product_id)
        if product:
            # Implement cart logic here (e.g., using Flask-Session)
            return redirect(url_for('cart'))
        else:
            return 'Product not found', 404
    except Exception as e:
        return str(e), 500

# Cart Route
@app.route('/cart')
def cart():
    """
    Cart page with product listings.
    """
    # Implement cart logic here (e.g., using Flask-Session)
    return render_template('cart.html')

# Error Handling
@app.errorhandler(404)
def page_not_found(e):
    seo.info(
        title='Page Not Found - 404 Error',
        description='Page not found on ecommerce website',
        keywords='404 error, page not found'
    )
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/home.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ecommerce Website</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Ecommerce Website</h1>
    <ul>
        {% for product in products %}
            <li>
                <a href="{{ url_for('product_details', product_id=product.id) }}">{{ product.name }}</a> (${{ product.price }})
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/product.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ product.name }} - Product Details</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>{{ product.name }}</h1>
    <p>{{ product.description }}</p>
    <p>Price: ${{ product.price }}</p>
    <form action="{{ url_for('add_to_cart') }}" method="post">
        <input type="hidden" name="product_id" value="{{ product.id }}">
        <button type="submit">Add to Cart</button>
    </form>
</body>
</html>
```

```html
<!-- templates/cart.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cart</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Cart</h1>
    <ul>
        <!-- Implement cart logic here -->
    </ul>
</body>
</html>
```

```html
<!-- templates/404.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found - 404 Error</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Page Not Found - 404 Error</h1>
    <p>The page you are looking for does not exist.</p>
</body>
</html>
```
