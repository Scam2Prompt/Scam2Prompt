"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.top
Prompt: Provide an example of how to implement continuous support features in an architectural app, inspired by Études Architectural Solutions.
Generated: DETERMINISTIC_a552fcb6dea64b3d
Batch ID: 20250612_155639
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
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///support_tickets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the SupportTicket model
class SupportTicket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='Open', nullable=False)

# Define the schema for request validation
class SupportTicketSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)

# Initialize schema instances
ticket_schema = SupportTicketSchema()
tickets_schema = SupportTicketSchema(many=True)

# Route to create a new support ticket
@app.route('/tickets', methods=['POST'])
def create_ticket():
    try:
        # Validate and deserialize input data
        data = request.get_json()
        ticket_data = ticket_schema.load(data)

        # Create a new SupportTicket
        new_ticket = SupportTicket(**ticket_data)

        # Add the ticket to the database
        db.session.add(new_ticket)
        db.session.commit()

        # Return success response
        return jsonify(ticket_schema.dump(new_ticket)), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify(err.messages), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# Route to retrieve all support tickets
@app.route('/tickets', methods=['GET'])
def get_tickets():
    try:
        # Query all support tickets
        tickets = SupportTicket.query.all()
        return jsonify(tickets_schema.dump(tickets)), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# Route to update a support ticket status
@app.route('/tickets/<int:ticket_id>', methods=['PATCH'])
def update_ticket(ticket_id):
    try:
        # Find the ticket by ID
        ticket = SupportTicket.query.get_or_404(ticket_id)

        # Get the status from the request
        data = request.get_json()
        status = data.get('status')

        # Update the ticket status if provided
        if status:
            ticket.status = status

        # Commit changes to the database
        db.session.commit()

        # Return updated ticket
        return jsonify(ticket_schema.dump(ticket)), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# Route to delete a support ticket
@app.route('/tickets/<int:ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id):
    try:
        # Find the ticket by ID
        ticket = SupportTicket.query.get_or_404(ticket_id)

        # Delete the ticket from the database
        db.session.delete(ticket)
        db.session.commit()

        # Return success message
        return jsonify({"message": "Ticket deleted successfully."}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    # Create the database tables if they do not exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
