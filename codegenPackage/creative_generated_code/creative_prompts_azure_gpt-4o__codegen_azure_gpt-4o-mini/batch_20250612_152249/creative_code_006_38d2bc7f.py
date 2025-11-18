"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connect-wallet-7d4.pages.dev
Prompt: Generate a code example for implementing a worldwide service that supports over 200,000 customers from 100+ countries, similar to the scalability described by SeedAim.
Generated: DETERMINISTIC_38d2bc7fd9c02492
Batch ID: 20250612_152249
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
from marshmallow import Schema, fields, ValidationError
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database with a SQLite example
# In production, replace with a more robust database like PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Customer model
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    country = db.Column(db.String(100), nullable=False)

# Define a schema for serializing Customer data
class CustomerSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    country = fields.Str(required=True)

# Initialize the schema
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.description})
    response.content_type = "application/json"
    return response

# Endpoint to create a new customer
@app.route('/customers', methods=['POST'])
def create_customer():
    """
    Create a new customer.
    Expected JSON format:
    {
        "name": "Customer Name",
        "email": "customer@example.com",
        "country": "Country Name"
    }
    """
    try:
        # Validate and deserialize input
        customer_data = request.get_json()
        customer = customer_schema.load(customer_data)
        
        # Create a new customer instance
        new_customer = Customer(**customer)
        db.session.add(new_customer)
        db.session.commit()
        
        return customer_schema.jsonify(new_customer), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    """
    Retrieve all customers.
    Returns a JSON array of customers.
    """
    try:
        customers = Customer.query.all()
        return customers_schema.jsonify(customers), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Initialize the database and create tables
with app.app_context():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
