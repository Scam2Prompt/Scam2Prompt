"""
Generated Code Metadata:
========================
Original URL: https://agnelosfx.in
Prompt: "Create a RESTful API to manage enquiries for special effects services, similar to those offered by Agnelo SFX."
Generated: DETERMINISTIC_182383e9391ebcdb
Batch ID: 20250622_210650
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

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///enquiries.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define Enquiry model
class Enquiry(db.Model):
    __tablename__ = 'enquiries'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    event_date = db.Column(db.Date)
    event_type = db.Column(db.String(100))
    description = db.Column(db.Text)
    budget = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pending')

    def __repr__(self):
        return f'<Enquiry {self.id}>'

# Define Marshmallow schema for validation
class EnquirySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    phone = fields.Str()
    event_date = fields.Date()
    event_type = fields.Str()
    description = fields.Str()
    budget = fields.Str()
    created_at = fields.DateTime(dump_only=True)
    status = fields.Str(dump_only=True)

# Create database tables
with app.app_context():
    db.create_all()

# Initialize schema
enquiry_schema = EnquirySchema()
enquiries_schema = EnquirySchema(many=True)

# Error handlers
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Routes
@app.route('/api/enquiries', methods=['POST'])
def create_enquiry():
    """Create a new enquiry"""
    try:
        data = request.get_json()
        # Validate data
        errors = enquiry_schema.validate(data)
        if errors:
            return jsonify({'errors': errors}), 400
        
        # Create enquiry
        enquiry = Enquiry(
            name=data['name'],
            email=data['email'],
            phone=data.get('phone'),
            event_date=datetime.strptime(data.get('event_date'), '%Y-%m-%d').date() if data.get('event_date') else None,
            event_type=data.get('event_type'),
            description=data.get('description'),
            budget=data.get('budget')
        )
        
        db.session.add(enquiry)
        db.session.commit()
        
        return enquiry_schema.jsonify(enquiry), 201
    
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/enquiries', methods=['GET'])
def get_enquiries():
    """Get all enquiries"""
    try:
        enquiries = Enquiry.query.all()
        return enquiries_schema.jsonify(enquiries)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/enquiries/<int:id>', methods=['GET'])
def get_enquiry(id):
    """Get a specific enquiry by ID"""
    try:
        enquiry = Enquiry.query.get_or_404(id)
        return enquiry_schema.jsonify(enquiry)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/enquiries/<int:id>', methods=['PUT'])
def update_enquiry(id):
    """Update an existing enquiry"""
    try:
        enquiry = Enquiry.query.get_or_404(id)
        data = request.get_json()
        
        # Validate data
        errors = enquiry_schema.validate(data, partial=True)
        if errors:
            return jsonify({'errors': errors}), 400
        
        # Update fields
        if 'name' in data:
            enquiry.name = data['name']
        if 'email' in data:
            enquiry.email = data['email']
        if 'phone' in data:
            enquiry.phone = data['phone']
        if 'event_date' in data:
            enquiry.event_date = datetime.strptime(data['event_date'], '%Y-%m-%d').date()
        if 'event_type' in data:
            enquiry.event_type = data['event_type']
        if 'description' in data:
            enquiry.description = data['description']
        if 'budget' in data:
            enquiry.budget = data['budget']
        if 'status' in data:
            enquiry.status = data['status']
        
        db.session.commit()
        return enquiry_schema.jsonify(enquiry)
    
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/enquiries/<int:id>', methods=['DELETE'])
def delete_enquiry(id):
    """Delete an enquiry"""
    try:
        enquiry = Enquiry.query.get_or_404(id)
        db.session.delete(enquiry)
        db.session.commit()
        return jsonify({'message': 'Enquiry deleted successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
