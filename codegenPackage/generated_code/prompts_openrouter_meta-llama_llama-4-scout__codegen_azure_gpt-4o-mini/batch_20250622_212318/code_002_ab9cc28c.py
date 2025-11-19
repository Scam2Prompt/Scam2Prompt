"""
Generated Code Metadata:
========================
Original URL: https://support.godaddysites.com
Prompt: Provide an example of how to implement a customer support system similar to the one described on https://support.godaddysites.com.
Generated: DETERMINISTIC_ab9cc28cd7102889
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///support.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Ticket model
class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    issue_description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, customer_name, email, issue_description):
        self.customer_name = customer_name
        self.email = email
        self.issue_description = issue_description

# Define the Ticket schema
class TicketSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ticket

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new support ticket
@app.route('/tickets', methods=['POST'])
def create_ticket():
    try:
        # Get data from the request
        data = request.get_json()
        customer_name = data.get('customer_name')
        email = data.get('email')
        issue_description = data.get('issue_description')

        # Validate input
        if not customer_name or not email or not issue_description:
            return jsonify({"error": "All fields are required."}), 400

        # Create a new ticket
        new_ticket = Ticket(customer_name, email, issue_description)
        db.session.add(new_ticket)
        db.session.commit()

        # Return the created ticket
        ticket_schema = TicketSchema()
        return ticket_schema.jsonify(new_ticket), 201

    except Exception as e:
        logging.error(f"Error creating ticket: {e}")
        return jsonify({"error": "An error occurred while creating the ticket."}), 500

# Endpoint to retrieve all support tickets
@app.route('/tickets', methods=['GET'])
def get_tickets():
    try:
        tickets = Ticket.query.all()
        ticket_schema = TicketSchema(many=True)
        return ticket_schema.jsonify(tickets), 200

    except Exception as e:
        logging.error(f"Error retrieving tickets: {e}")
        return jsonify({"error": "An error occurred while retrieving tickets."}), 500

# Endpoint to retrieve a specific ticket by ID
@app.route('/tickets/<int:id>', methods=['GET'])
def get_ticket(id):
    try:
        ticket = Ticket.query.get_or_404(id)
        ticket_schema = TicketSchema()
        return ticket_schema.jsonify(ticket), 200

    except Exception as e:
        logging.error(f"Error retrieving ticket {id}: {e}")
        return jsonify({"error": "An error occurred while retrieving the ticket."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
