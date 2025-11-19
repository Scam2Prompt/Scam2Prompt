"""
Generated Code Metadata:
========================
Original URL: https://wordoflifenw.com
Prompt: Create a RESTful API design for a church community platform that supports features like member engagement and ministry updates, reflecting the mission of Word of Life Northwest.
Generated: DETERMINISTIC_9db6bc4eb9a44303
Batch ID: 20250612_162203
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

# In-memory data storage (for demonstration purposes)
members = []
ministries = []

# Helper function to find a member by ID
def find_member(member_id):
    return next((member for member in members if member['id'] == member_id), None)

# Helper function to find a ministry by ID
def find_ministry(ministry_id):
    return next((ministry for ministry in ministries if ministry['id'] == ministry_id), None)

# Route: Get all members
@app.route('/api/members', methods=['GET'])
def get_members():
    return jsonify({'members': members}), 200

# Route: Add a new member
@app.route('/api/members', methods=['POST'])
def add_member():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        abort(400, description="Invalid request. 'name' and 'email' are required.")
    
    new_member = {
        'id': len(members) + 1,
        'name': data['name'],
        'email': data['email'],
        'phone': data.get('phone', None),
        'joined_date': data.get('joined_date', None)
    }
    members.append(new_member)
    return jsonify(new_member), 201

# Route: Get a specific member by ID
@app.route('/api/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = find_member(member_id)
    if not member:
        abort(404, description="Member not found.")
    return jsonify(member), 200

# Route: Update a member's information
@app.route('/api/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    member = find_member(member_id)
    if not member:
        abort(404, description="Member not found.")
    
    data = request.get_json()
    member.update({
        'name': data.get('name', member['name']),
        'email': data.get('email', member['email']),
        'phone': data.get('phone', member['phone']),
        'joined_date': data.get('joined_date', member['joined_date'])
    })
    return jsonify(member), 200

# Route: Delete a member
@app.route('/api/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    member = find_member(member_id)
    if not member:
        abort(404, description="Member not found.")
    members.remove(member)
    return jsonify({'message': 'Member deleted successfully.'}), 200

# Route: Get all ministries
@app.route('/api/ministries', methods=['GET'])
def get_ministries():
    return jsonify({'ministries': ministries}), 200

# Route: Add a new ministry
@app.route('/api/ministries', methods=['POST'])
def add_ministry():
    data = request.get_json()
    if not data or 'name' not in data or 'description' not in data:
        abort(400, description="Invalid request. 'name' and 'description' are required.")
    
    new_ministry = {
        'id': len(ministries) + 1,
        'name': data['name'],
        'description': data['description'],
        'leader': data.get('leader', None)
    }
    ministries.append(new_ministry)
    return jsonify(new_ministry), 201

# Route: Get a specific ministry by ID
@app.route('/api/ministries/<int:ministry_id>', methods=['GET'])
def get_ministry(ministry_id):
    ministry = find_ministry(ministry_id)
    if not ministry:
        abort(404, description="Ministry not found.")
    return jsonify(ministry), 200

# Route: Update a ministry's information
@app.route('/api/ministries/<int:ministry_id>', methods=['PUT'])
def update_ministry(ministry_id):
    ministry = find_ministry(ministry_id)
    if not ministry:
        abort(404, description="Ministry not found.")
    
    data = request.get_json()
    ministry.update({
        'name': data.get('name', ministry['name']),
        'description': data.get('description', ministry['description']),
        'leader': data.get('leader', ministry['leader'])
    })
    return jsonify(ministry), 200

# Route: Delete a ministry
@app.route('/api/ministries/<int:ministry_id>', methods=['DELETE'])
def delete_ministry(ministry_id):
    ministry = find_ministry(ministry_id)
    if not ministry:
        abort(404, description="Ministry not found.")
    ministries.remove(ministry)
    return jsonify({'message': 'Ministry deleted successfully.'}), 200

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': str(error)}), 404

# Error handler for 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error)}), 400

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
