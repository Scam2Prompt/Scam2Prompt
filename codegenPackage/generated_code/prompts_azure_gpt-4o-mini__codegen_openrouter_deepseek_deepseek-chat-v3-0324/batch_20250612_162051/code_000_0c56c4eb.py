"""
Generated Code Metadata:
========================
Original URL: https://bepretty.hamburg
Prompt: Generate a code snippet for a web application that allows users to book professional hair and makeup services, similar to the offerings at bePretty Hamburg.
Generated: DETERMINISTIC_0c56c4eb513cb600
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from werkzeug.utils import secure_filename

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///beauty_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Initialize database
db = SQLAlchemy(app)

# Define database models
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # in minutes
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)  # hair, makeup, etc.
    image_path = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_email = db.Column(db.String(100), nullable=False)
    customer_phone = db.Column(db.String(20), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pending')  # pending, confirmed, cancelled, completed

    service = db.relationship('Service', backref='bookings')

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# API Endpoints
@app.route('/')
def home():
    """Render the home page with available services."""
    services = Service.query.all()
    return render_template('index.html', services=services)

@app.route('/services', methods=['GET'])
def get_services():
    """Get all available services."""
    try:
        services = Service.query.all()
        return jsonify([{
            'id': service.id,
            'name': service.name,
            'description': service.description,
            'duration': service.duration,
            'price': service.price,
            'category': service.category,
            'image_path': service.image_path
        } for service in services]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """Get details of a specific service."""
    try:
        service = Service.query.get_or_404(service_id)
        return jsonify({
            'id': service.id,
            'name': service.name,
            'description': service.description,
            'duration': service.duration,
            'price': service.price,
            'category': service.category,
            'image_path': service.image_path
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/bookings', methods=['POST'])
def create_booking():
    """Create a new booking."""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['service_id', 'customer_name', 'customer_email', 'customer_phone', 'booking_date']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Check if service exists
        service = Service.query.get(data['service_id'])
        if not service:
            return jsonify({'error': 'Service not found'}), 404
        
        # Create booking
        booking = Booking(
            service_id=data['service_id'],
            customer_name=data['customer_name'],
            customer_email=data['customer_email'],
            customer_phone=data['customer_phone'],
            booking_date=datetime.strptime(data['booking_date'], '%Y-%m-%d %H:%M'),
            notes=data.get('notes', ''),
            status='pending'
        )
        
        db.session.add(booking)
        db.session.commit()
        
        return jsonify({
            'id': booking.id,
            'message': 'Booking created successfully',
            'status': booking.status
        }), 201
    except ValueError as e:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD HH:MM'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/bookings/<int:booking_id>', methods=['GET'])
def get_booking(booking_id):
    """Get details of a specific booking."""
    try:
        booking = Booking.query.get_or_404(booking_id)
        return jsonify({
            'id': booking.id,
            'service_id': booking.service_id,
            'service_name': booking.service.name,
            'customer_name': booking.customer_name,
            'customer_email': booking.customer_email,
            'customer_phone': booking.customer_phone,
            'booking_date': booking.booking_date.isoformat(),
            'notes': booking.notes,
            'status': booking.status,
            'created_at': booking.created_at.isoformat()
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/services', methods=['POST'])
def create_service():
    """Create a new service (admin only)."""
    try:
        # In production, you would add authentication/authorization here
        
        # Handle file upload
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400
            
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
            
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
        else:
            return jsonify({'error': 'File type not allowed'}), 400
        
        # Get other form data
        data = request.form
        required_fields = ['name', 'description', 'duration', 'price', 'category']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Create service
        service = Service(
            name=data['name'],
            description=data['description'],
            duration=int(data['duration']),
            price=float(data['price']),
            category=data['category'],
            image_path=filepath
        )
        
        db.session.add(service)
        db.session.commit()
        
        return jsonify({
            'id': service.id,
            'message': 'Service created successfully',
            'image_path': service.image_path
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
```
