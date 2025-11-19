"""
Generated Code Metadata:
========================
Original URL: https://fuelinjectorservices.com.au
Prompt: Describe an API that could be used to manage customer inquiries for mobile fuel injector cleaning services, similar to those offered in Gold Coast.
Generated: DETERMINISTIC_e230ba155f41d66c
Batch ID: 20250612_155150
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
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inquiries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Customer Inquiry
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    contact_number = db.Column(db.String(15), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'contact_number': self.contact_number,
            'service_type': self.service_type,
            'message': self.message
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new inquiry
@app.route('/inquiries', methods=['POST'])
def create_inquiry():
    data = request.get_json()
    try:
        new_inquiry = Inquiry(
            customer_name=data['customer_name'],
            contact_number=data['contact_number'],
            service_type=data['service_type'],
            message=data.get('message')
        )
        db.session.add(new_inquiry)
        db.session.commit()
        return jsonify(new_inquiry.to_dict()), 201
    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error occurred'}), 500

# Endpoint to retrieve all inquiries
@app.route('/inquiries', methods=['GET'])
def get_inquiries():
    try:
        inquiries = Inquiry.query.all()
        return jsonify([inquiry.to_dict() for inquiry in inquiries]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error occurred'}), 500

# Endpoint to retrieve a specific inquiry by ID
@app.route('/inquiries/<int:id>', methods=['GET'])
def get_inquiry(id):
    try:
        inquiry = Inquiry.query.get_or_404(id)
        return jsonify(inquiry.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error occurred'}), 500

# Endpoint to update an inquiry
@app.route('/inquiries/<int:id>', methods=['PUT'])
def update_inquiry(id):
    data = request.get_json()
    try:
        inquiry = Inquiry.query.get_or_404(id)
        inquiry.customer_name = data.get('customer_name', inquiry.customer_name)
        inquiry.contact_number = data.get('contact_number', inquiry.contact_number)
        inquiry.service_type = data.get('service_type', inquiry.service_type)
        inquiry.message = data.get('message', inquiry.message)
        
        db.session.commit()
        return jsonify(inquiry.to_dict()), 200
    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error occurred'}), 500

# Endpoint to delete an inquiry
@app.route('/inquiries/<int:id>', methods=['DELETE'])
def delete_inquiry(id):
    try:
        inquiry = Inquiry.query.get_or_404(id)
        db.session.delete(inquiry)
        db.session.commit()
        return jsonify({'message': 'Inquiry deleted successfully'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
