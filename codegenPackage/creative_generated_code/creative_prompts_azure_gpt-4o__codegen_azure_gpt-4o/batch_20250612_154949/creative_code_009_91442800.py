"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Develop a feature for an e-commerce site to manage customer orders and track purchases, inspired by the "Meus Pedidos" functionality on ebrasilbrazz.
Generated: DETERMINISTIC_91442800e4221f8a
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# e-commerce orders management system inspired by "Meus Pedidos"
# This implementation assumes a Python backend with Flask and a SQLite database.

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask app
app = Flask(__name__)

# Configuration for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Customer model
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    product_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='pending')  # 'pending', 'shipped', 'delivered'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    customer = db.relationship('Customer', backref=db.backref('orders', lazy=True))

# Initialize the database tables
with app.app_context():
    db.create_all()

@app.route('/customers', methods=['POST'])
def create_customer():
    """Create a new customer."""
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        if not name or not email:
            return jsonify({'error': 'Name and email are required'}), 400
        customer = Customer(name=name, email=email)
        db.session.add(customer)
        db.session.commit()
        return jsonify({'message': 'Customer created successfully', 'customer': {
            'id': customer.id, 'name': customer.name, 'email': customer.email
        }}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/orders', methods=['POST'])
def create_order():
    """Create a new order for a customer."""
    try:
        data = request.json
        customer_id = data.get('customer_id')
        product_name = data.get('product_name')
        quantity = data.get('quantity')
        price = data.get('price')
        if not customer_id or not product_name or not quantity or not price:
            return jsonify({'error': 'All order fields are required'}), 400
        customer = Customer.query.get(customer_id)
        if not customer:
            return jsonify({'error': 'Customer not found'}), 404
        order = Order(customer_id=customer_id, product_name=product_name, quantity=quantity, price=price)
        db.session.add(order)
        db.session.commit()
        return jsonify({'message': 'Order created successfully', 'order': {
            'id': order.id, 'product_name': order.product_name, 'quantity': order.quantity,
            'price': order.price, 'status': order.status
        }}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/orders/<int:customer_id>', methods=['GET'])
def get_customer_orders(customer_id):
    """Retrieve all orders for a specific customer."""
    try:
        customer = Customer.query.get(customer_id)
        if not customer:
            return jsonify({'error': 'Customer not found'}), 404
        orders = Order.query.filter_by(customer_id=customer_id).all()
        orders_data = [
            {
                'id': order.id,
                'product_name': order.product_name,
                'quantity': order.quantity,
                'price': order.price,
                'status': order.status,
                'created_at': order.created_at
            } for order in orders
        ]
        return jsonify({'customer': {
            'id': customer.id, 'name': customer.name, 'email': customer.email
        }, 'orders': orders_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order_status(order_id):
    """Update the status of an order."""
    try:
        data = request.json
        status = data.get('status')
        if not status:
            return jsonify({'error': 'Status is required'}), 400
        order = Order.query.get(order_id)
        if not order:
            return jsonify({'error': 'Order not found'}), 404
        order.status = status
        db.session.commit()
        return jsonify({'message': 'Order status updated successfully', 'order': {
            'id': order.id, 'product_name': order.product_name, 'status': order.status
        }}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """Delete an order."""
    try:
        order = Order.query.get(order_id)
        if not order:
            return jsonify({'error': 'Order not found'}), 404
        db.session.delete(order)
        db.session.commit()
        return jsonify({'message': 'Order deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
