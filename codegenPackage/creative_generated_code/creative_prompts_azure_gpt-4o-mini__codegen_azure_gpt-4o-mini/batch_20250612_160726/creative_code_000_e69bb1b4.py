"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symibyotic.fi
Prompt: How can I implement a secure payment system for purchasing domain names similar to the one described on symibyotic.fi?
Generated: DETERMINISTIC_e69bb1b4f3df0a91
Batch ID: 20250612_160726
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
import requests
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Load environment variables from .env file
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

# Configuration for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model for database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

# Payment model for storing payment information
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    domain_name = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='Pending')

# Endpoint for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Invalid input'}), 400
    
    hashed_password = generate_password_hash(data['password'])
    
    new_user = User(username=data['username'], password_hash=hashed_password)
    
    try:
        db.session.add(new_user)
        db.session.commit()
    except IntegrityError:
        return jsonify({'message': 'Username already exists'}), 400

    return jsonify({'message': 'User registered successfully'}), 201

# Endpoint for initiating a payment
@app.route('/pay', methods=['POST'])
def pay():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('domain_name') or not data.get('amount'):
        return jsonify({'message': 'Invalid input'}), 400

    user = User.query.filter_by(username=data['username']).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404

    payment = Payment(user_id=user.id, domain_name=data['domain_name'], amount=data['amount'])
    db.session.add(payment)
    db.session.commit()

    # Here you would integrate with a payment gateway
    # Simulating a payment gateway response
    payment_response = simulate_payment_gateway(payment)
    
    # Update payment status based on payment gateway response
    payment.status = payment_response['status']
    db.session.commit()

    return jsonify({'message': 'Payment processed', 'status': payment.status}), 200

def simulate_payment_gateway(payment):
    # Simulated payment processing logic; In a real scenario, this would call an external API
    return {'status': 'Success'}

# Error handling for all unhandled exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({'message': str(e)}), 500

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create tables if they don't exist
    app.run(host='0.0.0.0', port=5000)
``` 

**Note**: Ensure your `.env` file contains the `DATABASE_URI` for the SQLAlchemy connection. Configure the payment processing with a real payment gateway like Stripe or PayPal for production use.
