"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reddecomercio.com
Prompt: Develop a REST API endpoint that handles client inquiries about import/export regulations, inspired by the customer support approach of Red de Comercio.
Generated: DETERMINISTIC_1266b4e324ff3f0a
Batch ID: 20250612_160010
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inquiries.db'  # Change to your DB URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Inquiry model to store client inquiries
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    question = db.Column(db.Text, nullable=False)

# Schema for validating incoming data
class InquirySchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    question = fields.String(required=True)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/api/inquiries', methods=['POST'])
def create_inquiry():
    """Endpoint to create a new client inquiry."""
    try:
        # Validate and deserialize input data
        inquiry_schema = InquirySchema()
        inquiry_data = inquiry_schema.load(request.json)

        # Create new Inquiry record
        new_inquiry = Inquiry(
            name=inquiry_data['name'],
            email=inquiry_data['email'],
            question=inquiry_data['question']
        )
        db.session.add(new_inquiry)
        db.session.commit()

        # Respond with the created inquiry
        return jsonify(inquiry_schema.dump(new_inquiry)), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

@app.route('/api/inquiries/<int:inquiry_id>', methods=['GET'])
def get_inquiry(inquiry_id):
    """Endpoint to retrieve a specific inquiry by ID."""
    inquiry = Inquiry.query.get_or_404(inquiry_id)
    inquiry_schema = InquirySchema()
    return jsonify(inquiry_schema.dump(inquiry)), 200

@app.route('/api/inquiries', methods=['GET'])
def get_inquiries():
    """Endpoint to retrieve all inquiries."""
    inquiries = Inquiry.query.all()
    inquiry_schema = InquirySchema(many=True)
    return jsonify(inquiry_schema.dump(inquiries)), 200

if __name__ == '__main__':
    app.run(debug=True)  # Change to False in production
```
