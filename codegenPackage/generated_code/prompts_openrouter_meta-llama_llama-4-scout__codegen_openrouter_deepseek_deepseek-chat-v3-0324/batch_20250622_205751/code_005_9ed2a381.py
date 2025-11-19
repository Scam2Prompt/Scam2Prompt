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
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_marshmallow import Marshmallow
from marshmallow import fields, ValidationError
import datetime
import uuid

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///budi_bromo_tours.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Initialize extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Database Models
class Customer(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class TourPackage(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    duration = db.Column(db.String(50))
    available = db.Column(db.Boolean, default=True)

class Booking(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    customer_id = db.Column(db.String(36), db.ForeignKey('customer.id'), nullable=False)
    package_id = db.Column(db.String(36), db.ForeignKey('tour_package.id'), nullable=False)
    booking_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    tour_date = db.Column(db.DateTime, nullable=False)
    participants = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, confirmed, cancelled, completed
    payment_status = db.Column(db.String(20), default='unpaid')  # unpaid, paid, refunded

    customer = db.relationship('Customer', backref='bookings')
    package = db.relationship('TourPackage', backref='bookings')

class Payment(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    booking_id = db.Column(db.String(36), db.ForeignKey('booking.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    payment_method = db.Column(db.String(50), nullable=False)
    transaction_id = db.Column(db.String(100))
    status = db.Column(db.String(20), default='pending')  # pending, completed, failed

    booking = db.relationship('Booking', backref='payments')

# Marshmallow Schemas
class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer
        exclude = ('password_hash',)

    password = fields.String(required=True, load_only=True)

class TourPackageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TourPackage

class BookingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Booking
        include_fk = True

    customer = fields.Nested(CustomerSchema)
    package = fields.Nested(TourPackageSchema)

class PaymentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Payment
        include_fk = True

    booking = fields.Nested(BookingSchema)

# Initialize schemas
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
tour_package_schema = TourPackageSchema()
tour_packages_schema = TourPackageSchema(many=True)
booking_schema = BookingSchema()
bookings_schema = BookingSchema(many=True)
payment_schema = PaymentSchema()
payments_schema = PaymentSchema(many=True)

# Routes
@app.route('/')
def index():
    return jsonify({"message": "Welcome to Budi Bromo Tours API"})

# Customer Routes
@app.route('/customers', methods=['POST'])
def create_customer():
    try:
        data = customer_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    if Customer.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already registered"}), 400

    customer = Customer(
        name=data['name'],
        email=data['email'],
        phone=data['phone']
    )
    customer.set_password(data['password'])

    db.session.add(customer)
    db.session.commit()

    return customer_schema.jsonify(customer), 201

@app.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return customers_schema.jsonify(customers)

@app.route('/customers/<id>', methods=['GET'])
def get_customer(id):
    customer = Customer.query.get_or_404(id)
    return customer_schema.jsonify(customer)

@app.route('/customers/<id>', methods=['PUT'])
def update_customer(id):
    customer = Customer.query.get_or_404(id)
    try:
        data = customer_schema.load(request.json, partial=True)
    except ValidationError as err:
        return jsonify(err.messages), 400

    if 'name' in data:
        customer.name = data['name']
    if 'email' in data:
        customer.email = data['email']
    if 'phone' in data:
        customer.phone = data['phone']
    if 'password' in data:
        customer.set_password(data['password'])

    db.session.commit()
    return customer_schema.jsonify(customer)

@app.route('/customers/<id>', methods=['DELETE'])
def delete_customer(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    return jsonify({"message": "Customer deleted successfully"})

# Tour Package Routes
@app.route('/packages', methods=['POST'])
def create_package():
    try:
        data = tour_package_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    package = TourPackage(
        name=data['name'],
        description=data.get('description'),
        price=data['price'],
        duration=data.get('duration'),
        available=data.get('available', True)
    )

    db.session.add(package)
    db.session.commit()

    return tour_package_schema.jsonify(package), 201

@app.route('/packages', methods=['GET'])
def get_packages():
    packages = TourPackage.query.all()
    return tour_packages_schema.jsonify(packages)

@app.route('/packages/<id>', methods=['GET'])
def get_package(id):
    package = TourPackage.query.get_or_404(id)
    return tour_package_schema.jsonify(package)

@app.route('/packages/<id>', methods=['PUT'])
def update_package(id):
    package = TourPackage.query.get_or_404(id)
    try:
        data = tour_package_schema.load(request.json, partial=True)
    except ValidationError as err:
        return jsonify(err.messages), 400

    if 'name' in data:
        package.name = data['name']
    if 'description' in data:
        package.description = data['description']
    if 'price' in data:
        package.price = data['price']
    if 'duration' in data:
        package.duration = data['duration']
    if 'available' in data:
        package.available = data['available']

    db.session.commit()
    return tour_package_schema.jsonify(package)

@app.route('/packages/<id>', methods=['DELETE'])
def delete_package(id):
    package = TourPackage.query.get_or_404(id)
    db.session.delete(package)
    db.session.commit()
    return jsonify({"message": "Package deleted successfully"})

# Booking Routes
@app.route('/bookings', methods=['POST'])
def create_booking():
    try:
        data = booking_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    booking = Booking(
        customer_id=data['customer_id'],
        package_id=data['package_id'],
        tour_date=data['tour_date'],
        participants=data['participants'],
        status=data.get('status', 'pending')
    )

    db.session.add(booking)
    db.session.commit()

    return booking_schema.jsonify(booking), 201

@app.route('/bookings', methods=['GET'])
def get_bookings():
    bookings = Booking.query.all()
    return bookings_schema.jsonify(bookings)

@app.route('/bookings/<id>', methods=['GET'])
def get_booking(id):
    booking = Booking.query.get_or
