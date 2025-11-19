"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presval.co
Prompt: Outline a RESTful API design for a real estate platform that includes endpoints for property listings, user inquiries, and transaction management, reflecting the comprehensive services provided by Presval.
Generated: DETERMINISTIC_40f635253f5b76b6
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///realestate.db'
db = SQLAlchemy(app)

# Database model for Property Listings
class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    price = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(255), nullable=False)

# Database model for User Inquiries
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'), nullable=False)
    user_email = db.Column(db.String(255), nullable=False)
    message = db.Column(db.String(1000), nullable=False)

# Schema for Property validation
class PropertySchema(Schema):
    title = fields.String(required=True)
    description = fields.String(required=True)
    price = fields.Float(required=True)
    location = fields.String(required=True)

# Schema for Inquiry validation
class InquirySchema(Schema):
    property_id = fields.Integer(required=True)
    user_email = fields.String(required=True)
    message = fields.String(required=True)

# Initialize schemas
property_schema = PropertySchema()
properties_schema = PropertySchema(many=True)
inquiry_schema = InquirySchema()
inquiries_schema = InquirySchema(many=True)

# Create property listing
@app.route('/properties', methods=['POST'])
def add_property():
    """Create a new property listing."""
    try:
        data = request.get_json()
        validated_data = property_schema.load(data)
        new_property = Property(**validated_data)
        db.session.add(new_property)
        db.session.commit()
        return property_schema.jsonify(new_property), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Retrieve all properties
@app.route('/properties', methods=['GET'])
def get_properties():
    """Retrieve all property listings."""
    properties = Property.query.all()
    return properties_schema.jsonify(properties), 200

# Create user inquiry
@app.route('/inquiries', methods=['POST'])
def add_inquiry():
    """Create a new user inquiry."""
    try:
        data = request.get_json()
        validated_data = inquiry_schema.load(data)
        new_inquiry = Inquiry(**validated_data)
        db.session.add(new_inquiry)
        db.session.commit()
        return inquiry_schema.jsonify(new_inquiry), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Retrieve all inquiries for a specific property
@app.route('/properties/<int:property_id>/inquiries', methods=['GET'])
def get_inquiries(property_id):
    """Retrieve all inquiries for a specific property."""
    inquiries = Inquiry.query.filter_by(property_id=property_id).all()
    return inquiries_schema.jsonify(inquiries), 200

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug to False in production
```
