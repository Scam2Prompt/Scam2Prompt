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
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)  # E.g., "Essential Oils" or "Diffusers"

# Define the cart model
class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    product = db.relationship('Product', backref=db.backref('cart_items', lazy=True))

# Routes
@app.route('/')
def home():
    """
    Home page displays all products.
    """
    try:
        products = Product.query.all()
        return render_template('home.html', products=products)
    except Exception as e:
        flash(f"An error occurred: {str(e)}", "error")
        return render_template('error.html')

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    """
    Product detail page.
    """
    try:
        product = Product.query.get_or_404(product_id)
        return render_template('product_detail.html', product=product)
    except Exception as e:
        flash(f"An error occurred: {str(e)}", "error")
        return render_template('error.html')

@app.route('/cart')
def cart():
    """
    Cart page displays items added to the cart.
    """
    try:
        cart_items = CartItem.query.all()
        return render_template('cart.html', cart_items=cart_items)
    except Exception as e:
        flash(f"An error occurred: {str(e)}", "error")
        return render_template('error.html')

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    """
    Add a product to the cart.
    """
    try:
        product_id = request.form.get('product_id')
        quantity = int(request.form.get('quantity', 1))
        product = Product.query.get_or_404(product_id)

        # Check if the product is already in the cart
        cart_item = CartItem.query.filter_by(product_id=product_id).first()
        if cart_item:
            cart_item.quantity += quantity
        else:
            cart_item = CartItem(product_id=product.id, quantity=quantity)
            db.session.add(cart_item)

        db.session.commit()
        flash(f"Added {product.name} to the cart!", "success")
        return redirect(url_for('cart'))
    except Exception as e:
        db.session.rollback()
        flash(f"An error occurred: {str(e)}", "error")
        return render_template('error.html')

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    """
    Checkout page to purchase items in the cart.
    """
    try:
        if request.method == 'POST':
            # In production, implement payment gateway logic here
            # For now, clear the cart (simulate purchase)
            CartItem.query.delete()
            db.session.commit()
            flash("Thank you for your purchase!", "success")
            return redirect(url_for('home'))

        return render_template('checkout.html')
    except Exception as e:
        flash(f"An error occurred: {str(e)}", "error")
        return render_template('error.html')

# Error handling
@app.errorhandler(HTTPException)
def handle_exception(e):
    """
    Handle HTTP errors.
    """
    return render_template("error.html", error=e), e.code

# Initialize the database and add sample data
@app.before_first_request
def setup():
    db.create_all()

    if not Product.query.first():
        sample_products = [
            Product(name="Lavender Oil", description="100% pure lavender essential oil.", price=15.99, category="Essential Oils"),
            Product(name="Peppermint Oil", description="Cool, refreshing peppermint essential oil.", price=12.99, category="Essential Oils"),
            Product(name="Ceramic Diffuser", description="Elegant ceramic diffuser for essential oils.", price=39.99, category="Diffusers")
        ]
        db.session.bulk_save_objects(sample_products)
        db.session.commit()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
1. HTML templates (`home.html`, `product_detail.html`, `cart.html`, `checkout.html`, `error.html`) should be created to render the views appropriately.
2. This code uses SQLite for simplicity; in production, replace it with a more robust database.
3. Add CSRF protection and implement secure payment logic for production use.
