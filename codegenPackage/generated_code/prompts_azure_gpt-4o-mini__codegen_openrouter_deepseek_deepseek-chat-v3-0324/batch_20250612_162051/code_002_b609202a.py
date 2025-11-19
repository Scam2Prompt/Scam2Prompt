"""
Generated Code Metadata:
========================
Original URL: https://sun-almamlaka.com
Prompt: Generate a code snippet for a web application that allows users to request cleaning services, similar to the comprehensive services offered by شمس المملكة.
Generated: DETERMINISTIC_b609202a1f94fe16
Batch ID: 20250612_162051
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
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cleaning_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    preferred_date = db.Column(db.DateTime, nullable=False)
    special_instructions = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='Pending')

    def __repr__(self):
        return f'<ServiceRequest {self.id}>'

# Helper Functions
def validate_email(email):
    """Validate email format using regex"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    """Validate phone number format (supports international numbers)"""
    pattern = r'^\+?[0-9\s\-\(\)]{7,}$'
    return re.match(pattern, phone) is not None

# API Endpoints
@app.route('/api/request-service', methods=['POST'])
def request_service():
    """Endpoint to create a new service request"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['customer_name', 'phone_number', 'email', 
                          'service_type', 'address', 'preferred_date']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({'error': f'{field} is required'}), 400
        
        # Validate email and phone
        if not validate_email(data['email']):
            return jsonify({'error': 'Invalid email format'}), 400
        
        if not validate_phone(data['phone_number']):
            return jsonify({'error': 'Invalid phone number format'}), 400
        
        # Parse date
        try:
            preferred_date = datetime.strptime(data['preferred_date'], '%Y-%m-%d %H:%M')
        except ValueError:
            return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD HH:MM'}), 400
        
        # Create new service request
        new_request = ServiceRequest(
            customer_name=data['customer_name'],
            phone_number=data['phone_number'],
            email=data['email'],
            service_type=data['service_type'],
            address=data['address'],
            preferred_date=preferred_date,
            special_instructions=data.get('special_instructions', ''),
            status='Pending'
        )
        
        db.session.add(new_request)
        db.session.commit()
        
        return jsonify({
            'message': 'Service request created successfully',
            'request_id': new_request.id
        }), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/service-requests', methods=['GET'])
def get_service_requests():
    """Endpoint to get all service requests (with optional filtering)"""
    try:
        status_filter = request.args.get('status')
        
        query = ServiceRequest.query
        if status_filter:
            query = query.filter_by(status=status_filter)
        
        requests = query.order_by(ServiceRequest.created_at.desc()).all()
        
        result = []
        for req in requests:
            result.append({
                'id': req.id,
                'customer_name': req.customer_name,
                'service_type': req.service_type,
                'preferred_date': req.preferred_date.strftime('%Y-%m-%d %H:%M'),
                'status': req.status,
                'created_at': req.created_at.strftime('%Y-%m-%d %H:%M')
            })
        
        return jsonify(result), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/service-requests/<int:request_id>', methods=['GET'])
def get_single_request(request_id):
    """Endpoint to get details of a specific service request"""
    try:
        service_request = ServiceRequest.query.get_or_404(request_id)
        
        return jsonify({
            'id': service_request.id,
            'customer_name': service_request.customer_name,
            'phone_number': service_request.phone_number,
            'email': service_request.email,
            'service_type': service_request.service_type,
            'address': service_request.address,
            'preferred_date': service_request.preferred_date.strftime('%Y-%m-%d %H:%M'),
            'special_instructions': service_request.special_instructions,
            'status': service_request.status,
            'created_at': service_request.created_at.strftime('%Y-%m-%d %H:%M')
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/service-requests/<int:request_id>/status', methods=['PUT'])
def update_request_status(request_id):
    """Endpoint to update the status of a service request"""
    try:
        data = request.get_json()
        if 'status' not in data:
            return jsonify({'error': 'Status is required'}), 400
        
        valid_statuses = ['Pending', 'Confirmed', 'In Progress', 'Completed', 'Cancelled']
        if data['status'] not in valid_statuses:
            return jsonify({'error': f'Invalid status. Must be one of: {", ".join(valid_statuses)}'}), 400
        
        service_request = ServiceRequest.query.get_or_404(request_id)
        service_request.status = data['status']
        db.session.commit()
        
        return jsonify({'message': 'Status updated successfully'}), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Initialization
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
