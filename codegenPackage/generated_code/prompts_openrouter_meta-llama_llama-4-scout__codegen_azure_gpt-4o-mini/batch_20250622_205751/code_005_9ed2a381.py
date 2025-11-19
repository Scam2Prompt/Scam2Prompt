"""
Generated Code Metadata:
========================
Original URL: https://budibromotour.ilmaweb.com
Prompt: Design a RESTful API to manage Budi Bromo Tour's services, including booking, payment, and customer management.
Generated: DETERMINISTIC_9ed2a3810ae8ae12
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///budi_bromo_tour.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Customer model
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

# Define the Booking model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    tour_date = db.Column(db.String(10), nullable=False)
    payment_status = db.Column(db.String(20), default='Pending')

# Define the Customer Schema for serialization
class CustomerSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    email = fields.Email(required=True)

# Define the Booking Schema for serialization
class BookingSchema(Schema):
    id = fields.Int()
    customer_id = fields.Int(required=True)
    tour_date = fields.Str(required=True)
    payment_status = fields.Str()

# Initialize schemas
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
booking_schema = BookingSchema()
bookings_schema = BookingSchema(many=True)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Error handling for invalid data
@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err.messages), 400

# Route to create a new customer
@app.route('/customers', methods=['POST'])
def add_customer():
    json_data = request.get_json()
    try:
        customer = customer_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    new_customer = Customer(name=customer['name'], email=customer['email'])
    db.session.add(new_customer)
    db.session.commit()
    return customer_schema.jsonify(new_customer), 201

# Route to get all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return customers_schema.jsonify(customers)

# Route to create a new booking
@app.route('/bookings', methods=['POST'])
def add_booking():
    json_data = request.get_json()
    try:
        booking = booking_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    new_booking = Booking(customer_id=booking['customer_id'], tour_date=booking['tour_date'])
    db.session.add(new_booking)
    db.session.commit()
    return booking_schema.jsonify(new_booking), 201

# Route to get all bookings
@app.route('/bookings', methods=['GET'])
def get_bookings():
    bookings = Booking.query.all()
    return bookings_schema.jsonify(bookings)

# Route to update payment status
@app.route('/bookings/<int:booking_id>/payment', methods=['PUT'])
def update_payment_status(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    json_data = request.get_json()
    payment_status = json_data.get('payment_status')

    if payment_status not in ['Pending', 'Completed', 'Failed']:
        abort(400, description="Invalid payment status")

    booking.payment_status = payment_status
    db.session.commit()
    return booking_schema.jsonify(booking)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
