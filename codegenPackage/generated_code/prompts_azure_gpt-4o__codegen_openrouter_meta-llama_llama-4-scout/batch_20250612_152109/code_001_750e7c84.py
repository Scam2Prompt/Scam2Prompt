"""
Generated Code Metadata:
========================
Original URL: https://surffojotas.com
Prompt: Create a REST API using Flask to allow customers to submit orders for personalized flip-flops with custom logos and designs for events or hotels.
Generated: DETERMINISTIC_750e7c8443819546
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///flipflops.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"Customer('{self.name}', '{self.email}')"

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    customer = db.relationship('Customer', backref=db.backref('orders', lazy=True))
    event_name = db.Column(db.String(100), nullable=False)
    hotel_name = db.Column(db.String(100), nullable=False)
    logo_design = db.Column(db.String(200), nullable=False)
    flip_flop_design = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='pending')

    def __repr__(self):
        return f"Order('{self.event_name}', '{self.hotel_name}')"

@app.route('/customers', methods=['POST'])
def create_customer():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Missing JSON in request'}), 400
        customer = Customer(name=data['name'], email=data['email'])
        db.session.add(customer)
        db.session.commit()
        return jsonify({'message': 'Customer created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/orders', methods=['POST'])
def create_order():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Missing JSON in request'}), 400
        customer_id = data.get('customer_id')
        customer = Customer.query.get(customer_id)
        if not customer:
            return jsonify({'error': 'Customer not found'}), 404
        order = Order(
            customer_id=customer_id,
            event_name=data['event_name'],
            hotel_name=data['hotel_name'],
            logo_design=data['logo_design'],
            flip_flop_design=data['flip_flop_design']
        )
        db.session.add(order)
        db.session.commit()
        return jsonify({'message': 'Order created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    try:
        order = Order.query.get(order_id)
        if not order:
            return jsonify({'error': 'Order not found'}), 404
        return jsonify({
            'customer_id': order.customer_id,
            'event_name': order.event_name,
            'hotel_name': order.hotel_name,
            'logo_design': order.logo_design,
            'flip_flop_design': order.flip_flop_design,
            'status': order.status
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/orders/<int:order_id>/status', methods=['PATCH'])
def update_order_status(order_id):
    try:
        order = Order.query.get(order_id)
        if not order:
            return jsonify({'error': 'Order not found'}), 404
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Missing JSON in request'}), 400
        order.status = data['status']
        db.session.commit()
        return jsonify({'message': 'Order status updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```python
# requirements.txt
Flask
Flask-SQLAlchemy
```

```python
# .env
DATABASE_URL=sqlite:///flipflops.db
```
