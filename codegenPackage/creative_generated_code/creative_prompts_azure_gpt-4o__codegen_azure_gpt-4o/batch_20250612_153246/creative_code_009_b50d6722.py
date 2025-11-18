"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eyemagazine.gr
Prompt: Create a REST API that allows users to subscribe to newsletters like the one offered by Eye Magazine, ensuring compliance with privacy regulations.
Generated: DETERMINISTIC_b50d6722c3d06fae
Batch ID: 20250612_153246
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

# Mock database for storing subscribers
subscribers = []

# Helper function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Endpoint to allow users to subscribe to the newsletter.

    Request JSON format:
    {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    """
    try:
        # Retrieve and validate the JSON payload
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request. JSON data is required."}), 400

        name = data.get('name')
        email = data.get('email')

        # Validate name and email presence
        if not name or not email:
            return jsonify({"error": "Name and email are required fields."}), 400

        # Validate email format
        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format."}), 400

        # Check if email is already subscribed
        if any(subscriber['email'] == email for subscriber in subscribers):
            return jsonify({"message": "Email is already subscribed."}), 200

        # Add subscriber to the mock database
        subscribers.append({"name": name, "email": email})

        # Respond with success message
        return jsonify({"message": "Subscription successful!"}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

@app.route('/subscribers', methods=['GET'])
def list_subscribers():
    """
    Endpoint to retrieve the list of subscribers.

    Returns JSON format:
    [
        {"name": "John Doe", "email": "john.doe@example.com"},
        ...
    ]
    """
    return jsonify(subscribers), 200

if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True)
```
