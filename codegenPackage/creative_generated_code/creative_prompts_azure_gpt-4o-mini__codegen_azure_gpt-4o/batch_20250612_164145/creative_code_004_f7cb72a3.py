"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomware.net
Prompt: Create a simple API that tracks user consent for cookies and aggregates data, similar to the approach discussed on phantomware.net.
Generated: DETERMINISTIC_f7cb72a3dd33ac33
Batch ID: 20250612_164145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database to store user consents
user_consent_db = {}

# Endpoint to update or record user consent
@app.route('/api/consent', methods=['POST'])
def update_consent():
    try:
        # Parse the request JSON
        data = request.json
        if not data or 'user_id' not in data or 'consent' not in data:
            return jsonify({'error': 'Invalid request format. Please include user_id and consent fields.'}), 400

        user_id = data['user_id']
        consent = data['consent']

        # Validate consent value
        if consent not in ['accepted', 'rejected']:
            return jsonify({'error': 'Consent value must be either "accepted" or "rejected".'}), 400

        # Update in-memory database
        user_consent_db[user_id] = consent

        return jsonify({'message': 'Consent successfully recorded.', 'user_id': user_id, 'consent': consent}), 200
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred.', 'details': str(e)}), 500

# Endpoint to aggregate consent data
@app.route('/api/consent-summary', methods=['GET'])
def consent_summary():
    try:
        # Aggregate consent data
        summary = {
            'accepted': sum(1 for consent in user_consent_db.values() if consent == 'accepted'),
            'rejected': sum(1 for consent in user_consent_db.values() if consent == 'rejected'),
            'total_users': len(user_consent_db)
        }

        return jsonify({'summary': summary}), 200
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred.', 'details': str(e)}), 500

# Starting point of the application
if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)
```

This code defines a simple Flask-based API with routes for recording user consent and retrieving a summary of consent data. Each endpoint is equipped with error handling, validation, and adheres to clean coding principles.
