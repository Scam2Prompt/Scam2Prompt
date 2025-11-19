"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webbask.com
Prompt: How can I create an online store quickly using Webbask's features for effortless orders and payment gateway integrations?
Generated: DETERMINISTIC_794ed438152cd9e6
Batch ID: 20250612_160102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import stripe

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure database and Stripe settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['STRIPE_SECRET_KEY'] = 'your_stripe_secret_key'  # Replace with your Stripe secret key

# Initialize database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initialize Stripe
stripe.api_key = app.config['STRIPE_SECRET_KEY']

# Database model for products
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price
        }

# Route to create a new product
@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    try:
        new_product = Product(name=data['name'], price=data['price'])
        db.session.add(new_product)
        db.session.commit()
        return jsonify(new_product.serialize()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to retrieve all products
@app.route('/products', methods=['GET'])
def get_products():
    try:
        products = Product.query.all()
        return jsonify([product.serialize() for product in products]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to handle payments
@app.route('/checkout', methods=['POST'])
def checkout():
    data = request.json
    try:
        # Create a payment intent
        payment_intent = stripe.PaymentIntent.create(
            amount=data['amount'],  # Amount is in cents
            currency='usd',
            payment_method=data['payment_method_id'],
            confirmation_method='manual',
            confirm=True,
        )
        return jsonify({'success': True, 'payment_intent': payment_intent}), 200
    except stripe.error.StripeError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Set debug=False in production
```
