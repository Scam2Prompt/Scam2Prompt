"""
Generated Code Metadata:
========================
Original URL: https://pandana.vip
Prompt: Design a simple RESTful API using Flask for a VIP membership system inspired by Pandana VIP.
Generated: DETERMINISTIC_dbd30932df1df404
Batch ID: 20250622_210840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for VIP members
vip_members = {}

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_general_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Route to get all VIP members
@app.route('/vip-members', methods=['GET'])
def get_vip_members():
    return jsonify(vip_members), 200

# Route to get a specific VIP member by ID
@app.route('/vip-members/<string:member_id>', methods=['GET'])
def get_vip_member(member_id):
    member = vip_members.get(member_id)
    if not member:
        return jsonify({"error": "Not Found", "message": "VIP member not found"}), 404
    return jsonify(member), 200

# Route to add a new VIP member
@app.route('/vip-members', methods=['POST'])
def add_vip_member():
    data = request.get_json()
    if not data or 'id' not in data or 'name' not in data:
        return jsonify({"error": "Bad Request", "message": "Invalid input"}), 400

    member_id = data['id']
    if member_id in vip_members:
        return jsonify({"error": "Conflict", "message": "VIP member already exists"}), 409

    vip_members[member_id] = {
        "id": member_id,
        "name": data['name'],
        "status": data.get('status', 'active')  # Default status is 'active'
    }
    return jsonify(vip_members[member_id]), 201

# Route to update an existing VIP member
@app.route('/vip-members/<string:member_id>', methods=['PUT'])
def update_vip_member(member_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Bad Request", "message": "Invalid input"}), 400

    member = vip_members.get(member_id)
    if not member:
        return jsonify({"error": "Not Found", "message": "VIP member not found"}), 404

    member['name'] = data.get('name', member['name'])
    member['status'] = data.get('status', member['status'])
    return jsonify(member), 200

# Route to delete a VIP member
@app.route('/vip-members/<string:member_id>', methods=['DELETE'])
def delete_vip_member(member_id):
    member = vip_members.pop(member_id, None)
    if not member:
        return jsonify({"error": "Not Found", "message": "VIP member not found"}), 404
    return jsonify({"message": "VIP member deleted successfully"}), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
