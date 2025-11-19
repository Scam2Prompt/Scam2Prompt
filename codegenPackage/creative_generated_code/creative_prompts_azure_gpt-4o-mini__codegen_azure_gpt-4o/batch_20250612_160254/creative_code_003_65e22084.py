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
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import stripe
import os

# Initialize the Flask application
app = Flask(__name__)

# Configuration for database, JWT, and Stripe
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
app.config['STRIPE_SECRET_KEY'] = 'your_stripe_secret_key'

db = SQLAlchemy(app)
jwt = JWTManager(app)
stripe.api_key = app.config['STRIPE_SECRET_KEY']

### Database Models ###
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)

### Routes ###
@app.route('/register', methods=['POST'])
def register():
    """
    Register a new user.
    """
    data = request.json
    if not data or 'username' not in data or 'password' not in data:
        abort(400, description="Invalid request data")
        
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists'}), 400

    # Create and save the new user
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    """
    Authenticate user and generate JWT token.
    """
    data = request.json
    if not data or 'username' not in data or 'password' not in data:
        abort(400, description="Invalid request data")
    
    # Check user credentials
    user = User.query.filter_by(username=data['username']).first()
    if user and user.password == data['password']:
        access_token = create_access_token(identity=user.username)
        return jsonify({'access_token': access_token}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/products', methods=['GET'])
@jwt_required()
def get_products():
    """
    Fetch all products. Requires JWT authentication.
    """
    products = Product.query.all()
    product_list = [{'id': p.id, 'name': p.name, 'price': p.price} for p in products]
    return jsonify({'products': product_list}), 200

@app.route('/purchase', methods=['POST'])
@jwt_required()
def purchase_product():
    """
    Process payment and purchase a product.
    """
    data = request.json
    if not data or 'product_id' not in data or 'payment_token' not in data:
        abort(400, description="Invalid request data")
    
    product = Product.query.get(data['product_id'])
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    
    # Process payment with Stripe
    try:
        stripe.PaymentIntent.create(
            amount=int(product.price * 100),  # Stripe requires price in cents
            currency='usd',
            payment_method=data['payment_token'],
            confirm=True
        )
        return jsonify({'message': 'Payment successful, product purchased'}), 200
    except stripe.error.StripeError as e:
        return jsonify({'message': f"Payment failed: {str(e)}"}), 400

### Error Handling ###
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad Request', 'message': error.description}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found', 'message': error.description}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal Server Error', 'message': 'An unexpected error occurred'}), 500

### Application Entry Point ###
if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    
    # Run the application
    app.run(debug=True)
```
