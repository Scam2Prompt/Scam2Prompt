"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abve.xyz
Prompt: Generate a sample code snippet for a subscription feature that collects user emails for updates, similar to the one mentioned on abve.xyz.
Generated: DETERMINISTIC_d258c40ae33a8904
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import re

# Initialize the Flask application
app = Flask(__name__)

# In-memory storage for emails (for demonstration purposes only)
# In production, replace this with a database.
subscribed_emails = set()

# Function to validate email format
def is_valid_email(email):
    """
    Validates the email address format using regex.

    :param email: The email address to validate
    :return: True if the email is valid, False otherwise
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Endpoint to handle email subscriptions.

    Request Body (JSON):
    {
        "email": "user@example.com"
    }

    Response:
    - 200 OK: Successfully subscribed
    - 400 Bad Request: Invalid email or other error
    """
    try:
        # Parse incoming JSON data
        data = request.get_json()
        email = data.get('email')

        # Validate email presence
        if not email:
            return jsonify({"error": "Email is required"}), 400

        # Validate email format
        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format"}), 400

        # Check if email is already subscribed
        if email in subscribed_emails:
            return jsonify({"message": "Email is already subscribed"}), 200

        # Add email to the subscription list
        subscribed_emails.add(email)
        return jsonify({"message": "Successfully subscribed"}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
