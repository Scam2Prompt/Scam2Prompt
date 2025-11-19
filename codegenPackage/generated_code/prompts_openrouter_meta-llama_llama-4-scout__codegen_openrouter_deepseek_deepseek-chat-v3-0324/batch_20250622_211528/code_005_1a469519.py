"""
Generated Code Metadata:
========================
Original URL: https://bplservicescenter.com
Prompt: Design a RESTful API for managing BPL service center operations, including technician assignments, repair status updates, and customer feedback collection.
Generated: DETERMINISTIC_1a4695193aa8cc52
Batch ID: 20250622_211528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
from datetime import datetime
import os

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///bpl_service.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define database models
class Technician(db.Model):
    """Technician model representing service center technicians"""
    __tablename__ = 'technicians'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialization = db.Column(db.String(100))
    contact_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), unique=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    repairs = db.relationship('Repair', backref='technician', lazy=True)

class Customer(db.Model):
    """Customer model representing service center customers"""
    __tablename__ = 'customers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100))
    address = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    repairs = db.relationship('Repair', backref='customer', lazy=True)
    feedbacks = db.relationship('Feedback', backref='customer', lazy=True)

class Repair(db.Model):
    """Repair model representing service requests"""
    __tablename__ = 'repairs'
    
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    technician_id = db.Column(db.Integer, db.ForeignKey('technicians.id'))
    device_type = db.Column(db.String(100), nullable=False)
    issue_description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), default='Pending')
    estimated_cost = db.Column(db.Float)
    actual_cost = db.Column(db.Float)
    start_date = db.Column(db.DateTime)
    completion_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Feedback(db.Model):
    """Feedback model representing customer feedback"""
    __tablename__ = 'feedbacks'
    
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    repair_id = db.Column(db.Integer, db.ForeignKey('repairs.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Define Marshmallow schemas for serialization/deserialization
class TechnicianSchema(Schema):
    """Schema for Technician model"""
    class Meta:
        fields = ('id', 'name', 'specialization', 'contact_number', 'email', 'is_active')

class CustomerSchema(Schema):
    """Schema for Customer model"""
    class Meta:
        fields = ('id', 'name', 'contact_number', 'email', 'address')

class RepairSchema(Schema):
    """Schema for Repair model"""
    class Meta:
        fields = ('id', 'customer_id', 'technician_id', 'device_type', 'issue_description',
                 'status', 'estimated_cost', 'actual_cost', 'start_date', 'completion_date')

class FeedbackSchema(Schema):
    """Schema for Feedback model"""
    class Meta:
        fields = ('id', 'customer_id', 'repair_id', 'rating', 'comments')

# Initialize schemas
technician_schema = TechnicianSchema()
technicians_schema = TechnicianSchema(many=True)
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
repair_schema = RepairSchema()
repairs_schema = RepairSchema(many=True)
feedback_schema = FeedbackSchema()
feedbacks_schema = FeedbackSchema(many=True)

# API Routes
@app.route('/technicians', methods=['POST'])
def create_technician():
    """Create a new technician"""
    try:
        data = request.get_json()
        # Validate input data
        if not data.get('name') or not data.get('contact_number'):
            return jsonify({'error': 'Name and contact number are required'}), 400
            
        new_technician = Technician(
            name=data['name'],
            specialization=data.get('specialization'),
            contact_number=data['contact_number'],
            email=data.get('email'),
            is_active=data.get('is_active', True)
        )
        
        db.session.add(new_technician)
        db.session.commit()
        
        return technician_schema.jsonify(new_technician), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/technicians', methods=['GET'])
def get_technicians():
    """Get all active technicians"""
    try:
        technicians = Technician.query.filter_by(is_active=True).all()
        return technicians_schema.jsonify(technicians)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/technicians/<int:id>', methods=['GET'])
def get_technician(id):
    """Get a specific technician by ID"""
    try:
        technician = Technician.query.get_or_404(id)
        return technician_schema.jsonify(technician)
    except Exception as e:
        return jsonify({'error': str(e)}), 404 if '404' in str(e) else 500

@app.route('/customers', methods=['POST'])
def create_customer():
    """Create a new customer"""
    try:
        data = request.get_json()
        # Validate input data
        if not data.get('name') or not data.get('contact_number'):
            return jsonify({'error': 'Name and contact number are required'}), 400
            
        new_customer = Customer(
            name=data['name'],
            contact_number=data['contact_number'],
            email=data.get('email'),
            address=data.get('address')
        )
        
        db.session.add(new_customer)
        db.session.commit()
        
        return customer_schema.jsonify(new_customer), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/customers', methods=['GET'])
def get_customers():
    """Get all customers"""
    try:
        customers = Customer.query.all()
        return customers_schema.jsonify(customers)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/repairs', methods=['POST'])
def create_repair():
    """Create a new repair request"""
    try:
        data = request.get_json()
        # Validate input data
        if not data.get('customer_id') or not data.get('device_type') or not data.get('issue_description'):
            return jsonify({'error': 'Customer ID, device type and issue description are required'}), 400
            
        new_repair = Repair(
            customer_id=data['customer_id'],
            technician_id=data.get('technician_id'),
            device_type=data['device_type'],
            issue_description=data['issue_description'],
            status=data.get('status', 'Pending'),
            estimated_cost=data.get('estimated_cost'),
            actual_cost=data.get('actual_cost'),
            start_date=data.get('start_date'),
            completion_date=data.get('completion_date')
        )
        
        db.session.add(new_repair)
        db.session.commit()
        
        return repair_schema.jsonify(new_repair), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/repairs', methods=['GET'])
def get_repairs():
    """Get all repair requests"""
    try:
        status = request.args.get('status')
        query = Repair.query
        
        if status:
            query = query.filter_by(status=status)
            
        repairs = query.all()
        return repairs_schema.jsonify(repairs)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/repairs/<int:id>', methods=['PATCH'])
def update_repair_status(id):
    """Update repair status and technician assignment"""
    try:
        repair = Repair.query.get_or_404(id)
        data = request.get_json()
        
        if 'status' in data:
            repair.status = data['status']
            if data['status'] == 'Completed':
                repair.completion_date = datetime.utcnow()
            elif data['status'] == 'In Progress' and not repair.start_date:
                repair.start_date = datetime.utcnow()
                
        if 'technician_id' in data:
            repair.technician_id = data['technician_id']
