"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imts.com.pk
Prompt: How can I implement a 24/7 IT support system using the managed services framework outlined by IMTS?
Generated: DETERMINISTIC_4ff23bae1b2eed91
Batch ID: 20250612_155938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from flask import Flask, request, jsonify
from datetime import datetime
import threading
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a Flask application
app = Flask(__name__)

# A simple in-memory store for support tickets
support_tickets = []

# Function to simulate ticket processing
def process_tickets():
    while True:
        if support_tickets:
            for ticket in support_tickets:
                logging.info(f"Processing ticket: {ticket['id']} - {ticket['issue']}")
                # Simulate ticket resolution time
                time.sleep(5)  # Simulate time taken to resolve the ticket
                logging.info(f"Resolved ticket: {ticket['id']}")
                support_tickets.remove(ticket)
        time.sleep(10)  # Check for new tickets every 10 seconds

# Start the ticket processing thread
threading.Thread(target=process_tickets, daemon=True).start()

@app.route('/api/tickets', methods=['POST'])
def create_ticket():
    """
    Endpoint to create a new support ticket.
    Expects a JSON body with 'issue' field.
    Returns the created ticket ID.
    """
    try:
        data = request.json
        if 'issue' not in data:
            return jsonify({"error": "Issue description is required."}), 400

        ticket_id = len(support_tickets) + 1
        ticket = {"id": ticket_id, "issue": data['issue'], "created_at": datetime.now()}
        support_tickets.append(ticket)

        logging.info(f"Created ticket: {ticket}")
        return jsonify({"ticket_id": ticket_id}), 201

    except Exception as e:
        logging.error(f"Error creating ticket: {str(e)}")
        return jsonify({"error": "An error occurred while creating the ticket."}), 500

@app.route('/api/tickets', methods=['GET'])
def get_tickets():
    """
    Endpoint to retrieve all support tickets.
    Returns a list of tickets.
    """
    return jsonify(support_tickets), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### Requirements
To run the above code, the following Python packages must be installed:
```bash
pip install Flask
```

### Usage
1. Start the application using `python <filename>.py`.
2. Use tools like Postman or curl to interact with the API:
   - Create a ticket: `POST /api/tickets` with JSON body `{"issue": "Your issue description"}`
   - Retrieve all tickets: `GET /api/tickets`
