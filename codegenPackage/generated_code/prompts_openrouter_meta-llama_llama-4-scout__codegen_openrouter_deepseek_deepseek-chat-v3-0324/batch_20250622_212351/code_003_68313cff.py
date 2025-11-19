"""
Generated Code Metadata:
========================
Original URL: https://la-guarida.com.ar
Prompt: "Create a Python script to integrate e-commerce functionality into a website, referencing La Guarida's digital solutions approach."
Generated: DETERMINISTIC_68313cfffb4ec806
Batch ID: 20250622_212351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
E-commerce Integration Script for Website
Inspired by La Guarida's Digital Solutions Approach

This script provides core e-commerce functionality including:
- Product management
- Shopping cart operations
- Order processing
- Payment gateway integration
"""

import os
import json
import uuid
from datetime import datetime
from typing import Dict, List, Optional
import stripe  # type: ignore
from flask import Flask, request, jsonify, session, redirect, url_for  # type: ignore
from flask_sqlalchemy import SQLAlchemy  # type: ignore
from werkzeug.security import generate_password_hash, check_password_hash  # type: ignore

# Initialize Flask application
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY') or 'dev-secret-key'

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Stripe configuration
stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

# Models
class User(db.Model):
    """User model for authentication and profile management"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Product(db.Model):
    """Product model for inventory management"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(200))
    category = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Order(db.Model):
    """Order model for tracking customer purchases"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    order_number = db.Column(db.String(20), unique=True)
    total_amount = db.Column(db.Float)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    payment_id = db.Column(db.String(100))
    shipping_address = db.Column(db.Text)

class OrderItem(db.Model):
    """Order items model for tracking products in orders"""
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)

# Helper functions
def generate_order_number():
    """Generate a unique order number"""
    return f"ORD-{uuid.uuid4().hex[:8].upper()}"

def calculate_cart_total(cart_items: List[Dict]) -> float:
    """Calculate total amount for cart items"""
    return sum(item['price'] * item['quantity'] for item in cart_items)

# Routes
@app.route('/')
def home():
    """Home page with featured products"""
    products = Product.query.filter(Product.stock > 0).limit(8).all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'price': p.price,
        'image_url': p.image_url
    } for p in products])

@app.route('/products')
def list_products():
    """List all available products"""
    category = request.args.get('category')
    query = Product.query.filter(Product.stock > 0)
    
    if category:
        query = query.filter(Product.category == category)
    
    products = query.all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'price': p.price,
        'image_url': p.image_url,
        'category': p.category
    } for p in products])

@app.route('/products/<int:product_id>')
def product_detail(product_id):
    """Get details for a specific product"""
    product = Product.query.get_or_404(product_id)
    return jsonify({
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'stock': product.stock,
        'image_url': product.image_url,
        'category': product.category
    })

@app.route('/cart', methods=['GET'])
def view_cart():
    """View current shopping cart"""
    cart = session.get('cart', [])
    return jsonify(cart)

@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    """Add product to shopping cart"""
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)
    
    product = Product.query.get_or_404(product_id)
    
    if product.stock < quantity:
        return jsonify({'error': 'Not enough stock available'}), 400
    
    cart = session.get('cart', [])
    
    # Check if product already in cart
    for item in cart:
        if item['product_id'] == product_id:
            item['quantity'] += quantity
            break
    else:
        cart.append({
            'product_id': product_id,
            'name': product.name,
            'price': product.price,
            'quantity': quantity,
            'image_url': product.image_url
        })
    
    session['cart'] = cart
    return jsonify({'message': 'Product added to cart', 'cart': cart})

@app.route('/cart/update/<int:product_id>', methods=['PUT'])
def update_cart_item(product_id):
    """Update quantity of a cart item"""
    data = request.get_json()
    new_quantity = data.get('quantity')
    
    product = Product.query.get_or_404(product_id)
    
    if product.stock < new_quantity:
        return jsonify({'error': 'Not enough stock available'}), 400
    
    cart = session.get('cart', [])
    
    for item in cart:
        if item['product_id'] == product_id:
            item['quantity'] = new_quantity
            break
    
    session['cart'] = cart
    return jsonify({'message': 'Cart updated', 'cart': cart})

@app.route('/cart/remove/<int:product_id>', methods=['DELETE'])
def remove_from_cart(product_id):
    """Remove product from shopping cart"""
    cart = session.get('cart', [])
    session['cart'] = [item for item in cart if item['product_id'] != product_id]
    return jsonify({'message': 'Product removed from cart', 'cart': session['cart']})

@app.route('/checkout', methods=['POST'])
def checkout():
    """Process order checkout"""
    if 'user_id' not in session:
        return jsonify({'error': 'Authentication required'}), 401
    
    cart = session.get('cart', [])
    if not cart:
        return jsonify({'error': 'Cart is empty'}), 400
    
    # Verify stock availability
    for item in cart:
        product = Product.query.get(item['product_id'])
        if product.stock < item['quantity']:
            return jsonify({'error': f'Not enough stock for {product.name}'}), 400
    
    # Create order
    order_number = generate_order_number()
    total_amount = calculate_cart_total(cart)
    
    data = request.get_json()
    shipping_address = data.get('shipping_address', '')
    
    new_order = Order(
        user_id=session['user_id'],
        order_number=order_number,
        total_amount=total_amount,
        shipping_address=shipping_address
    )
    db.session.add(new_order)
    db.session.flush()  # To get the order ID
    
    # Add order items
    for item in cart:
        product = Product.query.get(item['product_id'])
        order_item = OrderItem(
            order_id=new_order.id,
            product_id=product.id,
            quantity=item['quantity'],
            price=product.price
        )
        db.session.add(order_item)
        
        # Update product stock
        product.stock -= item['quantity']
    
    # Process payment
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=int(total_amount * 100),  # Amount in cents
            currency='usd',
            metadata={'order_number': order_number}
        )
        
        new_order.payment_id = payment_intent.id
        db.session.commit()
        
        # Clear cart
        session.pop('cart', None)
        
        return jsonify({
            'order_number': order_number,
            'total_amount': total_amount,
            'client_secret': payment_intent.client_secret
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}),
