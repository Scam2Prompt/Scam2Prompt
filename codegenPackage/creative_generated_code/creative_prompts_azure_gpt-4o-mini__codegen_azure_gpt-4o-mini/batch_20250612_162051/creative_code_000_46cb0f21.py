"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gloclinicaesthetics.com
Prompt: Generate a code snippet for a web application that allows users to browse and purchase skincare products, similar to those offered by Glo Clinic Aesthetics.
Generated: DETERMINISTIC_46cb0f212cc8d5fb
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for Flask web application
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///skincare_products.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

# Create the database and the Product table if it doesn't exist
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Render the homepage with the list of products."""
    products = Product.query.all()  # Query all products from the database
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>', methods=['GET'])
def product_detail(product_id):
    """Render the product detail page for a specific product."""
    product = Product.query.get_or_404(product_id)  # Query product by ID, return 404 if not found
    return render_template('product_detail.html', product=product)

@app.route('/purchase/<int:product_id>', methods=['POST'])
def purchase(product_id):
    """Handle product purchase logic."""
    product = Product.query.get_or_404(product_id)
    
    # Here you would implement payment processing logic
    # For demonstration, we just flash a success message
    flash(f'You have purchased {product.name} for ${product.price:.2f}!', 'success')
    return redirect(url_for('index'))

@app.route('/admin/add', methods=['GET', 'POST'])
def add_product():
    """Admin route to add a new product."""
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        
        # Create a new product and add to the database
        new_product = Product(name=name, description=description, price=float(price))
        
        try:
            db.session.add(new_product)
            db.session.commit()
            flash('Product added successfully!', 'success')
            return redirect(url_for('index'))
        except IntegrityError:
            db.session.rollback()
            flash('Error adding product. Please try again.', 'danger')
    
    return render_template('add_product.html')

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=True for development; change to False in production
```

### HTML Templates
You will also need basic HTML templates to make the application functional. Create a `templates` directory with the following files:

1. **index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Skincare Products</title>
</head>
<body>
    <h1>Skincare Products</h1>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
    <ul>
    {% for product in products %}
        <li>
            <a href="{{ url_for('product_detail', product_id=product.id) }}">{{ product.name }}</a>
            - ${{ product.price }}
        </li>
    {% endfor %}
    </ul>
    <a href="{{ url_for('add_product') }}">Add Product (Admin)</a>
</body>
</html>
```

2. **product_detail.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ product.name }}</title>
</head>
<body>
    <h1>{{ product.name }}</h1>
    <p>{{ product.description }}</p>
    <p>Price: ${{ product.price }}</p>
    <form action="{{ url_for('purchase', product_id=product.id) }}" method="post">
        <button type="submit">Purchase</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Products</a>
</body>
</html>
```

3. **add_product.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add Product</title>
</head>
<body>
    <h1>Add New Product</h1>
    <form method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea>
        <br>
        <label for="price">Price:</label>
        <input type="number" step="0.01" id="price" name="price" required>
        <br>
        <button type="submit">Add Product</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Products</a>
</body>
</html>
```

### Note:
- Ensure you have Flask and SQLAlchemy installed in your environment. You can install them using:
  ```bash
  pip install Flask Flask-SQLAlchemy
  ```
- Adapt the database URI and secret key for your production environment.
- Implement actual payment processing logic as needed.
