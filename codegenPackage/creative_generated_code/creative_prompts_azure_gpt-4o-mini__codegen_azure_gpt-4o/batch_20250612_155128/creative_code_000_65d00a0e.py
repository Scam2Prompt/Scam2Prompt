"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ogma.ca
Prompt: Generate a code snippet for a web application that allows users to register for the OGMA Spring Golf Tournament, including fields for name, email, and golf skill level.
Generated: DETERMINISTIC_65d00a0e82754e75
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# In-memory storage for registered users (in production, this would be a database)
registered_users = []

# Helper function to validate email
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# Helper function to validate skill level
def is_valid_skill_level(skill_level):
    valid_levels = ['Beginner', 'Intermediate', 'Advanced']
    return skill_level in valid_levels

@app.route('/register', methods=['POST'])
def register():
    """
    Endpoint for registering for the OGMA Spring Golf Tournament.
    Expected JSON payload:
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "skill_level": "Intermediate"
    }
    """
    try:
        # Parse request data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request format."}), 400

        # Extract fields
        name = data.get('name')
        email = data.get('email')
        skill_level = data.get('skill_level')

        # Validate fields
        if not name or not isinstance(name, str) or len(name.strip()) == 0:
            return jsonify({"error": "Name is required and must be a non-empty string."}), 400
        if not email or not is_valid_email(email):
            return jsonify({"error": "A valid email address is required."}), 400
        if not skill_level or not is_valid_skill_level(skill_level):
            return jsonify({"error": "Skill level must be one of ['Beginner', 'Intermediate', 'Advanced']."}), 400

        # Check for duplicate email registration
        if any(user['email'] == email for user in registered_users):
            return jsonify({"error": f"Email {email} is already registered."}), 409

        # Store registration
        registered_users.append({
            "name": name,
            "email": email,
            "skill_level": skill_level
        })

        # Return success response
        return jsonify({"message": f"{name} has been successfully registered for the OGMA Spring Golf Tournament."}), 201

    except Exception as e:
        # Generic error handler
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route('/registrations', methods=['GET'])
def list_registrations():
    """
    Endpoint to retrieve all registrations for the tournament.
    """
    return jsonify(registered_users), 200

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```
