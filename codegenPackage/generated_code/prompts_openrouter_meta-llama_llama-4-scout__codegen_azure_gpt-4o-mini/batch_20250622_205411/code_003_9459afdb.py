"""
Generated Code Metadata:
========================
Original URL: https://1inch.danngol.com
Prompt: Design a system architecture for a social value-creating platform that benefits both customers and stores through prepaid discounts.
Generated: DETERMINISTIC_9459afdbd65fa94a
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# social_value_platform.py

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///social_value_platform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Customer model
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    prepaid_balance = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return f'<Customer {self.name}>'

# Define the Store model
class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    discount_rate = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Store {self.name}>'

# Define the Transaction model
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    customer = db.relationship('Customer', backref='transactions')
    store = db.relationship('Store', backref='transactions')

    def __repr__(self):
        return f'<Transaction {self.id}>'

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to add a new customer
@app.route('/customers', methods=['POST'])
def add_customer():
    data = request.get_json()
    new_customer = Customer(name=data['name'], email=data['email'])
    try:
        db.session.add(new_customer)
        db.session.commit()
        return jsonify({'message': 'Customer added successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Email already exists!'}), 400

# Endpoint to add a new store
@app.route('/stores', methods=['POST'])
def add_store():
    data = request.get_json()
    new_store = Store(name=data['name'], discount_rate=data['discount_rate'])
    db.session.add(new_store)
    db.session.commit()
    return jsonify({'message': 'Store added successfully!'}), 201

# Endpoint to add prepaid balance to a customer
@app.route('/customers/<int:customer_id>/balance', methods=['POST'])
def add_balance(customer_id):
    data = request.get_json()
    customer = Customer.query.get_or_404(customer_id)
    customer.prepaid_balance += data['amount']
    db.session.commit()
    return jsonify({'message': 'Balance updated successfully!'}), 200

# Endpoint to create a transaction
@app.route('/transactions', methods=['POST'])
def create_transaction():
    data = request.get_json()
    customer = Customer.query.get_or_404(data['customer_id'])
    store = Store.query.get_or_404(data['store_id'])

    # Calculate the discount
    discount = store.discount_rate * data['amount']
    total_amount = data['amount'] - discount

    # Check if customer has enough balance
    if customer.prepaid_balance < total_amount:
        return jsonify({'error': 'Insufficient balance!'}), 400

    # Deduct the amount from the customer's balance
    customer.prepaid_balance -= total_amount
    new_transaction = Transaction(customer_id=customer.id, store_id=store.id, amount=total_amount)
    
    db.session.add(new_transaction)
    db.session.commit()
    
    return jsonify({'message': 'Transaction completed successfully!'}), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
