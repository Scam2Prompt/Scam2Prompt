"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://obsidiajeans.com.br
Prompt: Illustrate how to implement a secure payment system for an online clothing store that accepts multiple payment methods, similar to the options provided by Obsidia Jeans.
Generated: DETERMINISTIC_3db77fd01477aa43
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import stripe

app = Flask(__name__)

# Configure your database URI and Stripe secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['STRIPE_SECRET_KEY'] = 'your_stripe_secret_key_here'

db = SQLAlchemy(app)
stripe.api_key = app.config['STRIPE_SECRET_KEY']

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='Pending')

# Endpoint to register a new user
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'error': 'Username and password required'}), 400
    
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password)
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully'}), 201

# Endpoint to handle payment
@app.route('/pay', methods=['POST'])
def process_payment():
    data = request.get_json()
    token = data.get('token')
    amount = data.get('amount')
    user_id = data.get('user_id')

    if not token or not amount or not user_id:
        return jsonify({'error': 'Payment token, amount, and user ID are required'}), 400

    try:
        # Create a charge with Stripe
        charge = stripe.Charge.create(
            amount=int(amount * 100),  # Stripe expects the amount in cents
            currency='usd',
            description='Clothing Store Purchase',
            source=token
        )

        # Record the order in the database
        order = Order(user_id=user_id, amount=amount, status='Paid')
        db.session.add(order)
        db.session.commit()

        return jsonify({'message': 'Payment successful', 'charge_id': charge.id}), 200

    except stripe.error.StripeError as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'An error occurred, please try again later.'}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
```
