"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trackdieselperu.com
Prompt: Create a RESTful API in Flask to handle customer inquiries for machinery parts and technical assistance, referencing the brands and services offered by Track Diesel Peru.
Generated: DETERMINISTIC_d61c0f7cffc9c240
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the CustomerInquiry model
class CustomerInquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'<Inquiry {self.id}: {self.name}>'

# Schema for customer inquiries
class CustomerInquirySchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    message = fields.Str(required=True)
    brand = fields.Str(required=True)

# Initialize the schema
inquiry_schema = CustomerInquirySchema()

# Route for creating a new customer inquiry
@app.route('/inquiries', methods=['POST'])
def create_inquiry():
    try:
        # Validate and deserialize input data
        data = request.get_json()
        inquiry_data = inquiry_schema.load(data)
        
        # Create a new customer inquiry
        new_inquiry = CustomerInquiry(**inquiry_data)
        db.session.add(new_inquiry)
        db.session.commit()
        
        return jsonify({"message": "Inquiry created successfully", "id": new_inquiry.id}), 201
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for retrieving all customer inquiries
@app.route('/inquiries', methods=['GET'])
def get_inquiries():
    try:
        inquiries = CustomerInquiry.query.all()
        inquiries_schema = CustomerInquirySchema(many=True)
        return jsonify(inquiries_schema.dump(inquiries)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for retrieving a specific inquiry by ID
@app.route('/inquiries/<int:id>', methods=['GET'])
def get_inquiry(id):
    try:
        inquiry = CustomerInquiry.query.get_or_404(id)
        return jsonify(inquiry_schema.dump(inquiry)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for updating a specific inquiry by ID
@app.route('/inquiries/<int:id>', methods=['PUT'])
def update_inquiry(id):
    try:
        inquiry = CustomerInquiry.query.get_or_404(id)
        data = request.get_json()
        inquiry_schema.load(data, partial=True)
        
        for key, value in data.items():
            setattr(inquiry, key, value)
        
        db.session.commit()
        return jsonify({"message": "Inquiry updated successfully"}), 200
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for deleting a specific inquiry by ID
@app.route('/inquiries/<int:id>', methods=['DELETE'])
def delete_inquiry(id):
    try:
        inquiry = CustomerInquiry.query.get_or_404(id)
        db.session.delete(inquiry)
        db.session.commit()
        return jsonify({"message": "Inquiry deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app in debug mode on the specified port
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
```
