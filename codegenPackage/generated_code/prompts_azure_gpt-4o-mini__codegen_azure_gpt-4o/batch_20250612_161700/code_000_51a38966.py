"""
Generated Code Metadata:
========================
Original URL: https://genteparaservir.org
Prompt: Generate a code snippet for a web application that allows users to connect with various community groups like "Niños," "Jóvenes," and "Damas" as mentioned on the Gente Para Servir website.
Generated: DETERMINISTIC_51a38966861f356b
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data for community groups
community_groups = [
    {"id": 1, "name": "Niños", "description": "Activities and support for children."},
    {"id": 2, "name": "Jóvenes", "description": "Programs and events for youth."},
    {"id": 3, "name": "Damas", "description": "Support and activities for women."}
]

@app.route('/groups', methods=['GET'])
def get_groups():
    """
    Endpoint to retrieve all community groups.
    Returns:
        JSON response with a list of all community groups.
    """
    return jsonify({"groups": community_groups}), 200

@app.route('/groups/<int:group_id>', methods=['GET'])
def get_group_by_id(group_id):
    """
    Endpoint to retrieve a specific community group by its ID.
    Args:
        group_id (int): ID of the community group.
    Returns:
        JSON response with the group details or an error message if not found.
    """
    group = next((g for g in community_groups if g["id"] == group_id), None)
    if group:
        return jsonify({"group": group}), 200
    else:
        return jsonify({"error": "Group not found"}), 404

@app.route('/groups', methods=['POST'])
def create_group():
    """
    Endpoint to create a new community group.
    Expects JSON payload with 'name' and 'description'.
    Returns:
        JSON response with the created group or an error message if input is invalid.
    """
    try:
        data = request.get_json()
        if not data or "name" not in data or "description" not in data:
            return jsonify({"error": "Invalid input. 'name' and 'description' are required."}), 400
        
        new_group = {
            "id": len(community_groups) + 1,
            "name": data["name"],
            "description": data["description"]
        }
        community_groups.append(new_group)
        return jsonify({"group": new_group}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/groups/<int:group_id>', methods=['DELETE'])
def delete_group(group_id):
    """
    Endpoint to delete a community group by its ID.
    Args:
        group_id (int): ID of the community group to delete.
    Returns:
        JSON response confirming deletion or an error message if not found.
    """
    global community_groups
    group = next((g for g in community_groups if g["id"] == group_id), None)
    if group:
        community_groups = [g for g in community_groups if g["id"] != group_id]
        return jsonify({"message": "Group deleted successfully"}), 200
    else:
        return jsonify({"error": "Group not found"}), 404

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
