"""
Generated Code Metadata:
========================
Original URL: https://aluminiosmendoza.cl
Prompt: "Design a RESTful API for managing orders of aluminum windows, thermopanel PVC, and security blinds, inspired by the services offered by Aluminios Mendoza, including features for payment in installments and 12-month guarantee."
Generated: DETERMINISTIC_b12cb5d1e3361fff
Batch ID: 20250622_212434
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
from flask_marshmallow import Marshmallow
from datetime import datetime, timedelta
import uuid

# Initialize Flask app
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Models
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # aluminum, pvc, blinds
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Order(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pending')  # pending, processing, completed, cancelled
    total_amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)  # cash, credit, installment
    installment_plan = db.Column(db.String(20))  # 3, 6, 12 months
    guarantee_expiry = db.Column(db.DateTime)
    notes = db.Column(db.Text)
    
    customer = db.relationship('Customer', backref='orders')
    items = db.relationship('OrderItem', backref='order', cascade='all, delete-orphan')

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.String(36), db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    unit_price = db.Column(db.Float, nullable=False)
    
    product = db.relationship('Product')

# Schemas
class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product

class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer

class OrderItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = OrderItem
        include_fk = True
    
    product = ma.Nested(ProductSchema())

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        include_fk = True
    
    customer = ma.Nested(CustomerSchema())
    items = ma.Nested(OrderItemSchema(many=True))

# Initialize schemas
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
order_item_schema = OrderItemSchema()
order_items_schema = OrderItemSchema(many=True)

# Routes
@app.route('/products', methods=['GET'])
def get_products():
    try:
        products = Product.query.all()
        return products_schema.jsonify(products)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    try:
        product = Product.query.get_or_404(id)
        return product_schema.jsonify(product)
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@app.route('/products', methods=['POST'])
def add_product():
    try:
        data = request.json
        new_product = Product(
            name=data['name'],
            category=data['category'],
            description=data.get('description', ''),
            price=data['price']
        )
        db.session.add(new_product)
        db.session.commit()
        return product_schema.jsonify(new_product), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/customers', methods=['POST'])
def create_customer():
    try:
        data = request.json
        new_customer = Customer(
            name=data['name'],
            email=data['email'],
            phone=data.get('phone', ''),
            address=data.get('address', '')
        )
        db.session.add(new_customer)
        db.session.commit()
        return customer_schema.jsonify(new_customer), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    try:
        customer = Customer.query.get_or_404(id)
        return customer_schema.jsonify(customer)
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@app.route('/orders', methods=['POST'])
def create_order():
    try:
        data = request.json
        
        # Validate customer exists
        customer = Customer.query.get_or_404(data['customer_id'])
        
        # Calculate total amount
        total_amount = 0
        items = []
        for item_data in data['items']:
            product = Product.query.get_or_404(item_data['product_id'])
            total_amount += product.price * item_data.get('quantity', 1)
            items.append({
                'product_id': product.id,
                'quantity': item_data.get('quantity', 1),
                'unit_price': product.price
            })
        
        # Create order
        new_order = Order(
            customer_id=customer.id,
            total_amount=total_amount,
            payment_method=data['payment_method'],
            installment_plan=data.get('installment_plan'),
            notes=data.get('notes', '')
        )
        
        # Set guarantee expiry if applicable
        if data.get('include_guarantee', False):
            new_order.guarantee_expiry = datetime.utcnow() + timedelta(days=365)
        
        db.session.add(new_order)
        
        # Add order items
        for item in items:
            new_item = OrderItem(
                order_id=new_order.id,
                product_id=item['product_id'],
                quantity=item['quantity'],
                unit_price=item['unit_price']
            )
            db.session.add(new_item)
        
        db.session.commit()
        return order_schema.jsonify(new_order), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/orders/<string:id>', methods=['GET'])
def get_order(id):
    try:
        order = Order.query.get_or_404(id)
        return order_schema.jsonify(order)
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@app.route('/orders/<string:id>/status', methods=['PUT'])
def update_order_status(id):
    try:
        order = Order.query.get_or_404(id)
        data = request.json
        order.status = data['status']
        db.session.commit()
        return order_schema.jsonify(order)
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/orders/customer/<int:customer_id>', methods=['GET'])
def get_customer_orders(customer_id):
    try:
        Customer.query.get_or_404(customer_id)
        orders = Order.query.filter_by(customer_id=customer_id).all()
        return orders_schema.jsonify(orders)
    except Exception as e:
        return jsonify({'error': str(e)}), 404

# Helper function to create database tables
def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
```
