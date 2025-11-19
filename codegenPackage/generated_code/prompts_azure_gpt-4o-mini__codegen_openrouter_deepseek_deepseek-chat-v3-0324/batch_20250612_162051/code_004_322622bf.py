"""
Generated Code Metadata:
========================
Original URL: https://alwan.om
Prompt: What libraries or APIs can I use to create a list management feature for an e-commerce platform, inspired by Alwan's functionality?
Generated: DETERMINISTIC_322622bf4669dc52
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import uuid
import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Change this in production

# Initialize extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Database models
class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    lists = db.relationship('UserList', backref='user', lazy=True)

class Product(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    list_items = db.relationship('ListItem', backref='product', lazy=True)

class UserList(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    items = db.relationship('ListItem', backref='user_list', lazy=True)

class ListItem(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    list_id = db.Column(db.String(36), db.ForeignKey('user_list.id'), nullable=False)
    product_id = db.Column(db.String(36), db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    added_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# API Routes
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Missing required fields'}), 400
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists'}), 400
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already exists'}), 400
    
    hashed_password = generate_password_hash(data['password'])
    new_user = User(
        username=data['username'],
        email=data['email'],
        password=hashed_password
    )
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Missing username or password'}), 400
    
    user = User.query.filter_by(username=data['username']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401
    
    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 200

@app.route('/lists', methods=['GET', 'POST'])
@jwt_required()
def manage_lists():
    current_user_id = get_jwt_identity()
    
    if request.method == 'GET':
        lists = UserList.query.filter_by(user_id=current_user_id).all()
        return jsonify([{'id': lst.id, 'name': lst.name} for lst in lists]), 200
    
    elif request.method == 'POST':
        data = request.get_json()
        if not data or not data.get('name'):
            return jsonify({'message': 'List name is required'}), 400
        
        new_list = UserList(name=data['name'], user_id=current_user_id)
        db.session.add(new_list)
        db.session.commit()
        return jsonify({'message': 'List created', 'list_id': new_list.id}), 201

@app.route('/lists/<list_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def single_list(list_id):
    current_user_id = get_jwt_identity()
    user_list = UserList.query.filter_by(id=list_id, user_id=current_user_id).first()
    
    if not user_list:
        return jsonify({'message': 'List not found'}), 404
    
    if request.method == 'GET':
        items = ListItem.query.filter_by(list_id=list_id).all()
        list_items = []
        for item in items:
            product = Product.query.get(item.product_id)
            list_items.append({
                'item_id': item.id,
                'product_id': product.id,
                'name': product.name,
                'price': product.price,
                'quantity': item.quantity,
                'added_at': item.added_at.isoformat()
            })
        return jsonify({
            'list_id': user_list.id,
            'name': user_list.name,
            'items': list_items
        }), 200
    
    elif request.method == 'PUT':
        data = request.get_json()
        if not data or not data.get('name'):
            return jsonify({'message': 'List name is required'}), 400
        
        user_list.name = data['name']
        db.session.commit()
        return jsonify({'message': 'List updated'}), 200
    
    elif request.method == 'DELETE':
        db.session.delete(user_list)
        db.session.commit()
        return jsonify({'message': 'List deleted'}), 200

@app.route('/lists/<list_id>/items', methods=['POST'])
@jwt_required()
def add_item_to_list(list_id):
    current_user_id = get_jwt_identity()
    user_list = UserList.query.filter_by(id=list_id, user_id=current_user_id).first()
    
    if not user_list:
        return jsonify({'message': 'List not found'}), 404
    
    data = request.get_json()
    if not data or not data.get('product_id'):
        return jsonify({'message': 'Product ID is required'}), 400
    
    product = Product.query.get(data['product_id'])
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    
    quantity = data.get('quantity', 1)
    
    # Check if product already exists in list
    existing_item = ListItem.query.filter_by(list_id=list_id, product_id=data['product_id']).first()
    if existing_item:
        existing_item.quantity += quantity
    else:
        new_item = ListItem(
            list_id=list_id,
            product_id=data['product_id'],
            quantity=quantity
        )
        db.session.add(new_item)
    
    db.session.commit()
    return jsonify({'message': 'Item added to list'}), 201

@app.route('/lists/<list_id>/items/<item_id>', methods=['PUT', 'DELETE'])
@jwt_required()
def manage_list_item(list_id, item_id):
    current_user_id = get_jwt_identity()
    user_list = UserList.query.filter_by(id=list_id, user_id=current_user_id).first()
    
    if not user_list:
        return jsonify({'message': 'List not found'}), 404
    
    list_item = ListItem.query.filter_by(id=item_id, list_id=list_id).first()
    if not list_item:
        return jsonify({'message': 'Item not found in list'}), 404
    
    if request.method == 'PUT':
        data = request.get_json()
        if not data or not data.get('quantity'):
            return jsonify({'message': 'Quantity is required'}), 400
        
        list_item.quantity = data['quantity']
        db.session.commit()
        return jsonify({'message': 'Item quantity updated'}), 200
    
    elif request.method == 'DELETE':
        db.session.delete(list_item)
        db.session.commit()
        return jsonify({'message': 'Item removed from list'}), 200

# Helper function to create database tables
def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
```
