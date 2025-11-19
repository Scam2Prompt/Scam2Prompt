"""
Generated Code Metadata:
========================
Original URL: https://swiftnetprotocol.web.app
Prompt: Create a support ticket system with categories for issues like login, trading wallet, whitelist, and NFT minting/transfer problems, inspired by the Upside support page.
Generated: DETERMINISTIC_7967e8a94a68530f
Batch ID: 20250622_211941
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
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///support_tickets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Ticket model
class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Ticket {self.id} - {self.category}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Define the categories for support tickets
CATEGORIES = ['login', 'trading wallet', 'whitelist', 'NFT minting/transfer']

@app.route('/tickets', methods=['POST'])
def create_ticket():
    """
    Create a new support ticket.
    Expects JSON with 'category' and 'description'.
    """
    try:
        data = request.get_json()
        category = data.get('category')
        description = data.get('description')

        # Validate input
        if not category or category not in CATEGORIES:
            return jsonify({'error': 'Invalid category. Choose from: ' + ', '.join(CATEGORIES)}), 400
        if not description:
            return jsonify({'error': 'Description is required.'}), 400

        # Create a new ticket
        new_ticket = Ticket(category=category, description=description)
        db.session.add(new_ticket)
        db.session.commit()

        logging.info(f'Ticket created: {new_ticket}')
        return jsonify({'message': 'Ticket created successfully!', 'ticket_id': new_ticket.id}), 201

    except Exception as e:
        logging.error(f'Error creating ticket: {e}')
        return jsonify({'error': 'An error occurred while creating the ticket.'}), 500

@app.route('/tickets', methods=['GET'])
def get_tickets():
    """
    Retrieve all support tickets.
    """
    try:
        tickets = Ticket.query.all()
        return jsonify([{'id': ticket.id, 'category': ticket.category, 'description': ticket.description, 'created_at': ticket.created_at} for ticket in tickets]), 200

    except Exception as e:
        logging.error(f'Error retrieving tickets: {e}')
        return jsonify({'error': 'An error occurred while retrieving tickets.'}), 500

@app.route('/tickets/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    """
    Retrieve a specific support ticket by ID.
    """
    try:
        ticket = Ticket.query.get_or_404(ticket_id)
        return jsonify({'id': ticket.id, 'category': ticket.category, 'description': ticket.description, 'created_at': ticket.created_at}), 200

    except Exception as e:
        logging.error(f'Error retrieving ticket {ticket_id}: {e}')
        return jsonify({'error': 'An error occurred while retrieving the ticket.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
