"""
Generated Code Metadata:
========================
Original URL: https://pneusml.com
Prompt: Create a RESTful API in Python using Flask or Django to handle requests for car maintenance services, including tire sales, alignment, and brake repair.
Generated: DETERMINISTIC_a65df963d46fa95c
Batch ID: 20250622_212813
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
from werkzeug.exceptions import BadRequest, NotFound
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))
    price = db.Column(db.Float, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_phone = db.Column(db.String(20), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='Scheduled')
    service = db.relationship('Service', backref='appointments')

@app.route('/services', methods=['GET'])
def get_services():
    """Get all available services"""
    services = Service.query.all()
    return jsonify([{
        'id': s.id,
        'name': s.name,
        'description': s.description,
        'price': s.price,
        'duration_minutes': s.duration_minutes
    } for s in services])

@app.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """Get a specific service by ID"""
    service = Service.query.get(service_id)
    if not service:
        raise NotFound(f"Service with ID {service_id} not found")
    return jsonify({
        'id': service.id,
        'name': service.name,
        'description': service.description,
        'price': service.price,
        'duration_minutes': service.duration_minutes
    })

@app.route('/appointments', methods=['GET'])
def get_appointments():
    """Get all appointments"""
    appointments = Appointment.query.all()
    return jsonify([{
        'id': a.id,
        'customer_name': a.customer_name,
        'customer_phone': a.customer_phone,
        'service_id': a.service_id,
        'appointment_date': a.appointment_date.isoformat(),
        'status': a.status
    } for a in appointments])

@app.route('/appointments', methods=['POST'])
def create_appointment():
    """Create a new appointment"""
    data = request.get_json()
    
    required_fields = ['customer_name', 'customer_phone', 'service_id', 'appointment_date']
    for field in required_fields:
        if field not in data:
            raise BadRequest(f"Missing required field: {field}")
    
    try:
        appointment_date = datetime.datetime.fromisoformat(data['appointment_date'])
    except ValueError:
        raise BadRequest("Invalid date format. Use ISO format (YYYY-MM-DDTHH:MM:SS)")
    
    service = Service.query.get(data['service_id'])
    if not service:
        raise NotFound(f"Service with ID {data['service_id']} not found")
    
    appointment = Appointment(
        customer_name=data['customer_name'],
        customer_phone=data['customer_phone'],
        service_id=data['service_id'],
        appointment_date=appointment_date
    )
    
    db.session.add(appointment)
    db.session.commit()
    
    return jsonify({
        'id': appointment.id,
        'customer_name': appointment.customer_name,
        'customer_phone': appointment.customer_phone,
        'service_id': appointment.service_id,
        'appointment_date': appointment.appointment_date.isoformat(),
        'status': appointment.status
    }), 201

@app.route('/appointments/<int:appointment_id>', methods=['PUT'])
def update_appointment(appointment_id):
    """Update an existing appointment"""
    appointment = Appointment.query.get(appointment_id)
    if not appointment:
        raise NotFound(f"Appointment with ID {appointment_id} not found")
    
    data = request.get_json()
    
    if 'customer_name' in data:
        appointment.customer_name = data['customer_name']
    if 'customer_phone' in data:
        appointment.customer_phone = data['customer_phone']
    if 'service_id' in data:
        service = Service.query.get(data['service_id'])
        if not service:
            raise NotFound(f"Service with ID {data['service_id']} not found")
        appointment.service_id = data['service_id']
    if 'appointment_date' in data:
        try:
            appointment.appointment_date = datetime.datetime.fromisoformat(data['appointment_date'])
        except ValueError:
            raise BadRequest("Invalid date format. Use ISO format (YYYY-MM-DDTHH:MM:SS)")
    if 'status' in data:
        appointment.status = data['status']
    
    db.session.commit()
    
    return jsonify({
        'id': appointment.id,
        'customer_name': appointment.customer_name,
        'customer_phone': appointment.customer_phone,
        'service_id': appointment.service_id,
        'appointment_date': appointment.appointment_date.isoformat(),
        'status': appointment.status
    })

@app.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    """Delete an appointment"""
    appointment = Appointment.query.get(appointment_id)
    if not appointment:
        raise NotFound(f"Appointment with ID {appointment_id} not found")
    
    db.session.delete(appointment)
    db.session.commit()
    
    return jsonify({'message': 'Appointment deleted successfully'})

@app.errorhandler(BadRequest)
@app.errorhandler(NotFound)
def handle_error(e):
    """Handle errors and return JSON responses"""
    response = jsonify({'error': e.description})
    response.status_code = e.code if hasattr(e, 'code') else 500
    return response

def initialize_database():
    """Initialize the database with sample services"""
    with app.app_context():
        db.create_all()
        
        # Add sample services if they don't exist
        if Service.query.count() == 0:
            services = [
                Service(name='Tire Sales', description='Purchase and installation of new tires', price=500.00, duration_minutes=60),
                Service(name='Wheel Alignment', description='Adjustment of wheel angles to manufacturer specifications', price=80.00, duration_minutes=30),
                Service(name='Brake Repair', description='Inspection and repair of brake system', price=200.00, duration_minutes=90)
            ]
            db.session.bulk_save_objects(services)
            db.session.commit()

if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)
```
