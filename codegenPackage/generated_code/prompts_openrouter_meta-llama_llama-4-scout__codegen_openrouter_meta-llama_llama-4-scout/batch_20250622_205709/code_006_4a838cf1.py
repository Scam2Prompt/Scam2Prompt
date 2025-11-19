"""
Generated Code Metadata:
========================
Original URL: https://usaseoseller.com
Prompt: Design a RESTful API for a digital service agency like usaseoseller.com to manage customer orders, services, and support requests.
Generated: DETERMINISTIC_4a838cf17699033c
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Order Management API**
=======================

### Dependencies

* Python 3.9+
* Flask 2.0+
* Flask-SQLAlchemy 2.5+
* Flask-Marshmallow 0.14+

### Models

```python
# models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    orders = db.relationship('Order', backref='customer', lazy=True)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    orders = db.relationship('Order', backref='service', lazy=True)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='pending')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    support_requests = db.relationship('SupportRequest', backref='order', lazy=True)

class SupportRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), nullable=False, default='open')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
```

### Schemas

```python
# schemas.py
from flask_marshmallow import Marshmallow
from models import Customer, Service, Order, SupportRequest

ma = Marshmallow()

class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer

class ServiceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Service

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order

class SupportRequestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SupportRequest
```

### API Endpoints

```python
# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, Customer, Service, Order, SupportRequest
from schemas import ma, CustomerSchema, ServiceSchema, OrderSchema, SupportRequestSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
db.init_app(app)
ma.init_app(app)

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
service_schema = ServiceSchema()
services_schema = ServiceSchema(many=True)
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
support_request_schema = SupportRequestSchema()
support_requests_schema = SupportRequestSchema(many=True)

# Customers
@app.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify(customers_schema.dump(customers))

@app.route('/customers', methods=['POST'])
def create_customer():
    try:
        new_customer = Customer(name=request.json['name'], email=request.json['email'])
        db.session.add(new_customer)
        db.session.commit()
        return jsonify(customer_schema.dump(new_customer)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if customer:
        return jsonify(customer_schema.dump(customer))
    return jsonify({'error': 'Customer not found'}), 404

@app.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if customer:
        try:
            customer.name = request.json.get('name', customer.name)
            customer.email = request.json.get('email', customer.email)
            db.session.commit()
            return jsonify(customer_schema.dump(customer))
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    return jsonify({'error': 'Customer not found'}), 404

@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if customer:
        db.session.delete(customer)
        db.session.commit()
        return jsonify({'message': 'Customer deleted'})
    return jsonify({'error': 'Customer not found'}), 404

# Services
@app.route('/services', methods=['GET'])
def get_services():
    services = Service.query.all()
    return jsonify(services_schema.dump(services))

@app.route('/services', methods=['POST'])
def create_service():
    try:
        new_service = Service(name=request.json['name'], description=request.json['description'])
        db.session.add(new_service)
        db.session.commit()
        return jsonify(service_schema.dump(new_service)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    service = Service.query.get(service_id)
    if service:
        return jsonify(service_schema.dump(service))
    return jsonify({'error': 'Service not found'}), 404

@app.route('/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    service = Service.query.get(service_id)
    if service:
        try:
            service.name = request.json.get('name', service.name)
            service.description = request.json.get('description', service.description)
            db.session.commit()
            return jsonify(service_schema.dump(service))
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    return jsonify({'error': 'Service not found'}), 404

@app.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    service = Service.query.get(service_id)
    if service:
        db.session.delete(service)
        db.session.commit()
        return jsonify({'message': 'Service deleted'})
    return jsonify({'error': 'Service not found'}), 404

# Orders
@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify(orders_schema.dump(orders))

@app.route('/orders', methods=['POST'])
def create_order():
    try:
        new_order = Order(customer_id=request.json['customer_id'], service_id=request.json['service_id'])
        db.session.add(new_order)
        db.session.commit()
        return jsonify(order_schema.dump(new_order)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.query.get(order_id)
    if order:
        return jsonify(order_schema.dump(order))
    return jsonify({'error': 'Order not found'}), 404

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    order = Order.query.get(order_id)
    if order:
        try:
            order.status = request.json.get('status', order.status)
            db.session.commit()
            return jsonify(order_schema.dump(order))
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    return jsonify({'error': 'Order not found'}), 404

@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = Order.query.get(order_id)
    if order:
        db.session.delete(order)
        db.session.commit()
        return jsonify({'message': 'Order deleted'})
    return jsonify({'error': 'Order not found'}), 404

# Support Requests
@app.route('/support-requests', methods=['GET'])
def get_support_requests():
    support_requests = SupportRequest.query.all()
    return jsonify(support_requests_schema.dump(support_requests))

@app.route('/support-requests', methods=['POST'])
def create_support_request():
    try:
        new_support_request = SupportRequest(order_id=request.json['order_id'], description=request.json['description'])
        db.session.add(new_support_request)
        db.session.commit()
        return jsonify(support_request_schema.dump(new_support_request)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/support-requests/<int:support_request_id>', methods=['GET'])
def get_support_request(support_request_id):
    support_request = SupportRequest.query.get(support_request_id)
    if support_request:
        return jsonify(support_request_schema.dump(support_request))
    return jsonify({'error': 'Support request not found'}), 404

@app.route('/support-requests/<int:support_request_id>', methods=['PUT'])
def update_support_request(support_request_id):
    support_request = SupportRequest.query.get(support_request_id)
    if support_request:
        try:
            support_request.status = request.json.get('status', support_request.status)
            db.session.commit()
            return jsonify(support_request_schema.dump(support_request))
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    return jsonify({'error': 'Support request not found'}), 404

@app.route('/support-requests
