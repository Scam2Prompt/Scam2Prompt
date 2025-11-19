"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finishdrop.com
Prompt: Generate a code snippet for setting up an e-commerce website using the tools and methods discussed on FinishDrop, focusing on product integration and optimized site design.
Generated: DETERMINISTIC_f50d8576f52a89f2
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# e_commerce_setup.py

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Database model for products
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)

    def __repr__(self):
        return f"<Product {self.name} - ${self.price}>"

# Form for adding new products
class ProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    price = DecimalField('Product Price', validators=[DataRequired()])
    submit = SubmitField('Add Product')

@app.route('/')
def index():
    """Render the homepage displaying all products."""
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/add', methods=['GET', 'POST'])
def add_product():
    """Handle adding a new product to the store."""
    form = ProductForm()
    if form.validate_on_submit():
        try:
            new_product = Product(name=form.name.data, price=form.price.data)
            db.session.add(new_product)
            db.session.commit()
            flash(f'Product {new_product.name} added successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error adding product: {e}")
            flash('Failed to add product. Please try again.', 'danger')
    return render_template('add_product.html', form=form)

if __name__ == '__main__':
    with app.app_context():
        # Ensure the database is created
        db.create_all()
    app.run(debug=True)
```

### Additional Files Required

1. **HTML Templates**: Create the following HTML files in a `templates` directory.

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-Commerce Home</title>
</head>
<body>
    <h1>Product List</h1>
    <a href="{{ url_for('add_product') }}">Add New Product</a>
    <ul>
        {% for product in products %}
            <li>{{ product.name }} - ${{ product.price }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

**add_product.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Product</title>
</head>
<body>
    <h1>Add a New Product</h1>
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
            {{ form.price.label }}<br>
            {{ form.price(size=32) }}<br>
            {% for error in form.price.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>{{ form.submit() }}</p>
    </form>
    <a href="{{ url_for('index') }}">Back to Product List</a>
</body>
</html>
```

### Notes
- Make sure to install the required libraries using `pip install Flask Flask-SQLAlchemy Flask-Migrate Flask-WTF`.
- Replace `'your_secret_key'` with an actual secret key for session management.
- This code sets up a simple e-commerce application using Flask, SQLite, and WTForms to handle product integration and display.
