"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ticomsoftware.com
Prompt: Recommend software development practices for creating a scalable and secure electronic invoicing system, inspired by TICOM Software's emphasis on reliability and scalability.
Generated: DETERMINISTIC_5a8e444ea259f7fe
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.exceptions import BadRequest, NotFound

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///invoices.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Invoice model
class Invoice(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    customer_name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='Pending')  # Example statuses: 'Pending', 'Paid', 'Cancelled'

    def to_dict(self):
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'amount': self.amount,
            'status': self.status
        }

# Error handler for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({'error': 'Bad Request', 'message': str(error)}), 400

# Error handler for not found
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({'error': 'Not Found', 'message': str(error)}), 404

# Function to create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new invoice
@app.route('/invoices', methods=['POST'])
def create_invoice():
    try:
        data = request.get_json()
        if not data or 'customer_name' not in data or 'amount' not in data:
            raise BadRequest("Missing 'customer_name' or 'amount' in request data")

        new_invoice = Invoice(customer_name=data['customer_name'], amount=data['amount'])
        db.session.add(new_invoice)
        db.session.commit()
        return jsonify(new_invoice.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error', 'message': str(e)}), 500

# Endpoint to fetch all invoices
@app.route('/invoices', methods=['GET'])
def get_invoices():
    invoices = Invoice.query.all()
    return jsonify([invoice.to_dict() for invoice in invoices]), 200

# Endpoint to fetch a specific invoice by ID
@app.route('/invoices/<string:invoice_id>', methods=['GET'])
def get_invoice(invoice_id):
    invoice = Invoice.query.get(invoice_id)
    if not invoice:
        raise NotFound(f'Invoice with ID {invoice_id} not found')
    return jsonify(invoice.to_dict()), 200

# Endpoint to update an invoice status
@app.route('/invoices/<string:invoice_id>', methods=['PATCH'])
def update_invoice(invoice_id):
    invoice = Invoice.query.get(invoice_id)
    if not invoice:
        raise NotFound(f'Invoice with ID {invoice_id} not found')

    data = request.get_json()
    if 'status' in data:
        invoice.status = data['status']

    try:
        db.session.commit()
        return jsonify(invoice.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error', 'message': str(e)}), 500

# Endpoint to delete an invoice
@app.route('/invoices/<string:invoice_id>', methods=['DELETE'])
def delete_invoice(invoice_id):
    invoice = Invoice.query.get(invoice_id)
    if not invoice:
        raise NotFound(f'Invoice with ID {invoice_id} not found')

    try:
        db.session.delete(invoice)
        db.session.commit()
        return jsonify({'message': 'Invoice deleted successfully'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error', 'message': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
