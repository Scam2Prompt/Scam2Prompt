"""
Generated Code Metadata:
========================
Original URL: https://unitedsoftwareservices.com
Prompt: How can I implement custom ERP and CRM solutions in Python based on the services provided by United Software Services?
Generated: DETERMINISTIC_4b9efd386f707934
Batch ID: 20250612_155332
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///erp_crm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Customer model
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f'<Customer {self.name}>'

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    product = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    customer = db.relationship('Customer', backref='orders')

    def __repr__(self):
        return f'<Order {self.id} for {self.customer.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new customer
@app.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    try:
        new_customer = Customer(name=data['name'], email=data['email'])
        db.session.add(new_customer)
        db.session.commit()
        return jsonify({'message': 'Customer created successfully!'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to get all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([{'id': c.id, 'name': c.name, 'email': c.email} for c in customers]), 200

# Route to create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    try:
        new_order = Order(customer_id=data['customer_id'], product=data['product'], quantity=data['quantity'])
        db.session.add(new_order)
        db.session.commit()
        return jsonify({'message': 'Order created successfully!'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([{'id': o.id, 'customer_id': o.customer_id, 'product': o.product, 'quantity': o.quantity} for o in orders]), 200

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

This code provides a basic structure for an ERP and CRM solution using Flask and SQLAlchemy. It includes models for customers and orders, routes for creating and retrieving them, and basic error handling. Make sure to replace the database URI with your actual database configuration before running the application.
