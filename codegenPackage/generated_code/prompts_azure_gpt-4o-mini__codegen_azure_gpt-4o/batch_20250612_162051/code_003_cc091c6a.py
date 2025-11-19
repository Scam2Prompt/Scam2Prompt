"""
Generated Code Metadata:
========================
Original URL: https://drcelsolemos.com.br
Prompt: Develop an API endpoint that retrieves information about dental services such as implants and orthodontics available at Dr. Celso Lemos' clinic.
Generated: DETERMINISTIC_cc091c6ad8c3fc49
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data for dental services
dental_services = [
    {
        "id": 1,
        "name": "Dental Implants",
        "description": "Permanent solution for missing teeth using titanium implants.",
        "price_range": "$1500 - $3000",
        "available": True
    },
    {
        "id": 2,
        "name": "Orthodontics",
        "description": "Braces and aligners to straighten teeth and correct bite issues.",
        "price_range": "$2000 - $6000",
        "available": True
    },
    {
        "id": 3,
        "name": "Teeth Whitening",
        "description": "Professional teeth whitening for a brighter smile.",
        "price_range": "$300 - $800",
        "available": False
    }
]

@app.route('/api/dental-services', methods=['GET'])
def get_dental_services():
    """
    API endpoint to retrieve information about dental services available at Dr. Celso Lemos' clinic.
    Returns:
        JSON response containing a list of available dental services.
    """
    try:
        # Filter only available services
        available_services = [service for service in dental_services if service["available"]]
        
        # Return the list of available services as a JSON response
        return jsonify({
            "clinic_name": "Dr. Celso Lemos' Clinic",
            "services": available_services
        }), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({
            "error": "An error occurred while retrieving dental services.",
            "details": str(e)
        }), 500

# Error handler for 404 - Not Found
@app.errorhandler(404)
def not_found(error):
    """
    Custom error handler for 404 errors.
    """
    return jsonify({
        "error": "Endpoint not found."
    }), 404

# Error handler for 405 - Method Not Allowed
@app.errorhandler(405)
def method_not_allowed(error):
    """
    Custom error handler for 405 errors.
    """
    return jsonify({
        "error": "Method not allowed on this endpoint."
    }), 405

# Main entry point for running the Flask application
if __name__ == '__main__':
    # Run the Flask app on localhost and port 5000
    app.run(debug=True)
```
