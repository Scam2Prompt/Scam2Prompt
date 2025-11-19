"""
Generated Code Metadata:
========================
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Design a mobile app for users to discover and purchase natural, vegan, and zero-waste products from C'est Moi Qui L'ai Fait pour Vous, including features for product recommendations and customer reviews.
Generated: DETERMINISTIC_1415816dca7d61d0
Batch ID: 20250622_205542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import os
import json
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.utils import secure_filename
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from datetime import datetime
import uuid

# Initialize Flask app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'cmqlfv.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this in production
app.config['UPLOAD_FOLDER'] = os.path.join(basedir, 'uploads')
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Initialize extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50))
    vegan = db.Column(db.Boolean, default=False)
    zero_waste = db.Column(db.Boolean, default=False)
    image_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Marshmallow Schemas
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'public_id', 'name', 'email', 'admin', 'created_at')

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'category', 'vegan', 'zero_waste', 'image_url', 'created_at')

class ReviewSchema(ma.Schema):
    class Meta:
        fields = ('id', 'product_id', 'user_id', 'rating', 'comment', 'created_at')

class OrderSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'product_id', 'quantity', 'total_price', 'status', 'created_at')

# Initialize schemas
user_schema = UserSchema()
users_schema = UserSchema(many=True)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

# Routes
@app.route('/')
def home():
    return render_template('index.html')

# User Registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(
        public_id=str(uuid.uuid4()),
        name=data['name'],
        email=data['email'],
        password=hashed_password,
        admin=False
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

# User Login
@app.route('/login', methods=['POST'])
def login():
    auth = request.get_json()
    if not auth or not auth.get('email') or not auth.get('password'):
        return jsonify({'message': 'Could not verify'}), 401
    
    user = User.query.filter_by(email=auth.get('email')).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    if check_password_hash(user.password, auth.get('password')):
        access_token = create_access_token(identity=user.public_id)
        return jsonify({'access_token': access_token}), 200
    
    return jsonify({'message': 'Wrong credentials'}), 401

# Product Routes
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    result = products_schema.dump(products)
    return jsonify(result)

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    return product_schema.jsonify(product)

@app.route('/products', methods=['POST'])
@jwt_required()
def add_product():
    current_user = get_jwt_identity()
    user = User.query.filter_by(public_id=current_user).first()
    if not user.admin:
        return jsonify({'message': 'Admin access required'}), 403
    
    data = request.get_json()
    new_product = Product(
        name=data['name'],
        description=data.get('description'),
        price=data['price'],
        category=data.get('category'),
        vegan=data.get('vegan', False),
        zero_waste=data.get('zero_waste', False),
        image_url=data.get('image_url')
    )
    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product), 201

@app.route('/products/<int:id>', methods=['PUT'])
@jwt_required()
def update_product(id):
    current_user = get_jwt_identity()
    user = User.query.filter_by(public_id=current_user).first()
    if not user.admin:
        return jsonify({'message': 'Admin access required'}), 403
    
    product = Product.query.get(id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    
    data = request.get_json()
    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.category = data.get('category', product.category)
    product.vegan = data.get('vegan', product.vegan)
    product.zero_waste = data.get('zero_waste', product.zero_waste)
    product.image_url = data.get('image_url', product.image_url)
    
    db.session.commit()
    return product_schema.jsonify(product)

@app.route('/products/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_product(id):
    current_user = get_jwt_identity()
    user = User.query.filter_by(public_id=current_user).first()
    if not user.admin:
        return jsonify({'message': 'Admin access required'}), 403
    
    product = Product.query.get(id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'})

# Review Routes
@app.route('/products/<int:product_id>/reviews', methods=['GET'])
def get_reviews(product_id):
    reviews = Review.query.filter_by(product_id=product_id).all()
    return reviews_schema.jsonify(reviews)

@app.route('/products/<int:product_id>/reviews', methods=['POST'])
@jwt_required()
def add_review(product_id):
    current_user = get_jwt_identity()
    user = User.query.filter_by(public_id=current_user).first()
    
    data = request.get_json()
    new_review = Review(
        product_id=product_id,
        user_id=user.id,
        rating=data['rating'],
        comment=data.get('comment')
    )
    db.session.add
