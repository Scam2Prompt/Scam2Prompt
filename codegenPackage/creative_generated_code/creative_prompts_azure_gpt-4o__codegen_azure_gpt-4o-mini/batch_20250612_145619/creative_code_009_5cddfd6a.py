"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethjya.com
Prompt: Recommend best practices for implementing BTC pledge functionality on websites with a focus on user experience and security.
Generated: DETERMINISTIC_5cddfd6abed4896c
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# btc_pledge.py

import json
import hashlib
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# In-memory storage for user pledges
# In a production application, this should be replaced with a secure database
pledges = {}

def validate_address(address):
    """Validate Bitcoin address format."""
    if len(address) not in (26, 35):
        return False
    # Further validation logic for Bitcoin addresses can be added here
    return True

def hash_pledge(amount, address):
    """Generate a secure hash for the pledge to enhance security."""
    pledge_data = f"{amount}{address}"
    return hashlib.sha256(pledge_data.encode('utf-8')).hexdigest()

@app.route('/pledge', methods=['POST'])
def pledge():
    """Endpoint for users to make a Bitcoin pledge."""
    try:
        data = request.get_json()
        amount = data.get('amount')
        address = data.get('address')

        # Validate input data
        if amount is None or address is None:
            raise BadRequest("Amount and address are required.")

        if not validate_address(address):
            raise BadRequest("Invalid Bitcoin address format.")

        # Process pledge
        pledge_hash = hash_pledge(amount, address)
        pledges[pledge_hash] = {'amount': amount, 'address': address}

        return jsonify({"message": "Pledge successful", "pledge_hash": pledge_hash}), 201

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500

@app.route('/pledges', methods=['GET'])
def get_pledges():
    """Endpoint to retrieve all pledges."""
    return jsonify(pledges), 200

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=False)
```

This code implements a basic BTC pledge functionality using Flask, ensuring user experience and security through input validation, error handling, and secure data hashing.
