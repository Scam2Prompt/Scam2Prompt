"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gvika.in
Prompt: Generate code for an API that handles user authentication and wishlist functionality for an e-commerce site, inspired by Gvika's login and wishlist features.
Generated: DETERMINISTIC_2c52df7e174faef6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, jwt_refresh_token_required
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'super-secret')  # Change this in production
db = SQLAlchemy(app)
jwt = JWTManager(app)

# User model for authentication
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    wishlist = db.relationship('WishlistItem', backref='user', lazy=True)

# Wishlist item model
class WishlistItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"msg": "Username and password are required."}), 400

    # Check if user already exists
    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "User already exists."}), 400

    # Create new user
    new_user = User(username=username, password=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully."}), 201

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        # Create JWT token
        access_token = create_access_token(identity={'username': username})
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Invalid username or password."}), 401

# Add item to wishlist
@app.route('/wishlist', methods=['POST'])
@jwt_required()
def add_to_wishlist():
    data = request.get_json()
    item_name = data.get('item_name')

    if not item_name:
        return jsonify({"msg": "Item name is required."}), 400

    user_identity = get_jwt_identity()
    user = User.query.filter_by(username=user_identity['username']).first()

    wishlist_item = WishlistItem(item_name=item_name, user_id=user.id)
    db.session.add(wishlist_item)
    db.session.commit()

    return jsonify({"msg": "Item added to wishlist."}), 201

# Retrieve user's wishlist
@app.route('/wishlist', methods=['GET'])
@jwt_required()
def get_wishlist():
    user_identity = get_jwt_identity()
    user = User.query.filter_by(username=user_identity['username']).first()
    
    wishlist_items = WishlistItem.query.filter_by(user_id=user.id).all()
    items = [{"id": item.id, "item_name": item.item_name} for item in wishlist_items]

    return jsonify(items), 200

# Error handler for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    response = {
        "msg": "An unexpected error occurred.",
        "error": str(e)
    }
    return jsonify(response), 500

if __name__ == '__main__':
    app.run(debug=True)
```
