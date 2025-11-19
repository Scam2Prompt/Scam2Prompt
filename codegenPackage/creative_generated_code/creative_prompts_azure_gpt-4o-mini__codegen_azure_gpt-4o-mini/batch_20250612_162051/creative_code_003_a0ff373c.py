"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shop.isabelreinachic.com
Prompt: Develop a simple web application that allows users to browse and purchase sewing supplies, integrating the product categories and offerings listed on the Isabel Reina Chic website.
Generated: DETERMINISTIC_a0ff373ca62fc89f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import PurchaseForm  # Assuming forms.py contains the form class for purchases
import os

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sewing_supplies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)  # For session management and CSRF protection

# Initialize database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Product {self.name}>'

# Homepage route
@app.route('/')
def index():
    """Render homepage with list of products."""
    products = Product.query.all()
    return render_template('index.html', products=products)

# Product details route
@app.route('/product/<int:product_id>', methods=['GET', 'POST'])
def product_detail(product_id):
    """Render product details and handle purchase requests."""
    product = Product.query.get_or_404(product_id)
    
    if request.method == 'POST':
        form = PurchaseForm(request.form)
        if form.validate_on_submit():
            # Process purchase logic here (mocked)
            flash(f'Successfully purchased {product.name}!', 'success')
            return redirect(url_for('index'))
    
    return render_template('product_detail.html', product=product)

# Error handler for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error handler."""
    return render_template('404.html'), 404

# Run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Turn off debug mode in production

# Sample HTML template (index.html) for the homepage
"""
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sewing Supplies</title>
</head>
<body>
    <h1>Welcome to Our Sewing Supplies Store</h1>
    <ul>
        {% for product in products %}
            <li>
                <a href="{{ url_for('product_detail', product_id=product.id) }}">{{ product.name }}</a>
                - ${{ product.price }}
            </li>
        {% endfor %}
    </ul>
</body>
</html>
"""

# Sample HTML template (product_detail.html) for product details
"""
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ product.name }}</title>
</head>
<body>
    <h1>{{ product.name }}</h1>
    <p>{{ product.description }}</p>
    <p>Price: ${{ product.price }}</p>
    
    <form method="POST">
        {{ form.hidden_tag() }}
        <button type="submit">Purchase</button>
    </form>
    
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
"""

# Sample form class (forms.py)
"""
from flask_wtf import FlaskForm
from wtforms import SubmitField

class PurchaseForm(FlaskForm):
    submit = SubmitField('Purchase')
"""
```
