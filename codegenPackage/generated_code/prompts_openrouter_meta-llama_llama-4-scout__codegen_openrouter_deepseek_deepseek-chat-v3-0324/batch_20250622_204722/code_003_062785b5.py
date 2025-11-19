"""
Generated Code Metadata:
========================
Original URL: https://ankarateknikservisi.com
Prompt: Design a RESTful API for managing repair services for white goods, including endpoints for scheduling appointments, tracking repair status, and providing diagnostic information, inspired by the services offered on the Ankara Teknik Servisi website.
Generated: DETERMINISTIC_062785b5e8e8aa2a
Batch ID: 20250622_204722
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
from werkzeug.exceptions import HTTPException
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///repair_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class Customer(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Appliance(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    customer_id = db.Column(db.String(36), db.ForeignKey('customer.id'), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # e.g., refrigerator, washing machine
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    serial_number = db.Column(db.String(100))
    purchase_date = db.Column(db.Date)
    warranty_expiry = db.Column(db.Date)

class RepairService(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    appliance_id = db.Column(db.String(36), db.ForeignKey('appliance.id'), nullable=False)
    technician_id = db.Column(db.String(36), nullable=False)
    scheduled_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='Scheduled')  # Scheduled, In Progress, Completed, Cancelled
    diagnosis = db.Column(db.Text)
    repair_notes = db.Column(db.Text)
    parts_used = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

# Error Handler
@app.errorhandler(HTTPException)
def handle_exception(e):
    response = jsonify({
        "error": e.name,
        "message": e.description,
    })
    response.status_code = e.code
    return response

# Customer Endpoints
@app.route('/api/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    try:
        customer = Customer(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            address=data['address']
        )
        db.session.add(customer)
        db.session.commit()
        return jsonify({"message": "Customer created successfully", "customer_id": customer.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to create customer", "details": str(e)}), 400

@app.route('/api/customers/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    return jsonify({
        "id": customer.id,
        "name": customer.name,
        "email": customer.email,
        "phone": customer.phone,
        "address": customer.address,
        "created_at": customer.created_at.isoformat()
    })

# Appliance Endpoints
@app.route('/api/appliances', methods=['POST'])
def create_appliance():
    data = request.get_json()
    try:
        appliance = Appliance(
            customer_id=data['customer_id'],
            type=data['type'],
            brand=data['brand'],
            model=data['model'],
            serial_number=data.get('serial_number'),
            purchase_date=datetime.strptime(data['purchase_date'], '%Y-%m-%d').date() if 'purchase_date' in data else None,
            warranty_expiry=datetime.strptime(data['warranty_expiry'], '%Y-%m-%d').date() if 'warranty_expiry' in data else None
        )
        db.session.add(appliance)
        db.session.commit()
        return jsonify({"message": "Appliance registered successfully", "appliance_id": appliance.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to register appliance", "details": str(e)}), 400

@app.route('/api/appliances/<appliance_id>', methods=['GET'])
def get_appliance(appliance_id):
    appliance = Appliance.query.get_or_404(appliance_id)
    return jsonify({
        "id": appliance.id,
        "customer_id": appliance.customer_id,
        "type": appliance.type,
        "brand": appliance.brand,
        "model": appliance.model,
        "serial_number": appliance.serial_number,
        "purchase_date": appliance.purchase_date.isoformat() if appliance.purchase_date else None,
        "warranty_expiry": appliance.warranty_expiry.isoformat() if appliance.warranty_expiry else None
    })

# Repair Service Endpoints
@app.route('/api/repairs', methods=['POST'])
def schedule_repair():
    data = request.get_json()
    try:
        repair = RepairService(
            appliance_id=data['appliance_id'],
            technician_id=data['technician_id'],
            scheduled_date=datetime.strptime(data['scheduled_date'], '%Y-%m-%d %H:%M'),
            diagnosis=data.get('diagnosis'),
            status=data.get('status', 'Scheduled')
        )
        db.session.add(repair)
        db.session.commit()
        return jsonify({"message": "Repair scheduled successfully", "repair_id": repair.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to schedule repair", "details": str(e)}), 400

@app.route('/api/repairs/<repair_id>', methods=['GET'])
def get_repair(repair_id):
    repair = RepairService.query.get_or_404(repair_id)
    return jsonify({
        "id": repair.id,
        "appliance_id": repair.appliance_id,
        "technician_id": repair.technician_id,
        "scheduled_date": repair.scheduled_date.isoformat(),
        "status": repair.status,
        "diagnosis": repair.diagnosis,
        "repair_notes": repair.repair_notes,
        "parts_used": repair.parts_used,
        "created_at": repair.created_at.isoformat(),
        "updated_at": repair.updated_at.isoformat() if repair.updated_at else None
    })

@app.route('/api/repairs/<repair_id>/status', methods=['PATCH'])
def update_repair_status(repair_id):
    data = request.get_json()
    repair = RepairService.query.get_or_404(repair_id)
    try:
        repair.status = data['status']
        if 'repair_notes' in data:
            repair.repair_notes = data['repair_notes']
        if 'parts_used' in data:
            repair.parts_used = data['parts_used']
        db.session.commit()
        return jsonify({"message": "Repair status updated successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to update repair status", "details": str(e)}), 400

@app.route('/api/repairs/<repair_id>/diagnosis', methods=['PATCH'])
def update_diagnosis(repair_id):
    data = request.get_json()
    repair = RepairService.query.get_or_404(repair_id)
    try:
        repair.diagnosis = data['diagnosis']
        db.session.commit()
        return jsonify({"message": "Diagnosis updated successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to update diagnosis", "details": str(e)}), 400

# Utility Endpoint
@app.route('/api/repairs/customer/<customer_id>', methods=['GET'])
def get_customer_repairs(customer_id):
    appliances = Appliance.query.filter_by(customer_id=customer_id).all()
    appliance_ids = [appliance.id for appliance in appliances]
    repairs = RepairService.query.filter(RepairService.appliance_id.in_(appliance_ids)).all()
    
    repairs_list = []
    for repair in repairs:
        repairs_list.append({
            "id": repair.id,
            "appliance_id": repair.appliance_id,
            "status": repair.status,
            "scheduled_date": repair.scheduled_date.isoformat(),
            "diagnosis": repair.diagnosis
        })
    
    return jsonify({"repairs": repairs_list})

# Initialize Database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
```
