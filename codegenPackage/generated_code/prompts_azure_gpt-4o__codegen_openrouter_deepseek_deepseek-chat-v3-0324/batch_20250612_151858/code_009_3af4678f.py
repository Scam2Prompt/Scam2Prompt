"""
Generated Code Metadata:
========================
Original URL: https://jurunensebrazz.blogspot.com
Prompt: Provide a solution using Flask or Django to build a backend system for managing product inventory and promotions for a site like "Jurunense Home Center."
Generated: DETERMINISTIC_3af4678fc919a95f
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py - Flask backend for product inventory and promotions management

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_marshmallow import Marshmallow
from datetime import datetime, timedelta
import os

# Initialize Flask app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'jurunense.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Initialize extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text)
    products = db.relationship('Product', backref='category', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    image_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    promotions = db.relationship('Promotion', backref='product', lazy=True)

class Promotion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    discount_percentage = db.Column(db.Float, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

# Schemas
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ('password_hash',)

class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
    
    promotions = ma.Nested('PromotionSchema', many=True, exclude=('product',))

class PromotionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Promotion
    
    product = ma.Nested(ProductSchema, exclude=('promotions',))

# Initialize schemas
user_schema = UserSchema()
users_schema = UserSchema(many=True)
category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
promotion_schema = PromotionSchema()
promotions_schema = PromotionSchema(many=True)

# Helper functions
def validate_admin(user_id):
    user = User.query.get(user_id)
    return user and user.is_admin

# Routes
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Missing required fields'}), 400
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists'}), 400
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already exists'}), 400
    
    new_user = User(
        username=data['username'],
        email=data['email'],
        is_admin=data.get('is_admin', False)
    )
    new_user.set_password(data['password'])
    
    db.session.add(new_user)
    db.session.commit()
    
    return user_schema.jsonify(new_user), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Missing username or password'}), 400
    
    user = User.query.filter_by(username=data['username']).first()
    if not user or not user.check_password(data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401
    
    return user_schema.jsonify(user), 200

@app.route('/api/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return categories_schema.jsonify(categories), 200

@app.route('/api/categories', methods=['POST'])
def create_category():
    if not validate_admin(request.headers.get('user_id')):
        return jsonify({'message': 'Unauthorized'}), 403
    
    data = request.get_json()
    if not data or not data.get('name'):
        return jsonify({'message': 'Name is required'}), 400
    
    if Category.query.filter_by(name=data['name']).first():
        return jsonify({'message': 'Category already exists'}), 400
    
    new_category = Category(
        name=data['name'],
        description=data.get('description')
    )
    
    db.session.add(new_category)
    db.session.commit()
    
    return category_schema.jsonify(new_category), 201

@app.route('/api/products', methods=['GET'])
def get_products():
    category_id = request.args.get('category_id')
    query = Product.query
    
    if category_id:
        query = query.filter_by(category_id=category_id)
    
    products = query.all()
    return products_schema.jsonify(products), 200

@app.route('/api/products', methods=['POST'])
def create_product():
    if not validate_admin(request.headers.get('user_id')):
        return jsonify({'message': 'Unauthorized'}), 403
    
    data = request.get_json()
    if not data or not data.get('name') or not data.get('price') or not data.get('stock_quantity') or not data.get('category_id'):
        return jsonify({'message': 'Missing required fields'}), 400
    
    category = Category.query.get(data['category_id'])
    if not category:
        return jsonify({'message': 'Category not found'}), 404
    
    new_product = Product(
        name=data['name'],
        description=data.get('description'),
        price=data['price'],
        stock_quantity=data['stock_quantity'],
        category_id=data['category_id'],
        image_url=data.get('image_url')
    )
    
    db.session.add(new_product)
    db.session.commit()
    
    return product_schema.jsonify(new_product), 201

@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    if not validate_admin(request.headers.get('user_id')):
        return jsonify({'message': 'Unauthorized'}), 403
    
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data provided'}), 400
    
    if 'name' in data:
        product.name = data['name']
    if 'description' in data:
        product.description = data['description']
    if 'price' in data:
        product.price = data['price']
    if 'stock_quantity' in data:
        product.stock_quantity = data['stock_quantity']
    if 'category_id' in data:
        category = Category.query.get(data['category_id'])
        if not category:
            return jsonify({'message': 'Category not found'}), 404
        product.category_id = data['category_id']
    if 'image_url' in data:
        product.image_url = data['image_url']
    
    db.session.commit()
    return product_schema.jsonify(product), 200

@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    if not validate_admin(request.headers.get('user_id')):
        return jsonify({'message': 'Unauthorized'}), 403
    
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted
