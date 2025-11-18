"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.izikard.com
Prompt: Create a REST API for managing NFC tag configurations, allowing users to update actions like redirecting to a webpage or collecting reviews, inspired by Izikard's web app.
Generated: DETERMINISTIC_5a3ac436201912c8
Batch ID: 20250612_153224
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

# In-memory database to store NFC tag configurations
nfc_tags = {}

@app.route('/nfc-tags', methods=['GET'])
def get_all_tags():
    """
    Endpoint to retrieve all NFC tag configurations.
    """
    return jsonify(nfc_tags), 200

@app.route('/nfc-tags/<tag_id>', methods=['GET'])
def get_tag(tag_id):
    """
    Endpoint to retrieve a specific NFC tag configuration by ID.
    """
    tag = nfc_tags.get(tag_id)
    if not tag:
        return jsonify({"error": "Tag not found"}), 404
    return jsonify(tag), 200

@app.route('/nfc-tags', methods=['POST'])
def create_tag():
    """
    Endpoint to create a new NFC tag configuration.
    Requires a JSON body with 'action_type' and 'action_data'.
    """
    try:
        data = request.json
        if 'action_type' not in data or 'action_data' not in data:
            return jsonify({"error": "Invalid data. 'action_type' and 'action_data' are required."}), 400

        tag_id = str(uuid.uuid4())  # Generate a unique ID for the tag
        nfc_tags[tag_id] = {
            'id': tag_id,
            'action_type': data['action_type'],
            'action_data': data['action_data']
        }
        return jsonify(nfc_tags[tag_id]), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/nfc-tags/<tag_id>', methods=['PUT'])
def update_tag(tag_id):
    """
    Endpoint to update an existing NFC tag configuration by ID.
    Requires a JSON body with optional 'action_type' and/or 'action_data'.
    """
    try:
        tag = nfc_tags.get(tag_id)
        if not tag:
            return jsonify({"error": "Tag not found"}), 404

        data = request.json
        if 'action_type' in data:
            tag['action_type'] = data['action_type']
        if 'action_data' in data:
            tag['action_data'] = data['action_data']

        nfc_tags[tag_id] = tag
        return jsonify(tag), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/nfc-tags/<tag_id>', methods=['DELETE'])
def delete_tag(tag_id):
    """
    Endpoint to delete an NFC tag configuration by ID.
    """
    tag = nfc_tags.pop(tag_id, None)
    if not tag:
        return jsonify({"error": "Tag not found"}), 404
    return jsonify({"message": "Tag deleted successfully"}), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
