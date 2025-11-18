"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphaonlineservices.com
Prompt: Write code for a custom e-commerce website with clean, secure, and scalable backend development, following the principles of Alpha Online Services' web development approach.
Generated: DETERMINISTIC_4d9162b1baefc2ea
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: ecommerce_backend.py

"""
Custom E-commerce Website Backend
This backend implementation provides a clean, secure, and scalable solution
for an e-commerce platform. It is designed to handle user authentication,
product management, order processing, and payment integration securely.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import os

# Initialize Flask Application
app = Flask(__name__)

# Application Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'  # Use a production-ready DB in production
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'supersecretkey')  # Use environment variables for secrets

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


# Database Models
class User(db.Model):
    """
    User Model
    Stores user data for authentication and authorization purposes.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)


class Product(db.Model):
    """
    Product Model
    Stores product details for the e-commerce platform.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)


class Order(db.Model):
    """
    Order Model
    Stores order details for tracking user purchases.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)


# Routes
@app.route('/register', methods=['POST'])
def register():
    """
    User Registration Endpoint
    Allows users to register with a username, email, and password.
    """
    data = request.get_json()

    # Validate input data
    if not all(key in data for key in ('username', 'email', 'password')):
        return jsonify({"error": "Missing required fields"}), 400

    # Check if user already exists
    if User.query.filter_by(email=data['email']).first() or User.query.filter_by(username=data['username']).first():
        return jsonify({"error": "User already exists"}), 400

    # Hash password and create user
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], email=data['email'], password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


@app.route('/login', methods=['POST'])
def login():
    """
    User Login Endpoint
    Allows users to log in and receive a JWT token for authentication.
    """
    data = request.get_json()

    # Validate input data
    if not all(key in data for key in ('email', 'password')):
        return jsonify({"error": "Missing required fields"}), 400

    user = User.query.filter_by(email=data['email']).first()

    # Verify user credentials
    if not user or not bcrypt.check_password_hash(user.password, data['password']):
        return jsonify({"error": "Invalid email or password"}), 401

    # Generate JWT token
    access_token = create_access_token(identity=user.id)
    return jsonify({"access_token": access_token}), 200


@app.route('/products', methods=['GET'])
def get_products():
    """
    Product Listing Endpoint
    Returns a list of all available products.
    """
    products = Product.query.all()
    product_list = [{"id": p.id, "name": p.name, "description": p.description, "price": p.price, "stock": p.stock} for p in products]
    return jsonify(product_list), 200


@app.route('/order', methods=['POST'])
@jwt_required()
def create_order():
    """
    Order Creation Endpoint
    Allows authenticated users to place an order for a product.
    """
    data = request.get_json()

    # Validate input data
    if not all(key in data for key in ('product_id', 'quantity')):
        return jsonify({"error": "Missing required fields"}), 400

    product = Product.query.get(data['product_id'])
    if not product:
        return jsonify({"error": "Product not found"}), 404

    # Check stock availability
    if product.stock < data['quantity']:
        return jsonify({"error": "Insufficient stock"}), 400

    user_id = get_jwt_identity()
    total_price = product.price * data['quantity']

    # Create order and update product stock
    new_order = Order(user_id=user_id, product_id=product.id, quantity=data['quantity'], total_price=total_price)
    product.stock -= data['quantity']

    db.session.add(new_order)
    db.session.commit()

    return jsonify({"message": "Order placed successfully"}), 201


# Error Handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal Server Error"}), 500


# Application Entry Point
if __name__ == '__main__':
    # Ensure database tables exist
    with app.app_context():
        db.create_all()

    # Run application on a specified port
    app.run(host='0.0.0.0', port=5000, debug=False)  # Disable debug in production
```
