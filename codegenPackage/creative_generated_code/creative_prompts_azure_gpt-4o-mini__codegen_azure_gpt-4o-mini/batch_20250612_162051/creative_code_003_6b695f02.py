"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sunnyhurghada.com
Prompt: Develop a RESTful API endpoint that allows users to submit inquiries for real estate services, specifically targeting properties in the Red Sea region, similar to the inquiry form on Sunny Hurghada's site.
Generated: DETERMINISTIC_6b695f02ed79fa1b
Batch ID: 20250612_162051
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

# Initialize Flask app
app = Flask(__name__)

# Set up database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///inquiries.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define Inquiry model
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=True)
    message = db.Column(db.Text, nullable=True)

# Schema for validating inquiries
class InquirySchema(Schema):
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    phone = fields.Str(required=False)
    message = fields.Str(required=True)

# Create database tables
with app.app_context():
    db.create_all()

# Endpoint to submit inquiries
@app.route('/api/inquiries', methods=['POST'])
def submit_inquiry():
    # Parse request JSON
    json_data = request.get_json()

    # Validate input data using schema
    try:
        inquiry_data = InquirySchema().load(json_data)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    # Create a new Inquiry object
    new_inquiry = Inquiry(
        name=inquiry_data['name'],
        email=inquiry_data['email'],
        phone=inquiry_data.get('phone'),
        message=inquiry_data['message']
    )

    # Save the inquiry to the database
    try:
        db.session.add(new_inquiry)
        db.session.commit()
        return jsonify({"message": "Inquiry submitted successfully!", "id": new_inquiry.id}), 201
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
