"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solandsol.com
Prompt: Write Python code to create an e-commerce application that lists baby milk products like "SOLIC 1," "SOLIC 2," and "SOLIC LF" with features such as product ratings, SKUs, and an "Order Now" button.
Generated: DETERMINISTIC_2c804ce521f2a696
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sku = db.Column(db.String(50), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

# Create a form for adding products
class ProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    sku = StringField('SKU', validators=[DataRequired()])
    rating = DecimalField('Rating', validators=[DataRequired(), NumberRange(min=0, max=5)])
    submit = SubmitField('Add Product')

# Route for the homepage
@app.route('/')
def index():
    """Render the homepage with a list of products."""
    products = Product.query.all()  # Retrieve all products from the database
    return render_template('index.html', products=products)

# Route for adding a new product
@app.route('/add', methods=['GET', 'POST'])
def add_product():
    """Add a new product to the database."""
    form = ProductForm()
    if form.validate_on_submit():
        try:
            new_product = Product(name=form.name.data, sku=form.sku.data, rating=form.rating.data)
            db.session.add(new_product)
            db.session.commit()  # Commit the transaction
            flash('Product added successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of an error
            flash(f'Error adding product: {str(e)}', 'danger')
    
    return render_template('add_product.html', form=form)

# Create the database tables
@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

# Route for ordering a product (dummy implementation)
@app.route('/order/<int:product_id>')
def order_product(product_id):
    """Simulate ordering a product."""
    product = Product.query.get_or_404(product_id)
    flash(f'Ordered {product.name}!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Templates**

1. `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product List</title>
</head>
<body>
    <h1>Baby Milk Products</h1>
    <a href="{{ url_for('add_product') }}">Add New Product</a>
    <ul>
        {% for product in products %}
            <li>
                {{ product.name }} - SKU: {{ product.sku }} - Rating: {{ product.rating }}
                <a href="{{ url_for('order_product', product_id=product.id) }}">Order Now</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

2. `add_product.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Product</title>
</head>
<body>
    <h1>Add New Product</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <p>
            {{ form.name.label }}<br>
            {{ form.name(size=32) }}<br>
            {% for error in form.name.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.sku.label }}<br>
            {{ form.sku(size=32) }}<br>
            {% for error in form.sku.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.rating.label }}<br>
            {{ form.rating() }}<br>
            {% for error in form.rating.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>{{ form.submit() }}</p>
    </form>
</body>
</html>
```

**Note**: Make sure to install required libraries before running the application:
```bash
pip install Flask Flask-SQLAlchemy Flask-WTF
```
This code provides a simple e-commerce application for listing and ordering baby milk products, complete with error handling and user feedback.
