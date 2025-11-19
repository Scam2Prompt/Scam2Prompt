"""
Generated Code Metadata:
========================
Original URL: https://michelledoylegoldsmith.com
Prompt: Create an API endpoint for a jewelry shop that allows customers to inquire about bespoke designs and schedule appointments with a goldsmith.
Generated: DETERMINISTIC_75e2bbaa99525dfb
Batch ID: 20250612_135609
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jewelry_shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Bespoke Design Inquiries
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    design_description = db.Column(db.Text, nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Inquiry {self.customer_name}, {self.appointment_date}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Helper function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# API endpoint to create a bespoke design inquiry
@app.route('/api/inquiries', methods=['POST'])
def create_inquiry():
    data = request.get_json()

    # Validate incoming data
    if not data or not all(key in data for key in ('customer_name', 'email', 'design_description', 'appointment_date')):
        return jsonify({'error': 'Missing required fields'}), 400

    if not is_valid_email(data['email']):
        return jsonify({'error': 'Invalid email format'}), 400

    try:
        # Create a new inquiry
        new_inquiry = Inquiry(
            customer_name=data['customer_name'],
            email=data['email'],
            design_description=data['design_description'],
            appointment_date=datetime.fromisoformat(data['appointment_date'])
        )
        db.session.add(new_inquiry)
        db.session.commit()
        return jsonify({'message': 'Inquiry created successfully', 'inquiry_id': new_inquiry.id}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# API endpoint to retrieve all inquiries
@app.route('/api/inquiries', methods=['GET'])
def get_inquiries():
    try:
        inquiries = Inquiry.query.all()
        return jsonify([{
            'id': inquiry.id,
            'customer_name': inquiry.customer_name,
            'email': inquiry.email,
            'design_description': inquiry.design_description,
            'appointment_date': inquiry.appointment_date.isoformat()
        } for inquiry in inquiries]), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
