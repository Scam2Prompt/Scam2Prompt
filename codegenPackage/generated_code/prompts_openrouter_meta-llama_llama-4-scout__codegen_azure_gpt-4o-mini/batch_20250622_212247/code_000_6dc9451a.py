"""
Generated Code Metadata:
========================
Original URL: https://monadtech.net
Prompt: "Write a code solution for a business that needs to modernize its technology and elevate customer experiences, using cutting-edge tech solutions."
Generated: DETERMINISTIC_6dc9451a6dd763ab
Batch ID: 20250622_212247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application
app = Flask(__name__)

# Configure database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define Customer model
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

# Create a schema for validating customer data
class CustomerSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)

# Initialize the schema
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

# Error handling for database operations
@app.errorhandler(SQLAlchemyError)
def handle_db_error(error):
    return jsonify({"error": str(error)}), 500

# Endpoint to create a new customer
@app.route('/customers', methods=['POST'])
def add_customer():
    try:
        # Validate and deserialize input data
        data = request.get_json()
        customer_data = customer_schema.load(data)

        # Create a new customer instance
        new_customer = Customer(name=customer_data['name'], email=customer_data['email'])
        
        # Add the customer to the session and commit
        db.session.add(new_customer)
        db.session.commit()

        return customer_schema.jsonify(new_customer), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except SQLAlchemyError as e:
        return handle_db_error(e)

# Endpoint to retrieve all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    try:
        customers = Customer.query.all()
        return customers_schema.jsonify(customers), 200
    except SQLAlchemyError as e:
        return handle_db_error(e)

# Endpoint to retrieve a customer by ID
@app.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    try:
        customer = Customer.query.get_or_404(id)
        return customer_schema.jsonify(customer), 200
    except SQLAlchemyError as e:
        return handle_db_error(e)

# Endpoint to update a customer
@app.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    try:
        data = request.get_json()
        customer_data = customer_schema.load(data)

        customer = Customer.query.get_or_404(id)
        customer.name = customer_data['name']
        customer.email = customer_data['email']

        db.session.commit()
        return customer_schema.jsonify(customer), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except SQLAlchemyError as e:
        return handle_db_error(e)

# Endpoint to delete a customer
@app.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    try:
        customer = Customer.query.get_or_404(id)
        db.session.delete(customer)
        db.session.commit()
        return jsonify({"message": "Customer deleted successfully."}), 204
    except SQLAlchemyError as e:
        return handle_db_error(e)

# Run the application
if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
