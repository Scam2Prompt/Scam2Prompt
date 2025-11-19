"""
Generated Code Metadata:
========================
Original URL: https://getgrass.im
Prompt: Write a Python script to create a simple e-commerce website for ordering grass online, including customer testimonials and benefits of the product.
Generated: DETERMINISTIC_7c51ec0891d848b1
Batch ID: 20250622_212235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///grass_shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    orders = db.relationship('Order', backref='customer', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(100), nullable=False, default='default.jpg')

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.String(20), nullable=False, default='Processing')
    product = db.relationship('Product', backref='orders')

class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def home():
    products = Product.query.all()
    testimonials = Testimonial.query.order_by(Testimonial.date_posted.desc()).limit(3).all()
    return render_template('home.html', products=products, testimonials=testimonials)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if User.query.filter_by(username=username).first():
            flash('Username already taken', 'error')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Account created successfully! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if not user or not check_password_hash(user.password, password):
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))
        
        login_user(user)
        return redirect(url_for('home'))
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/products')
def products():
    all_products = Product.query.all()
    return render_template('products.html', products=all_products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)
    quantity = int(request.form.get('quantity', 1))
    
    # Check if product already in cart
    existing_order = Order.query.filter_by(
        user_id=current_user.id,
        product_id=product.id,
        status='Cart'
    ).first()
    
    if existing_order:
        existing_order.quantity += quantity
    else:
        new_order = Order(
            user_id=current_user.id,
            product_id=product.id,
            quantity=quantity,
            status='Cart'
        )
        db.session.add(new_order)
    
    db.session.commit()
    flash('Product added to cart!', 'success')
    return redirect(url_for('product_detail', product_id=product.id))

@app.route('/cart')
@login_required
def cart():
    cart_items = Order.query.filter_by(
        user_id=current_user.id,
        status='Cart'
    ).all()
    
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/checkout', methods=['POST'])
@login_required
def checkout():
    cart_items = Order.query.filter_by(
        user_id=current_user.id,
        status='Cart'
    ).all()
    
    if not cart_items:
        flash('Your cart is empty!', 'error')
        return redirect(url_for('cart'))
    
    for item in cart_items:
        item.status = 'Processing'
    
    db.session.commit()
    flash('Order placed successfully!', 'success')
    return redirect(url_for('orders'))

@app.route('/orders')
@login_required
def orders():
    user_orders = Order.query.filter_by(
        user_id=current_user.id
    ).filter(Order.status != 'Cart').order_by(Order.order_date.desc()).all()
    
    return render_template('orders.html', orders=user_orders)

@app.route('/testimonials')
def testimonials():
    all_testimonials = Testimonial.query.order_by(Testimonial.date_posted.desc()).all()
    return render_template('testimonials.html', testimonials=all_testimonials)

@app.route('/add_testimonial', methods=['GET', 'POST'])
@login_required
def add_testimonial():
    if request.method == 'POST':
        content = request.form.get('content')
        rating = int(request.form.get('rating'))
        
        if not content or rating < 1 or rating > 5:
            flash('Please provide valid testimonial content and rating', 'error')
            return redirect(url_for('add_testimonial'))
        
        new_testimonial = Testimonial(
            author=current_user.username,
            content=content,
            rating=rating
        )
        db.session.add(new_testimonial)
        db.session.commit()
        
        flash('Thank you for your testimonial!', 'success')
        return redirect(url_for('testimonials'))
    
    return render_template('add_testimonial.html')

@app.route('/benefits')
def benefits():
    return render_template('benefits.html')

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    db.session.rollback()
    return render_template('500.html'), 500

# Initialize Database
with app.app_context():
    db.create_all()
    
    # Add sample products if none exist
    if not Product.query.first():
        products = [
            Product(
                name='Premium Grass',
                description='Our highest quality grass, grown with organic fertilizers and natural sunlight.',
                price=19.99,
                image='premium.jpg'
            ),
            Product(
                name='Standard Grass',
                description='Good quality grass at an affordable price. Perfect for everyday use.',
                price=12.99,
                image='standard.jpg'
            ),
            Product(
                name='Budget Grass',
                description='Economical option for those on a tight budget. Still maintains decent quality.',
                price=8.99,
                image='budget.jpg'
            )
        ]
        db.session.add_all(products)
        db.session.commit()
    
    # Add sample testimonials if none exist
    if not Testimonial.query.first():
        testimonials = [
            Testimonial(
                author='Happy Customer',
                content='The grass was delivered quickly and was fresher than I expected! Will definitely order again.',
                rating=5
            ),
            Testimonial(
                author='Lawn Enthusiast',
                content='Great
