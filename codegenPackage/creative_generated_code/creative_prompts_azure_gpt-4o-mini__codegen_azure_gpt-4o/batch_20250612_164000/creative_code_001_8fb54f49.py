"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jieyasoft.com
Prompt: How can I create a custom e-commerce platform that integrates with a direct selling system, based on the features outlined by Jieya Software?
Generated: DETERMINISTIC_8fb54f49b85b8884
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Since the request is for code only, here's an implementation in Python using Flask, SQLAlchemy, and REST APIs to demonstrate how you could create a basic e-commerce platform with integration for direct selling. Note that this is a simplified structure suitable for expansion based on custom requirements inspired by Jieya Software.

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)

# Database configuration (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define models
class User(db.Model):
    """Model representing a user in the platform."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    referral_code = db.Column(db.String(100), unique=True)
    referred_by = db.Column(db.String(100), db.ForeignKey('user.referral_code'), nullable=True)
    
    def __repr__(self):
        return f"<User {self.name}>"

class Product(db.Model):
    """Model representing a product in the platform."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"<Product {self.name}>"

class Order(db.Model):
    """Model representing an order in the platform."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f"<Order {self.id}>"

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Define routes
@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a new user.
    Required data: name, email, password, referral_code (optional)
    """
    try:
        data = request.json
        name = data['name']
        email = data['email']
        password = data['password']
        referral_code = data.get('referral_code')
        referred_by = data.get('referred_by')
        
        user = User(
            name=name,
            email=email,
            password=password,
            referral_code=referral_code,
            referred_by=referred_by
        )
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User registered successfully!", "user": {
            "name": user.name,
            "email": user.email,
            "referral_code": user.referral_code
        }}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Email or referral code already exists."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/products', methods=['GET'])
def get_products():
    """Endpoint to retrieve the list of all products."""
    products = Product.query.all()
    return jsonify([
        {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "stock": product.stock
        } for product in products
    ]), 200

@app.route('/order', methods=['POST'])
def create_order():
    """
    Endpoint to create a new order.
    Required data: user_id, product_id, quantity
    """
    try:
        data = request.json
        user_id = data['user_id']
        product_id = data['product_id']
        quantity = data['quantity']
        
        # Fetch user and product from the database
        user = User.query.get(user_id)
        product = Product.query.get(product_id)
        
        if not user or not product:
            return jsonify({"error": "Invalid user or product ID."}), 404
        
        if product.stock < quantity:
            return jsonify({"error": "Insufficient stock available."}), 400
        
        total_price = product.price * quantity
        order = Order(
            user_id=user_id,
            product_id=product_id,
            quantity=quantity,
            total_price=total_price
        )
        
        # Update product stock
        product.stock -= quantity
        
        db.session.add(order)
        db.session.commit()
        return jsonify({"message": "Order created successfully!", "order": {
            "id": order.id,
            "user_id": order.user_id,
            "product_id": order.product_id,
            "quantity": order.quantity,
            "total_price": order.total_price
        }}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/referrals/<user_id>', methods=['GET'])
def get_referrals(user_id):
    """
    Endpoint to get referrals for a specific user.
    """
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({"error": "User not found."}), 404
        
        referrals = User.query.filter_by(referred_by=user.referral_code).all()
        return jsonify([
            {
                "id": referral.id,
                "name": referral.name,
                "email": referral.email
            } for referral in referrals
        ]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Set up the database before running the application by calling the `/` route or the `create_tables` function.
- Replace SQLite with a production-grade database like PostgreSQL or MySQL for scalability.
- Implement authentication and authorization mechanisms for better security.
