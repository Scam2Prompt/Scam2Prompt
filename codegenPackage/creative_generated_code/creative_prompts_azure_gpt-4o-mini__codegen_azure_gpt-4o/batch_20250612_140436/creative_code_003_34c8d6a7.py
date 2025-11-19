"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thegraphicdesigner.link
Prompt: Create a library recommendation for building an online store specifically tailored for graphic designers.
Generated: DETERMINISTIC_34c8d6a76b234b64
Batch ID: 20250612_140436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Online Store Library for Graphic Designers

This library provides essential functionalities to build an online store
specifically tailored for graphic designers. It includes product management,
checkout processing, and customer interaction features.

Dependencies:
- Flask: Lightweight web framework for building the store's interface.
- SQLAlchemy: Database management for storing product details and orders.
- Stripe: Payment gateway integration for checkout processing.

Install dependencies using pip:
pip install flask sqlalchemy stripe
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import stripe

# Initialize Flask app
app = Flask(__name__)

# Configure database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Stripe API key (replace with your actual key)
stripe.api_key = "your_stripe_api_key_here"

# Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)  # Price in USD
    image_url = db.Column(db.String(200), nullable=False)  # URL for product image

    def to_dict(self):
        """Convert product details to dictionary format for JSON responses."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "image_url": self.image_url,
        }

# Initialize database
with app.app_context():
    db.create_all()

# Route to list all products
@app.route('/products', methods=['GET'])
def list_products():
    try:
        products = Product.query.all()
        return jsonify([product.to_dict() for product in products]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to add a new product (for admin use)
@app.route('/products', methods=['POST'])
def add_product():
    try:
        data = request.json
        new_product = Product(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            image_url=data['image_url']
        )
        db.session.add(new_product)
        db.session.commit()
        return jsonify({"message": "Product added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to process checkout
@app.route('/checkout', methods=['POST'])
def checkout():
    try:
        data = request.json
        # Example format: {"product_id": 1, "quantity": 2, "payment_method_id": "pm_card_visa"}
        product = Product.query.get(data['product_id'])
        if not product:
            return jsonify({"error": "Product not found"}), 404

        # Calculate total price
        total_price = product.price * data['quantity']

        # Payment processing using Stripe
        payment_intent = stripe.PaymentIntent.create(
            amount=int(total_price * 100),  # Stripe expects amount in cents
            currency='usd',
            payment_method=data['payment_method_id'],
            confirm=True
        )

        return jsonify({
            "message": "Payment successful",
            "payment_intent": payment_intent
        }), 200
    except stripe.error.StripeError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
