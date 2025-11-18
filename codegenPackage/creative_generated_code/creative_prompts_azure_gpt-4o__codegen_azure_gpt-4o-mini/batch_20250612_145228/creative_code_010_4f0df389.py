"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://champsonly.xyz
Prompt: Suggest libraries or APIs for implementing a round-the-clock support ticket system, similar to the Champs Only customer service model.
Generated: DETERMINISTIC_4f0df38907db13b8
Batch ID: 20250612_145228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import datetime
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tickets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration engine
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Ticket model
class Ticket(db.Model):
    """Model to represent a support ticket."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    status = db.Column(db.String(20), default='Open')

    def __repr__(self):
        return f'<Ticket {self.title}>'

@app.route('/tickets', methods=['POST'])
def create_ticket():
    """Create a new support ticket."""
    data = request.get_json()
    
    # Validate incoming data
    if not data or not 'title' in data or not 'description' in data:
        return jsonify({'error': 'Title and description are required.'}), 400
    
    try:
        new_ticket = Ticket(title=data['title'], description=data['description'])
        db.session.add(new_ticket)
        db.session.commit()
        return jsonify({'message': 'Ticket created successfully.', 'ticket_id': new_ticket.id}), 201
    except Exception as e:
        logging.error(f'Error creating ticket: {e}')
        db.session.rollback()
        return jsonify({'error': 'Failed to create ticket.'}), 500

@app.route('/tickets', methods=['GET'])
def list_tickets():
    """Retrieve a list of all support tickets."""
    tickets = Ticket.query.all()
    return jsonify([{'id': ticket.id, 'title': ticket.title, 'status': ticket.status} for ticket in tickets]), 200

@app.route('/tickets/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    """Retrieve a specific ticket by its ID."""
    ticket = Ticket.query.get_or_404(ticket_id)
    return jsonify({'id': ticket.id, 'title': ticket.title, 'description': ticket.description, 'status': ticket.status, 'created_at': ticket.created_at}), 200

@app.route('/tickets/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    """Update the status of a specific ticket."""
    data = request.get_json()
    ticket = Ticket.query.get_or_404(ticket_id)

    if 'status' in data:
        ticket.status = data['status']
        try:
            db.session.commit()
            return jsonify({'message': 'Ticket updated successfully.'}), 200
        except Exception as e:
            logging.error(f'Error updating ticket: {e}')
            db.session.rollback()
            return jsonify({'error': 'Failed to update ticket.'}), 500
    
    return jsonify({'error': 'Status is required to update the ticket.'}), 400

@app.route('/tickets/<int:ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id):
    """Delete a specific ticket."""
    ticket = Ticket.query.get_or_404(ticket_id)
    try:
        db.session.delete(ticket)
        db.session.commit()
        return jsonify({'message': 'Ticket deleted successfully.'}), 200
    except Exception as e:
        logging.error(f'Error deleting ticket: {e}')
        db.session.rollback()
        return jsonify({'error': 'Failed to delete ticket.'}), 500

if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    # Run the app
    app.run(debug=True, host='0.0.0.0', port=5000)
```
