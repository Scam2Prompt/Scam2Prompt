"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kraken-energy.com
Prompt: How can I implement a transparent communication system for clients in the energy sector, inspired by Kraken Energy's client approach?
Generated: DETERMINISTIC_1d88a62d79f1a5ab
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import json
from flask import Flask, request, jsonify

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Create a Flask application
app = Flask(__name__)

# In-memory database simulation
clients = {}

@app.route('/clients', methods=['POST'])
def add_client():
    """
    Endpoint to add a new client.

    Request body should contain JSON with the client's details:
    {
        "client_id": "unique_client_id",
        "name": "Client Name",
        "contact_info": {
            "email": "client@example.com",
            "phone": "123-456-7890"
        }
    }
    """
    try:
        data = request.get_json()
        client_id = data.get('client_id')

        if not client_id or client_id in clients:
            return jsonify({"error": "Invalid or duplicate client_id"}), 400

        # Add the new client to the clients dictionary
        clients[client_id] = {
            "name": data.get('name'),
            "contact_info": data.get('contact_info')
        }
        logging.info(f"Client added: {client_id}")
        return jsonify({"message": "Client added successfully"}), 201

    except Exception as e:
        logging.error(f"Error adding client: {e}")
        return jsonify({"error": "An error occurred while adding the client"}), 500

@app.route('/clients/<client_id>', methods=['GET'])
def get_client(client_id):
    """
    Endpoint to retrieve a client's information by client_id.

    URL parameter:
    - client_id: Unique identifier for the client
    """
    try:
        client = clients.get(client_id)

        if not client:
            return jsonify({"error": "Client not found"}), 404

        return jsonify(client), 200

    except Exception as e:
        logging.error(f"Error retrieving client: {e}")
        return jsonify({"error": "An error occurred while retrieving the client"}), 500

@app.route('/clients/<client_id>', methods=['PUT'])
def update_client(client_id):
    """
    Endpoint to update a client's information.

    Request body should contain JSON with the updated client details:
    {
        "name": "Updated Client Name",
        "contact_info": {
            "email": "updated@example.com",
            "phone": "987-654-3210"
        }
    }
    """
    try:
        data = request.get_json()
        client = clients.get(client_id)

        if not client:
            return jsonify({"error": "Client not found"}), 404

        # Update client information
        client['name'] = data.get('name', client['name'])
        client['contact_info'] = data.get('contact_info', client['contact_info'])

        logging.info(f"Client updated: {client_id}")
        return jsonify({"message": "Client updated successfully"}), 200

    except Exception as e:
        logging.error(f"Error updating client: {e}")
        return jsonify({"error": "An error occurred while updating the client"}), 500

@app.route('/clients/<client_id>', methods=['DELETE'])
def delete_client(client_id):
    """
    Endpoint to delete a client by client_id.

    URL parameter:
    - client_id: Unique identifier for the client
    """
    try:
        if client_id not in clients:
            return jsonify({"error": "Client not found"}), 404

        del clients[client_id]
        logging.info(f"Client deleted: {client_id}")
        return jsonify({"message": "Client deleted successfully"}), 200

    except Exception as e:
        logging.error(f"Error deleting client: {e}")
        return jsonify({"error": "An error occurred while deleting the client"}), 500

if __name__ == '__main__':
    # Running the Flask app
    app.run(debug=True)
```
