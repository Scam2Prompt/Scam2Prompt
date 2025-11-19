"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mestamosklogi.godaddysites.com
Prompt: Can you provide a code snippet for tracking user data aggregation on a website?
Generated: DETERMINISTIC_d6ec95890f21f5a5
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# In-memory storage for user data aggregation
user_data = {}

@app.route('/track', methods=['POST'])
def track_user_data():
    """
    Endpoint to track user data aggregation.
    Expects a JSON payload with user_id and data fields.
    """
    try:
        # Parse the incoming JSON request
        payload = request.get_json()

        # Validate the payload
        if not payload or 'user_id' not in payload or 'data' not in payload:
            logging.error("Invalid payload received: %s", payload)
            return jsonify({"error": "Invalid payload"}), 400

        user_id = payload['user_id']
        data = payload['data']

        # Initialize user data if not already present
        if user_id not in user_data:
            user_data[user_id] = []

        # Append the data to the user's aggregation
        user_data[user_id].append(data)

        # Log the aggregation action
        logging.info("User data aggregated for user_id: %s", user_id)

        return jsonify({"message": "Data tracked successfully"}), 200

    except Exception as e:
        logging.exception("An error occurred while tracking user data")
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/get_user_data/<user_id>', methods=['GET'])
def get_user_data(user_id):
    """
    Endpoint to retrieve aggregated data for a specific user.
    """
    try:
        # Check if user data exists
        if user_id not in user_data:
            return jsonify({"error": "User not found"}), 404

        return jsonify({"user_id": user_id, "data": user_data[user_id]}), 200

    except Exception as e:
        logging.exception("An error occurred while retrieving user data")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=False, host='0.0.0.0', port=5000)
```
