"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://travaux.fr.fo
Prompt: Create an API endpoint that retrieves the latest customer requests for home improvement services, including details like project type and estimated budget.
Generated: DETERMINISTIC_4edaedfa5eefd9c5
Batch ID: 20250612_160940
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

# Initialize the Flask application
app = Flask(__name__)

# Mock data representing customer requests
# In a production system, this would typically be fetched from a database.
customer_requests = [
    {"id": 1, "project_type": "Kitchen Renovation", "estimated_budget": 15000},
    {"id": 2, "project_type": "Bathroom Remodel", "estimated_budget": 8000},
    {"id": 3, "project_type": "Landscaping", "estimated_budget": 5000},
    {"id": 4, "project_type": "Roof Repair", "estimated_budget": 12000},
]

# API endpoint to retrieve the latest customer requests
@app.route('/api/latest-requests', methods=['GET'])
def get_latest_requests():
    """
    Retrieve the latest customer requests for home improvement services.

    Returns:
        JSON response containing the customer requests, sorted by ID in descending order.
    """
    try:
        # Sort the requests by ID in descending order to get the latest entries first
        sorted_requests = sorted(customer_requests, key=lambda req: req["id"], reverse=True)
        return jsonify({"success": True, "data": sorted_requests}), 200
    except Exception as e:
        # Handle any unexpected errors gracefully
        return jsonify({"success": False, "error": str(e)}), 500

# Custom error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Handle HTTP exceptions and return a JSON response.

    Args:
        e (HTTPException): The exception object containing error details.

    Returns:
        JSON response containing the error details.
    """
    return jsonify({"success": False, "error": e.description}), e.code

# Application entry point
if __name__ == '__main__':
    # Run the Flask application in debug mode for development
    # In production, the debug mode should be disabled, and a WSGI server should be used.
    app.run(debug=True)
```
