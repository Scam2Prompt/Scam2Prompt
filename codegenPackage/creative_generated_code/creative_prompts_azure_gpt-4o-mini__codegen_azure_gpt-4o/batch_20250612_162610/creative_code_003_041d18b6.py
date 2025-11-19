"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://workspace-563.com
Prompt: Provide an example of how to handle user verification requests in a web application using a Request ID system.
Generated: DETERMINISTIC_041d18b67a06e0fb
Batch ID: 20250612_162610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid
from datetime import datetime, timedelta

app = Flask(__name__)

# In-memory database to store request IDs and their expiration times
pending_verifications = {}

# Expiration time for a request ID (e.g., 15 minutes)
REQUEST_ID_EXPIRATION_MINUTES = 15


def generate_request_id():
    """
    Generate a unique Request ID using UUID.
    """
    return str(uuid.uuid4())


def is_request_id_valid(request_id):
    """
    Check if the given Request ID is valid and not expired.
    """
    if request_id in pending_verifications:
        expiration_time = pending_verifications[request_id]
        if datetime.utcnow() < expiration_time:
            return True
    return False


@app.route('/generate_verification', methods=['POST'])
def generate_verification_request():
    """
    Generate a new user verification request and return the Request ID.
    """
    try:
        # Generate a unique Request ID
        request_id = generate_request_id()
        
        # Calculate expiration time
        expiration_time = datetime.utcnow() + timedelta(minutes=REQUEST_ID_EXPIRATION_MINUTES)
        
        # Store the Request ID in the pending_verifications dictionary
        pending_verifications[request_id] = expiration_time
        
        return jsonify({"success": True, "request_id": request_id}), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/verify_request', methods=['POST'])
def verify_request():
    """
    Verify if a given Request ID is valid and has not expired.
    """
    try:
        # Extract Request ID from the JSON payload
        data = request.get_json()
        request_id = data.get('request_id')
        
        if not request_id:
            return jsonify({"success": False, "error": "Request ID is required"}), 400
        
        # Check if the Request ID is valid
        if is_request_id_valid(request_id):
            # Request ID is valid; remove it from pending_verifications
            del pending_verifications[request_id]
            return jsonify({"success": True, "message": "Request verified"}), 200
        else:
            # Invalid or expired Request ID
            return jsonify({"success": False, "error": "Invalid or expired Request ID"}), 400
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/pending_requests', methods=['GET'])
def list_pending_requests():
    """
    List all pending verification requests for debugging purposes.
    """
    try:
        # Return all pending requests along with their expiration times
        return jsonify({
            "success": True,
            "pending_requests": {
                request_id: expiration_time.isoformat()
                for request_id, expiration_time in pending_verifications.items()
            }
        }), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
