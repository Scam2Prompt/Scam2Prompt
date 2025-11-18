"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globallinknext.com
Prompt: Write code to implement a roundtable discussion feature for a conference platform, inspired by the interactive demos at GlobalLink NEXT.
Generated: DETERMINISTIC_b2842c9f1c57c47c
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Roundtable Discussion Feature for a Conference Platform

This Python code implements a basic roundtable discussion feature using Flask
(a lightweight web framework). The feature allows users to join, leave, and 
view information about a discussion, with backend support for managing participants.
The code follows best practices and includes proper error handling.
"""

from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# In-memory storage for roundtable discussions
# Example structure: {"discussion_id": {"name": "Topic", "participants": []}}
roundtable_discussions = {}

# Error messages
ERROR_DISCUSSION_NOT_FOUND = {"error": "Discussion not found"}
ERROR_PARTICIPANT_NOT_FOUND = {"error": "Participant not found"}

# Utility function to generate unique IDs
def generate_id():
    return str(uuid4())


@app.route('/create_discussion', methods=['POST'])
def create_discussion():
    """
    Endpoint to create a new roundtable discussion.
    Payload should include 'name': Name of the discussion.
    """
    data = request.json
    if not data or 'name' not in data:
        return jsonify({"error": "Invalid payload"}), 400

    discussion_id = generate_id()
    roundtable_discussions[discussion_id] = {
        "name": data['name'],
        "participants": []
    }

    return jsonify({"message": "Discussion created", "discussion_id": discussion_id}), 201


@app.route('/join_discussion/<discussion_id>', methods=['POST'])
def join_discussion(discussion_id):
    """
    Endpoint for a user to join a discussion.
    Payload should include 'participant_name': Name of the participant.
    """
    data = request.json
    if not data or 'participant_name' not in data:
        return jsonify({"error": "Invalid payload"}), 400

    discussion = roundtable_discussions.get(discussion_id)
    if not discussion:
        return jsonify(ERROR_DISCUSSION_NOT_FOUND), 404

    participant_id = generate_id()
    discussion['participants'].append({
        "id": participant_id,
        "name": data['participant_name']
    })

    return jsonify({"message": "Participant joined", "participant_id": participant_id}), 200


@app.route('/leave_discussion/<discussion_id>/<participant_id>', methods=['DELETE'])
def leave_discussion(discussion_id, participant_id):
    """
    Endpoint for a user to leave a discussion.
    """
    discussion = roundtable_discussions.get(discussion_id)
    if not discussion:
        return jsonify(ERROR_DISCUSSION_NOT_FOUND), 404

    participant = next((p for p in discussion['participants'] if p['id'] == participant_id), None)
    if not participant:
        return jsonify(ERROR_PARTICIPANT_NOT_FOUND), 404

    discussion['participants'].remove(participant)
    return jsonify({"message": "Participant removed"}), 200


@app.route('/get_discussion/<discussion_id>', methods=['GET'])
def get_discussion(discussion_id):
    """
    Endpoint to fetch information about a discussion.
    """
    discussion = roundtable_discussions.get(discussion_id)
    if not discussion:
        return jsonify(ERROR_DISCUSSION_NOT_FOUND), 404

    return jsonify(discussion), 200


@app.route('/list_discussions', methods=['GET'])
def list_discussions():
    """
    Endpoint to list all available discussions.
    """
    return jsonify(roundtable_discussions), 200


# Error handling for 404 routes
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Endpoint not found"}), 404


# Main entry point for running the application
if __name__ == '__main__':
    app.run(debug=True)
```
