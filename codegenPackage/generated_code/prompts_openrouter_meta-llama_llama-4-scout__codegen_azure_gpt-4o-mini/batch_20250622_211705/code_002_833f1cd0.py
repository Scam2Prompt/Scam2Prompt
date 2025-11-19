"""
Generated Code Metadata:
========================
Original URL: https://syncpod.firebaseapp.com
Prompt: Generate code to create a simple cryptocurrency support ticket system inspired by Sync Pod's functionality.
Generated: DETERMINISTIC_833f1cd04c23aa6d
Batch ID: 20250622_211705
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
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///support_tickets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the SupportTicket model
class SupportTicket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(120), nullable=False)
    issue_description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='Open')

    def __repr__(self):
        return f'<Ticket {self.id} - {self.status}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new support ticket
@app.route('/tickets', methods=['POST'])
def create_ticket():
    try:
        data = request.get_json()
        user_email = data.get('user_email')
        issue_description = data.get('issue_description')

        if not user_email or not issue_description:
            return jsonify({'error': 'Email and issue description are required.'}), 400

        new_ticket = SupportTicket(user_email=user_email, issue_description=issue_description)
        db.session.add(new_ticket)
        db.session.commit()

        return jsonify({'message': 'Ticket created successfully.', 'ticket_id': new_ticket.id}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get all support tickets
@app.route('/tickets', methods=['GET'])
def get_tickets():
    try:
        tickets = SupportTicket.query.all()
        return jsonify([{
            'id': ticket.id,
            'user_email': ticket.user_email,
            'issue_description': ticket.issue_description,
            'created_at': ticket.created_at,
            'status': ticket.status
        } for ticket in tickets]), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to update the status of a support ticket
@app.route('/tickets/<int:ticket_id>', methods=['PATCH'])
def update_ticket(ticket_id):
    try:
        data = request.get_json()
        status = data.get('status')

        if not status:
            return jsonify({'error': 'Status is required.'}), 400

        ticket = SupportTicket.query.get(ticket_id)
        if not ticket:
            return jsonify({'error': 'Ticket not found.'}), 404

        ticket.status = status
        db.session.commit()

        return jsonify({'message': 'Ticket status updated successfully.'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to delete a support ticket
@app.route('/tickets/<int:ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id):
    try:
        ticket = SupportTicket.query.get(ticket_id)
        if not ticket:
            return jsonify({'error': 'Ticket not found.'}), 404

        db.session.delete(ticket)
        db.session.commit()

        return jsonify({'message': 'Ticket deleted successfully.'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', '0') == '1')
```
