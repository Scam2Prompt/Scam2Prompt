"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aromaterapiasalud.cl
Prompt: Generate a code snippet for a web application that allows users to browse and purchase 100% pure essential oils and diffusers similar to those offered by Aromaterapiasalud.
Generated: DETERMINISTIC_235f5aba05e52df5
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# web_app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from wtforms import Form, StringField, DecimalField, IntegerField, SubmitField, validators

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a strong secret key
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Model for products in the store
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    description = db.Column(db.Text, nullable=True)
    stock = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

# Form for adding products
class ProductForm(Form):
    name = StringField('Product Name', [validators.Length(min=1, max=100)])
    price = DecimalField('Price', [validators.NumberRange(min=0)], places=2)
    description = StringField('Description', [validators.Optional()])
    stock = IntegerField('Stock Quantity', [validators.NumberRange(min=0)])
    submit = SubmitField('Add Product')

# Route to list all products
@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

# Route to add a new product
@app.route('/add', methods=['GET', 'POST'])
def add_product():
    form = ProductForm(request.form)
    if request.method == 'POST' and form.validate():
        new_product = Product(
            name=form.name.data,
            price=form.price.data,
            description=form.description.data,
            stock=form.stock.data
        )
        db.session.add(new_product)
        db.session.commit()
        flash('Product added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add_product.html', form=form)

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handling for internal server errors
@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Set debug to False in production

```

**HTML Templates (for completeness)**

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Essential Oils Store</title>
</head>
<body>
    <h1>Essential Oils and Diffusers</h1>
    <a href="{{ url_for('add_product') }}">Add New Product</a>
    <ul>
        {% for product in products %}
            <li>{{ product.name }} - ${{ product.price }} (Stock: {{ product.stock }})</li>
        {% endfor %}
    </ul>
</body>
</html>

<!-- templates/add_product.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Product</title>
</head>
<body>
    <h1>Add New Product</h1>
    <form method="post">
        {{ form.hidden_tag() }}
        {{ form.name.label }} {{ form.name(size=32) }}<br>
        {{ form.price.label }} {{ form.price(size=10) }}<br>
        {{ form.description.label }} {{ form.description(size=64) }}<br>
        {{ form.stock.label }} {{ form.stock(size=10) }}<br>
        {{ form.submit() }}
    </form>
    <a href="{{ url_for('index') }}">Back to Products</a>
</body>
</html>

<!-- templates/404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="{{ url_for('index') }}">Go to Homepage</a>
</body>
</html>

<!-- templates/500.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <a href="{{ url_for('index') }}">Go to Homepage</a>
</body>
</html>
```

**Note:** This code uses Flask for the web framework and SQLAlchemy for the database ORM, with forms managed by WTForms. Make sure to install the necessary packages (`Flask`, `Flask-SQLAlchemy`, `Flask-Migrate`, `WTForms`) before running the application. Adjust the database URI and secret key for production use.
