"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maestrofinance.co.uk
Prompt: Illustrate how to implement an invoice finance solution in a web application that unlocks immediate cash from unpaid invoices for small businesses.
Generated: DETERMINISTIC_2053354a94bd0548
Batch ID: 20250612_160158
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
import logging

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///invoices.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Invoice model
class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), default='unpaid')  # Status can be 'unpaid' or 'paid'

    def __repr__(self):
        return f'<Invoice {self.id}, Amount: {self.amount}, Due: {self.due_date}, Status: {self.status}>'

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to create a new invoice
@app.route('/invoices', methods=['POST'])
def create_invoice():
    """Create a new invoice."""
    data = request.get_json()
    
    # Validate input data
    if not data or 'amount' not in data or 'due_date' not in data:
        logging.error("Invalid data provided for creating invoice.")
        return jsonify({'error': 'Invalid data'}), 400

    try:
        amount = float(data['amount'])
        due_date = datetime.strptime(data['due_date'], '%Y-%m-%d')
    except (ValueError, TypeError):
        logging.error("Invalid amount or due date format.")
        return jsonify({'error': 'Invalid amount or due date format'}), 400

    # Create a new invoice
    new_invoice = Invoice(amount=amount, due_date=due_date)
    db.session.add(new_invoice)
    db.session.commit()

    return jsonify({'message': 'Invoice created', 'id': new_invoice.id}), 201

# API endpoint to unlock cash from unpaid invoices
@app.route('/unlock_cash', methods=['POST'])
def unlock_cash():
    """Unlock cash from unpaid invoices."""
    data = request.get_json()
    
    if not data or 'invoice_id' not in data:
        logging.error("Invalid data provided to unlock cash.")
        return jsonify({'error': 'Invalid data'}), 400

    invoice_id = data['invoice_id']
    
    # Fetch the invoice from the database
    invoice = Invoice.query.get(invoice_id)
    
    if not invoice or invoice.status != 'unpaid':
        logging.error(f"No unpaid invoice found with ID {invoice_id}.")
        return jsonify({'error': 'No unpaid invoice found or already paid'}), 404

    # Simulate unlocking cash
    invoice.status = 'paid'
    db.session.commit()

    logging.info(f"Cash unlocked for invoice ID {invoice_id}.")
    return jsonify({'message': 'Cash unlocked successfully', 'invoice_id': invoice.id}), 200

# Error handling for unexpected exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle unexpected exceptions."""
    logging.error(f"Unexpected error: {str(e)}")
    return jsonify({'error': 'Internal Server Error'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
