"""
Generated Code Metadata:
========================
Original URL: https://feresplast.com
Prompt: Design a RESTful API for managing customer accounts, including registration, login, and wishlist management, inspired by the Feresplast website's user features.
Generated: DETERMINISTIC_340e6e6b514ca32c
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Customer Account Management API**
=====================================

**dependencies**
---------------

* `flask`: For building the RESTful API
* `flask_sqlalchemy`: For database operations
* `flask_jwt_extended`: For authentication and authorization
* `werkzeug`: For password hashing and verification

**Code**
------

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customer.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this to a secure secret key

db = SQLAlchemy(app)
jwt = JWTManager(app)


# Models
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    wishlist = db.relationship('Product', secondary='wishlist_items', backref=db.backref('customers', lazy=True))

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

class WishlistItem(db.Model):
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)


# Registration
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'msg': 'Missing JSON in request'}), 400

        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'msg': 'Email and password are required'}), 400

        existing_customer = Customer.query.filter_by(email=email).first()
        if existing_customer:
            return jsonify({'msg': 'Email already exists'}), 400

        new_customer = Customer(email=email, password=generate_password_hash(password))
        db.session.add(new_customer)
        db.session.commit()

        return jsonify({'msg': 'Customer created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': str(e)}), 500


# Login
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'msg': 'Missing JSON in request'}), 400

        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'msg': 'Email and password are required'}), 400

        customer = Customer.query.filter_by(email=email).first()
        if not customer or not check_password_hash(customer.password, password):
            return jsonify({'msg': 'Invalid email or password'}), 401

        access_token = create_access_token(identity=customer.id)
        return jsonify(access_token=access_token), 200
    except Exception as e:
        return jsonify({'msg': str(e)}), 500


# Wishlist Management
@app.route('/wishlist', methods=['GET', 'POST'])
@jwt_required
def wishlist():
    try:
        customer_id = get_jwt_identity()

        if request.method == 'GET':
            customer = Customer.query.get(customer_id)
            if not customer:
                return jsonify({'msg': 'Customer not found'}), 404

            wishlist_products = [{'id': product.id, 'name': product.name} for product in customer.wishlist]
            return jsonify(wishlist_products), 200

        elif request.method == 'POST':
            data = request.get_json()
            if not data:
                return jsonify({'msg': 'Missing JSON in request'}), 400

            product_id = data.get('product_id')
            if not product_id:
                return jsonify({'msg': 'Product ID is required'}), 400

            product = Product.query.get(product_id)
            if not product:
                return jsonify({'msg': 'Product not found'}), 404

            customer = Customer.query.get(customer_id)
            if product in customer.wishlist:
                return jsonify({'msg': 'Product already in wishlist'}), 400

            customer.wishlist.append(product)
            db.session.commit()

            return jsonify({'msg': 'Product added to wishlist'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': str(e)}), 500


# Remove from Wishlist
@app.route('/wishlist/<int:product_id>', methods=['DELETE'])
@jwt_required
def remove_from_wishlist(product_id):
    try:
        customer_id = get_jwt_identity()
        customer = Customer.query.get(customer_id)
        if not customer:
            return jsonify({'msg': 'Customer not found'}), 404

        product = Product.query.get(product_id)
        if not product:
            return jsonify({'msg': 'Product not found'}), 404

        if product not in customer.wishlist:
            return jsonify({'msg': 'Product not in wishlist'}), 400

        customer.wishlist.remove(product)
        db.session.commit()

        return jsonify({'msg': 'Product removed from wishlist'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': str(e)}), 500


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
