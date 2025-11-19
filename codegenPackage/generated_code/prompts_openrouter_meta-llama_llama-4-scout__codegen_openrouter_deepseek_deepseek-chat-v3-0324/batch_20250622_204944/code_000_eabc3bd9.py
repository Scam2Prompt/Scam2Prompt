"""
Generated Code Metadata:
========================
Original URL: https://onlwallcone.blogspot.com
Prompt: Write a Python code snippet to create an e-commerce website for a Brazilian distributor of sweets and party supplies, similar to Alyne Distribuidora.
Generated: DETERMINISTIC_eabc3bd9c5e01ab1
Batch ID: 20250622_204944
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
from datetime import datetime
from functools import wraps

# Initialize Flask application
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY') or 'dev-secret-key'

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Initialize Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    orders = db.relationship('Order', backref='customer', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='Pending')
    total = db.Column(db.Float, nullable=False)
    items = db.relationship('OrderItem', backref='order', lazy=True)

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    product = db.relationship('Product')

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Admin required decorator
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin:
            flash('You need to be an admin to access this page.', 'danger')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
def index():
    categories = db.session.query(Product.category).distinct().all()
    products = Product.query.filter(Product.stock > 0).limit(8).all()
    return render_template('index.html', products=products, categories=categories)

@app.route('/products')
def products():
    category = request.args.get('category')
    if category:
        products = Product.query.filter_by(category=category, stock__gt=0).all()
    else:
        products = Product.query.filter(Product.stock > 0).all()
    categories = db.session.query(Product.category).distinct().all()
    return render_template('products.html', products=products, categories=categories, selected_category=category)

@app.route('/product/<int:id>')
def product_detail(id):
    product = Product.query.get_or_404(id)
    return render_template('product_detail.html', product=product)

@app.route('/cart')
@login_required
def cart():
    if 'cart' not in session:
        session['cart'] = {}
    cart_items = []
    total = 0
    for product_id, quantity in session['cart'].items():
        product = Product.query.get(product_id)
        if product and product.stock >= quantity:
            item_total = product.price * quantity
            total += item_total
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'item_total': item_total
            })
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)
    quantity = int(request.form.get('quantity', 1))
    
    if quantity > product.stock:
        flash('Not enough stock available.', 'danger')
        return redirect(url_for('product_detail', id=product_id))
    
    if 'cart' not in session:
        session['cart'] = {}
    
    if str(product_id) in session['cart']:
        session['cart'][str(product_id)] += quantity
    else:
        session['cart'][str(product_id)] = quantity
    
    session.modified = True
    flash('Product added to cart!', 'success')
    return redirect(url_for('product_detail', id=product_id))

@app.route('/remove_from_cart/<int:product_id>')
@login_required
def remove_from_cart(product_id):
    if 'cart' in session and str(product_id) in session['cart']:
        del session['cart'][str(product_id)]
        session.modified = True
        flash('Product removed from cart.', 'success')
    return redirect(url_for('cart'))

@app.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    if 'cart' not in session or not session['cart']:
        flash('Your cart is empty.', 'warning')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        # Validate cart items
        cart_items = []
        total = 0
        for product_id, quantity in session['cart'].items():
            product = Product.query.get(product_id)
            if not product or product.stock < quantity:
                flash(f'Product {product.name} is no longer available in the requested quantity.', 'danger')
                return redirect(url_for('cart'))
            
            item_total = product.price * quantity
            total += item_total
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'item_total': item_total
            })
        
        # Create order
        order = Order(user_id=current_user.id, total=total)
        db.session.add(order)
        db.session.commit()
        
        # Create order items and update stock
        for item in cart_items:
            order_item = OrderItem(
                order_id=order.id,
                product_id=item['product'].id,
                quantity=item['quantity'],
                price=item['product'].price
            )
            db.session.add(order_item)
            item['product'].stock -= item['quantity']
            db.session.add(item['product'])
        
        db.session.commit()
        session.pop('cart', None)
        flash('Order placed successfully!', 'success')
        return redirect(url_for('order_confirmation', order_id=order.id))
    
    return redirect(url_for('cart'))

@app.route('/order_confirmation/<int:order_id>')
@login_required
def order_confirmation(order_id):
    order = Order.query.get_or_404(order_id)
    if order.user_id != current_user.id and not current_user.is_admin:
        flash('You are not authorized to view this order.', 'danger')
        return redirect(url_for('index'))
    return render_template('order_confirmation.html', order=order)

@app.route('/orders')
@login_required
def orders():
    user_orders = Order.query.filter_by(user_id=current_user.id).order_by(Order.order_date.desc()).all()
    return render_template('orders.html', orders=user_orders)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            login_user(user)
            next_page = request.args.get('next')
            flash('Logged in successfully!', 'success')
            return redirect(next_page or url_for('index'))
        else:
            flash('Invalid email or password.', 'danger')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
