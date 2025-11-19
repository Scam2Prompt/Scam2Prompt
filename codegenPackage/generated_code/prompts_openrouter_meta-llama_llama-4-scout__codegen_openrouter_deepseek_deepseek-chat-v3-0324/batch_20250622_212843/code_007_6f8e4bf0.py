"""
Generated Code Metadata:
========================
Original URL: https://florerialima.com
Prompt: Create a RESTful API endpoint to handle customer orders for Florería Lima, including order creation, payment processing, and order status updates.
Generated: DETERMINISTIC_6f8e4bf039ec6096
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import datetime
import stripe

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///floreria_lima.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Initialize Stripe
stripe.api_key = 'your-stripe-secret-key'

# Initialize database
db = SQLAlchemy(app)

# Define models
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(500))
    price = db.Column(db.Float)
    stock = db.Column(db.Integer)
    category = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    total_amount = db.Column(db.Float)
    status = db.Column(db.String(20), default='pending')  # pending, paid, shipped, delivered, cancelled
    payment_method = db.Column(db.String(50))
    payment_status = db.Column(db.String(20), default='unpaid')  # unpaid, paid, failed
    shipping_address = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# Create database tables
with app.app_context():
    db.create_all()

# Helper functions
def validate_order_data(data):
    required_fields = ['customer_id', 'items', 'shipping_address']
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    
    if not isinstance(data['items'], list) or len(data['items']) == 0:
        return False, "Items must be a non-empty list"
    
    for item in data['items']:
        if 'product_id' not in item or 'quantity' not in item:
            return False, "Each item must have product_id and quantity"
    
    return True, ""

def calculate_order_total(items):
    total = 0
    for item in items:
        product = Product.query.get(item['product_id'])
        if not product:
            return None, f"Product with id {item['product_id']} not found"
        if product.stock < item['quantity']:
            return None, f"Insufficient stock for product {product.name}"
        total += product.price * item['quantity']
    return total, ""

# API Endpoints
@app.route('/orders', methods=['POST'])
def create_order():
    """
    Create a new order
    """
    data = request.get_json()
    
    # Validate input data
    is_valid, message = validate_order_data(data)
    if not is_valid:
        return jsonify({'message': message}), 400
    
    # Check customer exists
    customer = Customer.query.get(data['customer_id'])
    if not customer:
        return jsonify({'message': 'Customer not found'}), 404
    
    # Calculate order total and validate stock
    total_amount, message = calculate_order_total(data['items'])
    if total_amount is None:
        return jsonify({'message': message}), 400
    
    try:
        # Create order
        order = Order(
            public_id=str(uuid.uuid4()),
            customer_id=data['customer_id'],
            total_amount=total_amount,
            shipping_address=data['shipping_address']
        )
        db.session.add(order)
        db.session.flush()  # Get the order ID
        
        # Create order items
        for item in data['items']:
            product = Product.query.get(item['product_id'])
            order_item = OrderItem(
                order_id=order.id,
                product_id=item['product_id'],
                quantity=item['quantity'],
                price=product.price
            )
            db.session.add(order_item)
            # Update product stock
            product.stock -= item['quantity']
        
        db.session.commit()
        
        return jsonify({
            'message': 'Order created successfully',
            'order_id': order.public_id,
            'total_amount': order.total_amount
        }), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error creating order: {str(e)}'}), 500

@app.route('/orders/<order_id>/pay', methods=['POST'])
def process_payment(order_id):
    """
    Process payment for an order
    """
    data = request.get_json()
    
    if 'payment_method' not in data or 'payment_token' not in data:
        return jsonify({'message': 'Payment method and token are required'}), 400
    
    order = Order.query.filter_by(public_id=order_id).first()
    if not order:
        return jsonify({'message': 'Order not found'}), 404
    
    if order.payment_status == 'paid':
        return jsonify({'message': 'Order already paid'}), 400
    
    try:
        # Process payment with Stripe
        charge = stripe.Charge.create(
            amount=int(order.total_amount * 100),  # Convert to cents
            currency='usd',
            source=data['payment_token'],
            description=f'Payment for order {order_id}'
        )
        
        # Update order status
        order.payment_status = 'paid'
        order.payment_method = data['payment_method']
        order.status = 'paid'
        db.session.commit()
        
        return jsonify({
            'message': 'Payment processed successfully',
            'order_id': order.public_id,
            'payment_status': order.payment_status
        }), 200
    
    except stripe.error.CardError as e:
        return jsonify({'message': f'Payment failed: {e.user_message}'}), 400
    except Exception as e:
        return jsonify({'message': f'Error processing payment: {str(e)}'}), 500

@app.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    """
    Get order details
    """
    order = Order.query.filter_by(public_id=order_id).first()
    if not order:
        return jsonify({'message': 'Order not found'}), 404
    
    order_items = OrderItem.query.filter_by(order_id=order.id).all()
    items = []
    for item in order_items:
        product = Product.query.get(item.product_id)
        items.append({
            'product_id': item.product_id,
            'product_name': product.name,
            'quantity': item.quantity,
            'price': item.price,
            'subtotal': item.price * item.quantity
        })
    
    return jsonify({
        'order_id': order.public_id,
        'customer_id': order.customer_id,
        'total_amount': order.total_amount,
        'status': order.status,
        'payment_status': order.payment_status,
        'shipping_address': order.shipping_address,
        'created_at': order.created_at,
        'updated_at': order.updated_at,
        'items': items
    }), 200

@app.route('/orders/<order_id>/status', methods=['PUT'])
def update_order_status(order_id):
    """
    Update order status
    """
    data = request.get_json()
    
    if 'status' not in data:
        return jsonify({'message': 'Status is required'}), 400
    
    valid_statuses = ['pending', 'paid', 'shipped', 'delivered', 'cancelled']
    if data['status'] not in valid_statuses:
        return jsonify({'message': 'Invalid status'}), 400
    
    order = Order.query.filter_by(public_id=order_id).first()
    if not order:
        return jsonify({'message': 'Order not found'}), 404
    
    try:
        order.status = data['status']
        db.session.commit()
        
        return jsonify({
            'message': 'Order status updated successfully',
            'order_id': order
