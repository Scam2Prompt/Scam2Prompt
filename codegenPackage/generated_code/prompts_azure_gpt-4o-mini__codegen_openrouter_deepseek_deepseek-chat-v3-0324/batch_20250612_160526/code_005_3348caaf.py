"""
Generated Code Metadata:
========================
Original URL: https://tekrollindustrial.com.br
Prompt: Design a RESTful API for managing equipment maintenance schedules for lifting and moving machinery, based on Tekroll Industrial's service offerings.
Generated: DETERMINISTIC_3348caafe9e25c32
Batch ID: 20250612_160526
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
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///equipment.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class Equipment(db.Model):
    """Equipment model representing lifting/moving machinery"""
    __tablename__ = 'equipment'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    serial_number = db.Column(db.String(100), unique=True, nullable=False)
    purchase_date = db.Column(db.Date, nullable=False)
    last_maintenance_date = db.Column(db.Date)
    next_maintenance_date = db.Column(db.Date)
    maintenance_frequency_days = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default='operational')
    
    maintenance_records = db.relationship('MaintenanceRecord', backref='equipment', lazy=True)

class MaintenanceRecord(db.Model):
    """Maintenance record model"""
    __tablename__ = 'maintenance_records'
    
    id = db.Column(db.Integer, primary_key=True)
    equipment_id = db.Column(db.Integer, db.ForeignKey('equipment.id'), nullable=False)
    maintenance_date = db.Column(db.Date, nullable=False)
    technician = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    parts_replaced = db.Column(db.Text)
    next_maintenance_date = db.Column(db.Date, nullable=False)

# Error Handling
@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    response = e.get_response()
    response.data = jsonify({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    }).data
    response.content_type = "application/json"
    return response

# Helper Functions
def validate_equipment_data(data):
    """Validate equipment data"""
    required_fields = ['name', 'model', 'serial_number', 'purchase_date', 'maintenance_frequency_days']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")
    
    try:
        datetime.strptime(data['purchase_date'], '%Y-%m-%d')
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD")

# Routes
@app.route('/api/equipment', methods=['GET'])
def get_all_equipment():
    """Get all equipment"""
    equipment_list = Equipment.query.all()
    return jsonify([{
        'id': eq.id,
        'name': eq.name,
        'model': eq.model,
        'serial_number': eq.serial_number,
        'status': eq.status,
        'next_maintenance_date': eq.next_maintenance_date.strftime('%Y-%m-%d') if eq.next_maintenance_date else None
    } for eq in equipment_list])

@app.route('/api/equipment/<int:equipment_id>', methods=['GET'])
def get_equipment(equipment_id):
    """Get specific equipment by ID"""
    equipment = Equipment.query.get_or_404(equipment_id)
    return jsonify({
        'id': equipment.id,
        'name': equipment.name,
        'model': equipment.model,
        'serial_number': equipment.serial_number,
        'purchase_date': equipment.purchase_date.strftime('%Y-%m-%d'),
        'last_maintenance_date': equipment.last_maintenance_date.strftime('%Y-%m-%d') if equipment.last_maintenance_date else None,
        'next_maintenance_date': equipment.next_maintenance_date.strftime('%Y-%m-%d') if equipment.next_maintenance_date else None,
        'maintenance_frequency_days': equipment.maintenance_frequency_days,
        'status': equipment.status
    })

@app.route('/api/equipment', methods=['POST'])
def add_equipment():
    """Add new equipment"""
    data = request.get_json()
    try:
        validate_equipment_data(data)
        
        equipment = Equipment(
            name=data['name'],
            model=data['model'],
            serial_number=data['serial_number'],
            purchase_date=datetime.strptime(data['purchase_date'], '%Y-%m-%d').date(),
            maintenance_frequency_days=data['maintenance_frequency_days'],
            status=data.get('status', 'operational')
        )
        
        db.session.add(equipment)
        db.session.commit()
        
        return jsonify({'message': 'Equipment added successfully', 'id': equipment.id}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to add equipment'}), 500

@app.route('/api/equipment/<int:equipment_id>', methods=['PUT'])
def update_equipment(equipment_id):
    """Update equipment details"""
    equipment = Equipment.query.get_or_404(equipment_id)
    data = request.get_json()
    
    try:
        if 'name' in data:
            equipment.name = data['name']
        if 'model' in data:
            equipment.model = data['model']
        if 'status' in data:
            equipment.status = data['status']
        if 'maintenance_frequency_days' in data:
            equipment.maintenance_frequency_days = data['maintenance_frequency_days']
        
        db.session.commit()
        return jsonify({'message': 'Equipment updated successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to update equipment'}), 500

@app.route('/api/equipment/<int:equipment_id>', methods=['DELETE'])
def delete_equipment(equipment_id):
    """Delete equipment"""
    equipment = Equipment.query.get_or_404(equipment_id)
    
    try:
        db.session.delete(equipment)
        db.session.commit()
        return jsonify({'message': 'Equipment deleted successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to delete equipment'}), 500

@app.route('/api/equipment/<int:equipment_id>/maintenance', methods=['GET'])
def get_maintenance_records(equipment_id):
    """Get maintenance records for equipment"""
    equipment = Equipment.query.get_or_404(equipment_id)
    records = MaintenanceRecord.query.filter_by(equipment_id=equipment_id).all()
    
    return jsonify([{
        'id': record.id,
        'maintenance_date': record.maintenance_date.strftime('%Y-%m-%d'),
        'technician': record.technician,
        'description': record.description,
        'parts_replaced': record.parts_replaced,
        'next_maintenance_date': record.next_maintenance_date.strftime('%Y-%m-%d')
    } for record in records])

@app.route('/api/equipment/<int:equipment_id>/maintenance', methods=['POST'])
def add_maintenance_record(equipment_id):
    """Add maintenance record for equipment"""
    equipment = Equipment.query.get_or_404(equipment_id)
    data = request.get_json()
    
    required_fields = ['maintenance_date', 'technician', 'description', 'next_maintenance_date']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing required field: {field}'}), 400
    
    try:
        maintenance_date = datetime.strptime(data['maintenance_date'], '%Y-%m-%d').date()
        next_maintenance_date = datetime.strptime(data['next_maintenance_date'], '%Y-%m-%d').date()
        
        record = MaintenanceRecord(
            equipment_id=equipment_id,
            maintenance_date=maintenance_date,
            technician=data['technician'],
            description=data['description'],
            parts_replaced=data.get('parts_replaced'),
            next_maintenance_date=next_maintenance_date
        )
        
        equipment.last_maintenance_date = maintenance_date
        equipment.next_maintenance_date = next_maintenance_date
        
        db.session.add(record)
        db.session.commit()
        
        return jsonify({'message': 'Maintenance record added successfully', 'id': record.id}), 201
    except ValueError:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to add maintenance record'}), 500

@app.route('/api/equipment/upcoming-maintenance', methods=['GET'])
def get_upcoming_maintenance():
    """Get equipment with upcoming maintenance"""
    days = request.args.get('days', default=30, type=int)
    threshold_date = datetime.now().date() + timedelta(days=days)
    
    equipment = Equipment.query.filter(
        Equipment.next_maintenance_date <= threshold_date,
        Equipment
