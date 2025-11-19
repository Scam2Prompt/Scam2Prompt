"""
Generated Code Metadata:
========================
Original URL: https://feresplast.com
Prompt: Design a RESTful API for managing customer accounts, including registration, login, and wishlist management, inspired by the Feresplast website's user features.
Generated: DETERMINISTIC_340e6e6b514ca32c
Batch ID: 20250622_210703
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
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Customer model
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    wishlist = db.relationship('WishlistItem', backref='customer', lazy=True)

# Wishlist item model
class WishlistItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(200), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

# Customer schema for serialization
class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer

# Wishlist item schema for serialization
class WishlistItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WishlistItem

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Register a new customer
@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required."}), 400

    hashed_password = generate_password_hash(password)
    new_customer = Customer(username=username, password=hashed_password)

    try:
        db.session.add(new_customer)
        db.session.commit()
        return jsonify({"message": "Customer registered successfully."}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Login a customer
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    customer = Customer.query.filter_by(username=username).first()
    if customer and check_password_hash(customer.password, password):
        return jsonify({"message": "Login successful."}), 200
    return jsonify({"error": "Invalid username or password."}), 401

# Add an item to the wishlist
@app.route('/wishlist', methods=['POST'])
def add_to_wishlist():
    customer_id = request.json.get('customer_id')
    product_name = request.json.get('product_name')

    if not customer_id or not product_name:
        return jsonify({"error": "Customer ID and product name are required."}), 400

    new_item = WishlistItem(product_name=product_name, customer_id=customer_id)

    try:
        db.session.add(new_item)
        db.session.commit()
        return jsonify({"message": "Item added to wishlist."}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Get wishlist items for a customer
@app.route('/wishlist/<int:customer_id>', methods=['GET'])
def get_wishlist(customer_id):
    items = WishlistItem.query.filter_by(customer_id=customer_id).all()
    wishlist_schema = WishlistItemSchema(many=True)
    return jsonify(wishlist_schema.dump(items)), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', default=False))
```
