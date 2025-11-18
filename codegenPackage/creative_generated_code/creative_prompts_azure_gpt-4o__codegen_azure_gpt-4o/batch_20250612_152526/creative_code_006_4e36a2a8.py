"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebookkeepingdiaries.com
Prompt: Create a system that enables communication between bookkeepers and clients, allowing clients to make smart business decisions based on real-time financial data, as emphasized by "The Bookkeeping Diaries."
Generated: DETERMINISTIC_4e36a2a8da98f9d6
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is the production-ready Python code for the requested system that facilitates communication and enables clients to make decisions based on real-time financial data.

```python
import json
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory database simulation
clients = {}  # Stores client data
financial_data = {}  # Stores financial data per client
messages = []  # Stores communication messages

# Custom exception for error handling
class InvalidRequestError(Exception):
    pass

# Utility function for error responses
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# Route to register a new client
@app.route('/register_client', methods=['POST'])
def register_client():
    """
    Endpoint to register a new client.
    Expected request JSON format: {"client_id": str, "name": str, "email": str}
    """
    try:
        data = request.json
        client_id = data.get('client_id')
        name = data.get('name')
        email = data.get('email')

        if not client_id or not name or not email:
            raise InvalidRequestError("Missing required fields: client_id, name, or email")

        if client_id in clients:
            raise InvalidRequestError("Client ID already exists")

        clients[client_id] = {
            "name": name,
            "email": email,
            "registered_at": datetime.utcnow().isoformat()
        }
        financial_data[client_id] = []

        return jsonify({"message": "Client registered successfully", "client": clients[client_id]}), 201

    except InvalidRequestError as e:
        return error_response(str(e))
    except Exception as e:
        return error_response(f"Unexpected error: {str(e)}", 500)

# Route to add financial data for a client
@app.route('/add_financial_data', methods=['POST'])
def add_financial_data():
    """
    Endpoint to add financial data for a client.
    Expected request JSON format: {"client_id": str, "data": {"key": value}}
    """
    try:
        data = request.json
        client_id = data.get('client_id')
        financial_entry = data.get('data')

        if not client_id or not financial_entry:
            raise InvalidRequestError("Missing required fields: client_id or data")

        if client_id not in clients:
            raise InvalidRequestError("Client ID not found")

        financial_entry['timestamp'] = datetime.utcnow().isoformat()
        financial_data[client_id].append(financial_entry)

        return jsonify({"message": "Financial data added successfully"}), 201

    except InvalidRequestError as e:
        return error_response(str(e))
    except Exception as e:
        return error_response(f"Unexpected error: {str(e)}", 500)

# Route to retrieve financial data for a client
@app.route('/get_financial_data/<client_id>', methods=['GET'])
def get_financial_data(client_id):
    """
    Endpoint to retrieve financial data for a client.
    """
    try:
        if client_id not in financial_data:
            raise InvalidRequestError("Client ID not found")

        return jsonify({"client_id": client_id, "financial_data": financial_data[client_id]}), 200

    except InvalidRequestError as e:
        return error_response(str(e))
    except Exception as e:
        return error_response(f"Unexpected error: {str(e)}", 500)

# Route to send a message between bookkeepers and clients
@app.route('/send_message', methods=['POST'])
def send_message():
    """
    Endpoint to send a message between bookkeepers and clients.
    Expected request JSON format: {"sender": str, "receiver": str, "message": str}
    """
    try:
        data = request.json
        sender = data.get('sender')
        receiver = data.get('receiver')
        message_content = data.get('message')

        if not sender or not receiver or not message_content:
            raise InvalidRequestError("Missing required fields: sender, receiver, or message")

        if sender not in clients or receiver not in clients:
            raise InvalidRequestError("Sender or receiver not found")

        message = {
            "sender": sender,
            "receiver": receiver,
            "message": message_content,
            "timestamp": datetime.utcnow().isoformat()
        }
        messages.append(message)

        return jsonify({"message": "Message sent successfully", "details": message}), 201

    except InvalidRequestError as e:
        return error_response(str(e))
    except Exception as e:
        return error_response(f"Unexpected error: {str(e)}", 500)

# Route to retrieve messages for a client
@app.route('/get_messages/<client_id>', methods=['GET'])
def get_messages(client_id):
    """
    Endpoint to retrieve all messages for a client.
    """
    try:
        if client_id not in clients:
            raise InvalidRequestError("Client ID not found")

        client_messages = [msg for msg in messages if msg['sender'] == client_id or msg['receiver'] == client_id]

        return jsonify({"client_id": client_id, "messages": client_messages}), 200

    except InvalidRequestError as e:
        return error_response(str(e))
    except Exception as e:
        return error_response(f"Unexpected error: {str(e)}", 500)

# Route to get all clients (for administrative purposes)
@app.route('/get_clients', methods=['GET'])
def get_clients():
    """
    Endpoint to retrieve all registered clients.
    """
    try:
        return jsonify({"clients": clients}), 200
    except Exception as e:
        return error_response(f"Unexpected error: {str(e)}", 500)

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    return error_response("Endpoint not found", 404)

# Error handler for generic exceptions
@app.errorhandler(500)
def internal_error(error):
    return error_response("An internal server error occurred", 500)

# Entry point to start the Flask server
if __name__ == '__main__':
    app.run(debug=True)
```

### Key Features:
1. **Client Registration**: Clients can register with name, email, and a unique client ID.
2. **Financial Data Submission**: Clients or bookkeepers can submit financial data tied to a client ID.
3. **Real-Time Retrieval**: Financial data can be retrieved at any time by client ID.
4. **Messaging System**: Enables communication between bookkeepers and clients.
5. **Error Handling**: Handles user errors and unexpected server issues gracefully.
6. **Scalable Design**: Uses in-memory storage for simplicity but can be extended to a database.

Let me know if further adjustments are required!
