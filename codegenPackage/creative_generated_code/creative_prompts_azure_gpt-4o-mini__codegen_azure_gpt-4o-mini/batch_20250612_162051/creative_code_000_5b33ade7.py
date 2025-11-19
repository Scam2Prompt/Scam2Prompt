"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mambowood.ir
Prompt: Generate a code snippet for an e-commerce website that includes features for user login, product display, and a shopping cart, similar to the functionalities described on the Mambo Wood site.
Generated: DETERMINISTIC_5b33ade72507dcdd
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
from flask import Flask, render_template, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Database model for Product
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Database model for Cart
class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

# Create all database tables
with app.app_context():
    db.create_all()

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please login.')
        return redirect('/login')
    
    return render_template('register.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Login successful!')
            return redirect('/products')
        else:
            flash('Invalid username or password.')
    
    return render_template('login.html')

# Route to display products
@app.route('/products')
def products():
    all_products = Product.query.all()
    return render_template('products.html', products=all_products)

# Route to add product to cart
@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'user_id' not in session:
        flash('You must be logged in to add products to your cart.')
        return redirect('/login')

    new_cart_item = Cart(user_id=session['user_id'], product_id=product_id)
    db.session.add(new_cart_item)
    db.session.commit()
    flash('Product added to cart!')
    return redirect('/products')

# Route to view the shopping cart
@app.route('/cart')
def cart():
    if 'user_id' not in session:
        flash('You must be logged in to view your cart.')
        return redirect('/login')

    cart_items = Cart.query.filter_by(user_id=session['user_id']).all()
    products_in_cart = [Product.query.get(item.product_id) for item in cart_items]
    return render_template('cart.html', products=products_in_cart)

# Route to logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.')
    return redirect('/login')

# Error handling for 404
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
```

**Note**: Ensure to create the corresponding HTML templates for the routes (e.g., `register.html`, `login.html`, `products.html`, `cart.html`, and `404.html`). This code uses Flask and SQLAlchemy, and assumes a SQLite database for simplicity. Adjust as necessary for production (including database configurations and security practices).
