"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://parallels.top
Prompt: Develop an API that allows users to interact with Avatars in a growing colony simulation, inspired by the "Parallel Colony" concept on the website.
Generated: DETERMINISTIC_0bdcdee47fc1a906
Batch ID: 20250612_155024
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

# In-memory storage for avatars and colonies
colonies = {}

# Utility function to create a unique ID
def generate_id():
    return str(uuid.uuid4())

# Error handling constants
COLONY_NOT_FOUND_ERROR = "Colony not found."
AVATAR_NOT_FOUND_ERROR = "Avatar not found."

# Endpoint to create a new colony
@app.route('/colony', methods=['POST'])
def create_colony():
    """Create a new colony."""
    request_data = request.get_json()
    name = request_data.get("name", "Unnamed Colony")
    colony_id = generate_id()
    colonies[colony_id] = {
        "id": colony_id,
        "name": name,
        "avatars": []
    }
    return jsonify(colonies[colony_id]), 201

# Endpoint to add an avatar to a colony
@app.route('/colony/<colony_id>/avatar', methods=['POST'])
def add_avatar(colony_id):
    """Add a new avatar to a specified colony."""
    if colony_id not in colonies:
        return jsonify({"error": COLONY_NOT_FOUND_ERROR}), 404

    request_data = request.get_json()
    name = request_data.get("name", "Unnamed Avatar")
    role = request_data.get("role", "Worker")
    avatar_id = generate_id()
    avatar = {
        "id": avatar_id,
        "name": name,
        "role": role,
        "stats": {
            "health": 100,
            "energy": 100,
            "experience": 0
        }
    }
    colonies[colony_id]["avatars"].append(avatar)
    return jsonify(avatar), 201

# Endpoint to retrieve details of a colony
@app.route('/colony/<colony_id>', methods=['GET'])
def get_colony(colony_id):
    """Retrieve details of a specific colony."""
    if colony_id not in colonies:
        return jsonify({"error": COLONY_NOT_FOUND_ERROR}), 404

    return jsonify(colonies[colony_id]), 200

# Endpoint to retrieve details of a specific avatar
@app.route('/colony/<colony_id>/avatar/<avatar_id>', methods=['GET'])
def get_avatar(colony_id, avatar_id):
    """Retrieve details of a specific avatar in a colony."""
    if colony_id not in colonies:
        return jsonify({"error": COLONY_NOT_FOUND_ERROR}), 404

    avatars = colonies[colony_id]["avatars"]
    avatar = next((a for a in avatars if a["id"] == avatar_id), None)

    if not avatar:
        return jsonify({"error": AVATAR_NOT_FOUND_ERROR}), 404

    return jsonify(avatar), 200

# Endpoint to update an avatar's attributes
@app.route('/colony/<colony_id>/avatar/<avatar_id>', methods=['PUT'])
def update_avatar(colony_id, avatar_id):
    """Update attributes of an avatar in a colony."""
    if colony_id not in colonies:
        return jsonify({"error": COLONY_NOT_FOUND_ERROR}), 404

    avatars = colonies[colony_id]["avatars"]
    avatar = next((a for a in avatars if a["id"] == avatar_id), None)

    if not avatar:
        return jsonify({"error": AVATAR_NOT_FOUND_ERROR}), 404

    request_data = request.get_json()
    avatar["name"] = request_data.get("name", avatar["name"])
    avatar["role"] = request_data.get("role", avatar["role"])
    avatar["stats"]["health"] = request_data.get("health", avatar["stats"]["health"])
    avatar["stats"]["energy"] = request_data.get("energy", avatar["stats"]["energy"])
    avatar["stats"]["experience"] = request_data.get("experience", avatar["stats"]["experience"])

    return jsonify(avatar), 200

# Endpoint to delete an avatar from a colony
@app.route('/colony/<colony_id>/avatar/<avatar_id>', methods=['DELETE'])
def delete_avatar(colony_id, avatar_id):
    """Delete an avatar from a colony."""
    if colony_id not in colonies:
        return jsonify({"error": COLONY_NOT_FOUND_ERROR}), 404

    avatars = colonies[colony_id]["avatars"]
    avatar = next((a for a in avatars if a["id"] == avatar_id), None)

    if not avatar:
        return jsonify({"error": AVATAR_NOT_FOUND_ERROR}), 404

    colonies[colony_id]["avatars"].remove(avatar)
    return jsonify({"message": "Avatar deleted successfully."}), 200

# Endpoint to delete a colony along with all its avatars
@app.route('/colony/<colony_id>', methods=['DELETE'])
def delete_colony(colony_id):
    """Delete a colony and all its associated avatars."""
    if colony_id not in colonies:
        return jsonify({"error": COLONY_NOT_FOUND_ERROR}), 404
    
    del colonies[colony_id]
    return jsonify({"message": "Colony deleted successfully."}), 200

# Endpoint to list all colonies
@app.route('/colonies', methods=['GET'])
def list_colonies():
    """List all colonies."""
    return jsonify(list(colonies.values())), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
