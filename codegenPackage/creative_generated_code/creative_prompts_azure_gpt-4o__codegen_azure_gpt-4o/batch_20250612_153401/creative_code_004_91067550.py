"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artstrid-app-git-mm-943-phantom-confirm-tr-c95731-mintmyne-team.vercel.app
Prompt: Develop an API endpoint for submitting user requests or inquiries, similar to the "Submit a Request" feature on Artstrid.
Generated: DETERMINISTIC_91067550d4a49dfa
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready API implementation in Python using Flask:

```python
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory storage for user requests (for simplicity, using a dictionary)
# In production, this should be a database.
user_requests = {}

@app.route('/submit-request', methods=['POST'])
def submit_request():
    """
    API endpoint to submit a user request or inquiry.
    Expects JSON payload with 'name', 'email', and 'message'.
    """
    try:
        # Parse incoming JSON request body
        data = request.get_json()
        
        # Validate required fields
        if not data or 'name' not in data or 'email' not in data or 'message' not in data:
            return jsonify({"error": "Missing required fields: 'name', 'email', 'message'"}), 400
        
        name = data['name']
        email = data['email']
        message = data['message']

        # Validate data types
        if not isinstance(name, str) or not isinstance(email, str) or not isinstance(message, str):
            return jsonify({"error": "All fields must be of type string"}), 400

        # Generate a unique request ID
        request_id = str(uuid.uuid4())
        
        # Record the timestamp of the request
        timestamp = datetime.utcnow().isoformat()

        # Save the request details
        user_requests[request_id] = {
            "name": name,
            "email": email,
            "message": message,
            "timestamp": timestamp
        }

        # Return success response
        return jsonify({
            "message": "Request submitted successfully",
            "request_id": request_id,
            "timestamp": timestamp
        }), 201

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route('/requests/<request_id>', methods=['GET'])
def get_request(request_id):
    """
    API endpoint to retrieve a specific user request by its ID.
    """
    try:
        # Check if the request ID exists
        if request_id not in user_requests:
            return jsonify({"error": "Request ID not found"}), 404

        # Return the request details
        return jsonify(user_requests[request_id]), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```

### Notes:
- Replace the in-memory `user_requests` dictionary with a proper database in production.
- Flask's `debug=True` mode should be turned off in a production environment for security reasons.
