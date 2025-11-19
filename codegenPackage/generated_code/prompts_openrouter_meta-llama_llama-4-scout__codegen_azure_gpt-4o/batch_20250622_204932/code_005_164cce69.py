"""
Generated Code Metadata:
========================
Original URL: https://atualcontabilidade.com
Prompt: "Design a RESTful API for an accounting firm's client portal, allowing clients to submit requests, view documents, and communicate with the firm."
Generated: DETERMINISTIC_164cce695a2fc20b
Batch ID: 20250622_204932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Mock database for demonstration purposes
clients = {
    1: {"name": "John Doe", "requests": [], "documents": [], "messages": []},
    2: {"name": "Jane Smith", "requests": [], "documents": [], "messages": []},
}

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.description}).get_data()
    response.content_type = "application/json"
    return response

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": "An unexpected error occurred"}), 500

# Route to submit a request
@app.route('/clients/<int:client_id>/requests', methods=['POST'])
def submit_request(client_id):
    """
    Submit a new request for a client.
    :param client_id: ID of the client
    :return: JSON response with the submitted request
    """
    client = clients.get(client_id)
    if not client:
        return jsonify({"error": "Client not found"}), 404

    data = request.json
    if not data or 'request_details' not in data:
        return jsonify({"error": "Invalid request data"}), 400

    new_request = {"id": len(client["requests"]) + 1, "details": data["request_details"]}
    client["requests"].append(new_request)
    return jsonify(new_request), 201

# Route to view documents
@app.route('/clients/<int:client_id>/documents', methods=['GET'])
def view_documents(client_id):
    """
    View documents for a client.
    :param client_id: ID of the client
    :return: JSON response with the client's documents
    """
    client = clients.get(client_id)
    if not client:
        return jsonify({"error": "Client not found"}), 404

    return jsonify(client["documents"]), 200

# Route to upload a document
@app.route('/clients/<int:client_id>/documents', methods=['POST'])
def upload_document(client_id):
    """
    Upload a new document for a client.
    :param client_id: ID of the client
    :return: JSON response with the uploaded document
    """
    client = clients.get(client_id)
    if not client:
        return jsonify({"error": "Client not found"}), 404

    data = request.json
    if not data or 'document_name' not in data or 'document_content' not in data:
        return jsonify({"error": "Invalid document data"}), 400

    new_document = {
        "id": len(client["documents"]) + 1,
        "name": data["document_name"],
        "content": data["document_content"],
    }
    client["documents"].append(new_document)
    return jsonify(new_document), 201

# Route to send a message
@app.route('/clients/<int:client_id>/messages', methods=['POST'])
def send_message(client_id):
    """
    Send a message to the firm.
    :param client_id: ID of the client
    :return: JSON response with the sent message
    """
    client = clients.get(client_id)
    if not client:
        return jsonify({"error": "Client not found"}), 404

    data = request.json
    if not data or 'message_content' not in data:
        return jsonify({"error": "Invalid message data"}), 400

    new_message = {"id": len(client["messages"]) + 1, "content": data["message_content"]}
    client["messages"].append(new_message)
    return jsonify(new_message), 201

# Route to view messages
@app.route('/clients/<int:client_id>/messages', methods=['GET'])
def view_messages(client_id):
    """
    View messages for a client.
    :param client_id: ID of the client
    :return: JSON response with the client's messages
    """
    client = clients.get(client_id)
    if not client:
        return jsonify({"error": "Client not found"}), 404

    return jsonify(client["messages"]), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
