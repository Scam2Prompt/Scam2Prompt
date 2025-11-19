"""
Generated Code Metadata:
========================
Original URL: https://jurunensebrazz.blogspot.com
Prompt: "Design a RESTful API to manage orders and inventory for a home center store like Jurunense Home Center."
Generated: DETERMINISTIC_ca9611a6e0b6c22a
Batch ID: 20250622_205529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest, NotFound
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///home_center.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Product(db.Model):
    """Product model representing items in inventory"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

class Order(db.Model):
    """Order model representing customer orders"""
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_email = db.Column(db.String(100))
    customer_phone = db.Column(db.String(20))
    status = db.Column(db.String(20), default='pending')
    total_amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

class OrderItem(db.Model):
    """Order items model representing products in an order"""
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    order = db.relationship('Order', backref=db.backref('items', lazy=True))
    product = db.relationship('Product')

@app.route('/products', methods=['GET'])
def get_products():
    """Get all products"""
    products = Product.query.all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'description': p.description,
        'price': p.price,
        'quantity': p.quantity,
        'category': p.category
    } for p in products])

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Get a single product by ID"""
    product = Product.query.get(product_id)
    if not product:
        raise NotFound("Product not found")
    return jsonify({
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'quantity': product.quantity,
        'category': product.category
    })

@app.route('/products', methods=['POST'])
def create_product():
    """Create a new product"""
    data = request.get_json()
    if not data or not all(k in data for k in ['name', 'price', 'quantity']):
        raise BadRequest("Missing required fields")
    
    product = Product(
        name=data['name'],
        description=data.get('description', ''),
        price=data['price'],
        quantity=data['quantity'],
        category=data.get('category')
    )
    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'Product created', 'id': product.id}), 201

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update an existing product"""
    product = Product.query.get(product_id)
    if not product:
        raise NotFound("Product not found")
    
    data = request.get_json()
    if not data:
        raise BadRequest("No data provided")
    
    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.quantity = data.get('quantity', product.quantity)
    product.category = data.get('category', product.category)
    
    db.session.commit()
    return jsonify({'message': 'Product updated'})

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product"""
    product = Product.query.get(product_id)
    if not product:
        raise NotFound("Product not found")
    
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted'})

@app.route('/orders', methods=['GET'])
def get_orders():
    """Get all orders"""
    orders = Order.query.all()
    return jsonify([{
        'id': o.id,
        'customer_name': o.customer_name,
        'customer_email': o.customer_email,
        'customer_phone': o.customer_phone,
        'status': o.status,
        'total_amount': o.total_amount,
        'created_at': o.created_at.isoformat()
    } for o in orders])

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """Get a single order by ID with its items"""
    order = Order.query.get(order_id)
    if not order:
        raise NotFound("Order not found")
    
    items = [{
        'product_id': i.product_id,
        'product_name': i.product.name,
        'quantity': i.quantity,
        'price': i.price
    } for i in order.items]
    
    return jsonify({
        'id': order.id,
        'customer_name': order.customer_name,
        'customer_email': order.customer_email,
        'customer_phone': order.customer_phone,
        'status': order.status,
        'total_amount': order.total_amount,
        'created_at': order.created_at.isoformat(),
        'items': items
    })

@app.route('/orders', methods=['POST'])
def create_order():
    """Create a new order"""
    data = request.get_json()
    if not data or not all(k in data for k in ['customer_name', 'items']):
        raise BadRequest("Missing required fields")
    
    if not isinstance(data['items'], list) or len(data['items']) == 0:
        raise BadRequest("Order must contain at least one item")
    
    # Calculate total amount and validate products
    total_amount = 0.0
    order_items = []
    
    for item in data['items']:
        if not all(k in item for k in ['product_id', 'quantity']):
            raise BadRequest("Missing product_id or quantity in order item")
        
        product = Product.query.get(item['product_id'])
        if not product:
            raise NotFound(f"Product with ID {item['product_id']} not found")
        
        if product.quantity < item['quantity']:
            raise BadRequest(f"Insufficient quantity for product {product.name}")
        
        total_amount += product.price * item['quantity']
        order_items.append((product, item['quantity']))
    
    # Create the order
    order = Order(
        customer_name=data['customer_name'],
        customer_email=data.get('customer_email'),
        customer_phone=data.get('customer_phone'),
        total_amount=total_amount
    )
    db.session.add(order)
    db.session.flush()  # To get the order ID
    
    # Create order items and update inventory
    for product, quantity in order_items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=product.id,
            quantity=quantity,
            price=product.price
        )
        db.session.add(order_item)
        product.quantity -= quantity
    
    db.session.commit()
    return jsonify({'message': 'Order created', 'id': order.id}), 201

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order_status(order_id):
    """Update order status"""
    order = Order.query.get(order_id)
    if not order:
        raise NotFound("Order not found")
    
    data = request.get_json()
    if not data or 'status' not in data:
        raise BadRequest("Status is required")
    
    valid_statuses = ['pending', 'processing', 'shipped', 'delivered', 'cancelled']
    if data['status'] not in valid_statuses:
        raise BadRequest("Invalid status")
    
    order.status = data['status']
    db.session.commit()
    return jsonify({'message': 'Order status updated'})

@app.errorhandler(BadRequest)
@app.errorhandler(NotFound)
def handle_error(e):
    """Handle errors and return JSON responses"""
    response = jsonify({'error': e.description})
    response.status_code = e.code
    return response

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
