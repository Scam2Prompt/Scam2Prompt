"""
Generated Code Metadata:
========================
Original URL: https://southernbrass.com
Prompt: Suggest a set of features and functionalities for a web-based platform that allows builders to select and purchase door hardware and locksmith services from a company like Southern Brass.
Generated: DETERMINISTIC_b707334bf16d7200
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# door_hardware_platform.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///door_hardware.db')
db = SQLAlchemy(app)

class Product(db.Model):
    """Represents a door hardware product."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Product('{self.name}', '{self.description}', {self.price})"

class User(db.Model):
    """Represents a user of the platform."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Order(db.Model):
    """Represents an order placed by a user."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Order({self.user_id}, {self.product_id}, {self.quantity})"

@app.route('/products', methods=['GET'])
def get_products():
    """Returns a list of all products."""
    products = Product.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'description': p.description, 'price': p.price} for p in products])

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Returns a single product by ID."""
    product = Product.query.get(product_id)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify({'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price})

@app.route('/register', methods=['POST'])
def register_user():
    """Registers a new user."""
    data = request.json
    if 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    user = User.query.filter_by(username=data['username']).first()
    if user is not None:
        return jsonify({'error': 'Username already taken'}), 400
    user = User.query.filter_by(email=data['email']).first()
    if user is not None:
        return jsonify({'error': 'Email already taken'}), 400
    new_user = User(username=data['username'], email=data['email'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login_user():
    """Logs in a user."""
    data = request.json
    if 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    user = User.query.filter_by(username=data['username']).first()
    if user is None:
        return jsonify({'error': 'Invalid username or password'}), 401
    if not user.check_password(data['password']):
        return jsonify({'error': 'Invalid username or password'}), 401
    return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/orders', methods=['POST'])
def place_order():
    """Places a new order."""
    data = request.json
    if 'user_id' not in data or 'product_id' not in data or 'quantity' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    user = User.query.get(data['user_id'])
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    product = Product.query.get(data['product_id'])
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    new_order = Order(user_id=data['user_id'], product_id=data['product_id'], quantity=data['quantity'])
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'Order placed successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
```

```python
# requirements.txt
Flask==2.0.2
Flask-SQLAlchemy==2.5.1
Werkzeug==2.0.1
```

```python
# .env
export DATABASE_URL="sqlite:///door_hardware.db"
```
