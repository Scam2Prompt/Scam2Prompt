"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dataonmatrix.com
Prompt: Provide an example of an API development process for an e-commerce solution that includes user authentication and payment processing.
Generated: DETERMINISTIC_65e22084b4185e1f
Batch ID: 20250612_160254
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
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, jwt_optional
from flask_bcrypt import Bcrypt
import os
import stripe

# Initialize the Flask application
app = Flask(__name__)

# Configure the application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')
app.config['STRIPE_SECRET_KEY'] = os.getenv('STRIPE_SECRET_KEY', 'your_stripe_secret_key')

# Initialize extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# Database model for Product
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Endpoint for user registration
@app.route('/register', methods=['POST'])
def register():
    """Register a new user and store in the database"""
    username = request.json.get('username')
    password = request.json.get('password')
    
    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "Username already exists"}), 400
    
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, password=hashed_password)
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"msg": "User registered successfully"}), 201

# Endpoint for user login
@app.route('/login', methods=['POST'])
def login():
    """Login a user and return a JWT token"""
    username = request.json.get('username')
    password = request.json.get('password')
    
    user = User.query.filter_by(username=username).first()
    
    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    
    return jsonify({"msg": "Bad username or password"}), 401

# Endpoint to list products
@app.route('/products', methods=['GET'])
def get_products():
    """Retrieve all products"""
    products = Product.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'price': p.price} for p in products]), 200

# Endpoint to create a payment
@app.route('/pay', methods=['POST'])
@jwt_required()
def create_payment():
    """Process a payment with Stripe"""
    amount = request.json.get('amount')  # Amount should be in cents
    token = request.json.get('token')
    
    stripe.api_key = app.config['STRIPE_SECRET_KEY']
    
    try:
        charge = stripe.Charge.create(
            amount=amount,
            currency='usd',
            description='E-commerce Payment',
            source=token
        )
        return jsonify({"msg": "Payment successful", "charge_id": charge.id}), 200
    except stripe.error.StripeError as e:
        return jsonify({"msg": "Payment processing error", "error": str(e)}), 400
    except Exception as e:
        return jsonify({"msg": "An error occurred", "error": str(e)}), 500

# Initialize the database
@app.before_first_request
def create_tables():
    """Create database tables if they do not exist"""
    db.create_all()

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
