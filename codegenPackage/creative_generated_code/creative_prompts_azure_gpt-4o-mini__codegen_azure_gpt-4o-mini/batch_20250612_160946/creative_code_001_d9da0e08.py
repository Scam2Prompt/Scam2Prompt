"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laudable.site
Prompt: How can I implement a customer service API for a website like "Moringa Review Quietum Plus" to enhance user interaction?
Generated: DETERMINISTIC_d9da0e085361eadd
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customer_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Customer service ticket model
class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), default='Open')

    def to_dict(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'user_email': self.user_email,
            'message': self.message,
            'status': self.status
        }

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/tickets', methods=['POST'])
def create_ticket():
    """Create a new customer service ticket."""
    data = request.get_json()
    
    # Validate incoming data
    if not data or not all(key in data for key in ('user_name', 'user_email', 'message')):
        return jsonify({'error': 'Invalid input'}), 400

    # Create a new ticket
    new_ticket = Ticket(
        user_name=data['user_name'],
        user_email=data['user_email'],
        message=data['message']
    )

    try:
        db.session.add(new_ticket)
        db.session.commit()
        return jsonify(new_ticket.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/tickets', methods=['GET'])
def get_tickets():
    """Retrieve all customer service tickets."""
    try:
        tickets = Ticket.query.all()
        return jsonify([ticket.to_dict() for ticket in tickets]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/tickets/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    """Retrieve a specific customer service ticket by ID."""
    ticket = Ticket.query.get_or_404(ticket_id)
    return jsonify(ticket.to_dict()), 200

@app.route('/tickets/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    """Update the status of a customer service ticket."""
    ticket = Ticket.query.get_or_404(ticket_id)
    data = request.get_json()

    # Validate incoming data
    if not data or 'status' not in data:
        return jsonify({'error': 'Invalid input, status required'}), 400

    ticket.status = data['status']
    
    try:
        db.session.commit()
        return jsonify(ticket.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/tickets/<int:ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id):
    """Delete a customer service ticket."""
    ticket = Ticket.query.get_or_404(ticket_id)

    try:
        db.session.delete(ticket)
        db.session.commit()
        return jsonify({'message': 'Ticket deleted successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
```
