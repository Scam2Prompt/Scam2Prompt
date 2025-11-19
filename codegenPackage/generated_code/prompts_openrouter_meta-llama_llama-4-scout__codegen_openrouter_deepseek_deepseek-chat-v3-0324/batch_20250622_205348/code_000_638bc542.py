"""
Generated Code Metadata:
========================
Original URL: https://games-home-plays-galla.weebly.com
Prompt: Write a Python code snippet to create an e-commerce website similar to Baby Calçados, including features for product browsing, shopping cart management, and payment processing.
Generated: DETERMINISTIC_638bc542ff37ac70
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import stripe
import os
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Stripe configuration
stripe.api_key = os.environ.get('STRIPE_SECRET_KEY') or 'your-stripe-secret-key'
stripe_public_key = os.environ.get('STRIPE_PUBLIC_KEY') or 'your-stripe-public-key'

# Initialize database
db = SQLAlchemy(app)

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Database models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    orders = db.relationship('Order', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(100))
    stock = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50))

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    total = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='Pending')
    items = db.relationship('OrderItem', backref='order', lazy=True)

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    product = db.relationship('Product')

# User loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def home():
    products = Product.query.limit(8).all()
    return render_template('index.html', products=products)

@app.route('/products')
def products():
    category = request.args.get('category')
    if category:
        products = Product.query.filter_by(category=category).all()
    else:
        products = Product.query.all()
    return render_template('products.html', products=products)

@app.route('/product/<int:id>')
def product_detail(id):
    product = Product.query.get_or_404(id)
    return render_template('product_detail.html', product=product)

@app.route('/add_to_cart/<int:product_id>')
@login_required
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    
    product = Product.query.get_or_404(product_id)
    
    # Check if product is already in cart
    cart_item = next((item for item in session['cart'] if item['id'] == product_id), None)
    
    if cart_item:
        if cart_item['quantity'] < product.stock:
            cart_item['quantity'] += 1
    else:
        session['cart'].append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'quantity': 1,
            'image': product.image
        })
    
    session.modified = True
    flash('Product added to cart!', 'success')
    return redirect(request.referrer)

@app.route('/cart')
@login_required
def cart():
    cart_items = session.get('cart', [])
    total = sum(item['price'] * item['quantity'] for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/remove_from_cart/<int:index>')
@login_required
def remove_from_cart(index):
    try:
        session['cart'].pop(index)
        session.modified = True
        flash('Item removed from cart', 'success')
    except IndexError:
        flash('Item not found in cart', 'error')
    return redirect(url_for('cart'))

@app.route('/checkout')
@login_required
def checkout():
    cart_items = session.get('cart', [])
    if not cart_items:
        flash('Your cart is empty', 'warning')
        return redirect(url_for('cart'))
    
    total = sum(item['price'] * item['quantity'] for item in cart_items)
    return render_template('checkout.html', cart_items=cart_items, total=total, 
                          stripe_public_key=stripe_public_key)

@app.route('/process_payment', methods=['POST'])
@login_required
def process_payment():
    cart_items = session.get('cart', [])
    if not cart_items:
        flash('Your cart is empty', 'warning')
        return redirect(url_for('cart'))
    
    total = sum(item['price'] * item['quantity'] for item in cart_items)
    
    try:
        # Create Stripe charge
        charge = stripe.Charge.create(
            amount=int(total * 100),  # Convert to cents
            currency='usd',
            description='E-commerce Purchase',
            source=request.form['stripeToken']
        )
        
        # Create order
        order = Order(user_id=current_user.id, total=total)
        db.session.add(order)
        
        # Add order items
        for item in cart_items:
            product = Product.query.get(item['id'])
            order_item = OrderItem(
                order_id=order.id,
                product_id=product.id,
                quantity=item['quantity'],
                price=product.price
            )
            db.session.add(order_item)
            
            # Update product stock
            product.stock -= item['quantity']
        
        db.session.commit()
        
        # Clear cart
        session.pop('cart', None)
        
        flash('Payment successful! Your order has been placed.', 'success')
        return redirect(url_for('order_confirmation', order_id=order.id))
    
    except stripe.error.CardError as e:
        flash(f'Payment failed: {e.error.message}', 'error')
        return redirect(url_for('checkout'))
    except Exception as e:
        flash('An error occurred while processing your payment. Please try again.', 'error')
        return redirect(url_for('checkout'))

@app.route('/order_confirmation/<int:order_id>')
@login_required
def order_confirmation(order_id):
    order = Order.query.get_or_404(order_id)
    if order.user_id != current_user.id:
        flash('You are not authorized to view this order', 'error')
        return redirect(url_for('home'))
    return render_template('order_confirmation.html', order=order)

@app.route('/orders')
@login_required
def orders():
    user_orders = Order.query.filter_by(user_id=current_user.id).order_by(Order.date.desc()).all()
    return render_template('orders.html', orders=user_orders)

@app.route('/order/<int:order_id>')
@login_required
def order_detail(order_id):
    order = Order.query.get_or_404(order_id)
    if order.user_id != current_user.id:
        flash('You are not authorized to view this order', 'error')
        return redirect(url_for('home'))
    return render_template('order_detail.html', order=order)

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
            flash('Username already taken', 'error')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return redirect(url_for('register'))
        
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful!
