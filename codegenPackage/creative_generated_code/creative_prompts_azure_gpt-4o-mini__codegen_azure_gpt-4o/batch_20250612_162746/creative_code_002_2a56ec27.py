"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kabosu-bsc.pages.dev
Prompt: Create an API endpoint that allows users to view the charity partners of Kabosu Token and their contributions, similar to the partnerships mentioned on the website.
Generated: DETERMINISTIC_2a56ec2717d533e8
Batch ID: 20250612_162746
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample data representing charity partners and their contributions
CHARITY_DATA = [
    {
        "id": 1,
        "name": "Charity A",
        "description": "Helping underprivileged children through education.",
        "contributions": {
            "total_amount": 50000,
            "currency": "USD",
            "projects": [
                {"name": "School Supplies Distribution", "amount": 20000},
                {"name": "Scholarships for Students", "amount": 30000}
            ]
        }
    },
    {
        "id": 2,
        "name": "Charity B",
        "description": "Providing clean water to communities in need.",
        "contributions": {
            "total_amount": 75000,
            "currency": "USD",
            "projects": [
                {"name": "Water Well Construction", "amount": 50000},
                {"name": "Water Purification Systems", "amount": 25000}
            ]
        }
    }
]

@app.route('/api/charity-partners', methods=['GET'])
def get_charity_partners():
    """
    API endpoint to retrieve the list of charity partners and their contributions.

    Returns:
        JSON response containing charity data or an error message.
    """
    try:
        # Log the request
        logging.info('Received request to fetch charity partners.')

        # Return the charity data as a JSON response
        return jsonify({
            "success": True,
            "data": CHARITY_DATA
        }), 200

    except Exception as e:
        # Log the error
        logging.error(f"An error occurred while fetching charity partners: {str(e)}")

        # Return an error response
        return jsonify({
            "success": False,
            "message": "An error occurred while fetching charity partners."
        }), 500

@app.errorhandler(404)
def not_found(error):
    """
    Error handler for 404 Not Found.

    Args:
        error: The error object.

    Returns:
        JSON response indicating that the requested resource was not found.
    """
    return jsonify({
        "success": False,
        "message": "Resource not found."
    }), 404

@app.errorhandler(500)
def server_error(error):
    """
    Error handler for 500 Internal Server Error.

    Args:
        error: The error object.

    Returns:
        JSON response indicating that an internal server error occurred.
    """
    return jsonify({
        "success": False,
        "message": "Internal server error."
    }), 500

if __name__ == '__main__':
    # Start the Flask application
    # Use debug=True only in development; set debug=False for production
    app.run(debug=True)
```
