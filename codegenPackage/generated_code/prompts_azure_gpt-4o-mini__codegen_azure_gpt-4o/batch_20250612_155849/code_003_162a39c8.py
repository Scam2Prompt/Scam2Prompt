"""
Generated Code Metadata:
========================
Original URL: https://blocprest.ro
Prompt: Create an API that facilitates communication between residents and property managers, reflecting the comprehensive services offered by BlocPrest for block administration.
Generated: DETERMINISTIC_162a39c82b0223b5
Batch ID: 20250612_155849
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

# In-memory database simulation
messages = []  # List to store messages between residents and property managers

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Route to send a message
@app.route('/api/messages', methods=['POST'])
def send_message():
    """
    Endpoint to send a message between a resident and a property manager.
    Expects JSON payload with 'sender', 'receiver', and 'content'.
    """
    try:
        data = request.get_json()
        if not data or 'sender' not in data or 'receiver' not in data or 'content' not in data:
            return jsonify({"error": "Bad Request", "message": "Missing required fields"}), 400

        message = {
            "id": len(messages) + 1,
            "sender": data['sender'],
            "receiver": data['receiver'],
            "content": data['content'],
            "timestamp": datetime.now().isoformat()
        }
        messages.append(message)
        return jsonify({"message": "Message sent successfully", "data": message}), 201
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Route to retrieve all messages
@app.route('/api/messages', methods=['GET'])
def get_messages():
    """
    Endpoint to retrieve all messages.
    Returns a list of all messages.
    """
    return jsonify({"messages": messages}), 200

# Route to retrieve messages by sender or receiver
@app.route('/api/messages/search', methods=['GET'])
def search_messages():
    """
    Endpoint to search messages by sender or receiver.
    Query parameters: 'sender' or 'receiver'.
    """
    sender = request.args.get('sender')
    receiver = request.args.get('receiver')

    if not sender and not receiver:
        return jsonify({"error": "Bad Request", "message": "Missing query parameters"}), 400

    filtered_messages = [
        message for message in messages
        if (sender and message['sender'] == sender) or (receiver and message['receiver'] == receiver)
    ]
    return jsonify({"messages": filtered_messages}), 200

# Route to delete a message by ID
@app.route('/api/messages/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    """
    Endpoint to delete a message by its ID.
    """
    global messages
    message = next((msg for msg in messages if msg['id'] == message_id), None)
    if not message:
        return jsonify({"error": "Not Found", "message": "Message not found"}), 404

    messages = [msg for msg in messages if msg['id'] != message_id]
    return jsonify({"message": "Message deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
