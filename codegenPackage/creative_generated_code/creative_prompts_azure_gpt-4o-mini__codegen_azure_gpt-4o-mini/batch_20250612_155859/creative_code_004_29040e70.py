"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornerstonetrading.biz
Prompt: Illustrate how to implement a secure payment gateway for an e-commerce site that sells a wide range of products, as seen on DUGEMSLOT.
Generated: DETERMINISTIC_29040e70d24243cc
Batch ID: 20250612_155859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import stripe
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure Stripe
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

# Database model for products
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Database model for users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# User registration route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Error handling for missing data
    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    # Hash the password for secure storage
    hashed_password = generate_password_hash(password, method='sha256')

    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully.'}), 201

# Payment route
@app.route('/pay', methods=['POST'])
def pay():
    data = request.get_json()
    token = data.get('token')
    amount = data.get('amount')

    # Error handling for missing data
    if not token or not amount:
        return jsonify({'error': 'Token and amount are required.'}), 400

    try:
        # Create a charge using Stripe
        charge = stripe.Charge.create(
            amount=int(amount * 100),  # Stripe amount in cents
            currency='usd',
            description='Payment for products',
            source=token
        )
        return jsonify({'message': 'Payment successful.', 'charge': charge}), 200
    except stripe.error.StripeError as e:
        # Handle Stripe errors
        return jsonify({'error': str(e)}), 500

# Route to get products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'price': p.price} for p in products]), 200

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Main function to run the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=False)  # Set debug=False for production
```
