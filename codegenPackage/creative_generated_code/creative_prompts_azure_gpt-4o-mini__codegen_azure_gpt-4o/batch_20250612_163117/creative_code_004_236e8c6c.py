"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://let-talks.live
Prompt: Provide an example of a RESTful API endpoint for managing chat messages in a live chat system like let-talks.live.
Generated: DETERMINISTIC_236e8c6c8a32d0f3
Batch ID: 20250612_163117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory storage for chat messages (for demo purposes)
chat_messages = []

# Helper function to generate unique message ID
def generate_message_id():
    return len(chat_messages) + 1

@app.route('/api/messages', methods=['GET'])
def get_messages():
    """
    Endpoint: GET /api/messages
    Description: Retrieve all chat messages.
    Returns:
        JSON response containing an array of all chat messages.
    """
    return jsonify(chat_messages), 200

@app.route('/api/messages', methods=['POST'])
def add_message():
    """
    Endpoint: POST /api/messages
    Description: Add a new chat message.
    Request Body:
        - sender (str): Name of the sender.
        - message (str): The chat message content.
    Returns:
        JSON response containing the newly created message.
    """
    try:
        # Parse and validate request body
        data = request.get_json()
        sender = data.get('sender')
        message = data.get('message')
        
        if not sender or not message:
            return jsonify({"error": "Sender and message fields are required."}), 400
        
        # Create new message object
        new_message = {
            "id": generate_message_id(),
            "sender": sender,
            "message": message,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        # Save message to in-memory storage
        chat_messages.append(new_message)

        return jsonify(new_message), 201
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

@app.route('/api/messages/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    """
    Endpoint: DELETE /api/messages/<message_id>
    Description: Delete a specific chat message by ID.
    Path Parameter:
        - message_id (int): ID of the message to delete.
    Returns:
        JSON response indicating success or failure.
    """
    try:
        # Find the message by ID
        message_to_delete = next((msg for msg in chat_messages if msg['id'] == message_id), None)
        
        if not message_to_delete:
            return jsonify({"error": "Message not found."}), 404

        # Remove the message from storage
        chat_messages.remove(message_to_delete)
        
        return jsonify({"message": "Message deleted successfully."}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
