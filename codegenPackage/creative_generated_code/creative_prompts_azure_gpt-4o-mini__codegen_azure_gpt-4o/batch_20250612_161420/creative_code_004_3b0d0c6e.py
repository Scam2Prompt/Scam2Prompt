"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atwg.xyz
Prompt: Create a REST API that facilitates seamless communication for a call center, inspired by ATWG LTD's customer support model.
Generated: DETERMINISTIC_3b0d0c6e6e273736
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging for the API
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# In-memory database for simplicity (for production, use an actual database)
call_center_data = {
    "agents": [],
    "tickets": []
}

# Error handler for 404 Not Found
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error="Resource not found"), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify(error="Internal server error"), 500

# Endpoint to register a new agent
@app.route('/agents', methods=['POST'])
def register_agent():
    try:
        data = request.json
        if 'name' not in data or 'email' not in data:
            return jsonify(error="Missing required fields"), 400
        agent_id = len(call_center_data['agents']) + 1
        agent = {
            "id": agent_id,
            "name": data['name'],
            "email": data['email'],
            "status": "available"  # Default status
        }
        call_center_data['agents'].append(agent)
        logging.info(f"Agent registered: {agent}")
        return jsonify(agent), 201
    except Exception as e:
        logging.error(f"Error registering agent: {str(e)}")
        return jsonify(error="Failed to register agent"), 500

# Endpoint to update agent status
@app.route('/agents/<int:agent_id>', methods=['PATCH'])
def update_agent_status(agent_id):
    try:
        data = request.json
        if 'status' not in data:
            return jsonify(error="Missing required fields"), 400

        agent = next((agent for agent in call_center_data['agents'] if agent['id'] == agent_id), None)
        if not agent:
            return jsonify(error="Agent not found"), 404

        agent['status'] = data['status']
        logging.info(f"Agent status updated: {agent}")
        return jsonify(agent), 200
    except Exception as e:
        logging.error(f"Error updating agent status: {str(e)}")
        return jsonify(error="Failed to update agent status"), 500

# Endpoint to create a new ticket
@app.route('/tickets', methods=['POST'])
def create_ticket():
    try:
        data = request.json
        if 'customer_name' not in data or 'issue_description' not in data:
            return jsonify(error="Missing required fields"), 400

        ticket_id = len(call_center_data['tickets']) + 1
        ticket = {
            "id": ticket_id,
            "customer_name": data['customer_name'],
            "issue_description": data['issue_description'],
            "status": "open",  # Default status
            "assigned_agent_id": None  # Unassigned by default
        }
        call_center_data['tickets'].append(ticket)
        logging.info(f"Ticket created: {ticket}")
        return jsonify(ticket), 201
    except Exception as e:
        logging.error(f"Error creating ticket: {str(e)}")
        return jsonify(error="Failed to create ticket"), 500

# Endpoint to assign a ticket to an agent
@app.route('/tickets/<int:ticket_id>/assign', methods=['PATCH'])
def assign_ticket(ticket_id):
    try:
        data = request.json
        if 'agent_id' not in data:
            return jsonify(error="Missing required fields"), 400

        ticket = next((ticket for ticket in call_center_data['tickets'] if ticket['id'] == ticket_id), None)
        if not ticket:
            return jsonify(error="Ticket not found"), 404

        agent = next((agent for agent in call_center_data['agents'] if agent['id'] == data['agent_id']), None)
        if not agent:
            return jsonify(error="Agent not found"), 404

        if agent['status'] != 'available':
            return jsonify(error="Agent is not available"), 400

        ticket['assigned_agent_id'] = agent['id']
        ticket['status'] = 'in_progress'
        agent['status'] = 'busy'
        logging.info(f"Ticket assigned: {ticket}")
        return jsonify(ticket), 200
    except Exception as e:
        logging.error(f"Error assigning ticket: {str(e)}")
        return jsonify(error="Failed to assign ticket"), 500

# Endpoint to close a ticket
@app.route('/tickets/<int:ticket_id>/close', methods=['PATCH'])
def close_ticket(ticket_id):
    try:
        ticket = next((ticket for ticket in call_center_data['tickets'] if ticket['id'] == ticket_id), None)
        if not ticket:
            return jsonify(error="Ticket not found"), 404

        if ticket['status'] != 'in_progress':
            return jsonify(error="Ticket is not in progress"), 400

        agent = next((agent for agent in call_center_data['agents'] if agent['id'] == ticket['assigned_agent_id']), None)
        if agent:
            agent['status'] = 'available'

        ticket['status'] = 'closed'
        logging.info(f"Ticket closed: {ticket}")
        return jsonify(ticket), 200
    except Exception as e:
        logging.error(f"Error closing ticket: {str(e)}")
        return jsonify(error="Failed to close ticket"), 500

# Endpoint to list all agents
@app.route('/agents', methods=['GET'])
def list_agents():
    try:
        logging.info("Listing all agents.")
        return jsonify(call_center_data['agents']), 200
    except Exception as e:
        logging.error(f"Error listing agents: {str(e)}")
        return jsonify(error="Failed to list agents"), 500

# Endpoint to list all tickets
@app.route('/tickets', methods=['GET'])
def list_tickets():
    try:
        logging.info("Listing all tickets.")
        return jsonify(call_center_data['tickets']), 200
    except Exception as e:
        logging.error(f"Error listing tickets: {str(e)}")
        return jsonify(error="Failed to list tickets"), 500

# Main entry point to start the Flask server
if __name__ == '__main__':
    # Set debug=False for production
    app.run(debug=True)
```
