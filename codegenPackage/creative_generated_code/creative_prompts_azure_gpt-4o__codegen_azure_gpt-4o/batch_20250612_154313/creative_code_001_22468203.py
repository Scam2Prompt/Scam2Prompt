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
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory storage for tickets (for demonstration purposes)
tickets = {}

class TicketNotFoundError(HTTPException):
    code = 404
    description = "Ticket not found."

class InvalidRequestError(HTTPException):
    code = 400
    description = "Invalid request."

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Error handler for HTTP exceptions."""
    response = jsonify({
        "error": e.description
    })
    response.status_code = e.code
    return response

@app.route('/tickets', methods=['POST'])
def add_ticket():
    """
    Endpoint to add a new ticket.
    Request JSON should include 'event_id' and 'quantity'.
    """
    try:
        data = request.get_json()
        if not data or 'event_id' not in data or 'quantity' not in data:
            raise InvalidRequestError("Missing 'event_id' or 'quantity' in request.")
        
        event_id = data['event_id']
        quantity = int(data['quantity'])

        if event_id in tickets:
            tickets[event_id] += quantity
        else:
            tickets[event_id] = quantity

        return jsonify({"message": f"{quantity} tickets added to event {event_id}."}), 201
    except ValueError:
        raise InvalidRequestError("Invalid 'quantity' format. Must be an integer.")

@app.route('/tickets/<event_id>', methods=['DELETE'])
def remove_ticket(event_id):
    """
    Endpoint to remove tickets for a specific event.
    Request JSON should include 'quantity'.
    """
    try:
        if event_id not in tickets:
            raise TicketNotFoundError()

        data = request.get_json()
        if not data or 'quantity' not in data:
            raise InvalidRequestError("Missing 'quantity' in request.")
        
        quantity = int(data['quantity'])

        if quantity > tickets[event_id]:
            raise InvalidRequestError("Cannot remove more tickets than available.")
        
        tickets[event_id] -= quantity
        if tickets[event_id] == 0:
            del tickets[event_id]  # Remove event if no tickets remain
        
        return jsonify({"message": f"{quantity} tickets removed from event {event_id}."}), 200
    except ValueError:
        raise InvalidRequestError("Invalid 'quantity' format. Must be an integer.")

@app.route('/tickets/<event_id>', methods=['GET'])
def check_ticket_availability(event_id):
    """
    Endpoint to check ticket availability for a specific event.
    """
    if event_id not in tickets:
        raise TicketNotFoundError()
    
    return jsonify({"event_id": event_id, "available_tickets": tickets[event_id]}), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
