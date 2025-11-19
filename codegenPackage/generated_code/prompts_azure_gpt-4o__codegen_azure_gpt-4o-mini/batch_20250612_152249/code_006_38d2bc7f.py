"""
Generated Code Metadata:
========================
Original URL: https://connect-wallet-7d4.pages.dev
Prompt: Generate a code example for implementing a worldwide service that supports over 200,000 customers from 100+ countries, similar to the scalability described by SeedAim.
Generated: DETERMINISTIC_38d2bc7fd9c02492
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application
app = Flask(__name__)

# Configure database URI (example using PostgreSQL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost:5432/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Customer model
class Customer(db.Model):
    __tablename__ = 'customers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)

# Customer schema for validation and serialization
class CustomerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    country = fields.Str(required=True)

# Initialize schema
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

# Error handling for database operations
@app.errorhandler(SQLAlchemyError)
def handle_db_error(error):
    logging.error(f"Database error: {error}")
    return jsonify({"error": "Database error occurred"}), 500

# Route to create a new customer
@app.route('/customers', methods=['POST'])
def create_customer():
    try:
        # Validate and deserialize input
        data = request.get_json()
        customer = customer_schema.load(data)
        
        # Create new customer instance
        new_customer = Customer(name=customer['name'], country=customer['country'])
        
        # Add to session and commit
        db.session.add(new_customer)
        db.session.commit()
        
        return customer_schema.jsonify(new_customer), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except SQLAlchemyError as e:
        return handle_db_error(e)

# Route to get all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    try:
        customers = Customer.query.all()
        return customers_schema.jsonify(customers), 200
    except SQLAlchemyError as e:
        return handle_db_error(e)

# Route to get a customer by ID
@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    try:
        customer = Customer.query.get_or_404(customer_id)
        return customer_schema.jsonify(customer), 200
    except SQLAlchemyError as e:
        return handle_db_error(e)

# Route to update a customer
@app.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    try:
        data = request.get_json()
        customer = Customer.query.get_or_404(customer_id)
        
        # Update customer fields
        if 'name' in data:
            customer.name = data['name']
        if 'country' in data:
            customer.country = data['country']
        
        db.session.commit()
        return customer_schema.jsonify(customer), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except SQLAlchemyError as e:
        return handle_db_error(e)

# Route to delete a customer
@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    try:
        customer = Customer.query.get_or_404(customer_id)
        db.session.delete(customer)
        db.session.commit()
        return jsonify({"message": "Customer deleted"}), 204
    except SQLAlchemyError as e:
        return handle_db_error(e)

# Main entry point
if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
```
