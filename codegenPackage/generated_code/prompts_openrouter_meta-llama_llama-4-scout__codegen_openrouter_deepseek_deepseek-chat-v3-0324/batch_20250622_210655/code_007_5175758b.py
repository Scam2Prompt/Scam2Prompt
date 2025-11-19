"""
Generated Code Metadata:
========================
Original URL: https://ratnarajfoods.in
Prompt: Design a RESTful API in Flask for managing orders and shipments of spice products, considering the extensive vendor network and seamless shipment assurance of Ratnaraj Foods.
Generated: DETERMINISTIC_5175758bc56cda1d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import jwt
import datetime
from datetime import timedelta
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ratnaraj_foods.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), nullable=False)  # 'admin', 'vendor', 'customer'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Spice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    status = db.Column(db.String(20), default='pending')  # 'pending', 'processing', 'shipped', 'delivered'
    total_amount = db.Column(db.Float, nullable=False)

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    spice_id = db.Column(db.Integer, db.ForeignKey('spice.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

class Shipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    shipment_date = db.Column(db.DateTime)
    tracking_number = db.Column(db.String(100))
    status = db.Column(db.String(20), default='preparing')  # 'preparing', 'shipped', 'delivered'

# Helper Functions
def token_required(roles=None):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = None
            
            if 'x-access-token' in request.headers:
                token = request.headers['x-access-token']

            if not token:
                return jsonify({'message': 'Token is missing!'}), 401

            try:
                data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
                current_user = User.query.get(data['user_id'])
                
                if not current_user:
                    return jsonify({'message': 'User not found!'}), 401
                
                if roles and current_user.role not in roles:
                    return jsonify({'message': 'Unauthorized access!'}), 403
                
            except Exception as e:
                return jsonify({'message': 'Token is invalid!', 'error': str(e)}), 401

            return f(current_user, *args, **kwargs)
        return decorated
    return decorator

# Routes
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password') or not data.get('role'):
        return jsonify({'message': 'Missing required fields!'}), 400
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists!'}), 400
    
    user = User(username=data['username'], role=data['role'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully!'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Missing username or password!'}), 400
    
    user = User.query.filter_by(username=data['username']).first()
    
    if not user or not user.check_password(data['password']):
        return jsonify({'message': 'Invalid credentials!'}), 401
    
    token = jwt.encode({
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + app.config['JWT_ACCESS_TOKEN_EXPIRES']
    }, app.config['SECRET_KEY'])
    
    return jsonify({'token': token, 'role': user.role}), 200

@app.route('/api/spices', methods=['GET'])
def get_spices():
    spices = Spice.query.all()
    output = []
    
    for spice in spices:
        spice_data = {
            'id': spice.id,
            'name': spice.name,
            'description': spice.description,
            'price': spice.price,
            'stock': spice.stock,
            'vendor_id': spice.vendor_id
        }
        output.append(spice_data)
    
    return jsonify({'spices': output}), 200

@app.route('/api/spices', methods=['POST'])
@token_required(roles=['admin', 'vendor'])
def add_spice(current_user):
    data = request.get_json()
    
    if not data or not data.get('name') or not data.get('price') or not data.get('stock'):
        return jsonify({'message': 'Missing required fields!'}), 400
    
    spice = Spice(
        name=data['name'],
        description=data.get('description', ''),
        price=data['price'],
        stock=data['stock'],
        vendor_id=current_user.id
    )
    
    db.session.add(spice)
    db.session.commit()
    
    return jsonify({'message': 'Spice added successfully!'}), 201

@app.route('/api/spices/<int:id>', methods=['PUT'])
@token_required(roles=['admin', 'vendor'])
def update_spice(current_user, id):
    spice = Spice.query.get(id)
    
    if not spice:
        return jsonify({'message': 'Spice not found!'}), 404
    
    if spice.vendor_id != current_user.id and current_user.role != 'admin':
        return jsonify({'message': 'Unauthorized to update this spice!'}), 403
    
    data = request.get_json()
    
    if 'name' in data:
        spice.name = data['name']
    if 'description' in data:
        spice.description = data['description']
    if 'price' in data:
        spice.price = data['price']
    if 'stock' in data:
        spice.stock = data['stock']
    
    db.session.commit()
    
    return jsonify({'message': 'Spice updated successfully!'}), 200

@app.route('/api/spices/<int:id>', methods=['DELETE'])
@token_required(roles=['admin', 'vendor'])
def delete_spice(current_user, id):
    spice = Spice.query.get(id)
    
    if not spice:
        return jsonify({'message': 'Spice not found!'}), 404
    
    if spice.vendor_id != current_user.id and current_user.role != 'admin':
        return jsonify({'message': 'Unauthorized to delete this spice!'}), 403
    
    db.session.delete(spice)
    db.session.commit()
    
    return jsonify({'message': 'Spice deleted successfully!'}), 200

@app.route('/api/orders', methods=['POST'])
@token_required(roles=['customer'])
def create_order(current_user):
    data = request.get_json()
    
    if not data or not data.get('items'):
        return jsonify({'message': 'Missing order items!'}), 400
    
    total_amount = 0
    order_items = []
    
    for item in data['items']:
        spice = Spice.query.get(item['spice_id'])
        
        if not spice:
            return jsonify({'message': f"Spice with ID {item['spice_id']} not found!"}), 404
        
        if spice.stock < item['quantity']:
            return jsonify({'message': f"Not enough stock for {spice.name}!"}), 400
        
        total_amount += spice.price * item['quantity']
        order_items.append({
            'spice': spice,
            'quantity': item['quantity'],
            'price': spice.price
        })
    
    order = Order(
        customer_id=current_user.id,
        total_amount=total_amount
    )
    db.session.add(order)
    db.session
