"""
Generated Code Metadata:
========================
Original URL: https://crudo-protocol.xyz
Prompt: Generate a code snippet for a CRUDO token-based marketplace for enterprises in the Oil trading industry, enabling buyers, vendors, and distributors to establish new business relationships.
Generated: DETERMINISTIC_6607d7207d4b77c5
Batch ID: 20250622_212302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Oil Trading Marketplace API**
================================

### Dependencies

* Python 3.9+
* Flask 2.0+
* Flask-JWT-Extended 4.0+
* SQLAlchemy 1.4+

### Models
```python
# models.py
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Buyer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    contact_person = db.Column(db.String(100), nullable=False)

class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    contact_person = db.Column(db.String(100), nullable=False)

class Distributor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    contact_person = db.Column(db.String(100), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'), nullable=False)
    product_name = db.Column(db.String(100), nullable=False)
    product_description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.Integer, db.ForeignKey('buyer.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pending')

class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    token = db.Column(db.String(128), nullable=False)
```

### API Endpoints
```python
# app.py
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from models import db, User, Buyer, Vendor, Distributor, Product, Order, Token

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///oil_trading.db'
db.init_app(app)
jwt = JWTManager(app)

# Create
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        user = User(username=data['username'], email=data['email'], role=data['role'])
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/buyer', methods=['POST'])
@jwt_required
def create_buyer():
    try:
        data = request.get_json()
        buyer = Buyer(user_id=get_jwt_identity(), company_name=data['company_name'], contact_person=data['contact_person'])
        db.session.add(buyer)
        db.session.commit()
        return jsonify({'message': 'Buyer created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/vendor', methods=['POST'])
@jwt_required
def create_vendor():
    try:
        data = request.get_json()
        vendor = Vendor(user_id=get_jwt_identity(), company_name=data['company_name'], contact_person=data['contact_person'])
        db.session.add(vendor)
        db.session.commit()
        return jsonify({'message': 'Vendor created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/distributor', methods=['POST'])
@jwt_required
def create_distributor():
    try:
        data = request.get_json()
        distributor = Distributor(user_id=get_jwt_identity(), company_name=data['company_name'], contact_person=data['contact_person'])
        db.session.add(distributor)
        db.session.commit()
        return jsonify({'message': 'Distributor created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/product', methods=['POST'])
@jwt_required
def create_product():
    try:
        data = request.get_json()
        product = Product(vendor_id=data['vendor_id'], product_name=data['product_name'], product_description=data['product_description'], price=data['price'])
        db.session.add(product)
        db.session.commit()
        return jsonify({'message': 'Product created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Read
@app.route('/buyers', methods=['GET'])
@jwt_required
def get_buyers():
    try:
        buyers = Buyer.query.all()
        return jsonify([{'id': buyer.id, 'company_name': buyer.company_name, 'contact_person': buyer.contact_person} for buyer in buyers])
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/vendors', methods=['GET'])
@jwt_required
def get_vendors():
    try:
        vendors = Vendor.query.all()
        return jsonify([{'id': vendor.id, 'company_name': vendor.company_name, 'contact_person': vendor.contact_person} for vendor in vendors])
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/distributors', methods=['GET'])
@jwt_required
def get_distributors():
    try:
        distributors = Distributor.query.all()
        return jsonify([{'id': distributor.id, 'company_name': distributor.company_name, 'contact_person': distributor.contact_person} for distributor in distributors])
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/products', methods=['GET'])
@jwt_required
def get_products():
    try:
        products = Product.query.all()
        return jsonify([{'id': product.id, 'product_name': product.product_name, 'product_description': product.product_description, 'price': product.price} for product in products])
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Update
@app.route('/buyer/<int:buyer_id>', methods=['PUT'])
@jwt_required
def update_buyer(buyer_id):
    try:
        buyer = Buyer.query.get(buyer_id)
        if buyer:
            data = request.get_json()
            buyer.company_name = data['company_name']
            buyer.contact_person = data['contact_person']
            db.session.commit()
            return jsonify({'message': 'Buyer updated successfully'})
        else:
            return jsonify({'message': 'Buyer not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/vendor/<int:vendor_id>', methods=['PUT'])
@jwt_required
def update_vendor(vendor_id):
    try:
        vendor = Vendor.query.get(vendor_id)
        if vendor:
            data = request.get_json()
            vendor.company_name = data['company_name']
            vendor.contact_person = data['contact_person']
            db.session.commit()
            return jsonify({'message': 'Vendor updated successfully'})
        else:
            return jsonify({'message': 'Vendor not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/distributor/<int:distributor_id>', methods=['PUT'])
@jwt_required
def update_distributor(distributor_id):
    try:
        distributor = Distributor.query.get(distributor_id)
        if distributor:
            data = request.get_json()
            distributor.company_name = data['company_name']
            distributor.contact_person = data['contact_person']
            db.session.commit()
            return jsonify({'message': 'Distributor updated successfully'})
        else:
            return jsonify({'message': 'Distributor not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/product/<int:product_id>', methods=['PUT'])
@jwt_required
def update_product(product_id):
    try:
        product = Product.query.get(product_id)
        if product:
            data = request.get_json()
            product.product_name = data['product_name']
            product.product_description = data['product_description']
            product.price = data['price']
            db.session.commit()
            return jsonify({'message': 'Product updated successfully'})
        else:
            return jsonify({'message': 'Product not found'}), 404
    except
