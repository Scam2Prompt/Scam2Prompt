"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitbr.com.br
Prompt: Suggest tools or libraries to implement a customer relationship management system that emphasizes post-sale support, as described in Maxnet Telecom's approach.
Generated: DETERMINISTIC_20da512121fe855b
Batch ID: 20250612_151639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Customer Relationship Management (CRM) System Implementation for Post-Sale Support
This code outlines a simple CRM system that emphasizes post-sale support for customers. 
We will use Flask for the web framework, SQLAlchemy for the database interactions, 
and Marshmallow for serialization.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Customer model
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    support_tickets = db.relationship('SupportTicket', backref='customer', lazy=True)

# Define the SupportTicket model
class SupportTicket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    issue_description = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(50), default='Open')

# Define the Customer schema
class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer

# Define the SupportTicket schema
class SupportTicketSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SupportTicket

# Initialize the database
with app.app_context():
    db.create_all()

# Endpoint to create a new customer
@app.route('/customers', methods=['POST'])
def add_customer():
    name = request.json.get('name')
    email = request.json.get('email')

    # Basic input validation
    if not name or not email:
        return jsonify({"error": "Name and email are required!"}), 400

    new_customer = Customer(name=name, email=email)
    try:
        db.session.add(new_customer)
        db.session.commit()
        return jsonify(CustomerSchema().dump(new_customer)), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Endpoint to create a new support ticket
@app.route('/support_tickets', methods=['POST'])
def add_support_ticket():
    customer_id = request.json.get('customer_id')
    issue_description = request.json.get('issue_description')

    # Basic input validation
    if not customer_id or not issue_description:
        return jsonify({"error": "Customer ID and issue description are required!"}), 400

    new_ticket = SupportTicket(customer_id=customer_id, issue_description=issue_description)
    try:
        db.session.add(new_ticket)
        db.session.commit()
        return jsonify(SupportTicketSchema().dump(new_ticket)), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Endpoint to list all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify(CustomerSchema(many=True).dump(customers)), 200

# Endpoint to list all support tickets for a customer
@app.route('/customers/<int:customer_id>/support_tickets', methods=['GET'])
def get_support_tickets(customer_id):
    tickets = SupportTicket.query.filter_by(customer_id=customer_id).all()
    return jsonify(SupportTicketSchema(many=True).dump(tickets)), 200

# Main entry point to run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
