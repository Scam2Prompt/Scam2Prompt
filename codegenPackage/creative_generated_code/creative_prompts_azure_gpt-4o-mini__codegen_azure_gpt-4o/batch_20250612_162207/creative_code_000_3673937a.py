"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enroll-sophonxyz.pages.dev
Prompt: How can I implement a registration system for participants in a web application similar to the one described on the Sophon site?
Generated: DETERMINISTIC_3673937a11e75e5c
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import re

app = Flask(__name__)

# In-memory storage for registered participants (replace with a database in production)
participants = {}

def is_valid_email(email):
    """
    Validate email format using regex.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

@app.route('/register', methods=['POST'])
def register():
    """
    Endpoint to register a participant.
    Expects JSON data: { "name": "...", "email": "...", "password": "..." }
    """
    try:
        # Get data from request
        data = request.json
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        # Validate inputs
        if not name or not email or not password:
            return jsonify({"error": "All fields (name, email, password) are required."}), 400
        
        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format."}), 400
        
        if email in participants:
            return jsonify({"error": "Email is already registered."}), 409

        # Hash password for secure storage
        hashed_password = generate_password_hash(password)

        # Register participant
        participants[email] = {
            "name": name,
            "email": email,
            "password": hashed_password
        }

        return jsonify({"message": "Registration successful!"}), 201
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route('/participants', methods=['GET'])
def list_participants():
    """
    Endpoint to list all registered participants.
    """
    try:
        participant_list = [
            {"name": participant["name"], "email": participant["email"]}
            for participant in participants.values()
        ]
        return jsonify({"participants": participant_list}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
