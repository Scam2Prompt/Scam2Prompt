"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rope-bunny.com
Prompt: Develop a code example that integrates a payment gateway for a website selling custom leather products, inspired by the checkout process on Rope-Bunny.de.
Generated: DETERMINISTIC_1c7dbbef712c5e56
Batch ID: 20250612_162051
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
import stripe
import os

# Initialize Flask app
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up Stripe API keys
stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

# Database model for Products
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

# Route to get available products
@app.route('/products', methods=['GET'])
def get_products():
    try:
        products = Product.query.all()
        return jsonify([{'id': p.id, 'name': p.name, 'price': p.price} for p in products]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to create a payment intent
@app.route('/create-payment-intent', methods=['POST'])
def create_payment():
    try:
        data = request.json
        amount = data['amount']  # Amount in cents
        currency = data['currency']

        # Create a PaymentIntent with the order amount and currency
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            automatic_payment_methods={'enabled': True},
        )
        return jsonify({'clientSecret': payment_intent['client_secret']}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Route to handle successful payment
@app.route('/payment-success', methods=['POST'])
def payment_success():
    try:
        data = request.json
        # Here you can handle what to do on successful payment
        # e.g., saving order details to the database
        return jsonify({'status': 'success', 'message': 'Payment completed successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main driver function
if __name__ == '__main__':
    # Run the app
    app.run(debug=True)
```

### Note
- Make sure to set the `STRIPE_SECRET_KEY` environment variable with your Stripe secret key before running the application.
- You need to have Flask and Stripe libraries installed. You can install them using:
  ```bash
  pip install Flask Flask-SQLAlchemy stripe
  ```
- Replace the SQLite database with a production-ready database (like PostgreSQL or MySQL) for deployment.
