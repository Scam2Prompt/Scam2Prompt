"""
Generated Code Metadata:
========================
Original URL: https://karenfixing.com
Prompt: "Develop a RESTful API for managing orders and payments for dry facade system products, including authentication and error handling."
Generated: DETERMINISTIC_914b033fac995088
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Order and Payment API**
=========================

**dependencies:**
* `flask` for the API framework
* `flask_sqlalchemy` for database interactions
* `flask_jwt_extended` for authentication
* `marshmallow` for serialization and deserialization

**models.py**
```python
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Float, nullable=False)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    payment_method = db.Column(db.String(100), nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False)
```

**schemas.py**
```python
from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    password = fields.Str(load_only=True)

class ProductSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    price = fields.Float()

class OrderSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    product_id = fields.Int()
    quantity = fields.Int()
    total = fields.Float()

class PaymentSchema(Schema):
    id = fields.Int()
    order_id = fields.Int()
    payment_method = fields.Str()
    payment_date = fields.DateTime()
```

**auth.py**
```python
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from models import User

jwt = JWTManager()

def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity=username)
        return access_token
    return None

@jwt_required
def get_current_user():
    return get_jwt_identity()
```

**api.py**
```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import ValidationError
from models import db, User, Product, Order, Payment
from schemas import UserSchema, ProductSchema, OrderSchema, PaymentSchema
from auth import jwt, authenticate_user, get_current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dry_facade.db'
db.init_app(app)
jwt.init_app(app)

# User Endpoints

@app.route('/users', methods=['POST'])
def create_user():
    try:
        user_schema = UserSchema()
        data = user_schema.load(request.json)
        user = User(username=data['username'])
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400

@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.json['username']
        password = request.json['password']
        access_token = authenticate_user(username, password)
        if access_token:
            return jsonify({'access_token': access_token}), 200
        return jsonify({'error': 'Invalid credentials'}), 401
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400

# Product Endpoints

@app.route('/products', methods=['GET'])
@jwt_required
def get_products():
    try:
        products = Product.query.all()
        product_schema = ProductSchema(many=True)
        return jsonify(product_schema.dump(products)), 200
    except Exception as err:
        return jsonify({'error': str(err)}), 500

@app.route('/products', methods=['POST'])
@jwt_required
def create_product():
    try:
        product_schema = ProductSchema()
        data = product_schema.load(request.json)
        product = Product(name=data['name'], price=data['price'])
        db.session.add(product)
        db.session.commit()
        return jsonify({'message': 'Product created successfully'}), 201
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400

# Order Endpoints

@app.route('/orders', methods=['GET'])
@jwt_required
def get_orders():
    try:
        user_id = get_current_user()
        orders = Order.query.filter_by(user_id=user_id).all()
        order_schema = OrderSchema(many=True)
        return jsonify(order_schema.dump(orders)), 200
    except Exception as err:
        return jsonify({'error': str(err)}), 500

@app.route('/orders', methods=['POST'])
@jwt_required
def create_order():
    try:
        order_schema = OrderSchema()
        data = order_schema.load(request.json)
        user_id = get_current_user()
        order = Order(user_id=user_id, product_id=data['product_id'], quantity=data['quantity'], total=data['total'])
        db.session.add(order)
        db.session.commit()
        return jsonify({'message': 'Order created successfully'}), 201
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400

# Payment Endpoints

@app.route('/payments', methods=['GET'])
@jwt_required
def get_payments():
    try:
        payments = Payment.query.all()
        payment_schema = PaymentSchema(many=True)
        return jsonify(payment_schema.dump(payments)), 200
    except Exception as err:
        return jsonify({'error': str(err)}), 500

@app.route('/payments', methods=['POST'])
@jwt_required
def create_payment():
    try:
        payment_schema = PaymentSchema()
        data = payment_schema.load(request.json)
        payment = Payment(order_id=data['order_id'], payment_method=data['payment_method'], payment_date=data['payment_date'])
        db.session.add(payment)
        db.session.commit()
        return jsonify({'message': 'Payment created successfully'}), 201
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
