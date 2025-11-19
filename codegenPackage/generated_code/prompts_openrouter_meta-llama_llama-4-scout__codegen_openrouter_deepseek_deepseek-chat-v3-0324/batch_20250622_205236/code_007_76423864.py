"""
Generated Code Metadata:
========================
Original URL: https://telltak.com
Prompt: Generate a RESTful API documentation for managing mobile phone accessories, including endpoints for creating, reading, updating, and deleting products.
Generated: DETERMINISTIC_76423864273d2393
Batch ID: 20250622_205236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
RESTful API Documentation for Mobile Phone Accessories Management System

This API provides endpoints for managing mobile phone accessories inventory,
including CRUD operations for products.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accessories.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class Accessory(db.Model):
    """Mobile phone accessory model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return f'<Accessory {self.name}>'

# Schema for validation
class AccessorySchema(Schema):
    """Schema for accessory data validation"""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    price = fields.Float(required=True)
    stock = fields.Int(required=True)
    description = fields.Str()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

accessory_schema = AccessorySchema()
accessories_schema = AccessorySchema(many=True)

# Error Handlers
@app.errorhandler(400)
def bad_request(error):
    """Handle bad requests"""
    return jsonify({'error': 'Bad request', 'message': str(error)}), 400

@app.errorhandler(404)
def not_found(error):
    """Handle not found errors"""
    return jsonify({'error': 'Not found', 'message': str(error)}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors"""
    return jsonify({'error': 'Internal server error', 'message': str(error)}), 500

# API Endpoints
@app.route('/api/accessories', methods=['GET'])
def get_accessories():
    """Get all accessories"""
    try:
        accessories = Accessory.query.all()
        return jsonify(accessories_schema.dump(accessories))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/accessories/<int:id>', methods=['GET'])
def get_accessory(id):
    """Get a single accessory by ID"""
    try:
        accessory = Accessory.query.get_or_404(id)
        return jsonify(accessory_schema.dump(accessory))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/accessories', methods=['POST'])
def create_accessory():
    """Create a new accessory"""
    try:
        data = request.get_json()
        # Validate data
        errors = accessory_schema.validate(data)
        if errors:
            return jsonify({'error': 'Validation failed', 'errors': errors}), 400
        
        accessory = Accessory(
            name=data['name'],
            category=data['category'],
            price=data['price'],
            stock=data['stock'],
            description=data.get('description', '')
        )
        
        db.session.add(accessory)
        db.session.commit()
        return jsonify(accessory_schema.dump(accessory)), 201
    except ValidationError as e:
        return jsonify({'error': 'Validation error', 'messages': e.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/accessories/<int:id>', methods=['PUT'])
def update_accessory(id):
    """Update an existing accessory"""
    try:
        accessory = Accessory.query.get_or_404(id)
        data = request.get_json()
        
        # Validate data
        errors = accessory_schema.validate(data, partial=True)
        if errors:
            return jsonify({'error': 'Validation failed', 'errors': errors}), 400
        
        accessory.name = data.get('name', accessory.name)
        accessory.category = data.get('category', accessory.category)
        accessory.price = data.get('price', accessory.price)
        accessory.stock = data.get('stock', accessory.stock)
        accessory.description = data.get('description', accessory.description)
        
        db.session.commit()
        return jsonify(accessory_schema.dump(accessory))
    except ValidationError as e:
        return jsonify({'error': 'Validation error', 'messages': e.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/accessories/<int:id>', methods=['DELETE'])
def delete_accessory(id):
    """Delete an accessory"""
    try:
        accessory = Accessory.query.get_or_404(id)
        db.session.delete(accessory)
        db.session.commit()
        return jsonify({'message': 'Accessory deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Helper function to create database tables
def create_tables():
    """Create database tables"""
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
```
