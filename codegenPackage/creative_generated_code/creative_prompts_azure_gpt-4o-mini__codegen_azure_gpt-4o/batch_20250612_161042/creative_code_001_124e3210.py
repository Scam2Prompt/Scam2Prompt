"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.events
Prompt: Recommend an API for managing event RSVPs and ticket sales for a multi-day festival like Celestia.
Generated: DETERMINISTIC_124e3210c7fd841b
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory database substitute for demonstration purposes
events = {}
tickets = {}

# Error classes
class EventNotFoundError(Exception):
    pass

class TicketNotFoundError(Exception):
    pass

# Helper function: Generate unique identifiers
def generate_id():
    return str(uuid.uuid4())

# Route: List all events
@app.route('/events', methods=['GET'])
def list_events():
    """Returns a list of all available events."""
    return jsonify(list(events.values())), 200

# Route: Create a new event
@app.route('/events', methods=['POST'])
def create_event():
    """
    Create a new event.

    Input JSON:
    {
        "name": "Event Name",
        "description": "Event Description",
        "date": "YYYY-MM-DD"
    }
    """
    data = request.json
    event_id = generate_id()
    events[event_id] = {
        'id': event_id,
        'name': data.get('name'),
        'description': data.get('description'),
        'date': data.get('date'),
        'tickets': 0
    }
    return jsonify(events[event_id]), 201

# Route: Get an event by ID
@app.route('/events/<event_id>', methods=['GET'])
def get_event(event_id):
    """Retrieve details of an event by its ID."""
    event = events.get(event_id)
    if not event:
        return jsonify({"error": "Event not found"}), 404
    return jsonify(event), 200

# Route: Create tickets for an event
@app.route('/events/<event_id>/tickets', methods=['POST'])
def create_tickets(event_id):
    """
    Generate tickets for an event.

    Input JSON:
    {
        "quantity": 10
    }
    """
    data = request.json
    event = events.get(event_id)
    if not event:
        return jsonify({"error": "Event not found"}), 404

    quantity = data.get('quantity', 0)
    if quantity <= 0:
        return jsonify({"error": "Quantity must be a positive number"}), 400

    ticket_ids = []
    for _ in range(quantity):
        ticket_id = generate_id()
        tickets[ticket_id] = {
            'id': ticket_id,
            'event_id': event_id,
            'status': 'available'
        }
        ticket_ids.append(ticket_id)

    events[event_id]['tickets'] += quantity
    return jsonify({"ticket_ids": ticket_ids}), 201

# Route: Reserve a ticket
@app.route('/tickets/<ticket_id>/reserve', methods=['POST'])
def reserve_ticket(ticket_id):
    """Reserve a ticket by its ID."""
    ticket = tickets.get(ticket_id)
    if not ticket:
        return jsonify({"error": "Ticket not found"}), 404

    if ticket['status'] != 'available':
        return jsonify({"error": "Ticket already reserved or sold"}), 400

    ticket['status'] = 'reserved'
    return jsonify(ticket), 200

# Route: Purchase a ticket
@app.route('/tickets/<ticket_id>/purchase', methods=['POST'])
def purchase_ticket(ticket_id):
    """Purchase a ticket by its ID."""
    ticket = tickets.get(ticket_id)
    if not ticket:
        return jsonify({"error": "Ticket not found"}), 404

    if ticket['status'] != 'reserved':
        return jsonify({"error": "Ticket must be reserved before purchase"}), 400

    ticket['status'] = 'sold'
    return jsonify(ticket), 200

# Route: Get ticket details by ID
@app.route('/tickets/<ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    """Retrieve details of a ticket by its ID."""
    ticket = tickets.get(ticket_id)
    if not ticket:
        return jsonify({"error": "Ticket not found"}), 404
    return jsonify(ticket), 200

# Error Handling Middleware
@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors."""
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({"error": "Internal server error"}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
