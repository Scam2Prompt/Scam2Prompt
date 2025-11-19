"""
Generated Code Metadata:
========================
Original URL: https://insidesafety.com.mx
Prompt: Develop a solution for integrating video intercom systems with access control, as described in the services provided by Inside Safety.
Generated: DETERMINISTIC_ef09753b6e07dd05
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Mock database for users and access control
users_db = {
    "user1": {"name": "Alice", "access_level": "admin"},
    "user2": {"name": "Bob", "access_level": "user"},
}

# Mock database for video intercom system
intercom_db = {
    "intercom1": {"location": "Front Door", "status": "offline"},
    "intercom2": {"location": "Back Door", "status": "online"},
}

@app.route('/api/access', methods=['POST'])
def grant_access():
    """
    Grant access to a user based on their credentials and intercom status.
    Expects a JSON payload with 'username' and 'intercom_id'.
    """
    try:
        data = request.get_json()
        username = data.get('username')
        intercom_id = data.get('intercom_id')

        # Validate input
        if not username or not intercom_id:
            return jsonify({"error": "Username and intercom_id are required."}), 400

        # Check if user exists
        user = users_db.get(username)
        if not user:
            return jsonify({"error": "User not found."}), 404

        # Check intercom status
        intercom = intercom_db.get(intercom_id)
        if not intercom:
            return jsonify({"error": "Intercom not found."}), 404

        if intercom['status'] != 'online':
            return jsonify({"error": "Intercom is offline."}), 503

        # Grant access logic (placeholder)
        logging.info(f"Access granted to {user['name']} at {intercom['location']}.")
        return jsonify({"message": f"Access granted to {user['name']}."}), 200

    except Exception as e:
        logging.error(f"Error granting access: {str(e)}")
        return jsonify({"error": "An error occurred while processing your request."}), 500

@app.route('/api/intercom/status', methods=['GET'])
def get_intercom_status():
    """
    Retrieve the status of all intercoms.
    """
    try:
        return jsonify(intercom_db), 200
    except Exception as e:
        logging.error(f"Error retrieving intercom status: {str(e)}")
        return jsonify({"error": "An error occurred while retrieving intercom status."}), 500

if __name__ == '__main__':
    # Run the application
    app.run(host='0.0.0.0', port=5000)
```
