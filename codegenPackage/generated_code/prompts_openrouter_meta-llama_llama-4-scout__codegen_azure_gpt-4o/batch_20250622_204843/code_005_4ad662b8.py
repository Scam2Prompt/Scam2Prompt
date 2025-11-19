"""
Generated Code Metadata:
========================
Original URL: https://ipblockchain.pages.dev
Prompt: "Develop a simple application using Story's Application Ecosystem to showcase the potential of tokenized IP in a real-world scenario."
Generated: DETERMINISTIC_4ad662b8612c71dd
Batch ID: 20250622_204843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
A simple application using Story's Application Ecosystem to showcase the potential of tokenized IP.
This application demonstrates how tokenized intellectual property (IP) can be created, managed, and traded.
"""

import json
import uuid
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# In-memory database to store tokenized IPs
tokenized_ips = {}

# Error handling utility
def error_response(message, status_code=400):
    """Generate a standardized error response."""
    return jsonify({"error": message}), status_code

# Route: Create a new tokenized IP
@app.route('/create', methods=['POST'])
def create_tokenized_ip():
    """
    Endpoint to create a new tokenized IP.
    Expects JSON payload with 'title' and 'description'.
    """
    try:
        data = request.get_json()
        if not data or 'title' not in data or 'description' not in data:
            return error_response("Invalid input. 'title' and 'description' are required.")

        # Generate a unique token ID
        token_id = str(uuid.uuid4())
        tokenized_ips[token_id] = {
            "title": data['title'],
            "description": data['description'],
            "owner": data.get('owner', 'Unknown'),  # Optional owner field
            "token_id": token_id
        }

        return jsonify({"message": "Tokenized IP created successfully.", "token_id": token_id}), 201
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}")

# Route: Retrieve details of a tokenized IP
@app.route('/retrieve/<token_id>', methods=['GET'])
def retrieve_tokenized_ip(token_id):
    """
    Endpoint to retrieve details of a tokenized IP by its token ID.
    """
    try:
        tokenized_ip = tokenized_ips.get(token_id)
        if not tokenized_ip:
            return error_response("Tokenized IP not found.", 404)

        return jsonify(tokenized_ip), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}")

# Route: Transfer ownership of a tokenized IP
@app.route('/transfer/<token_id>', methods=['POST'])
def transfer_tokenized_ip(token_id):
    """
    Endpoint to transfer ownership of a tokenized IP.
    Expects JSON payload with 'new_owner'.
    """
    try:
        data = request.get_json()
        if not data or 'new_owner' not in data:
            return error_response("Invalid input. 'new_owner' is required.")

        tokenized_ip = tokenized_ips.get(token_id)
        if not tokenized_ip:
            return error_response("Tokenized IP not found.", 404)

        # Update the owner field
        tokenized_ip['owner'] = data['new_owner']
        return jsonify({"message": "Ownership transferred successfully.", "token_id": token_id}), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}")

# Route: List all tokenized IPs
@app.route('/list', methods=['GET'])
def list_tokenized_ips():
    """
    Endpoint to list all tokenized IPs.
    """
    try:
        return jsonify(list(tokenized_ips.values())), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}")

# Main entry point
if __name__ == '__main__':
    """
    Run the Flask application.
    """
    app.run(debug=True)
```
