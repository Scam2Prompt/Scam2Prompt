"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuelinjectorservices.com.au
Prompt: Describe an API that could be used to manage customer inquiries for mobile fuel injector cleaning services, similar to those offered in Gold Coast.
Generated: DETERMINISTIC_e230ba155f41d66c
Batch ID: 20250612_155150
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
from datetime import datetime
from marshmallow import Schema, fields, validate, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inquiries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Customer Inquiry
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_email = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    inquiry_date = db.Column(db.DateTime, default=datetime.utcnow)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Inquiry {self.customer_name}>'

# Schema for data validation
class InquirySchema(Schema):
    customer_name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    customer_email = fields.Email(required=True)
    phone_number = fields.Str(required=True, validate=validate.Length(min=10, max=15))
    message = fields.Str(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new inquiry
@app.route('/inquiries', methods=['POST'])
def create_inquiry():
    try:
        # Validate and deserialize input
        inquiry_data = InquirySchema().load(request.json)
        new_inquiry = Inquiry(**inquiry_data)
        db.session.add(new_inquiry)
        db.session.commit()
        return jsonify({"message": "Inquiry submitted successfully."}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Route to retrieve all inquiries
@app.route('/inquiries', methods=['GET'])
def get_inquiries():
    try:
        inquiries = Inquiry.query.all()
        inquiries_schema = InquirySchema(many=True)
        return jsonify(inquiries_schema.dump(inquiries)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete an inquiry by ID
@app.route('/inquiries/<int:id>', methods=['DELETE'])
def delete_inquiry(id):
    try:
        inquiry = Inquiry.query.get_or_404(id)
        db.session.delete(inquiry)
        db.session.commit()
        return jsonify({"message": "Inquiry deleted successfully."}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
