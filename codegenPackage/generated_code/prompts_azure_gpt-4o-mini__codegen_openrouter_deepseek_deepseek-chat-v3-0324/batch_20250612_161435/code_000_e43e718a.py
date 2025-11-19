"""
Generated Code Metadata:
========================
Original URL: https://ontariooffers.com
Prompt: Generate code to create a custom online store for retractable screens, similar to the features offered by Ontario Screen Systems Inc.
Generated: DETERMINISTIC_e43e718a477a9d39
Batch ID: 20250612_161435
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
from werkzeug.utils import secure_filename
import os
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///screens_store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure upload folder for product images
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    orders = db.relationship('Order', backref='user', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(100))
    category = db.Column(db.String(50))
    stock = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    total = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='Pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    items = db.relationship('OrderItem', backref='order', lazy=True)

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    product = db.relationship('Product')

# Create database tables
with app.app_context():
    db.create_all()

# Utility functions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

# Routes
@app.route('/')
def home():
    products = Product.query.limit(4).all()
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

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'danger')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists', 'danger')
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
            session['is_admin'] = user.is_admin
            flash('Login successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'info')
    return redirect(url_for('home'))

@app.route('/cart')
def cart():
    if 'user_id' not in session:
        flash('Please login to view your cart', 'warning')
        return redirect(url_for('login'))
    
    # Implement cart logic here (could use session or database)
    return render_template('cart.html')

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    if 'user_id' not in session:
        flash('Please login to add items to cart', 'warning')
        return redirect(url_for('login'))
    
    # Implement cart addition logic here
    flash('Product added to cart', 'success')
    return redirect(url_for('product_detail', id=product_id))

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if 'user_id' not in session:
        flash('Please login to checkout', 'warning')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        # Process order and payment
        flash('Order placed successfully', 'success')
        return redirect(url_for('order_confirmation'))
    
    return render_template('checkout.html')

@app.route('/order_confirmation')
def order_confirmation():
    return render_template('order_confirmation.html')

@app.route('/account')
def account():
    if 'user_id' not in session:
        flash('Please login to view your account', 'warning')
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    orders = Order.query.filter_by(user_id=user.id).all()
    return render_template('account.html', user=user, orders=orders)

# Admin routes
@app.route('/admin')
def admin_dashboard():
    if 'user_id' not in session or not session.get('is_admin'):
        flash('Unauthorized access', 'danger')
        return redirect(url_for('home'))
    
    products = Product.query.all()
    orders = Order.query.all()
    users = User.query.all()
    return render_template('admin/dashboard.html', products=products, orders=orders, users=users)

@app.route('/admin/products/new', methods=['GET', 'POST'])
def admin_add_product():
    if 'user_id' not in session or not session.get('is_admin'):
        flash('Unauthorized access', 'danger')
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = float(request.form['price'])
        category = request.form['category']
        stock = int(request.form['stock'])
        
        # Handle file upload
        if 'image' not in request.files:
            flash('No file uploaded', 'danger')
            return redirect(request.url)
        
        file = request.files['image']
        if file.filename == '':
            flash('No selected file', 'danger')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            new_product = Product(
                name=name,
                description=description,
                price=price,
                image=filename,
                category=category,
                stock=stock
            )
            db.session.add(new_product)
            db.session.commit()
            
            flash('Product added successfully', 'success')
            return redirect(url_for('admin_dashboard'))
    
    return render_template('admin/add_product.html')

@app.route('/admin/products/edit/<int:id>', methods=['GET', 'POST'])
def admin_edit_product(id):
    if 'user_id' not in session or not session.get('is_admin'):
        flash('Unauthorized access', 'danger')
        return redirect(url_for('home'))
    
    product = Product.query.get_or_404(id)
    
    if request.method == 'POST':
        product.name = request.form['name']
        product.description = request.form['description']
        product.price = float(request.form['price'])
        product.category = request.form['category']
        product.stock = int(request.form['stock'])
        
        # Handle file upload if new image is provided
        if 'image' in request
