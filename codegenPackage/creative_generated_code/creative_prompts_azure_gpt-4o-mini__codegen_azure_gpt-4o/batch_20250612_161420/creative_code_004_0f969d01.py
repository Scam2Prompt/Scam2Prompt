"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://play-sop.pages.dev
Prompt: Provide a code example that shows how to manage participant connections in a web app, based on the participant details from the Sophon Time webpage.
Generated: DETERMINISTIC_0f969d0123f93f27
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory store for participant connections
participant_connections = {}

# Helper function to validate participant data
def validate_participant_data(data):
    required_fields = ["name", "email", "connection_status"]
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    return True, None

# Endpoint to add a new participant connection
@app.route('/participants', methods=['POST'])
def add_participant():
    try:
        participant_data = request.json

        # Validate incoming data
        is_valid, error_message = validate_participant_data(participant_data)
        if not is_valid:
            return jsonify({"error": error_message}), 400

        # Generate a unique ID for the participant
        participant_id = str(uuid.uuid4())
        participant_connections[participant_id] = {
            "name": participant_data["name"],
            "email": participant_data["email"],
            "connection_status": participant_data["connection_status"]
        }

        return jsonify({"message": "Participant added successfully", "participant_id": participant_id}), 201
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Endpoint to list all participant connections
@app.route('/participants', methods=['GET'])
def list_participants():
    try:
        return jsonify(participant_connections), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Endpoint to update a participant connection
@app.route('/participants/<participant_id>', methods=['PUT'])
def update_participant(participant_id):
    try:
        if participant_id not in participant_connections:
            return jsonify({"error": "Participant not found"}), 404

        update_data = request.json

        # Validate incoming data
        is_valid, error_message = validate_participant_data(update_data)
        if not is_valid:
            return jsonify({"error": error_message}), 400

        # Update participant details
        participant_connections[participant_id].update(update_data)
        return jsonify({"message": "Participant updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Endpoint to delete a participant connection
@app.route('/participants/<participant_id>', methods=['DELETE'])
def delete_participant(participant_id):
    try:
        if participant_id not in participant_connections:
            return jsonify({"error": "Participant not found"}), 404

        # Remove participant from the store
        del participant_connections[participant_id]
        return jsonify({"message": "Participant deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Run the Flask web app
if __name__ == '__main__':
    app.run(debug=True)
```
