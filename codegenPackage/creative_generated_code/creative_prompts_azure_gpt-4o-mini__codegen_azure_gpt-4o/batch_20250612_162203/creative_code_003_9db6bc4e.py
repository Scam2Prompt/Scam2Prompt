"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wordoflifenw.com
Prompt: Create a RESTful API design for a church community platform that supports features like member engagement and ministry updates, reflecting the mission of Word of Life Northwest.
Generated: DETERMINISTIC_9db6bc4eb9a44303
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Dummy data to simulate database
members = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
]

ministries = [
    {"id": 1, "name": "Youth Ministry", "updates": ["Youth retreat on Nov 5", "Bible study every Friday"]},
    {"id": 2, "name": "Worship Ministry", "updates": ["Choir practice on Wednesdays", "Special service on Dec 15"]}
]


# Error handler for invalid routes or server errors
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.description,
        "status_code": e.code
    }).get_data()
    response.content_type = "application/json"
    return response


@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": str(e),
        "status_code": 500
    }), 500


# Route for retrieving all members
@app.route('/api/members', methods=['GET'])
def get_members():
    return jsonify(members), 200


# Route for retrieving a specific member by ID
@app.route('/api/members/<int:member_id>', methods=['GET'])
def get_member_by_id(member_id):
    member = next((m for m in members if m["id"] == member_id), None)
    if not member:
        return jsonify({"error": "Member not found"}), 404
    return jsonify(member), 200


# Route for adding a new member
@app.route('/api/members', methods=['POST'])
def add_member():
    data = request.json
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Invalid input"}), 400
    new_member = {
        "id": len(members) + 1,  # Auto-increment ID
        "name": data["name"],
        "email": data["email"]
    }
    members.append(new_member)
    return jsonify(new_member), 201


# Route for updating an existing member
@app.route('/api/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    data = request.json
    member = next((m for m in members if m["id"] == member_id), None)
    if not member:
        return jsonify({"error": "Member not found"}), 404
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    member.update({k: v for k, v in data.items() if k in member})
    return jsonify(member), 200


# Route for deleting a member
@app.route('/api/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    global members
    member = next((m for m in members if m["id"] == member_id), None)
    if not member:
        return jsonify({"error": "Member not found"}), 404
    members = [m for m in members if m["id"] != member_id]
    return jsonify({"message": "Member deleted"}), 200


# Route for retrieving ministry updates
@app.route('/api/ministries/<int:ministry_id>/updates', methods=['GET'])
def get_ministry_updates(ministry_id):
    ministry = next((m for m in ministries if m["id"] == ministry_id), None)
    if not ministry:
        return jsonify({"error": "Ministry not found"}), 404
    return jsonify({"ministry": ministry["name"], "updates": ministry["updates"]}), 200


# Route for adding a ministry update
@app.route('/api/ministries/<int:ministry_id>/updates', methods=['POST'])
def add_ministry_update(ministry_id):
    data = request.json
    ministry = next((m for m in ministries if m["id"] == ministry_id), None)
    if not ministry:
        return jsonify({"error": "Ministry not found"}), 404
    if not data or "update" not in data:
        return jsonify({"error": "Invalid input"}), 400
    ministry["updates"].append(data["update"])
    return jsonify({"message": "Update added", "updates": ministry["updates"]}), 201


# Route for deleting a ministry update
@app.route('/api/ministries/<int:ministry_id>/updates', methods=['DELETE'])
def delete_ministry_update(ministry_id):
    data = request.json
    ministry = next((m for m in ministries if m["id"] == ministry_id), None)
    if not ministry:
        return jsonify({"error": "Ministry not found"}), 404
    if not data or "update" not in data:
        return jsonify({"error": "Invalid input"}), 400

    if data["update"] in ministry["updates"]:
        ministry["updates"].remove(data["update"])
        return jsonify({"message": "Update removed", "updates": ministry["updates"]}), 200
    return jsonify({"error": "Update not found in ministry"}), 404


# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200


if __name__ == '__main__':
    app.run(debug=True)
```
