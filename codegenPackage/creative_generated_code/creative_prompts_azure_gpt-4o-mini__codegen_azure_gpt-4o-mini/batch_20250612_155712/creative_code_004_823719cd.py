"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mnswap.org
Prompt: Develop an API that integrates with MN Swap's award nomination system for activity professionals.
Generated: DETERMINISTIC_823719cd58206489
Batch ID: 20250612_155712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Sample in-memory storage for nominations
nominations = []

class Nomination:
    def __init__(self, nominee_name, activity, reason):
        self.nominee_name = nominee_name
        self.activity = activity
        self.reason = reason

    def to_dict(self):
        return {
            "nominee_name": self.nominee_name,
            "activity": self.activity,
            "reason": self.reason
        }

@app.route('/nominations', methods=['POST'])
def create_nomination():
    """
    Endpoint to create a new nomination for an activity professional.

    Request JSON payload should include:
    - nominee_name (str): Name of the nominee
    - activity (str): The activity for which the nomination is made
    - reason (str): The reason for the nomination
    """
    try:
        # Parse request JSON
        data = request.get_json()

        # Validate input data
        if not data or not all(key in data for key in ('nominee_name', 'activity', 'reason')):
            logger.error("Invalid input data: %s", data)
            return jsonify({"error": "Invalid input data"}), 400

        # Create a new nomination and store it
        nomination = Nomination(data['nominee_name'], data['activity'], data['reason'])
        nominations.append(nomination.to_dict())

        logger.info("Nomination created successfully: %s", nomination.to_dict())
        return jsonify(nomination.to_dict()), 201

    except Exception as e:
        logger.exception("Error creating nomination: %s", e)
        return jsonify({"error": "An internal error occurred"}), 500


@app.route('/nominations', methods=['GET'])
def get_nominations():
    """
    Endpoint to retrieve all nominations.

    Returns:
    - A list of all nominations
    """
    try:
        return jsonify(nominations), 200

    except Exception as e:
        logger.exception("Error retrieving nominations: %s", e)
        return jsonify({"error": "An internal error occurred"}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False, host='0.0.0.0', port=5000)
```
