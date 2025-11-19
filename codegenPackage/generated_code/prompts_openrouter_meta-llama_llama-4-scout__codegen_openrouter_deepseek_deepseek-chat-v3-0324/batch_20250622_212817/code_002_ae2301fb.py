"""
Generated Code Metadata:
========================
Original URL: https://fxtasian.com
Prompt: "Write a Python script using libraries such as Flask or Django to create a simple REST API for a cryptocurrency exchange platform similar to IJEX Exchange."
Generated: DETERMINISTIC_ae2301fb9f2c5f8f
Batch ID: 20250622_212817
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
from flask_httpauth import HTTPBasicAuth
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exchange.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
auth = HTTPBasicAuth()

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    balance = db.Column(db.Float, default=0.0)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    current_price = db.Column(db.Float, nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    asset_id = db.Column(db.Integer, db.ForeignKey('asset.id'), nullable=False)
    order_type = db.Column(db.String(4), nullable=False)  # 'buy' or 'sell'
    price = db.Column(db.Float, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(10), default='open')  # 'open', 'filled', 'cancelled'
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# Helper Functions
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.get(data['user_id'])
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_user, *args, **kwargs)
    
    return decorated

# Routes
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Username and password required'}), 400
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists'}), 400
    
    user = User(username=data['username'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Username and password required'}), 400
    
    user = User.query.filter_by(username=data['username']).first()
    
    if not user or not user.check_password(data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401
    
    token = jwt.encode({
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, app.config['SECRET_KEY'])
    
    return jsonify({'token': token}), 200

@app.route('/assets', methods=['GET'])
def get_assets():
    assets = Asset.query.all()
    output = []
    
    for asset in assets:
        asset_data = {
            'id': asset.id,
            'symbol': asset.symbol,
            'name': asset.name,
            'current_price': asset.current_price
        }
        output.append(asset_data)
    
    return jsonify({'assets': output}), 200

@app.route('/balance', methods=['GET'])
@token_required
def get_balance(current_user):
    return jsonify({'balance': current_user.balance}), 200

@app.route('/order', methods=['POST'])
@token_required
def create_order(current_user):
    data = request.get_json()
    
    required_fields = ['asset_id', 'order_type', 'price', 'amount']
    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Missing required fields'}), 400
    
    if data['order_type'] not in ['buy', 'sell']:
        return jsonify({'message': 'Invalid order type'}), 400
    
    asset = Asset.query.get(data['asset_id'])
    if not asset:
        return jsonify({'message': 'Asset not found'}), 404
    
    if data['order_type'] == 'buy' and current_user.balance < data['price'] * data['amount']:
        return jsonify({'message': 'Insufficient funds'}), 400
    
    order = Order(
        user_id=current_user.id,
        asset_id=data['asset_id'],
        order_type=data['order_type'],
        price=data['price'],
        amount=data['amount']
    )
    
    db.session.add(order)
    
    if data['order_type'] == 'buy':
        current_user.balance -= data['price'] * data['amount']
    
    db.session.commit()
    
    return jsonify({'message': 'Order created successfully'}), 201

@app.route('/orders', methods=['GET'])
@token_required
def get_orders(current_user):
    orders = Order.query.filter_by(user_id=current_user.id).all()
    output = []
    
    for order in orders:
        asset = Asset.query.get(order.asset_id)
        order_data = {
            'id': order.id,
            'asset_symbol': asset.symbol,
            'order_type': order.order_type,
            'price': order.price,
            'amount': order.amount,
            'status': order.status,
            'created_at': order.created_at
        }
        output.append(order_data)
    
    return jsonify({'orders': output}), 200

@app.route('/order/<int:order_id>', methods=['DELETE'])
@token_required
def cancel_order(current_user, order_id):
    order = Order.query.filter_by(id=order_id, user_id=current_user.id).first()
    
    if not order:
        return jsonify({'message': 'Order not found'}), 404
    
    if order.status != 'open':
        return jsonify({'message': 'Order cannot be cancelled'}), 400
    
    if order.order_type == 'buy':
        current_user.balance += order.price * order.amount
    
    order.status = 'cancelled'
    db.session.commit()
    
    return jsonify({'message': 'Order cancelled successfully'}), 200

# Initialize DB
@app.before_first_request
def create_tables():
    db.create_all()
    
    # Add some sample assets if none exist
    if Asset.query.count() == 0:
        assets = [
            Asset(symbol='BTC', name='Bitcoin', current_price=50000.0),
            Asset(symbol='ETH', name='Ethereum', current_price=3000.0),
            Asset(symbol='LTC', name='Litecoin', current_price=150.0)
        ]
        db.session.bulk_save_objects(assets)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
```
