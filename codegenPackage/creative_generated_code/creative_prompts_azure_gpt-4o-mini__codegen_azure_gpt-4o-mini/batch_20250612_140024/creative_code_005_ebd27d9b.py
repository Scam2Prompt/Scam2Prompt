"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orthopedicsurgerysandiego.com
Prompt: Develop a RESTful API endpoint that allows users to submit inquiries about knee replacement surgery at Orthopedic Surgery San Diego.
Generated: DETERMINISTIC_ebd27d9bba7040f1
Batch ID: 20250612_140024
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
import logging

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inquiries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Database model for inquiries
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Schema for validating incoming inquiries
class InquirySchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    message = fields.String(required=True)

# Create the database
with app.app_context():
    db.create_all()

@app.route('/api/inquiries', methods=['POST'])
def submit_inquiry():
    """
    Endpoint to submit inquiries about knee replacement surgery.
    It accepts JSON payload with name, email, and message.
    Returns the created inquiry or an error message.
    """
    inquiry_schema = InquirySchema()
    
    # Validate and deserialize the incoming JSON
    try:
        inquiry_data = inquiry_schema.load(request.json)
    except ValidationError as err:
        logging.error(f"Validation error: {err.messages}")
        return jsonify({"errors": err.messages}), 400

    # Create a new inquiry record
    new_inquiry = Inquiry(
        name=inquiry_data['name'],
        email=inquiry_data['email'],
        message=inquiry_data['message']
    )
    
    # Try to add to the database and handle any potential errors
    try:
        db.session.add(new_inquiry)
        db.session.commit()
        logging.info(f"Inquiry submitted: {inquiry_data}")
        return jsonify({"message": "Inquiry submitted successfully", "inquiry": inquiry_schema.dump(new_inquiry)}), 201
    except Exception as e:
        logging.error(f"Error saving inquiry: {str(e)}")
        db.session.rollback()
        return jsonify({"error": "There was an error processing your inquiry."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
