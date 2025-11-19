"""
Generated Code Metadata:
========================
Original URL: https://tecnicos-whirlpool.com
Prompt: Design a RESTful API for managing Whirlpool appliance repair and maintenance services, including endpoints for scheduling services, technician assignments, and customer notifications.
Generated: DETERMINISTIC_5dce0452c7bb503e
Batch ID: 20250622_210053
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
from datetime import datetime
import os
from werkzeug.exceptions import HTTPException
from flask_marshmallow import Marshmallow
from marshmallow import fields, ValidationError
from flask_mail import Mail, Message

# Initialize Flask app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'whirlpool.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'your-password'
app.config['MAIL_DEFAULT_SENDER'] = 'no-reply@whirlpool-service.com'

# Initialize extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)
mail = Mail(app)

# Models
class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Technician(db.Model):
    __tablename__ = 'technicians'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    specialization = db.Column(db.String(100), nullable=False)
    is_available = db.Column(db.Boolean, default=True)

class ServiceRequest(db.Model):
    __tablename__ = 'service_requests'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    appliance_type = db.Column(db.String(100), nullable=False)
    model_number = db.Column(db.String(50), nullable=False)
    issue_description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='Pending')
    scheduled_date = db.Column(db.DateTime, nullable=False)
    technician_id = db.Column(db.Integer, db.ForeignKey('technicians.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    customer = db.relationship('Customer', backref='service_requests')
    technician = db.relationship('Technician', backref='service_requests')

class Notification(db.Model):
    __tablename__ = 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    service_request_id = db.Column(db.Integer, db.ForeignKey('service_requests.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    sent_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_read = db.Column(db.Boolean, default=False)
    
    service_request = db.relationship('ServiceRequest', backref='notifications')

# Schemas
class CustomerSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Customer
    
    id = ma.auto_field()
    name = ma.auto_field()
    email = ma.auto_field()
    phone = ma.auto_field()
    address = ma.auto_field()
    created_at = ma.auto_field()

class TechnicianSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Technician
    
    id = ma.auto_field()
    name = ma.auto_field()
    email = ma.auto_field()
    phone = ma.auto_field()
    specialization = ma.auto_field()
    is_available = ma.auto_field()

class ServiceRequestSchema(ma.SQLAlchemySchema):
    class Meta:
        model = ServiceRequest
    
    id = ma.auto_field()
    customer_id = ma.auto_field()
    appliance_type = ma.auto_field()
    model_number = ma.auto_field()
    issue_description = ma.auto_field()
    status = ma.auto_field()
    scheduled_date = ma.auto_field()
    technician_id = ma.auto_field()
    created_at = ma.auto_field()
    
    customer = fields.Nested(CustomerSchema)
    technician = fields.Nested(TechnicianSchema)

class NotificationSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Notification
    
    id = ma.auto_field()
    service_request_id = ma.auto_field()
    message = ma.auto_field()
    sent_at = ma.auto_field()
    is_read = ma.auto_field()

# Initialize schemas
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
technician_schema = TechnicianSchema()
technicians_schema = TechnicianSchema(many=True)
service_request_schema = ServiceRequestSchema()
service_requests_schema = ServiceRequestSchema(many=True)
notification_schema = NotificationSchema()
notifications_schema = NotificationSchema(many=True)

# Error handling
@app.errorhandler(HTTPException)
def handle_exception(e):
    return jsonify({
        "error": e.name,
        "message": e.description
    }), e.code

@app.errorhandler(ValidationError)
def handle_validation_error(e):
    return jsonify(e.messages), 400

# Helper functions
def send_notification_email(recipient, subject, message):
    msg = Message(
        subject=subject,
        recipients=[recipient],
        body=message
    )
    mail.send(msg)

# Routes
@app.route('/customers', methods=['POST'])
def create_customer():
    try:
        data = request.get_json()
        customer = Customer(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            address=data['address']
        )
        db.session.add(customer)
        db.session.commit()
        return customer_schema.jsonify(customer), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    return customer_schema.jsonify(customer)

@app.route('/technicians', methods=['POST'])
def create_technician():
    try:
        data = request.get_json()
        technician = Technician(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            specialization=data['specialization']
        )
        db.session.add(technician)
        db.session.commit()
        return technician_schema.jsonify(technician), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@app.route('/technicians', methods=['GET'])
def get_technicians():
    technicians = Technician.query.all()
    return technicians_schema.jsonify(technicians)

@app.route('/technicians/<int:technician_id>', methods=['GET'])
def get_technician(technician_id):
    technician = Technician.query.get_or_404(technician_id)
    return technician_schema.jsonify(technician)

@app.route('/technicians/<int:technician_id>/availability', methods=['PUT'])
def update_technician_availability(technician_id):
    try:
        technician = Technician.query.get_or_404(technician_id)
        data = request.get_json()
        technician.is_available = data['is_available']
        db.session.commit()
        return technician_schema.jsonify(technician)
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@app.route('/service-requests', methods=['POST'])
def create_service_request():
    try:
        data = request.get_json()
        
        # Validate customer exists
        customer = Customer.query.get_or_404(data['customer_id'])
        
        service_request = ServiceRequest(
            customer_id=data['customer_id'],
            appliance_type=data['appliance_type'],
            model_number=data['model_number'],
            issue_description=data['issue_description'],
            scheduled_date=datetime.strptime(data['scheduled_date'], '%Y-%m-%d %H:%M:%S')
        )
        
        db.session.add(service_request)
        db.session.commit()
        
        # Send notification to customer
        message = f"Your service request for {data['appliance_type']} has been received."
        notification = Notification(
            service_request_id=service_request.id,
            message=message
        )
        db.session.add(notification)
        db.session.commit()
        
        send_notification_email(
            customer.email,
            "Service Request Confirmation",
            message
        )
        
        return service_request_schema.jsonify(service_request), 201
    except Exception as e:
        db.session.rollback()
        return jsonify
