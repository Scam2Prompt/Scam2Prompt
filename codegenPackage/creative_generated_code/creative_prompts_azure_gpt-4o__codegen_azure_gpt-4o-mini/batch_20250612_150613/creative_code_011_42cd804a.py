"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint-zielchain.vercel.app
Prompt: Write a script to handle user consent for sharing wallet address information with third-party NFT projects, as described in ZIELCHAIN's privacy policy.
Generated: DETERMINISTIC_42cd804ac2013118
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# In-memory storage for user consent records (use a database in production)
user_consents = {}

@app.route('/consent', methods=['POST'])
def handle_consent():
    """Handle user consent for sharing wallet address information."""
    
    try:
        # Parse the JSON request body
        data = request.get_json()
        
        # Validate request structure
        if 'user_id' not in data or 'wallet_address' not in data or 'consent' not in data:
            raise BadRequest("Missing required fields: user_id, wallet_address, consent")
        
        user_id = data['user_id']
        wallet_address = data['wallet_address']
        consent = data['consent']

        # Store or update user consent in-memory (in production, use a persistent database)
        user_consents[user_id] = {
            'wallet_address': wallet_address,
            'consent': consent
        }
        
        return jsonify({"message": "Consent recorded successfully", "user_id": user_id}), 200

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500

@app.route('/consent/<user_id>', methods=['GET'])
def get_consent(user_id):
    """Retrieve user consent information."""
    try:
        # Check if user consent exists
        if user_id not in user_consents:
            return jsonify({"error": "No consent found for this user ID"}), 404
        
        return jsonify(user_consents[user_id]), 200

    except Exception as e:
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
```
