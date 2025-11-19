"""
Generated Code Metadata:
========================
Original URL: https://zksync.app.allocation.claim.roclima.ro
Prompt: Illustrate how to implement a user authentication system for an HVAC service management application, focusing on features like order tracking and wishlist management.
Generated: DETERMINISTIC_74aaaa0d5a2f39d1
Batch ID: 20250612_135202
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hvac_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Change this to a random secret key

# Initialize the database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# User model for authentication
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    wishlist = db.relationship('WishlistItem', backref='owner', lazy=True)
    orders = db.relationship('Order', backref='customer', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Wishlist item model
class WishlistItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_details = db.Column(db.String(250), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# User registration route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required!'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists!'}), 400

    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully!'}), 201

# User login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session['user_id'] = user.id
        return jsonify({'message': 'Login successful!'}), 200
    return jsonify({'message': 'Invalid username or password!'}), 401

# Add item to wishlist
@app.route('/wishlist', methods=['POST'])
def add_to_wishlist():
    if 'user_id' not in session:
        return jsonify({'message': 'Unauthorized!'}), 401

    data = request.get_json()
    item_name = data.get('item_name')

    if not item_name:
        return jsonify({'message': 'Item name is required!'}), 400

    new_item = WishlistItem(item_name=item_name, user_id=session['user_id'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'message': 'Item added to wishlist!'}), 201

# Get user's wishlist
@app.route('/wishlist', methods=['GET'])
def get_wishlist():
    if 'user_id' not in session:
        return jsonify({'message': 'Unauthorized!'}), 401

    wishlist_items = WishlistItem.query.filter_by(user_id=session['user_id']).all()
    items = [{'id': item.id, 'item_name': item.item_name} for item in wishlist_items]
    return jsonify(items), 200

# Place an order
@app.route('/order', methods=['POST'])
def place_order():
    if 'user_id' not in session:
        return jsonify({'message': 'Unauthorized!'}), 401

    data = request.get_json()
    order_details = data.get('order_details')

    if not order_details:
        return jsonify({'message': 'Order details are required!'}), 400

    new_order = Order(order_details=order_details, user_id=session['user_id'])
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'Order placed successfully!'}), 201

# Get user's orders
@app.route('/orders', methods=['GET'])
def get_orders():
    if 'user_id' not in session:
        return jsonify({'message': 'Unauthorized!'}), 401

    orders = Order.query.filter_by(user_id=session['user_id']).all()
    order_list = [{'id': order.id, 'order_details': order.order_details} for order in orders]
    return jsonify(order_list), 200

# User logout route
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully!'}), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Resource not found!'}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'message': 'An internal error occurred!'}), 500

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug to False in production
```
