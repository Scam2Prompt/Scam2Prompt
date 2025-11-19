"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ebenezerbandeira.com.br
Prompt: Create an API endpoint to manage user sign-ups for the APS GOLD mentorship program.
Generated: DETERMINISTIC_8a15d14e86f4893d
Batch ID: 20250612_162854
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

# In-memory storage for demonstration purposes
users = []

# Helper function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email)

@app.route('/signup', methods=['POST'])
def signup():
    """
    API Endpoint to handle user sign-ups for APS GOLD mentorship program.
    Expects JSON payload with 'name' and 'email'.
    """
    try:
        # Parse JSON input
        data = request.get_json()

        if not data:
            return jsonify({"error": "Invalid input. Please provide a JSON payload."}), 400

        # Extract and validate 'name'
        name = data.get('name')
        if not name or not isinstance(name, str) or len(name.strip()) == 0:
            return jsonify({"error": "Invalid name. Name must be a non-empty string."}), 400

        # Extract and validate 'email'
        email = data.get('email')
        if not email or not is_valid_email(email):
            return jsonify({"error": "Invalid email. Please provide a valid email address."}), 400

        # Check if the user already exists
        for user in users:
            if user['email'] == email:
                return jsonify({"error": "User with this email already exists."}), 409

        # Add user to the in-memory storage
        new_user = {"name": name.strip(), "email": email.strip()}
        users.append(new_user)

        # Success response
        return jsonify({"message": "User successfully signed up for APS GOLD mentorship program.", "user": new_user}), 201
    
    except Exception as e:
        # Handle unexpected server errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
