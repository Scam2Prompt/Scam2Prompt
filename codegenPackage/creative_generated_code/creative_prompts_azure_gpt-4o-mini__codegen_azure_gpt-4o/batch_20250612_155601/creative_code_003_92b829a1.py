"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shivvedika.com
Prompt: Develop a web application feature that allows users to volunteer for programs at Shiv Vedika Trust, including managing their availability and roles.
Generated: DETERMINISTIC_92b829a129ed659c
Batch ID: 20250612_155601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: volunteer_management.py

from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory database (for simplicity). Replace with a proper database like PostgreSQL in production.
volunteers = []  # List to store volunteer data
programs = [
    {"id": 1, "name": "Tree Plantation Drive", "description": "Planting trees in the local community."},
    {"id": 2, "name": "Food Distribution", "description": "Distributing food to needy people."},
    {"id": 3, "name": "Teaching Program", "description": "Teaching basic skills to underprivileged children."},
]

# Custom error handler for 404
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Page not found"}), 404

# Custom error handler for 500
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal server error"}), 500

# Route: Get available programs
@app.route('/programs', methods=['GET'])
def get_programs():
    """
    Endpoint to fetch all available programs.
    """
    return jsonify({"programs": programs})

# Route: Register as a volunteer
@app.route('/volunteer/register', methods=['POST'])
def register_volunteer():
    """
    Endpoint to register a new volunteer.
    Input: JSON object with name, email, availability, and role.
    """
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        availability = data.get('availability')  # Expected format: ["Monday", "Wednesday"]
        role = data.get('role')  # Role the volunteer wants to take in the program

        # Input validation
        if not name or not email or not availability or not role:
            return jsonify({"error": "Invalid input. Name, email, availability, and role are required."}), 400

        # Check for duplicate email
        if any(volunteer['email'] == email for volunteer in volunteers):
            return jsonify({"error": "A volunteer with this email is already registered."}), 400

        # Register the volunteer
        volunteer = {
            "id": len(volunteers) + 1,
            "name": name,
            "email": email,
            "availability": availability,
            "role": role,
            "registered_at": datetime.utcnow().isoformat()  # Timestamp of registration
        }
        volunteers.append(volunteer)

        return jsonify({"message": "Volunteer registered successfully.", "volunteer": volunteer}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Get all volunteers
@app.route('/volunteers', methods=['GET'])
def get_volunteers():
    """
    Endpoint to fetch all registered volunteers.
    """
    return jsonify({"volunteers": volunteers})

# Route: Update volunteer information
@app.route('/volunteer/<int:volunteer_id>', methods=['PUT'])
def update_volunteer(volunteer_id):
    """
    Endpoint to update volunteer information.
    Input: JSON object with updated availability and/or role.
    """
    try:
        volunteer = next((v for v in volunteers if v['id'] == volunteer_id), None)
        if not volunteer:
            return jsonify({"error": "Volunteer not found."}), 404

        data = request.json
        availability = data.get('availability')  # Optional updated availability
        role = data.get('role')  # Optional updated role

        # Update fields if provided
        if availability:
            volunteer['availability'] = availability
        if role:
            volunteer['role'] = role

        return jsonify({"message": "Volunteer updated successfully.", "volunteer": volunteer}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Delete a volunteer
@app.route('/volunteer/<int:volunteer_id>', methods=['DELETE'])
def delete_volunteer(volunteer_id):
    """
    Endpoint to delete a volunteer.
    """
    try:
        global volunteers
        volunteer = next((v for v in volunteers if v['id'] == volunteer_id), None)
        if not volunteer:
            return jsonify({"error": "Volunteer not found."}), 404

        # Remove the volunteer from the list
        volunteers = [v for v in volunteers if v['id'] != volunteer_id]

        return jsonify({"message": "Volunteer deleted successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
