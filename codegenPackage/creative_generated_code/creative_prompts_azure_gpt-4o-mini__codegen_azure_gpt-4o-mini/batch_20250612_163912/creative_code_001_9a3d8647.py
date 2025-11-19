"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.eharmony.co.uk
Prompt: How can I implement a user registration API for a dating app similar to eharmony that includes gender specification and password compliance?
Generated: DETERMINISTIC_9a3d864785fabe0b
Batch ID: 20250612_163912
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

# Define a user schema for validation
class UserSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True, validate=lambda p: len(p) >= 8 and re.search(r'\d', p) and re.search(r'[A-Z]', p))
    gender = fields.Str(required=True, validate=lambda g: g in ['Male', 'Female', 'Other'])

# In-memory user storage (for demonstration purposes, use a database in production)
users = []

@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a new user with gender specification and password compliance.
    Request should include username, password, and gender.
    """
    try:
        # Validate input data using UserSchema
        user_schema = UserSchema()
        user_data = user_schema.load(request.json)

        # Hash the user's password
        hashed_password = generate_password_hash(user_data['password'])

        # Create user record
        user_record = {
            'username': user_data['username'],
            'password': hashed_password,
            'gender': user_data['gender']
        }

        # Store user record
        users.append(user_record)

        # Return success response
        return jsonify({"message": "User registered successfully"}), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
