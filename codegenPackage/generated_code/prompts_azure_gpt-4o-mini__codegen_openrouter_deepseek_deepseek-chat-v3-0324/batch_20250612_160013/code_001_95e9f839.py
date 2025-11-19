"""
Generated Code Metadata:
========================
Original URL: https://portal-crypto-io.com
Prompt: Write a code snippet for a web application that allows users to find and book appointments at barbershops across the country, inspired by the services offered by Gould Barbers.
Generated: DETERMINISTIC_95e9f8399c599c26
Batch ID: 20250612_160013
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
from datetime import datetime, timedelta
import pytz
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import re
from typing import List, Dict, Optional

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///barbershop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # In production, use environment variable
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20))
    appointments = db.relationship('Appointment', backref='user', lazy=True)

    def set_password(self, password):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters")
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class BarberShop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    zip_code = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120))
    website = db.Column(db.String(200))
    opening_time = db.Column(db.Time, nullable=False)
    closing_time = db.Column(db.Time, nullable=False)
    barbers = db.relationship('Barber', backref='barbershop', lazy=True)
    appointments = db.relationship('Appointment', backref='barbershop', lazy=True)

class Barber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialization = db.Column(db.String(100))
    barbershop_id = db.Column(db.Integer, db.ForeignKey('barber_shop.id'), nullable=False)
    appointments = db.relationship('Appointment', backref='barber', lazy=True)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    barber_id = db.Column(db.Integer, db.ForeignKey('barber.id'), nullable=False)
    barbershop_id = db.Column(db.Integer, db.ForeignKey('barber_shop.id'), nullable=False)
    service = db.Column(db.String(100), nullable=False)
    appointment_time = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # in minutes
    status = db.Column(db.String(20), default='booked')  # booked, completed, cancelled

# Helper functions
def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone: str) -> bool:
    pattern = r'^\+?[0-9]{10,15}$'
    return re.match(pattern, phone) is not None

def get_available_time_slots(barber_id: int, date: datetime) -> List[Dict]:
    barber = Barber.query.get(barber_id)
    if not barber:
        return []
    
    barbershop = BarberShop.query.get(barber.barbershop_id)
    if not barbershop:
        return []
    
    # Get all appointments for the barber on the given date
    start_of_day = datetime.combine(date, datetime.min.time())
    end_of_day = datetime.combine(date, datetime.max.time())
    
    appointments = Appointment.query.filter(
        Appointment.barber_id == barber_id,
        Appointment.appointment_time >= start_of_day,
        Appointment.appointment_time <= end_of_day,
        Appointment.status == 'booked'
    ).order_by(Appointment.appointment_time).all()
    
    # Generate time slots
    time_slots = []
    current_time = datetime.combine(date, barbershop.opening_time)
    closing_time = datetime.combine(date, barbershop.closing_time)
    slot_duration = timedelta(minutes=30)  # Default slot duration
    
    while current_time + slot_duration <= closing_time:
        slot_end = current_time + slot_duration
        available = True
        
        # Check if slot is available
        for appt in appointments:
            appt_end = appt.appointment_time + timedelta(minutes=appt.duration)
            if (current_time < appt_end) and (slot_end > appt.appointment_time):
                available = False
                current_time = appt_end  # Skip to after this appointment
                break
        
        if available:
            time_slots.append({
                'start': current_time,
                'end': slot_end
            })
            current_time += slot_duration
    
    return time_slots

# API Endpoints
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Validate input
    if not all(k in data for k in ['email', 'password', 'first_name', 'last_name']):
        return jsonify({'error': 'Missing required fields'}), 400
    
    if not validate_email(data['email']):
        return jsonify({'error': 'Invalid email format'}), 400
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already registered'}), 400
    
    try:
        user = User(
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            phone=data.get('phone')
        )
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Registration failed'}), 500
    
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not all(k in data for k in ['email', 'password']):
        return jsonify({'error': 'Missing email or password'}), 400
    
    user = User.query.filter_by(email=data['email']).first()
    if not user or not user.check_password(data['password']):
        return jsonify({'error': 'Invalid email or password'}), 401
    
    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 200

@app.route('/api/barbershops', methods=['GET'])
def get_barbershops():
    city = request.args.get('city')
    state = request.args.get('state')
    
    query = BarberShop.query
    if city:
        query = query.filter(BarberShop.city.ilike(f'%{city}%'))
    if state:
        query = query.filter(BarberShop.state.ilike(f'%{state}%'))
    
    barbershops = query.all()
    result = []
    for shop in barbershops:
        result.append({
            'id': shop.id,
            'name': shop.name,
            'address': shop.address,
            'city': shop.city,
            'state': shop.state,
            'phone': shop.phone
        })
    
    return jsonify(result), 200

@app.route('/api/barbershops/<int:shop_id>/barbers', methods=['GET'])
def get_barbers(shop_id):
    barbers = Barber.query.filter_by(barbershop_id=shop_id).all()
    result = []
    for barber in barbers:
        result.append({
            'id': barber.id,
            'name': barber.name,
            'specialization': barber.specialization
        })
    
    return jsonify(result), 200

@app.route('/api/barbers/<int:barber_id>/availability', methods=['GET'])
@jwt_required()
def get_availability(barber_id):
    date_str = request.args.get('date')
    if not date_str:
        return jsonify({'error': 'Date parameter is required'}), 400
    
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'error': 'Invalid date format
