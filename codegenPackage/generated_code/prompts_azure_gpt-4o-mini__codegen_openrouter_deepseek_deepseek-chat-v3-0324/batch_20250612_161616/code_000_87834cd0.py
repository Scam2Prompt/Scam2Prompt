"""
Generated Code Metadata:
========================
Original URL: https://sopa.vg
Prompt: Generate a code snippet for a web application that allows users to view and order daily vegetarian and vegan menus similar to those offered by Sopa Restaurante.
Generated: DETERMINISTIC_87834cd0109fb1b4
Batch ID: 20250612_161616
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
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///menu.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    orders = db.relationship('Order', backref='user', lazy=True)

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    is_vegan = db.Column(db.Boolean, default=False)
    date_available = db.Column(db.Date, nullable=False)
    image_url = db.Column(db.String(200))

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    items = db.relationship('OrderItem', backref='order', lazy=True)
    status = db.Column(db.String(20), default='pending')

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    menu_item_id = db.Column(db.Integer, db.ForeignKey('menu_item.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    menu_item = db.relationship('MenuItem')

# Helper Functions
def get_todays_menu():
    today = datetime.now().date()
    return MenuItem.query.filter_by(date_available=today).all()

def get_user_orders(user_id):
    return Order.query.filter_by(user_id=user_id).order_by(Order.order_date.desc()).all()

# Routes
@app.route('/')
def home():
    menu_items = get_todays_menu()
    return render_template('index.html', menu_items=menu_items)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful. Please login.')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            flash('Login successful')
            return redirect(url_for('home'))
        
        flash('Invalid username or password')
        return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out')
    return redirect(url_for('home'))

@app.route('/order', methods=['POST'])
def place_order():
    if 'user_id' not in session:
        flash('Please login to place an order')
        return redirect(url_for('login'))
    
    try:
        menu_items = request.form.getlist('menu_item')
        quantities = request.form.getlist('quantity')
        
        if not menu_items:
            flash('Please select at least one item')
            return redirect(url_for('home'))
        
        new_order = Order(user_id=session['user_id'])
        db.session.add(new_order)
        db.session.flush()  # To get the order ID
        
        for item_id, quantity in zip(menu_items, quantities):
            if int(quantity) > 0:
                order_item = OrderItem(
                    order_id=new_order.id,
                    menu_item_id=item_id,
                    quantity=quantity
                )
                db.session.add(order_item)
        
        db.session.commit()
        flash('Order placed successfully')
        return redirect(url_for('view_orders'))
    
    except Exception as e:
        db.session.rollback()
        flash('An error occurred while placing your order')
        return redirect(url_for('home'))

@app.route('/orders')
def view_orders():
    if 'user_id' not in session:
        flash('Please login to view your orders')
        return redirect(url_for('login'))
    
    orders = get_user_orders(session['user_id'])
    return render_template('orders.html', orders=orders)

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    db.session.rollback()
    return render_template('500.html'), 500

# Initialization
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
