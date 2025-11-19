"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksync.app.allocation.claim.roclima.ro
Prompt: Illustrate how to implement a user authentication system for an HVAC service management application, focusing on features like order tracking and wishlist management.
Generated: DETERMINISTIC_74aaaa0d5a2f39d1
Batch ID: 20250612_135202
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py
"""
A Flask-based user authentication system for an HVAC service management application.
Features:
1. User Registration
2. User Login
3. Order Tracking
4. Wishlist Management
"""

from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hvac.db'  # SQLite Database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Database models
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    item = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)

class Wishlist(db.Model):
    __tablename__ = 'wishlist'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    item = db.Column(db.String(100), nullable=False)

# Route: User Registration
@app.route('/register', methods=['POST'])
def register():
    """
    Register a new user.
    Request JSON: { "username": "user", "password": "pass" }
    """
    data = request.json
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Invalid input"}), 400

    username = data['username']
    password = data['password']

    # Check if user exists
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "User already exists"}), 400

    # Create user
    password_hash = generate_password_hash(password)
    new_user = User(username=username, password_hash=password_hash)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

# Route: User Login
@app.route('/login', methods=['POST'])
def login():
    """
    Login an existing user.
    Request JSON: { "username": "user", "password": "pass" }
    """
    data = request.json
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Invalid input"}), 400

    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Set session
    session['user_id'] = user.id
    return jsonify({"message": "Login successful"}), 200

# Route: Place an Order
@app.route('/order', methods=['POST'])
def place_order():
    """
    Place an order for a logged-in user.
    Request JSON: { "item": "Air Conditioner", "status": "Processing" }
    """
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    if not data or 'item' not in data or 'status' not in data:
        return jsonify({"error": "Invalid input"}), 400

    user_id = session['user_id']
    item = data['item']
    status = data['status']

    new_order = Order(user_id=user_id, item=item, status=status)
    db.session.add(new_order)
    db.session.commit()

    return jsonify({"message": "Order placed successfully"}), 201

# Route: View Orders
@app.route('/orders', methods=['GET'])
def view_orders():
    """
    View all orders for the logged-in user.
    """
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401

    user_id = session['user_id']
    orders = Order.query.filter_by(user_id=user_id).all()

    order_list = [{"id": order.id, "item": order.item, "status": order.status} for order in orders]
    return jsonify(order_list), 200

# Route: Add to Wishlist
@app.route('/wishlist', methods=['POST'])
def add_to_wishlist():
    """
    Add an item to the wishlist for a logged-in user.
    Request JSON: { "item": "Air Filter" }
    """
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    if not data or 'item' not in data:
        return jsonify({"error": "Invalid input"}), 400

    user_id = session['user_id']
    item = data['item']

    new_wishlist_item = Wishlist(user_id=user_id, item=item)
    db.session.add(new_wishlist_item)
    db.session.commit()

    return jsonify({"message": "Item added to wishlist"}), 201

# Route: View Wishlist
@app.route('/wishlist', methods=['GET'])
def view_wishlist():
    """
    View all items in the wishlist for the logged-in user.
    """
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401

    user_id = session['user_id']
    wishlist_items = Wishlist.query.filter_by(user_id=user_id).all()

    wishlist = [{"id": item.id, "item": item.item} for item in wishlist_items]
    return jsonify(wishlist), 200

# Route: Logout
@app.route('/logout', methods=['POST'])
def logout():
    """
    Logout the user.
    """
    session.pop('user_id', None)
    return jsonify({"message": "Logout successful"}), 200

# Initialize database and run the app
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)
```
