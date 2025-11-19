"""
Generated Code Metadata:
========================
Original URL: https://maderaselaboradas.com.ar
Prompt: Generate a code snippet for a web application that allows users to order wooden products, specifically focusing on the features of "Maderas Aserradas" and "Cabos" as described on the Maderas Elaboradas website.
Generated: DETERMINISTIC_4005ac386d548f17
Batch ID: 20250612_163251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready code snippet for a web application focused on ordering wooden products:

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'dev-key-123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wood_products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200))
    orders = db.relationship('Order', backref='customer', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)  # 'maderas_aserradas' or 'cabos'
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price_per_unit = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(20), nullable=False)  # 'm2', 'piece', 'meter', etc.
    stock = db.Column(db.Integer, default=0)
    image_url = db.Column(db.String(200))

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pending')  # pending, processing, shipped, delivered
    total_price = db.Column(db.Float, nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    maderas_aserradas = Product.query.filter_by(category='maderas_aserradas').all()
    cabos = Product.query.filter_by(category='cabos').all()
    return render_template('index.html', 
                         maderas_aserradas=maderas_aserradas,
                         cabos=cabos)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)
    quantity = int(request.form.get('quantity', 1))
    
    if quantity <= 0:
        flash('Invalid quantity', 'error')
        return redirect(url_for('product_detail', product_id=product_id))
    
    if quantity > product.stock:
        flash('Not enough stock available', 'error')
        return redirect(url_for('product_detail', product_id=product_id))
    
    # In a real app, you'd add to a cart session or create a Cart model
    # For simplicity, we'll create an order directly
    new_order = Order(
        user_id=current_user.id,
        product_id=product.id,
        quantity=quantity,
        total_price=quantity * product.price_per_unit
    )
    
    try:
        db.session.add(new_order)
        product.stock -= quantity
        db.session.commit()
        flash('Product added to your order successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error processing your order. Please try again.', 'error')
        app.logger.error(f"Order error: {str(e)}")
    
    return redirect(url_for('product_detail', product_id=product_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if not user or not check_password_hash(user.password_hash, password):
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))
        
        login_user(user)
        flash('Logged in successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return redirect(url_for('register'))
        
        new_user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password)
        )
        
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully! Please log in.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash('Error creating account. Please try again.', 'error')
            app.logger.error(f"Registration error: {str(e)}")
    
    return render_template('register.html')

@app.route('/my_orders')
@login_required
def my_orders():
    orders = Order.query.filter_by(user_id=current_user.id).order_by(Order.order_date.desc()).all()
    return render_template('my_orders.html', orders=orders)

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    db.session.rollback()
    return render_template('500.html'), 500

# Helper function to initialize sample data
def init_sample_data():
    # This would be called once to populate initial products
    sample_products = [
        # Maderas Aserradas
        Product(
            category='maderas_aserradas',
            name='Pino',
            description='Madera de pino aserrada de alta calidad',
            price_per_unit=150.00,
            unit='m2',
            stock=100,
            image_url='/static/images/pino.jpg'
        ),
        Product(
            category='maderas_aserradas',
            name='Cedro',
            description='Madera de cedro aserrada premium',
            price_per_unit=250.00,
            unit='m2',
            stock=75,
            image_url='/static/images/cedro.jpg'
        ),
        # Cabos
        Product(
            category='cabos',
            name='Cabo de Escoba',
            description='Cabo de escoba de madera resistente',
            price_per_unit=45.00,
            unit='piece',
            stock=200,
            image_url='/static/images/cabo_escoba.jpg'
        ),
        Product(
            category='cabos',
            name='Cabo de Pala',
            description='Cabo de pala reforzado',
            price_per_unit=60.00,
            unit='piece',
            stock=150,
            image_url='/static/images/cabo_pala.jpg'
        )
    ]
    
    for product in sample_products:
        if not Product.query.filter_by(name=product.name).first():
            db.session.add(product)
    
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        init_sample_data()
    app.run(debug=True)
```

Note: This is a complete Flask application that would require corresponding HTML templates (not included here) to work fully. The code includes user authentication, product management, and order processing for both "Maderas Aserradas" and "Cabos" product categories.
