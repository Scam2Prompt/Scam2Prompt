"""
Generated Code Metadata:
========================
Original URL: https://mambowood.ir
Prompt: Write a Python code snippet to create an e-commerce website for selling wooden kitchen utensils, including a product catalog with prices and discounts.
Generated: DETERMINISTIC_9502378b34110dfc
Batch ID: 20250622_210655
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
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wooden_utensils.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Float, default=0.0)
    stock = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(200), nullable=True)
    category = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='Pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Float, default=0.0)

# Create tables
with app.app_context():
    db.create_all()

# Utility Functions
def calculate_discounted_price(price, discount):
    return price * (1 - discount / 100)

def get_cart_count():
    if 'user_id' in session:
        return Cart.query.filter_by(user_id=session['user_id']).count()
    return 0

# Routes
@app.route('/')
def home():
    products = Product.query.filter(Product.stock > 0).limit(8).all()
    return render_template('home.html', products=products, cart_count=get_cart_count())

@app.route('/products')
def products():
    category = request.args.get('category', 'all')
    if category == 'all':
        products = Product.query.filter(Product.stock > 0).all()
    else:
        products = Product.query.filter(Product.stock > 0, Product.category == category).all()
    return render_template('products.html', products=products, category=category, cart_count=get_cart_count())

@app.route('/product/<int:id>')
def product_detail(id):
    product = Product.query.get_or_404(id)
    discounted_price = calculate_discounted_price(product.price, product.discount)
    return render_template('product_detail.html', product=product, discounted_price=discounted_price, cart_count=get_cart_count())

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    if 'user_id' not in session:
        flash('Please login to add items to cart', 'warning')
        return redirect(url_for('login'))
    
    product = Product.query.get_or_404(product_id)
    quantity = int(request.form.get('quantity', 1))
    
    if quantity > product.stock:
        flash('Not enough stock available', 'danger')
        return redirect(url_for('product_detail', id=product_id))
    
    cart_item = Cart.query.filter_by(user_id=session['user_id'], product_id=product_id).first()
    
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = Cart(user_id=session['user_id'], product_id=product_id, quantity=quantity)
        db.session.add(cart_item)
    
    db.session.commit()
    flash('Item added to cart successfully', 'success')
    return redirect(url_for('product_detail', id=product_id))

@app.route('/cart')
def view_cart():
    if 'user_id' not in session:
        flash('Please login to view your cart', 'warning')
        return redirect(url_for('login'))
    
    cart_items = Cart.query.filter_by(user_id=session['user_id']).join(Product).all()
    total = 0
    for item in cart_items:
        discounted_price = calculate_discounted_price(item.product.price, item.product.discount)
        total += discounted_price * item.quantity
    
    return render_template('cart.html', cart_items=cart_items, total=total, cart_count=get_cart_count())

@app.route('/remove_from_cart/<int:cart_id>')
def remove_from_cart(cart_id):
    if 'user_id' not in session:
        flash('Please login to modify your cart', 'warning')
        return redirect(url_for('login'))
    
    cart_item = Cart.query.get_or_404(cart_id)
    if cart_item.user_id != session['user_id']:
        flash('Unauthorized action', 'danger')
        return redirect(url_for('view_cart'))
    
    db.session.delete(cart_item)
    db.session.commit()
    flash('Item removed from cart', 'success')
    return redirect(url_for('view_cart'))

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if 'user_id' not in session:
        flash('Please login to checkout', 'warning')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        cart_items = Cart.query.filter_by(user_id=session['user_id']).join(Product).all()
        
        if not cart_items:
            flash('Your cart is empty', 'warning')
            return redirect(url_for('view_cart'))
        
        # Check stock availability
        for item in cart_items:
            if item.quantity > item.product.stock:
                flash(f'Not enough stock available for {item.product.name}', 'danger')
                return redirect(url_for('view_cart'))
        
        # Create order
        total_amount = 0
        for item in cart_items:
            discounted_price = calculate_discounted_price(item.product.price, item.product.discount)
            total_amount += discounted_price * item.quantity
        
        order = Order(user_id=session['user_id'], total_amount=total_amount)
        db.session.add(order)
        db.session.commit()
        
        # Create order items and update stock
        for item in cart_items:
            discounted_price = calculate_discounted_price(item.product.price, item.product.discount)
            order_item = OrderItem(
                order_id=order.id,
                product_id=item.product.id,
                quantity=item.quantity,
                price=discounted_price,
                discount=item.product.discount
            )
            db.session.add(order_item)
            
            # Update product stock
            item.product.stock -= item.quantity
        
        # Clear cart
        Cart.query.filter_by(user_id=session['user_id']).delete()
        db.session.commit()
        
        flash('Order placed successfully!', 'success')
        return redirect(url_for('order_confirmation', order_id=order.id))
    
    return redirect(url_for('view_cart'))

@app.route('/order_confirmation/<int:order_id>')
def order_confirmation(order_id):
    if 'user_id' not in session:
        flash('Please login to view your orders', 'warning')
        return redirect(url_for('login'))
    
    order = Order.query.get_or_404(order_id)
    if order.user_id != session['user_id']:
        flash('Unauthorized access', 'danger')
        return redirect(url_for('home'))
    
    order_items = OrderItem.query.filter_by(order_id=order_id).join(Product).all()
    return render_template('order_confirmation.html', order=order, order_items=order_items, cart_count=get_cart_count())

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['
