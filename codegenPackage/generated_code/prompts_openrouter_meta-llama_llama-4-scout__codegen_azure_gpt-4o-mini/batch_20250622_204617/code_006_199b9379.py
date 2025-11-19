"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-cqjggprvn-offchain-labs.vercel.app
Prompt: Develop a support ticketing system API for a decentralized platform like Arbitrum, ensuring compatibility with various wallet connections, including WalletConnect.
Generated: DETERMINISTIC_199b9379bd4164d1
Batch ID: 20250622_204617
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
from web3 import Web3
import os

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///tickets.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Ticket model
class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_address = db.Column(db.String(42), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='open')

    def to_dict(self):
        return {
            'id': self.id,
            'user_address': self.user_address,
            'subject': self.subject,
            'description': self.description,
            'status': self.status
        }

# Initialize the database
with app.app_context():
    db.create_all()

# Middleware to check wallet connection
def check_wallet_connection():
    wallet_address = request.headers.get('Wallet-Address')
    if not wallet_address or not Web3.isChecksumAddress(wallet_address):
        return jsonify({'error': 'Invalid wallet address'}), 400
    return wallet_address

# Create a new support ticket
@app.route('/tickets', methods=['POST'])
def create_ticket():
    wallet_address = check_wallet_connection()
    if isinstance(wallet_address, tuple):  # Check if error response
        return wallet_address

    data = request.json
    subject = data.get('subject')
    description = data.get('description')

    if not subject or not description:
        return jsonify({'error': 'Subject and description are required'}), 400

    new_ticket = Ticket(user_address=wallet_address, subject=subject, description=description)
    db.session.add(new_ticket)
    db.session.commit()

    return jsonify(new_ticket.to_dict()), 201

# Get all support tickets
@app.route('/tickets', methods=['GET'])
def get_tickets():
    tickets = Ticket.query.all()
    return jsonify([ticket.to_dict() for ticket in tickets]), 200

# Get a specific support ticket by ID
@app.route('/tickets/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    if not ticket:
        return jsonify({'error': 'Ticket not found'}), 404
    return jsonify(ticket.to_dict()), 200

# Update a support ticket status
@app.route('/tickets/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    if not ticket:
        return jsonify({'error': 'Ticket not found'}), 404

    data = request.json
    status = data.get('status')

    if status not in ['open', 'closed']:
        return jsonify({'error': 'Invalid status'}), 400

    ticket.status = status
    db.session.commit()

    return jsonify(ticket.to_dict()), 200

# Delete a support ticket
@app.route('/tickets/<int:ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    if not ticket:
        return jsonify({'error': 'Ticket not found'}), 404

    db.session.delete(ticket)
    db.session.commit()

    return jsonify({'message': 'Ticket deleted successfully'}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
