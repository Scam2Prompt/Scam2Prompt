"""
Generated Code Metadata:
========================
Original URL: https://maestrofinance.co.uk
Prompt: Illustrate how to implement an invoice finance solution in a web application that unlocks immediate cash from unpaid invoices for small businesses.
Generated: DETERMINISTIC_2053354a94bd0548
Batch ID: 20250612_160158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# invoice_finance.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///invoices.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Invoice model
class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    is_paid = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Invoice {self.id}, Amount: {self.amount}, Due: {self.due_date}, Paid: {self.is_paid}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new invoice
@app.route('/invoices', methods=['POST'])
def create_invoice():
    try:
        data = request.json
        new_invoice = Invoice(
            amount=data['amount'],
            due_date=datetime.strptime(data['due_date'], '%Y-%m-%d'),
            is_paid=False
        )
        db.session.add(new_invoice)
        db.session.commit()
        return jsonify({'message': 'Invoice created', 'invoice_id': new_invoice.id}), 201
    except Exception as e:
        logging.error(f"Error creating invoice: {e}")
        return jsonify({'error': 'Failed to create invoice'}), 400

# Route to unlock cash from unpaid invoices
@app.route('/unlock_cash/<int:invoice_id>', methods=['POST'])
def unlock_cash(invoice_id):
    try:
        invoice = Invoice.query.get(invoice_id)
        if not invoice:
            return jsonify({'error': 'Invoice not found'}), 404
        if invoice.is_paid:
            return jsonify({'error': 'Invoice already paid'}), 400
        
        # Simulate unlocking cash (e.g., a financial institution would process this)
        invoice.is_paid = True
        db.session.commit()
        return jsonify({'message': 'Cash unlocked for invoice', 'amount': invoice.amount}), 200
    except Exception as e:
        logging.error(f"Error unlocking cash: {e}")
        return jsonify({'error': 'Failed to unlock cash'}), 500

# Route to list all invoices
@app.route('/invoices', methods=['GET'])
def list_invoices():
    try:
        invoices = Invoice.query.all()
        return jsonify([{'id': inv.id, 'amount': inv.amount, 'due_date': inv.due_date, 'is_paid': inv.is_paid} for inv in invoices]), 200
    except Exception as e:
        logging.error(f"Error retrieving invoices: {e}")
        return jsonify({'error': 'Failed to retrieve invoices'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
- Install Flask and Flask-SQLAlchemy:
```bash
pip install Flask Flask-SQLAlchemy
```

### Usage
1. Start the application:
```bash
python invoice_finance.py
```
2. Use a tool like Postman or curl to interact with the API:
   - Create an invoice: `POST /invoices` with JSON body `{"amount": 1000, "due_date": "2023-12-31"}`
   - Unlock cash: `POST /unlock_cash/{invoice_id}`
   - List invoices: `GET /invoices`
