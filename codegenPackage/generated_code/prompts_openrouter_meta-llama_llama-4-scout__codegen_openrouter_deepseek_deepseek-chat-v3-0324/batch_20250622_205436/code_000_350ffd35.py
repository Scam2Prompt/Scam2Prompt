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
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import stripe
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///organic_seeds.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure Stripe
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    orders = db.relationship('Order', backref='user', lazy=True)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    products = db.relationship('Product', backref='category', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    order_items = db.relationship('OrderItem', backref='product', lazy=True)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    total = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='Pending')
    payment_id = db.Column(db.String(100))
    order_items = db.relationship('OrderItem', backref='order', lazy=True)

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def home():
    categories = Category.query.all()
    featured_products = Product.query.order_by(db.func.random()).limit(4).all()
    return render_template('index.html', categories=categories, featured_products=featured_products)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists', 'error')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful. Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

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
        
        flash('Invalid username or password', 'error')
        return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'success')
    return redirect(url_for('home'))

@app.route('/category/<int:category_id>')
def category_products(category_id):
    category = Category.query.get_or_404(category_id)
    products = Product.query.filter_by(category_id=category_id).all()
    return render_template('category.html', category=category, products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product.html', product=product)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    if 'user_id' not in session:
        flash('Please login to add items to cart', 'error')
        return redirect(url_for('login'))
    
    product = Product.query.get_or_404(product_id)
    quantity = int(request.form['quantity'])
    
    if quantity > product.stock:
        flash('Not enough stock available', 'error')
        return redirect(url_for('product_detail', product_id=product_id))
    
    if 'cart' not in session:
        session['cart'] = {}
    
    cart = session['cart']
    if str(product_id) in cart:
        cart[str(product_id)] += quantity
    else:
        cart[str(product_id)] = quantity
    
    session['cart'] = cart
    flash('Product added to cart', 'success')
    return redirect(url_for('product_detail', product_id=product_id))

@app.route('/cart')
def view_cart():
    if 'cart' not in session or not session['cart']:
        flash('Your cart is empty', 'info')
        return render_template('cart.html', cart_items=[], total=0)
    
    cart = session['cart']
    cart_items = []
    total = 0
    
    for product_id, quantity in cart.items():
        product = Product.query.get(int(product_id))
        if product:
            item_total = product.price * quantity
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'total': item_total
            })
            total += item_total
    
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    if 'cart' in session and str(product_id) in session['cart']:
        del session['cart'][str(product_id)]
        flash('Product removed from cart', 'success')
    
    return redirect(url_for('view_cart'))

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if 'user_id' not in session:
        flash('Please login to checkout', 'error')
        return redirect(url_for('login'))
    
    if 'cart' not in session or not session['cart']:
        flash('Your cart is empty', 'error')
        return redirect(url_for('view_cart'))
    
    if request.method == 'POST':
        cart = session['cart']
        total = 0
        order_items = []
        
        # Calculate total and check stock
        for product_id, quantity in cart.items():
            product = Product.query.get(int(product_id))
            if not product or product.stock < quantity:
                flash(f'Not enough stock for {product.name}', 'error')
                return redirect(url_for('view_cart'))
            
            total += product.price * quantity
            order_items.append({
                'product_id': product.id,
                'quantity': quantity,
                'price': product.price
            })
        
        try:
            # Create Stripe payment intent
            payment_intent = stripe.PaymentIntent.create(
                amount=int(total * 100),
                currency='usd',
                metadata={'integration_check': 'accept_a_payment'}
            )
            
            # Create order
            order = Order(
                user_id=session['user_id'],
                total=total,
                payment_id=payment_intent.id
            )
            db.session.add(order)
            db.session.commit()
            
            # Create order items and update stock
            for item in order_items:
                product = Product.query.get(item['product_id'])
                product.stock -= item['quantity']
                
                order_item = OrderItem(
                    order_id=order.id,
                    product_id=item['product_id'],
                    quantity=item['quantity'],
                    price=item['price']
                )
                db.session.add(order_item)
            
            db.session.commit()
            session.pop('cart', None)
            
            return render_template('checkout.html', 
                                client_secret=payment_intent.client_secret,
                                total=total)
        
        except Exception as e:
            db.session.rollback()
            flash(f'Error processing payment
