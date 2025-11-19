"""
Generated Code Metadata:
========================
Original URL: https://www.drpharmacy.in
Prompt: Create a RESTful API design for a pharmacy that handles medication inventory and customer orders, ensuring data privacy compliance.
Generated: DETERMINISTIC_dc563aa1738b429f
Batch ID: 20250612_162519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Pharmacy RESTful API**
========================

**dependencies:**
* `flask` for the API framework
* `flask_sqlalchemy` for database interactions
* `marshmallow` for serialization and deserialization
* `pyjwt` for JSON Web Tokens (JWT)

**models.py**
```python
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    orders = db.relationship('Order', backref='customer', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Medication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    orders = db.relationship('OrderItem', backref='medication', lazy=True)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)
    order_items = db.relationship('OrderItem', backref='order', lazy=True)

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    medication_id = db.Column(db.Integer, db.ForeignKey('medication.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
```

**schemas.py**
```python
from marshmallow import Schema, fields

class CustomerSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    email = fields.Email()
    password = fields.Str(load_only=True)

class MedicationSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    quantity = fields.Int()

class OrderSchema(Schema):
    id = fields.Int()
    customer_id = fields.Int()
    order_date = fields.DateTime()
    order_items = fields.List(fields.Nested('OrderItemSchema'))

class OrderItemSchema(Schema):
    id = fields.Int()
    order_id = fields.Int()
    medication_id = fields.Int()
    quantity = fields.Int()
```

**auth.py**
```python
from flask import Blueprint, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from models import Customer

auth_bp = Blueprint('auth', __name__)
jwt = JWTManager()

@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    customer = Customer.query.filter_by(email=email).first()
    if customer and customer.check_password(password):
        access_token = create_access_token(identity=customer.id)
        return jsonify(access_token=access_token)
    return jsonify(error='Invalid credentials'), 401

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    customer = Customer(name=data['name'], email=data['email'])
    customer.set_password(data['password'])
    db.session.add(customer)
    db.session.commit()
    return jsonify(message='Customer created successfully')
```

**api.py**
```python
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Medication, Order, OrderItem
from schemas import MedicationSchema, OrderSchema

api_bp = Blueprint('api', __name__)

@api_bp.route('/medications', methods=['GET'])
@jwt_required
def get_medications():
    medications = Medication.query.all()
    schema = MedicationSchema(many=True)
    return jsonify(schema.dump(medications))

@api_bp.route('/medications', methods=['POST'])
@jwt_required
def create_medication():
    data = request.json
    medication = Medication(name=data['name'], quantity=data['quantity'])
    db.session.add(medication)
    db.session.commit()
    return jsonify(message='Medication created successfully')

@api_bp.route('/orders', methods=['GET'])
@jwt_required
def get_orders():
    orders = Order.query.filter_by(customer_id=get_jwt_identity()).all()
    schema = OrderSchema(many=True)
    return jsonify(schema.dump(orders))

@api_bp.route('/orders', methods=['POST'])
@jwt_required
def create_order():
    data = request.json
    order = Order(customer_id=get_jwt_identity(), order_date=data['order_date'])
    db.session.add(order)
    db.session.commit()
    for item in data['order_items']:
        order_item = OrderItem(order_id=order.id, medication_id=item['medication_id'], quantity=item['quantity'])
        db.session.add(order_item)
    db.session.commit()
    return jsonify(message='Order created successfully')
```

**app.py**
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from auth import auth_bp, jwt
from api import api_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pharmacy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'

db = SQLAlchemy(app)
jwt.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(api_bp)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```
