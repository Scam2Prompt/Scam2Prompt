"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://berge.life
Prompt: Suggest an API for managing user consent related to privacy policies in web applications.
Generated: DETERMINISTIC_3f25037795267ad7
Batch ID: 20250612_155801
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
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# In-memory storage for user consents (for demonstration purposes; use a database in production)
consents = {}

# Helper functions
def validate_request_data(data, required_fields):
    """
    Validate request data to ensure required fields are present.
    Args:
        data (dict): The request data.
        required_fields (list): List of required field names.
    Returns:
        tuple: (is_valid, missing_fields)
    """
    missing_fields = [field for field in required_fields if field not in data]
    return (len(missing_fields) == 0, missing_fields)

# API Endpoints

@app.route('/consent', methods=['POST'])
def give_consent():
    """
    Endpoint to allow a user to give consent.
    Expects JSON payload with 'user_id', 'policy_id', and 'consent_status'.
    """
    data = request.get_json()

    # Validate incoming data
    is_valid, missing_fields = validate_request_data(data, ['user_id', 'policy_id', 'consent_status'])
    if not is_valid:
        return jsonify({"error": "Missing required fields", "missing_fields": missing_fields}), 400

    user_id = data['user_id']
    policy_id = data['policy_id']
    consent_status = data['consent_status']

    # Validate consent_status
    if consent_status not in ['granted', 'revoked']:
        return jsonify({"error": "Invalid consent_status. Must be 'granted' or 'revoked'"}), 400

    # Generate unique consent ID
    consent_id = str(uuid.uuid4())

    # Record consent
    consents[consent_id] = {
        'user_id': user_id,
        'policy_id': policy_id,
        'consent_status': consent_status,
        'timestamp': datetime.utcnow().isoformat()
    }

    return jsonify({"message": "Consent recorded", "consent_id": consent_id}), 201

@app.route('/consent/<user_id>', methods=['GET'])
def get_user_consents(user_id):
    """
    Endpoint to fetch all consents given by a specific user.
    """
    user_consents = [consent for consent in consents.values() if consent['user_id'] == user_id]

    if not user_consents:
        return jsonify({"message": "No consents found for the specified user"}), 404

    return jsonify(user_consents), 200

@app.route('/consent/<consent_id>', methods=['DELETE'])
def revoke_consent(consent_id):
    """
    Endpoint to revoke a specific consent by its ID.
    """
    if consent_id not in consents:
        return jsonify({"error": "Consent ID not found"}), 404

    del consents[consent_id]
    return jsonify({"message": "Consent successfully revoked"}), 200

@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors gracefully.
    """
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Handle server errors gracefully.
    """
    return jsonify({"error": "Internal server error"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
