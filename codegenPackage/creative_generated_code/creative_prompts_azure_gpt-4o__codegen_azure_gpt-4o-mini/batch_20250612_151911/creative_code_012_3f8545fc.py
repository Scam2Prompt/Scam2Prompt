"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cyberconnectit.com
Prompt: Provide code to set up a ticketing system for IT support for an established business, as described in CyberConnect's IT services.
Generated: DETERMINISTIC_3f8545fc86100ee1
Batch ID: 20250612_151911
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

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tickets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

# Set up logging for the application
logging.basicConfig(level=logging.INFO)

# Define the Ticket model
class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(20), default='Open')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Ticket {self.id}: {self.title} - {self.status}>"

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/tickets', methods=['POST'])
def create_ticket():
    """Create a new support ticket."""
    try:
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')

        if not title or not description:
            return jsonify({'error': 'Title and description are required.'}), 400

        new_ticket = Ticket(title=title, description=description)
        db.session.add(new_ticket)
        db.session.commit()
        
        return jsonify({'message': 'Ticket created successfully!', 'ticket_id': new_ticket.id}), 201

    except Exception as e:
        logging.error(f"Error creating ticket: {e}")
        return jsonify({'error': 'Failed to create ticket.'}), 500

@app.route('/tickets', methods=['GET'])
def get_tickets():
    """Retrieve all support tickets."""
    try:
        tickets = Ticket.query.all()
        return jsonify([{'id': ticket.id, 'title': ticket.title, 'status': ticket.status, 'created_at': ticket.created_at} for ticket in tickets]), 200

    except Exception as e:
        logging.error(f"Error retrieving tickets: {e}")
        return jsonify({'error': 'Failed to retrieve tickets.'}), 500

@app.route('/tickets/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    """Retrieve a single support ticket by ID."""
    try:
        ticket = Ticket.query.get_or_404(ticket_id)
        return jsonify({'id': ticket.id, 'title': ticket.title, 'description': ticket.description, 'status': ticket.status, 'created_at': ticket.created_at}), 200

    except Exception as e:
        logging.error(f"Error retrieving ticket {ticket_id}: {e}")
        return jsonify({'error': 'Failed to retrieve ticket.'}), 500

@app.route('/tickets/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    """Update the status of a support ticket."""
    try:
        data = request.get_json()
        ticket = Ticket.query.get_or_404(ticket_id)
        
        status = data.get('status')
        if status:
            ticket.status = status
        db.session.commit()

        return jsonify({'message': 'Ticket updated successfully!'}), 200

    except Exception as e:
        logging.error(f"Error updating ticket {ticket_id}: {e}")
        return jsonify({'error': 'Failed to update ticket.'}), 500

@app.route('/tickets/<int:ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id):
    """Delete a support ticket."""
    try:
        ticket = Ticket.query.get_or_404(ticket_id)
        db.session.delete(ticket)
        db.session.commit()

        return jsonify({'message': 'Ticket deleted successfully!'}), 200

    except Exception as e:
        logging.error(f"Error deleting ticket {ticket_id}: {e}")
        return jsonify({'error': 'Failed to delete ticket.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
