"""
Generated Code Metadata:
========================
Original URL: https://www.thompsonestateathletics.com.au
Prompt: Develop an API endpoint for managing membership registrations and inquiries for a running club, similar to the features offered by Thompson Estate Athletics.
Generated: DETERMINISTIC_f91270ead353990f
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for demonstration purposes
members = []

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

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Endpoint to register a new member
@app.route('/api/members/register', methods=['POST'])
def register_member():
    try:
        # Parse and validate input data
        data = request.get_json()
        if not data or 'name' not in data or 'email' not in data:
            return jsonify({"error": "Bad Request", "message": "Name and email are required"}), 400
        
        # Check for duplicate email
        if any(member['email'] == data['email'] for member in members):
            return jsonify({"error": "Conflict", "message": "Email already registered"}), 409
        
        # Add new member to the database
        new_member = {
            "id": len(members) + 1,
            "name": data['name'],
            "email": data['email']
        }
        members.append(new_member)
        
        return jsonify({"message": "Member registered successfully", "member": new_member}), 201
    except Exception as e:
        return handle_generic_exception(e)

# Endpoint to inquire about all members
@app.route('/api/members', methods=['GET'])
def get_members():
    try:
        return jsonify({"members": members}), 200
    except Exception as e:
        return handle_generic_exception(e)

# Endpoint to inquire about a specific member by ID
@app.route('/api/members/<int:member_id>', methods=['GET'])
def get_member_by_id(member_id):
    try:
        # Find member by ID
        member = next((m for m in members if m['id'] == member_id), None)
        if not member:
            return jsonify({"error": "Not Found", "message": "Member not found"}), 404
        
        return jsonify({"member": member}), 200
    except Exception as e:
        return handle_generic_exception(e)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
