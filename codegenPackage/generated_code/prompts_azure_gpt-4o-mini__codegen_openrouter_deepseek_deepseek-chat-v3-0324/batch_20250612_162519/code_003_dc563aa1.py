"""
Generated Code Metadata:
========================
Original URL: https://www.drpharmacy.in
Prompt: Create a RESTful API design for a pharmacy that handles medication inventory and customer orders, ensuring data privacy compliance.
Generated: DETERMINISTIC_dc563aa1738b429f
Batch ID: 20250612_162519
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
from functools import wraps
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pharmacy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'admin', 'pharmacist', 'customer'

class Medication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    requires_prescription = db.Column(db.Boolean, default=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    medication_id = db.Column(db.Integer, db.ForeignKey('medication.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    status = db.Column(db.String(20), default='pending')  # 'pending', 'approved', 'rejected', 'fulfilled'

class Prescription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    medication_id = db.Column(db.Integer, db.ForeignKey('medication.id'), nullable=False)
    doctor_name = db.Column(db.String(100), nullable=False)
    issue_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    expiry_date = db.Column(db.DateTime)

# Helper functions
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.filter_by(id=data['id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_user, *args, **kwargs)
    return decorated

def admin_required(f):
    @wraps(f)
    def decorated(current_user, *args, **kwargs):
        if current_user.role != 'admin':
            return jsonify({'message': 'Admin access required!'}), 403
        return f(current_user, *args, **kwargs)
    return decorated

def pharmacist_required(f):
    @wraps(f)
    def decorated(current_user, *args, **kwargs):
        if current_user.role not in ['admin', 'pharmacist']:
            return jsonify({'message': 'Pharmacist access required!'}), 403
        return f(current_user, *args, **kwargs)
    return decorated

# Authentication routes
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(
        username=data['username'],
        password=hashed_password,
        role=data['role']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Could not verify'}), 401
    
    user = User.query.filter_by(username=auth.username).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    if check_password_hash(user.password, auth.password):
        token = jwt.encode({
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, app.config['SECRET_KEY'])
        return jsonify({'token': token})
    
    return jsonify({'message': 'Invalid credentials'}), 401

# Medication routes
@app.route('/medications', methods=['GET'])
@token_required
def get_medications(current_user):
    medications = Medication.query.all()
    output = []
    for med in medications:
        med_data = {
            'id': med.id,
            'name': med.name,
            'description': med.description,
            'quantity': med.quantity,
            'price': med.price,
            'requires_prescription': med.requires_prescription
        }
        output.append(med_data)
    return jsonify({'medications': output})

@app.route('/medications', methods=['POST'])
@token_required
@admin_required
def add_medication(current_user):
    data = request.get_json()
    new_medication = Medication(
        name=data['name'],
        description=data.get('description', ''),
        quantity=data['quantity'],
        price=data['price'],
        requires_prescription=data.get('requires_prescription', False)
    )
    db.session.add(new_medication)
    db.session.commit()
    return jsonify({'message': 'Medication added successfully'}), 201

@app.route('/medications/<int:med_id>', methods=['PUT'])
@token_required
@admin_required
def update_medication(current_user, med_id):
    medication = Medication.query.get(med_id)
    if not medication:
        return jsonify({'message': 'Medication not found'}), 404
    
    data = request.get_json()
    medication.name = data.get('name', medication.name)
    medication.description = data.get('description', medication.description)
    medication.quantity = data.get('quantity', medication.quantity)
    medication.price = data.get('price', medication.price)
    medication.requires_prescription = data.get('requires_prescription', medication.requires_prescription)
    
    db.session.commit()
    return jsonify({'message': 'Medication updated successfully'})

# Order routes
@app.route('/orders', methods=['POST'])
@token_required
def create_order(current_user):
    data = request.get_json()
    medication = Medication.query.get(data['medication_id'])
    
    if not medication:
        return jsonify({'message': 'Medication not found'}), 404
    
    if medication.requires_prescription:
        prescription = Prescription.query.filter_by(
            user_id=current_user.id,
            medication_id=data['medication_id']
        ).filter(Prescription.expiry_date >= datetime.datetime.utcnow()).first()
        
        if not prescription:
            return jsonify({'message': 'Valid prescription required for this medication'}), 403
    
    if medication.quantity < data['quantity']:
        return jsonify({'message': 'Not enough stock available'}), 400
    
    new_order = Order(
        user_id=current_user.id,
        medication_id=data['medication_id'],
        quantity=data['quantity']
    )
    
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'Order created successfully'}), 201

@app.route('/orders', methods=['GET'])
@token_required
def get_orders(current_user):
    if current_user.role in ['admin', 'pharmacist']:
        orders = Order.query.all()
    else:
        orders = Order.query.filter_by(user_id=current_user.id).all()
    
    output = []
    for order in orders:
        order_data = {
            'id': order.id,
            'user_id': order.user_id,
            'medication_id': order.medication_id,
            'quantity': order.quantity,
            'order_date': order.order_date,
            'status': order.status
        }
        output.append(order_data)
    return jsonify({'orders': output})

@app.route('/orders/<int:order_id>', methods=['PUT'])
@token_required
@pharmacist_required
def update_order_status(current_user, order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'message': 'Order not found'}), 404
    
    data = request.get_json()
    order.status = data['status']
    
    if order.status == 'approved':
        medication = Medication.query.get(order.medication_id)
        medication.quantity -= order.quantity
    
    db.session.commit()
    return jsonify({'message': 'Order status updated successfully'})

# Prescription routes
@app.route('/prescriptions', methods=['POST'])
@token_required
def add_prescription(current_user):
    data = request.get_json()
    new_prescription = Prescription(
        user_id=current_user.id,
        medication_id=data
