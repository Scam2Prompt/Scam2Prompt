"""
Generated Code Metadata:
========================
Original URL: https://applestorebali.com
Prompt: Recommend APIs or libraries for building an e-commerce platform to sell Apple products online, considering features like payment gateways and trade-in options.
Generated: DETERMINISTIC_c9c265700fae29d0
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# E-commerce Platform for Apple Products
# This code demonstrates integration with various APIs/libraries for building an e-commerce platform

import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import stripe
import paypalrestsdk
from tradein import TradeInCalculator  # Hypothetical trade-in library

# Initialize Flask app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'apple_store.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Payment Gateway Configurations
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
paypalrestsdk.configure({
    "mode": os.getenv('PAYPAL_MODE', 'sandbox'),
    "client_id": os.getenv('PAYPAL_CLIENT_ID'),
    "client_secret": os.getenv('PAYPAL_CLIENT_SECRET')
})

# Product Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    category = db.Column(db.String(50))  # iPhone, Mac, iPad, etc.
    stock = db.Column(db.Integer)
    
    def __init__(self, name, description, price, category, stock):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.stock = stock

# Product Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'category', 'stock')

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Trade-in Endpoint
@app.route('/tradein', methods=['POST'])
def trade_in():
    try:
        data = request.json
        device = data['device']
        condition = data['condition']
        
        # Initialize trade-in calculator
        calculator = TradeInCalculator(api_key=os.getenv('TRADEIN_API_KEY'))
        value = calculator.estimate(device, condition)
        
        return jsonify({
            'status': 'success',
            'trade_in_value': value,
            'device': device,
            'condition': condition
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

# Payment Endpoints
@app.route('/payment/stripe', methods=['POST'])
def stripe_payment():
    try:
        data = request.json
        amount = int(data['amount'] * 100)  # Convert to cents
        
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='usd',
            payment_method=data['payment_method_id'],
            confirmation_method='manual',
            confirm=True
        )
        
        return jsonify({
            'status': 'success',
            'client_secret': payment_intent.client_secret
        }), 200
    except stripe.error.StripeError as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

@app.route('/payment/paypal', methods=['POST'])
def paypal_payment():
    try:
        data = request.json
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "transactions": [{
                "amount": {
                    "total": str(data['amount']),
                    "currency": "USD"
                },
                "description": "Apple Product Purchase"
            }],
            "redirect_urls": {
                "return_url": os.getenv('PAYPAL_RETURN_URL'),
                "cancel_url": os.getenv('PAYPAL_CANCEL_URL')
            }
        })
        
        if payment.create():
            return jsonify({
                'status': 'success',
                'approval_url': [link.href for link in payment.links if link.rel == 'approval_url'][0]
            }), 200
        else:
            return jsonify({'status': 'error', 'message': payment.error}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

# Product Endpoints
@app.route('/products', methods=['GET'])
def get_products():
    try:
        all_products = Product.query.all()
        result = products_schema.dump(all_products)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/product/<id>', methods=['GET'])
def get_product(id):
    try:
        product = Product.query.get(id)
        if not product:
            return jsonify({'status': 'error', 'message': 'Product not found'}), 404
        return product_schema.jsonify(product), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Main
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)
```

```python
# requirements.txt
flask==2.0.1
flask-sqlalchemy==2.5.1
flask-marshmallow==0.14.0
marshmallow-sqlalchemy==0.28.1
stripe==2.60.0
paypalrestsdk==1.13.1
python-dotenv==0.19.0
```
