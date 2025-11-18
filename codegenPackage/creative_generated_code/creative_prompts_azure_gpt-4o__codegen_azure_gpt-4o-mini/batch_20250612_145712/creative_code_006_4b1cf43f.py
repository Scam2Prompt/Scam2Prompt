"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://microlab.world
Prompt: Provide an example of an API endpoint for user registration in a service similar to MicroLab, including validation for username and password.
Generated: DETERMINISTIC_4b1cf43fb4b8a5a1
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash
from marshmallow import Schema, fields, ValidationError
import re

app = Flask(__name__)

# Schema for validating user input
class UserSchema(Schema):
    username = fields.Str(required=True, validate=lambda s: len(s) >= 3)
    password = fields.Str(required=True, validate=lambda s: len(s) >= 6)

# In-memory user storage (for demonstration purposes)
users_db = {}

def is_username_taken(username):
    """Check if the username is already taken in the database."""
    return username in users_db

@app.route('/register', methods=['POST'])
def register():
    """
    User registration endpoint.
    Expects a JSON payload with 'username' and 'password'.
    Returns a success message or an error response.
    """
    # Validate the incoming data against the schema
    schema = UserSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    username = data['username']
    password = data['password']

    # Check if the username is already taken
    if is_username_taken(username):
        return jsonify({"error": "Username already exists."}), 409

    # Hash the password for secure storage
    hashed_password = generate_password_hash(password)

    # Store the new user in the database
    users_db[username] = hashed_password

    return jsonify({"message": "User registered successfully."}), 201

if __name__ == '__main__':
    app.run(debug=True)
```
