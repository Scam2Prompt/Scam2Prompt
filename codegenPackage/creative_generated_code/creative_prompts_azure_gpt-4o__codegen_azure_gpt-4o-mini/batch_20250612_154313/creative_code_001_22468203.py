"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syncconnects.com
Prompt: Develop an API endpoint to manage event tickets for a platform like Sync Connects, ensuring functionality for adding, removing, and checking ticket availability.
Generated: DETERMINISTIC_22468203fc6f45c8
Batch ID: 20250612_154313
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
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tickets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Ticket model to represent ticket information in the database
class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Ticket {self.event_name}: {self.quantity}>"

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to add tickets
@app.route('/api/tickets', methods=['POST'])
def add_ticket():
    try:
        data = request.json
        new_ticket = Ticket(event_name=data['event_name'], quantity=data['quantity'])
        db.session.add(new_ticket)
        db.session.commit()
        return jsonify({'message': 'Ticket added successfully!', 'ticket': {'event_name': new_ticket.event_name, 'quantity': new_ticket.quantity}}), 201
    except (KeyError, TypeError) as e:
        return jsonify({'error': str(e), 'message': 'Invalid data provided.'}), 400
    except SQLAlchemyError as e:
        return jsonify({'error': str(e), 'message': 'Database error occurred.'}), 500

# Endpoint to remove tickets
@app.route('/api/tickets/<int:ticket_id>', methods=['DELETE'])
def remove_ticket(ticket_id):
    try:
        ticket = Ticket.query.get(ticket_id)
        if ticket is None:
            return jsonify({'message': 'Ticket not found.'}), 404
        db.session.delete(ticket)
        db.session.commit()
        return jsonify({'message': 'Ticket removed successfully!'}), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e), 'message': 'Database error occurred.'}), 500

# Endpoint to check ticket availability
@app.route('/api/tickets/<string:event_name>', methods=['GET'])
def check_availability(event_name):
    try:
        tickets = Ticket.query.filter_by(event_name=event_name).all()
        if not tickets:
            return jsonify({'message': 'No tickets found for this event.'}), 404
        return jsonify({'event_name': event_name, 'tickets': [{'id': ticket.id, 'quantity': ticket.quantity} for ticket in tickets]}), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e), 'message': 'Database error occurred.'}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
