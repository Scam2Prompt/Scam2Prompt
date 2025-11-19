"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ggeminiloginx.godaddysites.com
Prompt: What are the implications of cookie consent for user data aggregation in web applications like Gemiṇi: Loℊin?
Generated: DETERMINISTIC_503aa293ce474cd4
Batch ID: 20250612_164057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# Simulated database for user consent records
user_consent_db = {}

@app.route('/consent', methods=['POST'])
def record_consent():
    """
    Endpoint to record user cookie consent.

    Request body should include:
    - user_id: str: Unique identifier for the user
    - consent: bool: User consent for data aggregation
    """
    data = request.get_json()

    # Validate request payload
    if not data or 'user_id' not in data or 'consent' not in data:
        abort(400, description="Invalid request payload")

    user_id = data['user_id']
    consent = data['consent']

    # Record user consent status
    user_consent_db[user_id] = consent

    return jsonify({"message": "Consent recorded successfully"}), 200

@app.route('/aggregate_data', methods=['GET'])
def aggregate_data():
    """
    Endpoint to aggregate user data based on consent.

    Returns aggregated data only for users who have given consent.
    """
    aggregated_data = []

    for user_id, consent in user_consent_db.items():
        if consent:  # Only include users who have consented
            # Simulated data aggregation process
            user_data = {"user_id": user_id, "data": "Aggregated data for user"}
            aggregated_data.append(user_data)

    return jsonify(aggregated_data), 200

@app.errorhandler(400)
def bad_request(error):
    """Custom error handler for bad requests."""
    return jsonify({"error": str(error)}), 400

@app.errorhandler(404)
def not_found(error):
    """Custom error handler for not found resources."""
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Custom error handler for internal server errors."""
    return jsonify({"error": "An internal error occurred"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
