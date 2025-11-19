"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emarket.ps
Prompt: Describe how to set up a secure payment system for an e-commerce site that sells items like customizable mugs and framed posters.
Generated: DETERMINISTIC_3060e1b15011540d
Batch ID: 20250612_155356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import stripe

# Initialize the Flask application
app = Flask(__name__)

# Set up the database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///ecommerce.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Database model for Product
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Route to register a new user
@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    
    # Hash the password
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    # Create a new user
    new_user = User(username=username, password=hashed_password)
    
    # Add user to the database
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"msg": "User registered successfully!"}), 201

# Route to log in a user
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    user = User.query.filter_by(username=username).first()
    
    # Verify password
    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    
    return jsonify({"msg": "Bad credentials"}), 401

# Route to create a payment intent
@app.route('/create-payment-intent', methods=['POST'])
@jwt_required()
def create_payment():
    amount = request.json.get('amount')  # Amount should be in cents
    currency = request.json.get('currency', 'usd')
    
    try:
        # Create a Stripe payment intent
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
        )
        return jsonify({"client_secret": payment_intent['client_secret']}), 200
    
    except Exception as e:
        return jsonify(error=str(e)), 400  # Handle errors appropriately

# Main entry point for running the application
if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    # Run the app in debug mode for development
    app.run(debug=True, host='0.0.0.0', port=5000)
```
