"""
Generated Code Metadata:
========================
Original URL: https://redhorsereflex.com
Prompt: Design a RESTful API using Flask or Django to manage appointment bookings for Red Horse Reflexology, including endpoints for creating, reading, updating, and deleting appointments.
Generated: DETERMINISTIC_dde25bbc50cf4f41
Batch ID: 20250622_210650
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
from datetime import datetime
import os

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///appointments.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Appointment Model
class Appointment(db.Model):
    __tablename__ = 'appointments'
    
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    client_phone = db.Column(db.String(20), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)
    service_type = db.Column(db.String(100), nullable=False)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Appointment {self.id}>'

    def serialize(self):
        return {
            'id': self.id,
            'client_name': self.client_name,
            'client_phone': self.client_phone,
            'appointment_date': self.appointment_date.isoformat(),
            'service_type': self.service_type,
            'notes': self.notes,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

# Create database tables
with app.app_context():
    db.create_all()

# Error Handlers
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad Request', 'message': str(error)}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found', 'message': str(error)}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal Server Error', 'message': str(error)}), 500

# API Endpoints
@app.route('/api/appointments', methods=['GET'])
def get_appointments():
    """Get all appointments"""
    try:
        appointments = Appointment.query.order_by(Appointment.appointment_date.asc()).all()
        return jsonify([appointment.serialize() for appointment in appointments])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/appointments/<int:id>', methods=['GET'])
def get_appointment(id):
    """Get a specific appointment by ID"""
    try:
        appointment = Appointment.query.get_or_404(id)
        return jsonify(appointment.serialize())
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@app.route('/api/appointments', methods=['POST'])
def create_appointment():
    """Create a new appointment"""
    try:
        data = request.get_json()
        
        # Validate required fields
        if not all(key in data for key in ['client_name', 'client_phone', 'appointment_date', 'service_type']):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Parse date string to datetime object
        appointment_date = datetime.fromisoformat(data['appointment_date'])
        
        appointment = Appointment(
            client_name=data['client_name'],
            client_phone=data['client_phone'],
            appointment_date=appointment_date,
            service_type=data['service_type'],
            notes=data.get('notes', '')
        )
        
        db.session.add(appointment)
        db.session.commit()
        
        return jsonify(appointment.serialize()), 201
    except ValueError as e:
        return jsonify({'error': 'Invalid date format. Use ISO format (YYYY-MM-DDTHH:MM:SS)'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/appointments/<int:id>', methods=['PUT'])
def update_appointment(id):
    """Update an existing appointment"""
    try:
        appointment = Appointment.query.get_or_404(id)
        data = request.get_json()
        
        if 'client_name' in data:
            appointment.client_name = data['client_name']
        if 'client_phone' in data:
            appointment.client_phone = data['client_phone']
        if 'appointment_date' in data:
            appointment.appointment_date = datetime.fromisoformat(data['appointment_date'])
        if 'service_type' in data:
            appointment.service_type = data['service_type']
        if 'notes' in data:
            appointment.notes = data['notes']
        
        db.session.commit()
        return jsonify(appointment.serialize())
    except ValueError as e:
        return jsonify({'error': 'Invalid date format. Use ISO format (YYYY-MM-DDTHH:MM:SS)'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/appointments/<int:id>', methods=['DELETE'])
def delete_appointment(id):
    """Delete an appointment"""
    try:
        appointment = Appointment.query.get_or_404(id)
        db.session.delete(appointment)
        db.session.commit()
        return jsonify({'message': 'Appointment deleted successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```python
# requirements.txt
Flask==2.3.2
Flask-SQLAlchemy==3.0.3
python-dotenv==1.0.0
```

```python
# .env.example
DATABASE_URL=sqlite:///appointments.db
```
