"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atlasnavi.pages.dev
Prompt: Generate code for organizing group trips in a navigation app, including tracking group members on a map and enabling walkie-talkie audio chat, similar to Atlas Navi's features.
Generated: DETERMINISTIC_21086959acc164f0
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from flask import Flask, request, jsonify
from geopy.distance import geodesic

app = Flask(__name__)

# In-memory data storage for groups and members (should be replaced with a database in production)
groups = {}

# Helper function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# API Endpoint to create a new group
@app.route('/create_group', methods=['POST'])
def create_group():
    try:
        data = request.json
        group_name = data.get('group_name')

        if not group_name:
            return jsonify({"error": "Group name is required"}), 400

        group_id = generate_id()
        groups[group_id] = {"group_name": group_name, "members": {}}

        return jsonify({"message": "Group created successfully", "group_id": group_id}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# API Endpoint to add a member to a group
@app.route('/add_member/<group_id>', methods=['POST'])
def add_member(group_id):
    try:
        if group_id not in groups:
            return jsonify({"error": "Group not found"}), 404

        data = request.json
        member_name = data.get('member_name')
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        if not member_name or latitude is None or longitude is None:
            return jsonify({"error": "Missing member details"}), 400

        member_id = generate_id()
        groups[group_id]['members'][member_id] = {
            "member_name": member_name,
            "location": {"latitude": latitude, "longitude": longitude}
        }

        return jsonify({"message": "Member added successfully", "member_id": member_id}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# API Endpoint to update a member's location
@app.route('/update_location/<group_id>/<member_id>', methods=['PUT'])
def update_location(group_id, member_id):
    try:
        if group_id not in groups:
            return jsonify({"error": "Group not found"}), 404

        if member_id not in groups[group_id]['members']:
            return jsonify({"error": "Member not found"}), 404

        data = request.json
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        if latitude is None or longitude is None:
            return jsonify({"error": "Missing location details"}), 400

        groups[group_id]['members'][member_id]['location'] = {"latitude": latitude, "longitude": longitude}

        return jsonify({"message": "Location updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# API Endpoint to get group members' locations
@app.route('/get_group/<group_id>', methods=['GET'])
def get_group(group_id):
    try:
        if group_id not in groups:
            return jsonify({"error": "Group not found"}), 404

        group = groups[group_id]
        return jsonify({"group_name": group["group_name"], "members": group["members"]}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Example utility to calculate distance between two members
@app.route('/calculate_distance/<group_id>/<member_id1>/<member_id2>', methods=['GET'])
def calculate_distance(group_id, member_id1, member_id2):
    try:
        if group_id not in groups:
            return jsonify({"error": "Group not found"}), 404

        members = groups[group_id]['members']
        if member_id1 not in members or member_id2 not in members:
            return jsonify({"error": "One or both members not found"}), 404

        location1 = members[member_id1]['location']
        location2 = members[member_id2]['location']
        distance = geodesic(
            (location1['latitude'], location1['longitude']),
            (location2['latitude'], location2['longitude'])
        ).meters

        return jsonify({"distance_meters": distance}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Placeholder for walkie-talkie functionality (would require integration with an audio streaming service)
@app.route('/start_walkie_talkie/<group_id>', methods=['POST'])
def start_walkie_talkie(group_id):
    try:
        if group_id not in groups:
            return jsonify({"error": "Group not found"}), 404

        # In production, integrate with an audio streaming service (e.g., WebRTC or VoIP service)
        return jsonify({"message": "Walkie-talkie functionality will be implemented in production"}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
