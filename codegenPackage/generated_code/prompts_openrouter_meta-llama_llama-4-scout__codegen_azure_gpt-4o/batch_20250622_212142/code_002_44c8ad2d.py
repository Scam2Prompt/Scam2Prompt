"""
Generated Code Metadata:
========================
Original URL: https://travaux.fr.fo
Prompt: Generate a RESTful API endpoint to handle user requests for project estimates, including parameters for project type (e.g., cuisine, toiture, electricité) and location, and return a list of qualified artisans and their quotes.
Generated: DETERMINISTIC_44c8ad2def566c8d
Batch ID: 20250622_212142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Mock data for artisans and their quotes
ARTISANS = [
    {"id": 1, "name": "John Doe", "type": "cuisine", "location": "Paris", "quote": 1200},
    {"id": 2, "name": "Jane Smith", "type": "toiture", "location": "Lyon", "quote": 2500},
    {"id": 3, "name": "Mike Johnson", "type": "electricité", "location": "Marseille", "quote": 800},
    {"id": 4, "name": "Emily Davis", "type": "cuisine", "location": "Lyon", "quote": 1500},
    {"id": 5, "name": "Chris Brown", "type": "toiture", "location": "Paris", "quote": 2700},
]

@app.route('/api/project-estimates', methods=['GET'])
def get_project_estimates():
    """
    RESTful API endpoint to fetch project estimates based on project type and location.
    Query Parameters:
        - type: The type of project (e.g., cuisine, toiture, electricité)
        - location: The location of the project (e.g., Paris, Lyon, Marseille)
    Returns:
        - JSON response containing a list of qualified artisans and their quotes.
    """
    try:
        # Get query parameters
        project_type = request.args.get('type')
        location = request.args.get('location')

        # Validate query parameters
        if not project_type or not location:
            return jsonify({"error": "Missing required query parameters: 'type' and 'location'"}), 400

        # Filter artisans based on project type and location
        filtered_artisans = [
            artisan for artisan in ARTISANS
            if artisan['type'].lower() == project_type.lower() and artisan['location'].lower() == location.lower()
        ]

        # Return filtered artisans
        return jsonify({"artisans": filtered_artisans}), 200

    except Exception as e:
        # Log the error and return a generic error response
        logging.error(f"Error occurred while processing request: {e}")
        return jsonify({"error": "An internal error occurred. Please try again later."}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
