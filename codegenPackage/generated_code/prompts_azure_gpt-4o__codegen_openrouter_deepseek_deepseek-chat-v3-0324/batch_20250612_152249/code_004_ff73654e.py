"""
Generated Code Metadata:
========================
Original URL: https://ramjiacro.com
Prompt: Develop a web application prototype for a textile company like Ramji Acro, allowing customers to browse yarn types (grey, dyed, mélange) and place orders online.
Generated: DETERMINISTIC_ff73654e03701c34
Batch ID: 20250612_152249
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
import os
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///textile.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class YarnType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price_per_unit = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(20), default='kg')
    image_url = db.Column(db.String(200))
    stock = db.Column(db.Integer, default=0)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), default='Pending')
    total_amount = db.Column(db.Float, nullable=False)
    shipping_address = db.Column(db.Text, nullable=False)
    items = db.relationship('OrderItem', backref='order', lazy=True)

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    yarn_type_id = db.Column(db.Integer, db.ForeignKey('yarn_type.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    yarn_type = db.relationship('YarnType')

# Create database tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def home():
    yarn_types = YarnType.query.all()
    return render_template('index.html', yarn_types=yarn_types)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            password = generate_password_hash(request.form['password'])
            phone = request.form.get('phone', '')
            address = request.form.get('address', '')

            # Check if user already exists
            if User.query.filter_by(email=email).first():
                flash('Email already registered. Please login.', 'danger')
                return redirect(url_for('login'))

            new_user = User(
                name=name,
                email=email,
                password=password,
                phone=phone,
                address=address
            )
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash('Registration failed. Please try again.', 'danger')
            return redirect(url_for('register'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['user_name'] = user.name
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password.', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

@app.route('/yarn/<int:yarn_id>')
def yarn_detail(yarn_id):
    yarn = YarnType.query.get_or_404(yarn_id)
    return render_template('yarn_detail.html', yarn=yarn)

@app.route('/cart/add/<int:yarn_id>', methods=['POST'])
def add_to_cart(yarn_id):
    if 'user_id' not in session:
        flash('Please login to add items to cart.', 'warning')
        return redirect(url_for('login'))

    yarn = YarnType.query.get_or_404(yarn_id)
    quantity = int(request.form.get('quantity', 1))

    if quantity > yarn.stock:
        flash('Not enough stock available.', 'danger')
        return redirect(url_for('yarn_detail', yarn_id=yarn_id))

    # Initialize cart in session if not exists
    if 'cart' not in session:
        session['cart'] = {}

    # Add item to cart
    cart = session['cart']
    if str(yarn_id) in cart:
        cart[str(yarn_id)] += quantity
    else:
        cart[str(yarn_id)] = quantity
    session['cart'] = cart

    flash(f'{quantity} {yarn.unit} of {yarn.name} added to cart.', 'success')
    return redirect(url_for('view_cart'))

@app.route('/cart')
def view_cart():
    if 'user_id' not in session:
        flash('Please login to view your cart.', 'warning')
        return redirect(url_for('login'))

    cart_items = []
    total = 0
    if 'cart' in session:
        for yarn_id, quantity in session['cart'].items():
            yarn = YarnType.query.get(yarn_id)
            if yarn:
                item_total = yarn.price_per_unit * quantity
                cart_items.append({
                    'yarn': yarn,
                    'quantity': quantity,
                    'item_total': item_total
                })
                total += item_total

    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/cart/remove/<int:yarn_id>')
def remove_from_cart(yarn_id):
    if 'cart' in session and str(yarn_id) in session['cart']:
        del session['cart'][str(yarn_id)]
        flash('Item removed from cart.', 'info')
    return redirect(url_for('view_cart'))

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if 'user_id' not in session:
        flash('Please login to checkout.', 'warning')
        return redirect(url_for('login'))

    if 'cart' not in session or not session['cart']:
        flash('Your cart is empty.', 'warning')
        return redirect(url_for('home'))

    user = User.query.get(session['user_id'])

    if request.method == 'POST':
        try:
            # Create order
            total = 0
            cart_items = []
            for yarn_id, quantity in session['cart'].items():
                yarn = YarnType.query.get(yarn_id)
                if yarn:
                    total += yarn.price_per_unit * quantity
                    cart_items.append({
                        'yarn': yarn,
                        'quantity': quantity,
                        'price': yarn.price_per_unit
                    })

            shipping_address = request.form.get('shipping_address', user.address)
            if not shipping_address:
                flash('Shipping address is required.', 'danger')
                return redirect(url_for('checkout'))

            new_order = Order(
                user_id=user.id,
                total_amount=total,
                shipping_address=shipping_address
            )
            db.session.add(new_order)
            db.session.flush()  # To get the order ID

            # Add order items
            for item in cart_items:
                order_item = OrderItem(
                    order_id=new_order.id,
                    yarn_type_id=item['yarn'].id,
                    quantity=item['quantity'],
                    unit_price=item['price']
                )
                db.session.add(order_item)
                # Update stock
                item['yarn'].stock -= item['quantity']
                db.session.add(item['yarn'])

            db.session.commit()
            session.pop('cart', None)
            flash('Order placed successfully!', 'success')
            return redirect(url_for('order_confirmation', order_id=new_order.id))
        except Exception as e:
            db.session.rollback()
            flash('Error processing your order. Please try again.', 'danger')
            return redirect(url_for('checkout'))

    # Calculate total for GET request
    total = 0
    if 'cart' in session:
        for yarn_id, quantity in session['cart'].items():
            yarn = YarnType.query.get(yarn_id)
            if yarn:
                total += yarn.price_per_unit * quantity

    return render_template('checkout.html', user=user, total=total)

@app.route('/order/conf
