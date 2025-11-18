"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masitsolutions.net
Prompt: Develop a cloud-based solution for technical support outsourcing, leveraging MASIT Solutions' innovative cloud technology expertise.
Generated: DETERMINISTIC_652298e277ff02ec
Batch ID: 20250612_153224
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configuration for the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///support_tickets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the SupportTicket model
class SupportTicket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    issue_description = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(50), default='Open')

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'issue_description': self.issue_description,
            'status': self.status
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new support ticket
@app.route('/api/tickets', methods=['POST'])
def create_ticket():
    """Create a new support ticket."""
    data = request.json
    try:
        new_ticket = SupportTicket(
            customer_name=data['customer_name'],
            issue_description=data['issue_description']
        )
        db.session.add(new_ticket)
        db.session.commit()
        return jsonify(new_ticket.to_dict()), 201
    except KeyError as e:
        return jsonify({'error': f'Missing key: {str(e)}'}), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to get all support tickets
@app.route('/api/tickets', methods=['GET'])
def get_tickets():
    """Retrieve all support tickets."""
    try:
        tickets = SupportTicket.query.all()
        return jsonify([ticket.to_dict() for ticket in tickets]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Route to update a support ticket status
@app.route('/api/tickets/<int:ticket_id>', methods=['PATCH'])
def update_ticket(ticket_id):
    """Update the status of a support ticket."""
    data = request.json
    try:
        ticket = SupportTicket.query.get_or_404(ticket_id)
        ticket.status = data.get('status', ticket.status)
        db.session.commit()
        return jsonify(ticket.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)  # Set debug=True for development only
```
