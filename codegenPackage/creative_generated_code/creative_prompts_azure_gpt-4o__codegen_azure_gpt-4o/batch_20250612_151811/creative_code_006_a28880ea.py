"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kekgroup.net
Prompt: Design an API endpoint for KEK Insurance Brokers that retrieves branch network information (e.g., KEK Liberia, KEK Sierra Leone) and their respective services, as detailed on their webpage.
Generated: DETERMINISTIC_a28880ea6431ffb4
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Set up logging for error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock database for branch network information
BRANCH_NETWORK = [
    {
        "branch_name": "KEK Liberia",
        "services": [
            "Life Insurance",
            "Property Insurance",
            "Motor Insurance",
            "Health Insurance"
        ],
        "contact": "info@kekliberia.com"
    },
    {
        "branch_name": "KEK Sierra Leone",
        "services": [
            "Marine Insurance",
            "Fire Insurance",
            "Travel Insurance",
            "Business Insurance"
        ],
        "contact": "info@keksierra.com"
    },
    {
        "branch_name": "KEK Ghana",
        "services": [
            "Agriculture Insurance",
            "Vehicle Insurance",
            "Investment Insurance"
        ],
        "contact": "info@kekghana.com"
    }
]

@app.route('/api/branches', methods=['GET'])
def get_branch_network():
    """
    API Endpoint: /api/branches
    Method: GET
    Description: Retrieve branch network information and their respective services.
    Response:
        - 200: Returns a JSON array of branch network information.
        - 500: Returns an error message if an internal server error occurs.
    """
    try:
        # Respond with the branch network information
        return jsonify({"branches": BRANCH_NETWORK}), 200
    except Exception as e:
        # Log the error and respond with an internal error message
        logging.error(f"Error retrieving branch network information: {str(e)}")
        return jsonify({"error": "An error occurred while retrieving branch network information."}), 500


@app.route('/api/branches/<string:branch_name>', methods=['GET'])
def get_branch_details(branch_name):
    """
    API Endpoint: /api/branches/<branch_name>
    Method: GET
    Description: Retrieve details of a specific branch by name.
    Path Parameters:
        - branch_name: The name of the branch to retrieve information for.
    Response:
        - 200: Returns a JSON object with branch details.
        - 404: Returns an error message if the branch is not found.
        - 500: Returns an error message if an internal server error occurs.
    """
    try:
        # Search for the branch by name
        branch = next((b for b in BRANCH_NETWORK if b["branch_name"].lower() == branch_name.lower()), None)
        
        if branch:
            return jsonify(branch), 200
        else:
            return jsonify({"error": "Branch not found."}), 404
    except Exception as e:
        # Log the error and respond with an internal error message
        logging.error(f"Error retrieving branch details for '{branch_name}': {str(e)}")
        return jsonify({"error": "An error occurred while retrieving branch details."}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
