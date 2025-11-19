"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clarkconstructionllc.net
Prompt: Create a RESTful API endpoint that captures customer details for custom deck and patio designs, inspired by the services provided by Clark Construction LLC.
Generated: DETERMINISTIC_09fdfccb028e4552
Batch ID: 20250612_163526
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

# Initialize Flask application
app = Flask(__name__)

# Configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Customer model
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=False)
    project_type = db.Column(db.String(50), nullable=False)

# Customer Schema for serialization and validation
class CustomerSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    phone = fields.String(required=True)
    project_type = fields.String(required=True)

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to capture customer details
@app.route('/api/customers', methods=['POST'])
def add_customer():
    schema = CustomerSchema()

    # Validate incoming JSON data
    try:
        customer_data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create a new customer entry
    new_customer = Customer(
        name=customer_data['name'],
        email=customer_data['email'],
        phone=customer_data['phone'],
        project_type=customer_data['project_type']
    )

    # Add to the session and commit to the database
    try:
        db.session.add(new_customer)
        db.session.commit()
        return jsonify({"message": "Customer added successfully!", "customer_id": new_customer.id}), 201
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
