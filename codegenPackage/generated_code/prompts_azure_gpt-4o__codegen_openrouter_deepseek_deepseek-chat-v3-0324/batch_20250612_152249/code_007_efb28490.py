"""
Generated Code Metadata:
========================
Original URL: https://ramjiacro.com
Prompt: Create a REST API for a textile company to manage customer inquiries, orders, and inventory related to acrylic yarn products.
Generated: DETERMINISTIC_efb28490ad597786
Batch ID: 20250612_152249
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
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import jwt
import datetime

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///textile_company.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'admin' or 'customer'

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    color = db.Column(db.String(50))
    weight = db.Column(db.Float)  # in grams
    price_per_unit = db.Column(db.Float)
    stock_quantity = db.Column(db.Integer, default=0)

class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    message = db.Column(db.Text)
    status = db.Column(db.String(20), default='pending')  # pending, responded, resolved
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    status = db.Column(db.String(20), default='processing')  # processing, shipped, delivered, cancelled
    total_amount = db.Column(db.Float)

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)

# Helper functions
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.filter_by(id=data['id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_user, *args, **kwargs)
    return decorated

def admin_required(f):
    @wraps(f)
    def decorated(current_user, *args, **kwargs):
        if current_user.role != 'admin':
            return jsonify({'message': 'Admin access required!'}), 403
        return f(current_user, *args, **kwargs)
    return decorated

# Routes
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Username and password required!'}), 400
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists!'}), 400
    
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(
        username=data['username'],
        password=hashed_password,
        role='customer'
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully!'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Username and password required!'}), 400
    
    user = User.query.filter_by(username=data['username']).first()
    
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Invalid credentials!'}), 401
    
    token = jwt.encode({
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, app.config['SECRET_KEY'])
    
    return jsonify({'token': token}), 200

# Customer routes
@app.route('/customers', methods=['POST'])
@token_required
def create_customer(current_user):
    data = request.get_json()
    
    if not data or not data.get('name') or not data.get('email'):
        return jsonify({'message': 'Name and email are required!'}), 400
    
    if Customer.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Customer with this email already exists!'}), 400
    
    new_customer = Customer(
        name=data['name'],
        email=data['email'],
        phone=data.get('phone'),
        address=data.get('address'),
        user_id=current_user.id
    )
    
    db.session.add(new_customer)
    db.session.commit()
    
    return jsonify({'message': 'Customer created successfully!'}), 201

@app.route('/customers/<int:customer_id>', methods=['GET'])
@token_required
def get_customer(current_user, customer_id):
    customer = Customer.query.get(customer_id)
    
    if not customer:
        return jsonify({'message': 'Customer not found!'}), 404
    
    if customer.user_id != current_user.id and current_user.role != 'admin':
        return jsonify({'message': 'Unauthorized access!'}), 403
    
    customer_data = {
        'id': customer.id,
        'name': customer.name,
        'email': customer.email,
        'phone': customer.phone,
        'address': customer.address
    }
    
    return jsonify(customer_data), 200

# Product routes
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    output = []
    
    for product in products:
        product_data = {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'color': product.color,
            'weight': product.weight,
            'price_per_unit': product.price_per_unit,
            'stock_quantity': product.stock_quantity
        }
        output.append(product_data)
    
    return jsonify({'products': output}), 200

@app.route('/products', methods=['POST'])
@token_required
@admin_required
def create_product(current_user):
    data = request.get_json()
    
    if not data or not data.get('name') or not data.get('price_per_unit'):
        return jsonify({'message': 'Name and price are required!'}), 400
    
    new_product = Product(
        name=data['name'],
        description=data.get('description'),
        color=data.get('color'),
        weight=data.get('weight'),
        price_per_unit=data['price_per_unit'],
        stock_quantity=data.get('stock_quantity', 0)
    )
    
    db.session.add(new_product)
    db.session.commit()
    
    return jsonify({'message': 'Product created successfully!'}), 201

@app.route('/products/<int:product_id>', methods=['PUT'])
@token_required
@admin_required
def update_product(current_user, product_id):
    product = Product.query.get(product_id)
    
    if not product:
        return jsonify({'message': 'Product not found!'}), 404
    
    data = request.get_json()
    
    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.color = data.get('color', product.color)
    product.weight = data.get('weight', product.weight)
    product.price_per_unit = data.get('price_per_unit', product.price_per_unit)
    product.stock_quantity = data.get('stock_quantity', product.stock_quantity)
    
    db.session.commit()
    
    return jsonify({'message': 'Product updated successfully!'}), 200

# Inquiry routes
@app.route('/inquiries', methods=['POST'])
@token_required
def create_inquiry(current_user):
    data = request
