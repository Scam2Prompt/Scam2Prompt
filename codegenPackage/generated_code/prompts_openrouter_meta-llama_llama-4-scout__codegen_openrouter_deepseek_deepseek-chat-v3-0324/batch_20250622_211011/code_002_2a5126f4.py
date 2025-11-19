"""
Generated Code Metadata:
========================
Original URL: https://gematria.com
Prompt: Generate a Python code snippet to create a simple e-commerce website for a supplement company like Gematria, including features for product display and shopping cart functionality.
Generated: DETERMINISTIC_2a5126f443826f5b
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gematria.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(100), nullable=False)
    stock = db.Column(db.Integer, nullable=False)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    product = db.relationship('Product', backref='carts')

# Helper Functions
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

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
@login_required
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)
    if product.stock <= 0:
        flash('This product is out of stock!', 'danger')
        return redirect(url_for('product_detail', product_id=product_id))
    
    cart_item = Cart.query.filter_by(user_id=session['user_id'], product_id=product_id).first()
    
    if cart_item:
        if cart_item.quantity + 1 > product.stock:
            flash('Cannot add more than available stock!', 'danger')
        else:
            cart_item.quantity += 1
            db.session.commit()
            flash('Product quantity updated in cart!', 'success')
    else:
        new_cart_item = Cart(user_id=session['user_id'], product_id=product_id, quantity=1)
        db.session.add(new_cart_item)
        db.session.commit()
        flash('Product added to cart!', 'success')
    
    return redirect(url_for('product_detail', product_id=product_id))

@app.route('/cart')
@login_required
def cart():
    cart_items = Cart.query.filter_by(user_id=session['user_id']).all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/remove_from_cart/<int:cart_id>')
@login_required
def remove_from_cart(cart_id):
    cart_item = Cart.query.get_or_404(cart_id)
    if cart_item.user_id != session['user_id']:
        flash('You cannot remove this item!', 'danger')
        return redirect(url_for('cart'))
    
    db.session.delete(cart_item)
    db.session.commit()
    flash('Product removed from cart!', 'success')
    return redirect(url_for('cart'))

@app.route('/checkout')
@login_required
def checkout():
    cart_items = Cart.query.filter_by(user_id=session['user_id']).all()
    
    # Check stock before checkout
    for item in cart_items:
        product = Product.query.get(item.product_id)
        if item.quantity > product.stock:
            flash(f'Not enough stock for {product.name}!', 'danger')
            return redirect(url_for('cart'))
    
    # Update stock and clear cart
    for item in cart_items:
        product = Product.query.get(item.product_id)
        product.stock -= item.quantity
        db.session.delete(item)
    
    db.session.commit()
    flash('Order placed successfully!', 'success')
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists!', 'danger')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists!', 'danger')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if not user or not check_password_hash(user.password, password):
            flash('Invalid username or password!', 'danger')
            return redirect(url_for('login'))
        
        session['user_id'] = user.id
        session['username'] = user.username
        flash('Login successful!', 'success')
        return redirect(url_for('home'))
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

# Sample Data Initialization
def create_sample_data():
    with app.app_context():
        db.create_all()
        
        # Add sample products if none exist
        if Product.query.count() == 0:
            products = [
                Product(
                    name='Immune Boost',
                    description='Supports immune system function with vitamin C and zinc',
                    price=29.99,
                    image='immune_boost.jpg',
                    stock=50
                ),
                Product(
                    name='Energy Plus',
                    description='Natural energy supplement with B vitamins and ginseng',
                    price=34.99,
                    image='energy_plus.jpg',
                    stock=30
                ),
                Product(
                    name='Sleep Aid',
                    description='Promotes restful sleep with melatonin and chamomile',
                    price=24.99,
                    image='sleep_aid.jpg',
                    stock=40
                )
            ]
            db.session.add_all(products)
            db.session.commit()

if __name__ == '__main__':
    create_sample_data()
    app.run(debug=True)
```
