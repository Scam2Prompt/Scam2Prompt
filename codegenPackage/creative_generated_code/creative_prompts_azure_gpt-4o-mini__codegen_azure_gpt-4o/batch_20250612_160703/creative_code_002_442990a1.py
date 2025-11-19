"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stars-ksa.com
Prompt: Create an API endpoint for a cleaning service platform that retrieves available cleaning packages, similar to the customized solutions offered by Star Cleaning Services.
Generated: DETERMINISTIC_442990a1c0ad3d50
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Mock database of cleaning packages
cleaning_packages = [
    {
        "id": 1,
        "name": "Basic Cleaning",
        "description": "A standard cleaning service for small apartments.",
        "price": 50.00,
        "duration_hours": 2
    },
    {
        "id": 2,
        "name": "Deep Cleaning",
        "description": "A thorough cleaning service including hard-to-reach areas.",
        "price": 120.00,
        "duration_hours": 4
    },
    {
        "id": 3,
        "name": "Move-In/Move-Out Cleaning",
        "description": "Specialized cleaning for moving in or out of a property.",
        "price": 200.00,
        "duration_hours": 6
    },
    {
        "id": 4,
        "name": "Custom Cleaning Package",
        "description": "A fully customizable cleaning package tailored to your needs.",
        "price": None,  # Price depends on customization
        "duration_hours": None  # Duration depends on customization
    }
]

@app.errorhandler(Exception)
def handle_error(error):
    """
    Global error handler for the API to return JSON responses for exceptions.
    """
    response = {
        "error": True,
        "message": str(error)
    }
    if isinstance(error, HTTPException):
        response["status_code"] = error.code
    else:
        response["status_code"] = 500
    return jsonify(response), response["status_code"]

@app.route('/api/cleaning-packages', methods=['GET'])
def get_cleaning_packages():
    """
    API endpoint to retrieve all available cleaning packages.
    Returns a JSON response with the list of packages.
    """
    try:
        response = {
            "error": False,
            "data": cleaning_packages,
            "message": "Cleaning packages retrieved successfully."
        }
        return jsonify(response), 200
    except Exception as e:
        # Log the error (can be enhanced with a logging library in production)
        return handle_error(e)

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
