"""
Generated Code Metadata:
========================
Original URL: https://atakoynakliyat.gen.tr
Prompt: Create a RESTful API using Flask or Django to manage Ataköy nakliyat services, including endpoints for creating, reading, updating, and deleting customer requests, services, and payments.
Generated: DETERMINISTIC_7d3255498a4e7771
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
from werkzeug.exceptions import HTTPException
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'atakoy_nakliyat.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models
class CustomerRequest(db.Model):
    __tablename__ = 'customer_requests'
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100))
    from_address = db.Column(db.String(255), nullable=False)
    to_address = db.Column(db.String(255), nullable=False)
    request_date = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), default='Pending')
    notes = db.Column(db.Text)

class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    is_active = db.Column(db.Boolean, default=True)

class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)
    customer_request_id = db.Column(db.Integer, db.ForeignKey('customer_requests.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.String(20), nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    transaction_id = db.Column(db.String(100))
    status = db.Column(db.String(20), default='Pending')

# Schemas for validation
class CustomerRequestSchema(Schema):
    id = fields.Int(dump_only=True)
    customer_name = fields.Str(required=True)
    phone_number = fields.Str(required=True)
    email = fields.Str()
    from_address = fields.Str(required=True)
    to_address = fields.Str(required=True)
    request_date = fields.Str(required=True)
    status = fields.Str()
    notes = fields.Str()

class ServiceSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    price = fields.Float(required=True)
    is_active = fields.Bool()

class PaymentSchema(Schema):
    id = fields.Int(dump_only=True)
    customer_request_id = fields.Int(required=True)
    amount = fields.Float(required=True)
    payment_date = fields.Str(required=True)
    payment_method = fields.Str(required=True)
    transaction_id = fields.Str()
    status = fields.Str()

# Initialize schemas
customer_request_schema = CustomerRequestSchema()
service_schema = ServiceSchema()
payment_schema = PaymentSchema()

# Error handling
@app.errorhandler(HTTPException)
def handle_exception(e):
    return jsonify({
        "error": e.name,
        "message": e.description,
    }), e.code

@app.errorhandler(ValidationError)
def handle_validation_error(e):
    return jsonify({
        "error": "Validation Error",
        "messages": e.messages,
    }), 400

# Customer Request Endpoints
@app.route('/api/customer_requests', methods=['POST'])
def create_customer_request():
    try:
        data = request.get_json()
        errors = customer_request_schema.validate(data)
        if errors:
            raise ValidationError(errors)
        
        new_request = CustomerRequest(
            customer_name=data['customer_name'],
            phone_number=data['phone_number'],
            email=data.get('email'),
            from_address=data['from_address'],
            to_address=data['to_address'],
            request_date=data['request_date'],
            status=data.get('status', 'Pending'),
            notes=data.get('notes')
        )
        
        db.session.add(new_request)
        db.session.commit()
        
        return customer_request_schema.jsonify(new_request), 201
    except Exception as e:
        db.session.rollback()
        raise e

@app.route('/api/customer_requests', methods=['GET'])
def get_all_customer_requests():
    requests = CustomerRequest.query.all()
    return jsonify(customer_request_schema.dump(requests, many=True)), 200

@app.route('/api/customer_requests/<int:id>', methods=['GET'])
def get_customer_request(id):
    request = CustomerRequest.query.get_or_404(id)
    return customer_request_schema.jsonify(request), 200

@app.route('/api/customer_requests/<int:id>', methods=['PUT'])
def update_customer_request(id):
    try:
        request_to_update = CustomerRequest.query.get_or_404(id)
        data = request.get_json()
        errors = customer_request_schema.validate(data)
        if errors:
            raise ValidationError(errors)
        
        request_to_update.customer_name = data.get('customer_name', request_to_update.customer_name)
        request_to_update.phone_number = data.get('phone_number', request_to_update.phone_number)
        request_to_update.email = data.get('email', request_to_update.email)
        request_to_update.from_address = data.get('from_address', request_to_update.from_address)
        request_to_update.to_address = data.get('to_address', request_to_update.to_address)
        request_to_update.request_date = data.get('request_date', request_to_update.request_date)
        request_to_update.status = data.get('status', request_to_update.status)
        request_to_update.notes = data.get('notes', request_to_update.notes)
        
        db.session.commit()
        return customer_request_schema.jsonify(request_to_update), 200
    except Exception as e:
        db.session.rollback()
        raise e

@app.route('/api/customer_requests/<int:id>', methods=['DELETE'])
def delete_customer_request(id):
    try:
        request_to_delete = CustomerRequest.query.get_or_404(id)
        db.session.delete(request_to_delete)
        db.session.commit()
        return jsonify({"message": "Customer request deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        raise e

# Service Endpoints
@app.route('/api/services', methods=['POST'])
def create_service():
    try:
        data = request.get_json()
        errors = service_schema.validate(data)
        if errors:
            raise ValidationError(errors)
        
        new_service = Service(
            name=data['name'],
            description=data.get('description'),
            price=data['price'],
            is_active=data.get('is_active', True)
        )
        
        db.session.add(new_service)
        db.session.commit()
        
        return service_schema.jsonify(new_service), 201
    except Exception as e:
        db.session.rollback()
        raise e

@app.route('/api/services', methods=['GET'])
def get_all_services():
    services = Service.query.all()
    return jsonify(service_schema.dump(services, many=True)), 200

@app.route('/api/services/<int:id>', methods=['GET'])
def get_service(id):
    service = Service.query.get_or_404(id)
    return service_schema.jsonify(service), 200

@app.route('/api/services/<int:id>', methods=['PUT'])
def update_service(id):
    try:
        service_to_update = Service.query.get_or_404(id)
        data = request.get_json()
        errors = service_schema.validate(data)
        if errors:
            raise ValidationError(errors)
        
        service_to_update.name = data.get('name', service_to_update.name)
        service_to_update.description = data.get('description', service_to_update.description)
        service_to_update.price = data.get('price', service_to_update.price)
        service_to_update.is_active = data.get('is_active', service_to_update.is_active)
        
        db.session.commit()
        return service_schema.jsonify(service_to_update), 200
    except Exception as e:
        db.session.rollback()
        raise e

@app.route('/api/services/<int:id>', methods=['DELETE'])
def delete_service(id):
    try:
        service_to_delete = Service.query.get_or_404(id)
        db.session.delete(service_to_delete)
        db.session.commit()
        return jsonify({"message": "Service deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        raise e

# Payment Endpoints
@app.route('/api/payments', methods=['POST'])
def create_payment():
    try:
        data = request.get_json()
        errors = payment_schema.validate(data)
        if errors:
            raise ValidationError(errors)
        
        new_payment = Payment(
            customer_request_id=data['customer_request_id'],
            amount=data['amount'],
            payment_date=data['payment_date'],
            payment_method=data['payment_method'],
            transaction_id=data.get('transaction_id'),
            status=data.get('status', 'Pending')
        )
