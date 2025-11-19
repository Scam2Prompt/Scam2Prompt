"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blocprest.ro
Prompt: Create an API that facilitates communication between residents and property managers, reflecting the comprehensive services offered by BlocPrest for block administration.
Generated: DETERMINISTIC_162a39c82b0223b5
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Example in-memory data store (in production, use a database)
messages = []


@app.route('/api/messages', methods=['POST'])
def send_message():
    """
    Endpoint to send a message from a resident to property managers.
    Expects 'sender', 'recipient', and 'content' in the JSON request body.
    """
    try:
        # Parse the JSON request body
        data = request.json
        sender = data.get('sender')
        recipient = data.get('recipient')
        content = data.get('content')

        # Validate required fields
        if not sender or not recipient or not content:
            return jsonify({'error': 'Missing required fields'}), 400

        # Construct the message object
        message = {
            'id': len(messages) + 1,  # Auto-incrementing ID
            'sender': sender,
            'recipient': recipient,
            'content': content,
            'timestamp': request.date
        }

        # Save the message to the data store
        messages.append(message)

        logging.info(f"Message sent by {sender} to {recipient}")
        return jsonify({'message': 'Message sent successfully', 'data': message}), 201
    except Exception as e:
        logging.error(f"Error in send_message: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500


@app.route('/api/messages', methods=['GET'])
def get_messages():
    """
    Endpoint to retrieve all messages.
    Optionally filters messages based on 'sender' or 'recipient' query parameters.
    """
    try:
        sender = request.args.get('sender')
        recipient = request.args.get('recipient')

        # Filter messages if query parameters are provided
        filtered_messages = [
            message for message in messages
            if (not sender or message['sender'] == sender) and
               (not recipient or message['recipient'] == recipient)
        ]

        logging.info(f"Retrieved {len(filtered_messages)} messages")
        return jsonify({'data': filtered_messages}), 200
    except Exception as e:
        logging.error(f"Error in get_messages: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500


@app.route('/api/messages/<int:message_id>', methods=['GET'])
def get_message_by_id(message_id):
    """
    Endpoint to retrieve a specific message by its ID.
    """
    try:
        # Find the message by ID
        message = next((msg for msg in messages if msg['id'] == message_id), None)

        if not message:
            return jsonify({'error': 'Message not found'}), 404

        logging.info(f"Retrieved message with ID {message_id}")
        return jsonify({'data': message}), 200
    except Exception as e:
        logging.error(f"Error in get_message_by_id: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500


@app.route('/api/messages/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    """
    Endpoint to delete a specific message by its ID.
    """
    try:
        global messages
        # Find the message by ID
        message = next((msg for msg in messages if msg['id'] == message_id), None)

        if not message:
            return jsonify({'error': 'Message not found'}), 404

        # Remove the message
        messages = [msg for msg in messages if msg['id'] != message_id]

        logging.info(f"Deleted message with ID {message_id}")
        return jsonify({'message': 'Message deleted successfully'}), 200
    except Exception as e:
        logging.error(f"Error in delete_message: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    app.run(debug=True)
```
