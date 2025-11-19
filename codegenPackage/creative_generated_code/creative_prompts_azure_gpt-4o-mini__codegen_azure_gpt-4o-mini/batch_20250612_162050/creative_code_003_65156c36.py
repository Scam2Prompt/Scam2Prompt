"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taramediaworks.com
Prompt: Provide an example of a personalized bulk messaging API that could be used to enhance customer engagement for a digital marketing agency.
Generated: DETERMINISTIC_65156c36132a216e
Batch ID: 20250612_162050
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
from flask_marshmallow import Marshmallow
from twilio.rest import Client
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and schema
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Twilio configuration
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')

# Customer model
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False, unique=True)

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number


# Customer schema for serialization
class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer


# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/customers', methods=['POST'])
def add_customer():
    """
    Add a new customer to the database.
    Expects JSON with 'name' and 'phone_number'.
    """
    try:
        name = request.json['name']
        phone_number = request.json['phone_number']
        new_customer = Customer(name=name, phone_number=phone_number)
        db.session.add(new_customer)
        db.session.commit()
        return CustomerSchema().jsonify(new_customer), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/send_bulk_message', methods=['POST'])
def send_bulk_message():
    """
    Send a personalized message to all customers.
    Expects JSON with 'message'.
    """
    try:
        message_content = request.json['message']
        customers = Customer.query.all()
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        for customer in customers:
            message = client.messages.create(
                body=f"Hello {customer.name}, {message_content}",
                from_=TWILIO_PHONE_NUMBER,
                to=customer.phone_number
            )

        return jsonify({"message": "Messages sent successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

This code implements a simple RESTful API using Flask to manage a customer database and send personalized bulk messages via Twilio. Make sure to set the required environment variables for Twilio credentials before running the application.
