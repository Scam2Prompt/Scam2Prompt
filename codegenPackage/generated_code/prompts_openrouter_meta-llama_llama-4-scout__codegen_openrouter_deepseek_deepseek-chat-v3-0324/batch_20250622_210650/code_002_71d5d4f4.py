"""
Generated Code Metadata:
========================
Original URL: https://canatechinstitute.ca
Prompt: "Design a basic web application using agile methodology for a retail business to digitalize their transaction system."
Generated: DETERMINISTIC_71d5d4f49b7f6686
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py - Main application file for retail transaction system

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import uuid
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///retail.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), default='cashier')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    barcode = db.Column(db.String(50), unique=True)

class Transaction(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    total_amount = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    items = db.relationship('TransactionItem', backref='transaction', lazy=True)

class TransactionItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.String(50), db.ForeignKey('transaction.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    product = db.relationship('Product')

# Authentication
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            return jsonify({'status': 'success', 'message': 'Logged in successfully'})
        return jsonify({'status': 'error', 'message': 'Invalid credentials'}), 401
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'status': 'success', 'message': 'Logged out successfully'})

# Product Management
@app.route('/products', methods=['GET'])
@login_required
def get_products():
    products = Product.query.all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'price': p.price,
        'stock': p.stock,
        'barcode': p.barcode
    } for p in products])

@app.route('/products', methods=['POST'])
@login_required
def add_product():
    if current_user.role != 'admin':
        return jsonify({'status': 'error', 'message': 'Unauthorized'}), 403
    
    data = request.get_json()
    product = Product(
        name=data['name'],
        price=data['price'],
        stock=data.get('stock', 0),
        barcode=data.get('barcode', '')
    )
    db.session.add(product)
    db.session.commit()
    return jsonify({'status': 'success', 'message': 'Product added'}), 201

# Transaction Processing
@app.route('/transactions', methods=['POST'])
@login_required
def create_transaction():
    data = request.get_json()
    transaction_id = str(uuid.uuid4())
    total = 0
    items = []
    
    for item in data['items']:
        product = Product.query.get(item['product_id'])
        if not product or product.stock < item['quantity']:
            return jsonify({'status': 'error', 'message': 'Invalid product or insufficient stock'}), 400
        
        total += product.price * item['quantity']
        items.append({
            'product_id': product.id,
            'quantity': item['quantity'],
            'price': product.price
        })
        
        # Update stock
        product.stock -= item['quantity']
    
    transaction = Transaction(
        id=transaction_id,
        total_amount=total,
        user_id=current_user.id
    )
    db.session.add(transaction)
    
    for item in items:
        db.session.add(TransactionItem(
            transaction_id=transaction_id,
            product_id=item['product_id'],
            quantity=item['quantity'],
            price=item['price']
        ))
    
    db.session.commit()
    return jsonify({
        'status': 'success',
        'transaction_id': transaction_id,
        'total_amount': total
    }), 201

@app.route('/transactions/<transaction_id>', methods=['GET'])
@login_required
def get_transaction(transaction_id):
    transaction = Transaction.query.get(transaction_id)
    if not transaction:
        return jsonify({'status': 'error', 'message': 'Transaction not found'}), 404
    
    items = [{
        'product_id': item.product_id,
        'product_name': item.product.name,
        'quantity': item.quantity,
        'price': item.price,
        'subtotal': item.quantity * item.price
    } for item in transaction.items]
    
    return jsonify({
        'transaction_id': transaction.id,
        'timestamp': transaction.timestamp.isoformat(),
        'total_amount': transaction.total_amount,
        'cashier': transaction.user_id,
        'items': items
    })

# Error Handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({'status': 'error', 'message': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return jsonify({'status': 'error', 'message': 'Internal server error'}), 500

# Initialize Database
@app.before_first_request
def create_tables():
    db.create_all()
    # Create admin user if not exists
    if not User.query.filter_by(username='admin').first():
        admin = User(username='admin', role='admin')
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/login.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Retail System - Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .login-container {
            background-color: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            width: 300px;
        }
        h1 {
            text-align: center;
            margin-bottom: 1.5rem;
            color: #333;
        }
        .form-group {
            margin-bottom: 1rem;
        }
        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: bold;
        }
        input {
            width: 100%;
            padding: 0.5rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        button {
            width: 100%;
            padding: 0.75rem;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 1rem;
        }
        button:hover {
            background-color: #45a049;
        }
        .error {
            color: red;
            margin-top: 1rem;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h1>Retail System Login</h1>
        <form id="loginForm">
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" required>
            </div
