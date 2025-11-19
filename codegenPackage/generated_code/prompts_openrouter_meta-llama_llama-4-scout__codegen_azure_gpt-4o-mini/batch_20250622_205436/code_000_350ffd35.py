"""
Generated Code Metadata:
========================
Original URL: https://semillasplantae.com
Prompt: "Write a Python code snippet to create an e-commerce website for selling organic seeds, including product categories and payment gateway integration, inspired by Semillas Plantae."
Generated: DETERMINISTIC_350ffd35cbc78c0c
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SelectField, SubmitField
from wtforms.validators import DataRequired
import stripe

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///seeds.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Configure Stripe
stripe.api_key = 'your_stripe_secret_key'

# Database model for products
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Form for adding products
class ProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    category = SelectField('Category', choices=[('vegetables', 'Vegetables'), ('herbs', 'Herbs'), ('flowers', 'Flowers')], validators=[DataRequired()])
    price = DecimalField('Price', places=2, validators=[DataRequired()])
    submit = SubmitField('Add Product')

# Route for the homepage
@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

# Route for adding a new product
@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        new_product = Product(name=form.name.data, category=form.category.data, price=form.price.data)
        db.session.add(new_product)
        db.session.commit()
        flash('Product added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add_product.html', form=form)

# Route for processing payments
@app.route('/checkout', methods=['POST'])
def checkout():
    try:
        # Get the product ID and amount from the form
        product_id = request.form.get('product_id')
        product = Product.query.get(product_id)
        
        # Create a Stripe payment intent
        intent = stripe.PaymentIntent.create(
            amount=int(product.price * 100),  # Amount in cents
            currency='usd',
            payment_method_types=['card'],
        )
        return {'clientSecret': intent['client_secret']}
    except Exception as e:
        return str(e), 400

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the app in debug mode
```

### HTML Templates (for completeness)

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Organic Seeds Store</title>
</head>
<body>
    <h1>Welcome to Organic Seeds Store</h1>
    <a href="{{ url_for('add_product') }}">Add New Product</a>
    <h2>Products</h2>
    <ul>
        {% for product in products %}
            <li>{{ product.name }} - ${{ product.price }} <form action="/checkout" method="post"><input type="hidden" name="product_id" value="{{ product.id }}"><button type="submit">Buy Now</button></form></li>
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
    <h1>Add New Product</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.name.label }} {{ form.name(size=32) }}<br>
        {{ form.category.label }} {{ form.category() }}<br>
        {{ form.price.label }} {{ form.price(size=10) }}<br>
        {{ form.submit() }}
    </form>
</body>
</html>
```

### Note:
- Replace `'your_secret_key'` and `'your_stripe_secret_key'` with your actual keys.
- Ensure you have the necessary packages installed: `Flask`, `Flask-SQLAlchemy`, `Flask-WTF`, `Flask-Migrate`, `stripe`.
- This code is a basic structure and should be expanded with additional features like user authentication, product images, and more robust error handling for production use.
