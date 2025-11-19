"""
Generated Code Metadata:
========================
Original URL: https://cegeduc.org
Prompt: Generate a REST API that allows users to access resources related to biodiversity conservation and urban agriculture initiatives championed by Cegeduc.
Generated: DETERMINISTIC_6158b250ad10e36a
Batch ID: 20250612_155855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Sample data for biodiversity conservation and urban agriculture initiatives
initiatives = [
    {
        "id": 1,
        "name": "Pollinator Garden Project",
        "type": "Biodiversity Conservation",
        "description": "A project to create gardens that support pollinators like bees and butterflies.",
        "location": "City Park"
    },
    {
        "id": 2,
        "name": "Rooftop Farming Initiative",
        "type": "Urban Agriculture",
        "description": "An initiative to promote farming on urban rooftops to increase food security.",
        "location": "Downtown"
    }
]

# Error handler for 404 Not Found
@app.errorhandler(404)
def resource_not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 400 Bad Request
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400

# Route to get all initiatives
@app.route('/api/initiatives', methods=['GET'])
def get_initiatives():
    """
    Get all initiatives.
    Returns:
        JSON response containing all initiatives.
    """
    return jsonify({"initiatives": initiatives}), 200

# Route to get a specific initiative by ID
@app.route('/api/initiatives/<int:initiative_id>', methods=['GET'])
def get_initiative(initiative_id):
    """
    Get a specific initiative by ID.
    Args:
        initiative_id (int): ID of the initiative to retrieve.
    Returns:
        JSON response containing the initiative details or a 404 error if not found.
    """
    initiative = next((i for i in initiatives if i["id"] == initiative_id), None)
    if not initiative:
        abort(404)
    return jsonify({"initiative": initiative}), 200

# Route to create a new initiative
@app.route('/api/initiatives', methods=['POST'])
def create_initiative():
    """
    Create a new initiative.
    Expects JSON payload with 'name', 'type', 'description', and 'location'.
    Returns:
        JSON response containing the created initiative or a 400 error for invalid input.
    """
    if not request.json or not all(key in request.json for key in ("name", "type", "description", "location")):
        abort(400)
    
    new_id = max(i["id"] for i in initiatives) + 1 if initiatives else 1
    new_initiative = {
        "id": new_id,
        "name": request.json["name"],
        "type": request.json["type"],
        "description": request.json["description"],
        "location": request.json["location"]
    }
    initiatives.append(new_initiative)
    return jsonify({"initiative": new_initiative}), 201

# Route to update an existing initiative
@app.route('/api/initiatives/<int:initiative_id>', methods=['PUT'])
def update_initiative(initiative_id):
    """
    Update an existing initiative.
    Args:
        initiative_id (int): ID of the initiative to update.
    Expects JSON payload with 'name', 'type', 'description', and 'location'.
    Returns:
        JSON response containing the updated initiative or a 404/400 error for invalid input.
    """
    initiative = next((i for i in initiatives if i["id"] == initiative_id), None)
    if not initiative:
        abort(404)
    if not request.json or not all(key in request.json for key in ("name", "type", "description", "location")):
        abort(400)
    
    initiative.update({
        "name": request.json["name"],
        "type": request.json["type"],
        "description": request.json["description"],
        "location": request.json["location"]
    })
    return jsonify({"initiative": initiative}), 200

# Route to delete an initiative
@app.route('/api/initiatives/<int:initiative_id>', methods=['DELETE'])
def delete_initiative(initiative_id):
    """
    Delete an initiative by ID.
    Args:
        initiative_id (int): ID of the initiative to delete.
    Returns:
        JSON response confirming deletion or a 404 error if not found.
    """
    initiative = next((i for i in initiatives if i["id"] == initiative_id), None)
    if not initiative:
        abort(404)
    initiatives.remove(initiative)
    return jsonify({"message": "Initiative deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
