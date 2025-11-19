"""
Generated Code Metadata:
========================
Original URL: https://foolz.sellpass.io
Prompt: Design a customizable storefront using Sellpass for selling digital products, including subscriptions and serials.
Generated: DETERMINISTIC_deaeab893e254d05
Batch ID: 20250622_204915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import stripe
from datetime import datetime, timedelta
import secrets
import string

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///storefront.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Configure Stripe
stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    subscriptions = db.relationship('Subscription', backref='user', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    is_subscription = db.Column(db.Boolean, default=False)
    subscription_duration = db.Column(db.Integer)  # in days
    digital_file = db.Column(db.String(200))
    serials = db.relationship('Serial', backref='product', lazy=True)

class Serial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    serial_key = db.Column(db.String(100), unique=True, nullable=False)
    is_used = db.Column(db.Boolean, default=False)

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    end_date = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=True)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_intent = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    serial_key = db.Column(db.String(100))

# Helper functions
def generate_serial_key(length=16):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid email or password')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists')
            return redirect(url_for('register'))
        
        new_user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password)
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('index'))
    return render_template('register.html'))

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)

@app.route('/create-checkout-session', methods=['POST'])
@login_required
def create_checkout_session():
    product_id = request.form.get('product_id')
    product = Product.query.get_or_404(product_id)
    
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': product.name,
                    },
                    'unit_amount': int(product.price * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=url_for('payment_success', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=url_for('product_detail', product_id=product_id, _external=True),
        )
        
        # Create order record
        new_order = Order(
            user_id=current_user.id,
            product_id=product.id,
            amount=product.price,
            payment_intent=checkout_session.payment_intent,
            status='pending'
        )
        db.session.add(new_order)
        db.session.commit()
        
        return jsonify({'id': checkout_session.id})
    except Exception as e:
        return jsonify(error=str(e)), 403

@app.route('/payment-success')
@login_required
def payment_success():
    session_id = request.args.get('session_id')
    try:
        session = stripe.checkout.Session.retrieve(session_id)
        order = Order.query.filter_by(payment_intent=session.payment_intent).first()
        
        if order and order.status == 'pending':
            order.status = 'completed'
            
            # Handle product delivery
            product = Product.query.get(order.product_id)
            
            if product.is_subscription:
                # Create subscription
                end_date = datetime.utcnow() + timedelta(days=product.subscription_duration)
                subscription = Subscription(
                    user_id=current_user.id,
                    product_id=product.id,
                    end_date=end_date
                )
                db.session.add(subscription)
            else:
                # Assign serial key
                available_serial = Serial.query.filter_by(product_id=product.id, is_used=False).first()
                if available_serial:
                    available_serial.is_used = True
                    order.serial_key = available_serial.serial_key
                else:
                    flash('No available serial keys for this product')
            
            db.session.commit()
            return render_template('payment_success.html', order=order)
        else:
            flash('Order not found or already processed')
            return redirect(url_for('index'))
    except Exception as e:
        flash(str(e))
        return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    subscriptions = Subscription.query.filter_by(user_id=current_user.id, is_active=True).all()
    orders = Order.query.filter_by(user_id=current_user.id).order_by(Order.created_at.desc()).limit(5).all()
    return render_template('dashboard.html', subscriptions=subscriptions, orders=orders)

# Admin routes
@app.route('/admin')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        flash('Access denied')
        return redirect(url_for('index'))
    
    products = Product.query.all()
    users = User.query.all()
    orders = Order.query.order_by(Order.created_at.desc()).limit(10).all()
    return render_template('admin/dashboard.html', products=products, users=users, orders=orders)

@app.route('/admin/product/new', methods=['GET', 'POST'])
@login_required
def admin_add_product():
    if not current_user.is_admin:
        flash('Access denied')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = float(request.form.get('price'))
        is_subscription = 'is_subscription' in request.form
        subscription_duration = int(request.form.get('subscription_duration', 0))
