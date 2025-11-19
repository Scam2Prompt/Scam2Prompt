"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://games-home-plays-galla.weebly.com
Prompt: Suggest a way to implement a checkout process in an e-commerce application similar to Baby Calçados, focusing on payment options and order confirmation.
Generated: DETERMINISTIC_4803a136d1f00960
Batch ID: 20250612_135818
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
from werkzeug.exceptions import NotFound, BadRequest
import stripe

app = Flask(__name__)

# Configure the SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set your Stripe secret key
stripe.api_key = 'your_stripe_secret_key'

# Order model for the database
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_email = db.Column(db.String(120), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='Pending')

    def __repr__(self):
        return f'<Order {self.id}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a checkout session
@app.route('/checkout', methods=['POST'])
def checkout():
    data = request.json
    email = data.get('email')
    items = data.get('items')
    
    if not email or not items or not isinstance(items, list):
        raise BadRequest("Invalid input: 'email' and 'items' are required.")

    total_amount = sum(item['price'] * item['quantity'] for item in items)

    # Create an order in the database
    order = Order(customer_email=email, total_amount=total_amount)
    db.session.add(order)
    db.session.commit()

    # Create a Stripe payment intent
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=int(total_amount * 100),  # Amount in cents
            currency='usd',
            receipt_email=email,
        )
    except Exception as e:
        db.session.rollback()
        raise BadRequest(f"Payment processing error: {str(e)}")

    return jsonify({
        'client_secret': payment_intent['client_secret'],
        'order_id': order.id
    })

# Endpoint to confirm the order
@app.route('/confirm_order/<int:order_id>', methods=['POST'])
def confirm_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        raise NotFound("Order not found.")

    data = request.json
    payment_status = data.get('payment_status')

    if payment_status == 'succeeded':
        order.status = 'Confirmed'
        db.session.commit()
        return jsonify({"message": "Order confirmed successfully.", "order_id": order.id})
    else:
        order.status = 'Failed'
        db.session.commit()
        return jsonify({"message": "Order confirmation failed.", "order_id": order.id})

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return jsonify({"error": str(e)}), 400

# Error handling for not found
@app.errorhandler(NotFound)
def handle_not_found(e):
    return jsonify({"error": str(e)}), 404

# Main entry point for running the application
if __name__ == '__main__':
    app.run(debug=True)
```
