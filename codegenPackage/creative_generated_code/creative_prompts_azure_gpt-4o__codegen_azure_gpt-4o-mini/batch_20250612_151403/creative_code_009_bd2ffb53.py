"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gprobolsa.com
Prompt: Design a Flask web application that allows users to browse and order Grupo ProBolsa's sustainable promotional products, including reusable bags.
Generated: DETERMINISTIC_bd2ffb531a977a45
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the app with a SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize the database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity_available = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

# Home route to display all products
@app.route('/')
def index():
    products = Product.query.all()  # Fetch all products from the database
    return render_template('index.html', products=products)

# Route to order a product
@app.route('/order/<int:product_id>', methods=['POST'])
def order_product(product_id):
    product = Product.query.get_or_404(product_id)  # Get the product or return a 404
    quantity = request.form.get('quantity', type=int)  # Get the quantity from the form

    if quantity > product.quantity_available:
        flash('Not enough stock available!', 'danger')
        return redirect(url_for('index'))

    # Process the order (in a real application, you'd handle payments here)
    product.quantity_available -= quantity
    db.session.commit()
    flash('Order placed successfully!', 'success')
    return redirect(url_for('index'))

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# API endpoint to get product details
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify({
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'quantity_available': product.quantity_available
    })

# Main function to run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=False)  # Set debug to False for production
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ProBolsa Products</title>
</head>
<body>
    <h1>Our Sustainable Promotional Products</h1>
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
    <ul>
        {% for product in products %}
            <li>
                <h2>{{ product.name }}</h2>
                <p>{{ product.description }}</p>
                <p>Price: ${{ product.price }}</p>
                <p>Available: {{ product.quantity_available }}</p>
                <form action="{{ url_for('order_product', product_id=product.id) }}" method="post">
                    <label for="quantity">Quantity:</label>
                    <input type="number" name="quantity" min="1" max="{{ product.quantity_available }}" required>
                    <button type="submit">Order</button>
                </form>
            </li>
        {% endfor %}
    </ul>
</body>
</html>

<!-- templates/404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
    <a href="{{ url_for('index') }}">Go back to home</a>
</body>
</html>
```

### Notes:
1. Create the SQLite database and run migrations as needed.
2. The `SECRET_KEY` should be a strong random key in production.
3. Ensure that Flask, Flask-SQLAlchemy, and Flask-Migrate are installed in your environment.
4. Proper error handling is integrated with flash messages and redirects for user feedback.
