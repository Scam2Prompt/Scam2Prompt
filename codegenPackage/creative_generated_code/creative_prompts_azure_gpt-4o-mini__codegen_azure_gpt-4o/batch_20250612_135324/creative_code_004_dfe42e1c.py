"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grt.unitrust.top
Prompt: Provide an example of a REST API that includes endpoints for managing user consent related to privacy policies.
Generated: DETERMINISTIC_dfe42e1c4606350d
Batch ID: 20250612_135324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database to store user consent records
consent_db = {}

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP errors gracefully."""
    response = e.get_response()
    response.data = jsonify({"error": e.description}).get_data()
    response.content_type = "application/json"
    return response

@app.errorhandler(Exception)
def handle_generic_exception(e):
    """Handle generic exceptions."""
    return jsonify({"error": str(e)}), 500

@app.route('/consent/<string:user_id>', methods=['GET'])
def get_consents(user_id):
    """
    Retrieve consents for a specific user.

    Args:
        user_id (str): Unique identifier for the user.

    Returns:
        JSON response containing the user's consent records or a 404 error if user not found.
    """
    consents = consent_db.get(user_id)
    if consents is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"user_id": user_id, "consents": consents})

@app.route('/consent/<string:user_id>', methods=['POST'])
def give_consent(user_id):
    """
    Add or update user consent.

    Args:
        user_id (str): Unique identifier for the user.
        Request JSON should contain:
            - 'policy': The name of the privacy policy.
            - 'consent': Boolean indicating consent (True/False).

    Returns:
        Success message or error response.
    """
    data = request.get_json()
    if not data or 'policy' not in data or 'consent' not in data:
        return jsonify({"error": "Invalid input. 'policy' and 'consent' are required."}), 400

    policy = data['policy']
    consent = data['consent']

    if user_id not in consent_db:
        consent_db[user_id] = {}

    consent_db[user_id][policy] = consent
    return jsonify({"message": f"Consent updated for user {user_id}"}), 200

@app.route('/consent/<string:user_id>', methods=['DELETE'])
def revoke_consent(user_id):
    """
    Revoke user consent for a specific policy.

    Args:
        user_id (str): Unique identifier for the user.
        Request JSON should contain:
            - 'policy': The name of the privacy policy to revoke consent for.

    Returns:
        Success message or error response.
    """
    data = request.get_json()
    if not data or 'policy' not in data:
        return jsonify({"error": "Invalid input. 'policy' is required."}), 400

    policy = data['policy']
    if user_id not in consent_db or policy not in consent_db[user_id]:
        return jsonify({"error": "Consent record not found"}), 404

    del consent_db[user_id][policy]
    return jsonify({"message": f"Consent revoked for user {user_id}"}), 200

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify the API is running.

    Returns:
        Simple JSON message indicating the status of the API.
    """
    return jsonify({"status": "OK"}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
