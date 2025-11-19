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

Below is a Python implementation for a 24/7 IT support system using a managed services framework. The code leverages Flask for the web service and Celery for background task management.

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from celery import Celery
import logging
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure Celery for task management
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# IT support ticket store (simulated database)
tickets = []

# Celery task: Simulates ticket handling process
@celery.task
def handle_ticket(ticket_id):
    try:
        # Simulate ticket processing
        logging.info(f"Processing ticket ID: {ticket_id}")
        for ticket in tickets:
            if ticket['id'] == ticket_id:
                ticket['status'] = 'Resolved'
                ticket['resolved_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                logging.info(f"Ticket ID {ticket_id} resolved successfully.")
                return f"Ticket ID {ticket_id} has been resolved."
        return "Ticket not found."
    except Exception as e:
        logging.error(f"Error handling ticket ID {ticket_id}: {e}")
        return f"Error: {str(e)}"

# Route: Submit a new IT support ticket
@app.route('/submit_ticket', methods=['POST'])
def submit_ticket():
    try:
        # Parse ticket details from request
        data = request.json
        if not data or 'issue' not in data or 'submitted_by' not in data:
            return jsonify({'error': 'Invalid input. Issue and submitted_by fields are required.'}), 400
        
        # Generate ticket ID and store the ticket
        ticket_id = len(tickets) + 1
        ticket = {
            'id': ticket_id,
            'issue': data['issue'],
            'submitted_by': data['submitted_by'],
            'status': 'Pending',
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'resolved_at': None
        }
        tickets.append(ticket)
        logging.info(f"New ticket submitted: {ticket}")
        
        # Dispatch the ticket handling task asynchronously
        handle_ticket.delay(ticket_id)
        return jsonify({'message': 'Ticket submitted successfully.', 'ticket_id': ticket_id}), 200
    except Exception as e:
        logging.error(f"Error submitting ticket: {e}")
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500

# Route: Get the status of a specific ticket
@app.route('/ticket_status/<int:ticket_id>', methods=['GET'])
def ticket_status(ticket_id):
    try:
        # Find the ticket by ID
        for ticket in tickets:
            if ticket['id'] == ticket_id:
                return jsonify({'ticket': ticket}), 200
        return jsonify({'error': 'Ticket not found.'}), 404
    except Exception as e:
        logging.error(f"Error retrieving ticket status: {e}")
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500

# Route: List all tickets
@app.route('/list_tickets', methods=['GET'])
def list_tickets():
    try:
        return jsonify({'tickets': tickets}), 200
    except Exception as e:
        logging.error(f"Error listing tickets: {e}")
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500

# Main entry point to start the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### Dependencies:
Ensure you install the required dependencies before running the code:
```bash
pip install flask celery redis
```

### Redis Configuration:
Ensure Redis is installed and running locally for Celery to manage tasks:  
```bash
redis-server
```

### How to Run:
1. Start Redis: `redis-server`
2. Start Celery Worker: `celery -A <script_name> worker --loglevel=info`
3. Run the Flask app: `python <script_name>.py`

This code implements a scalable, asynchronous ticket processing system that can run 24/7.
