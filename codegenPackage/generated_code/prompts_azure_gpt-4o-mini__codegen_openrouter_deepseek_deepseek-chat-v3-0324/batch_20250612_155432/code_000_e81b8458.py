"""
Generated Code Metadata:
========================
Original URL: https://curaheridas.com
Prompt: Generate a code snippet to create an online shopping cart for medical supplies, similar to the one found on Curaheridas, including features for adding items and viewing the cart.
Generated: DETERMINISTIC_e81b8458a4864d5b
Batch ID: 20250612_155432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medical_supplies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(80), nullable=False)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    user = db.relationship('User', backref=db.backref('carts', lazy=True))
    product = db.relationship('Product', backref=db.backref('carts', lazy=True))

# Initialize database
with app.app_context():
    db.create_all()

# Helper functions
def get_cart_items():
    if 'user_id' not in session:
        return []
    user_id = session['user_id']
    cart_items = Cart.query.filter_by(user_id=user_id).all()
    return cart_items

def calculate_cart_total(cart_items):
    total = 0
    for item in cart_items:
        total += item.product.price * item.quantity
    return total

# Routes
@app.route('/')
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    if 'user_id' not in session:
        flash('Please login to add items to cart', 'error')
        return redirect(url_for('login'))
    
    product = Product.query.get_or_404(product_id)
    quantity = int(request.form.get('quantity', 1))
    
    if quantity > product.stock:
        flash('Not enough stock available', 'error')
        return redirect(url_for('product_detail', product_id=product_id))
    
    # Check if product already in cart
    existing_cart_item = Cart.query.filter_by(
        user_id=session['user_id'],
        product_id=product_id
    ).first()
    
    if existing_cart_item:
        existing_cart_item.quantity += quantity
    else:
        new_cart_item = Cart(
            user_id=session['user_id'],
            product_id=product_id,
            quantity=quantity
        )
        db.session.add(new_cart_item)
    
    db.session.commit()
    flash('Item added to cart successfully', 'success')
    return redirect(url_for('view_cart'))

@app.route('/cart')
def view_cart():
    if 'user_id' not in session:
        flash('Please login to view your cart', 'error')
        return redirect(url_for('login'))
    
    cart_items = get_cart_items()
    total = calculate_cart_total(cart_items)
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/remove_from_cart/<int:cart_item_id>')
def remove_from_cart(cart_item_id):
    if 'user_id' not in session:
        flash('Please login to modify your cart', 'error')
        return redirect(url_for('login'))
    
    cart_item = Cart.query.get_or_404(cart_item_id)
    if cart_item.user_id != session['user_id']:
        flash('Unauthorized action', 'error')
        return redirect(url_for('view_cart'))
    
    db.session.delete(cart_item)
    db.session.commit()
    flash('Item removed from cart', 'success')
    return redirect(url_for('view_cart'))

@app.route('/update_cart/<int:cart_item_id>', methods=['POST'])
def update_cart(cart_item_id):
    if 'user_id' not in session:
        flash('Please login to modify your cart', 'error')
        return redirect(url_for('login'))
    
    cart_item = Cart.query.get_or_404(cart_item_id)
    if cart_item.user_id != session['user_id']:
        flash('Unauthorized action', 'error')
        return redirect(url_for('view_cart'))
    
    new_quantity = int(request.form.get('quantity', 1))
    product = Product.query.get(cart_item.product_id)
    
    if new_quantity > product.stock:
        flash('Not enough stock available', 'error')
        return redirect(url_for('view_cart'))
    
    cart_item.quantity = new_quantity
    db.session.commit()
    flash('Cart updated successfully', 'success')
    return redirect(url_for('view_cart'))

# Authentication routes
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Login successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'success')
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return redirect(url_for('register'))
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists', 'error')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password=hashed_password)
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful. Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
```
