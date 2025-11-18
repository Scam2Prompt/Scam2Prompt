"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tronlinkapp.org
Prompt: Generate code for implementing community discussion and support channels in a wallet app, inspired by the TronLink wallet's community features.
Generated: DETERMINISTIC_5d558afd02f74fb0
Batch ID: 20250612_145916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory data storage (mock database)
channels = [
    {"id": 1, "name": "General Discussion", "description": "Discuss wallet-related topics", "messages": []},
    {"id": 2, "name": "Support", "description": "Get help and support from the community", "messages": []}
]
message_id_counter = 1

@app.route('/channels', methods=['GET'])
def get_channels():
    """
    Endpoint to get the list of community channels.
    """
    return jsonify(channels), 200

@app.route('/channels/<int:channel_id>/messages', methods=['GET'])
def get_channel_messages(channel_id):
    """
    Endpoint to get messages of a specific channel.
    :param channel_id: ID of the channel
    """
    channel = next((c for c in channels if c['id'] == channel_id), None)
    if not channel:
        return jsonify({"error": "Channel not found"}), 404
    return jsonify(channel['messages']), 200

@app.route('/channels/<int:channel_id>/messages', methods=['POST'])
def post_message(channel_id):
    """
    Endpoint to post a message to a specific channel.
    :param channel_id: ID of the channel
    """
    try:
        data = request.get_json()
        user = data.get('user')
        content = data.get('content')

        # Validate input
        if not user or not content:
            return jsonify({"error": "User and content are required"}), 400

        channel = next((c for c in channels if c['id'] == channel_id), None)
        if not channel:
            return jsonify({"error": "Channel not found"}), 404

        global message_id_counter
        message = {
            "id": message_id_counter,
            "user": user,
            "content": content,
            "timestamp": datetime.now().isoformat()
        }
        channel['messages'].append(message)
        message_id_counter += 1

        return jsonify(message), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/channels/<int:channel_id>/messages/<int:message_id>', methods=['DELETE'])
def delete_message(channel_id, message_id):
    """
    Endpoint to delete a message from a specific channel.
    :param channel_id: ID of the channel
    :param message_id: ID of the message
    """
    try:
        channel = next((c for c in channels if c['id'] == channel_id), None)
        if not channel:
            return jsonify({"error": "Channel not found"}), 404

        message = next((m for m in channel['messages'] if m['id'] == message_id), None)
        if not message:
            return jsonify({"error": "Message not found"}), 404

        channel['messages'].remove(message)
        return jsonify({"message": "Message deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```
