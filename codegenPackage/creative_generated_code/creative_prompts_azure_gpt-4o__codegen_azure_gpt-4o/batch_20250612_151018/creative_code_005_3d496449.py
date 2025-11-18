"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-200--nervous-kare-6f3c45.netlify.app
Prompt: Create a REST API endpoint to allow users in the City of York to query their recycling collection schedule based on their address.
Generated: DETERMINISTIC_3d496449f3346c8e
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import re

app = Flask(__name__)

# Mock data to simulate a database
RECYCLING_SCHEDULE = {
    "123 Main St": {
        "next_pickup": "2023-10-15",
        "pickup_day": "Sunday"
    },
    "456 Elm St": {
        "next_pickup": "2023-10-18",
        "pickup_day": "Wednesday"
    },
    "789 Oak St": {
        "next_pickup": "2023-10-20",
        "pickup_day": "Friday"
    }
}

@app.route('/api/recycling-schedule', methods=['GET'])
def get_recycling_schedule():
    """
    Endpoint to retrieve recycling collection schedule based on address.
    Query Parameter:
        address (str): The address of the user in the City of York.
    Returns:
        JSON object containing recycling schedule details if the address is valid.
    """
    try:
        # Get the address from query parameters
        address = request.args.get('address', '').strip()

        # Validate the input address
        if not address:
            return jsonify({"error": "Address parameter is required"}), 400

        # Check if the address exists in our mock database
        schedule = RECYCLING_SCHEDULE.get(address)

        if not schedule:
            return jsonify({"error": "Address not found in recycling schedule"}), 404

        # Return the recycling schedule as a JSON response
        return jsonify({"address": address, "schedule": schedule}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
