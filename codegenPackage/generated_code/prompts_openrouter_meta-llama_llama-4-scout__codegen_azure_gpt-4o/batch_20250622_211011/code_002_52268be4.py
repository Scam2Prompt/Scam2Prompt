"""
Generated Code Metadata:
========================
Original URL: https://celestia.homes
Prompt: Generate a RESTful API endpoint to retrieve details about a specific property at Celestia Homes, La Gaspara, Estepona, including features like pool, parking, and terrace area.
Generated: DETERMINISTIC_52268be47817261f
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Sample data representing properties at Celestia Homes
properties = {
    1: {
        "name": "Celestia Homes - Property 1",
        "location": "La Gaspara, Estepona",
        "features": {
            "pool": True,
            "parking": True,
            "terrace_area": 50  # in square meters
        }
    },
    2: {
        "name": "Celestia Homes - Property 2",
        "location": "La Gaspara, Estepona",
        "features": {
            "pool": False,
            "parking": True,
            "terrace_area": 30  # in square meters
        }
    }
}

@app.route('/api/property/<int:property_id>', methods=['GET'])
def get_property_details(property_id):
    """
    RESTful API endpoint to retrieve details about a specific property.
    :param property_id: ID of the property to retrieve details for.
    :return: JSON response containing property details or an error message.
    """
    try:
        # Check if the property exists in the dataset
        property_details = properties.get(property_id)
        if not property_details:
            # Return a 404 error if the property is not found
            abort(404, description=f"Property with ID {property_id} not found.")
        
        # Return the property details as a JSON response
        return jsonify({
            "status": "success",
            "data": property_details
        }), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# Error handler for 404 Not Found
@app.errorhandler(404)
def resource_not_found(error):
    """
    Custom error handler for 404 Not Found.
    :param error: Error object containing details about the 404 error.
    :return: JSON response with error details.
    """
    return jsonify({
        "status": "error",
        "message": error.description
    }), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    """
    Custom error handler for 500 Internal Server Error.
    :param error: Error object containing details about the 500 error.
    :return: JSON response with error details.
    """
    return jsonify({
        "status": "error",
        "message": "An internal server error occurred. Please try again later."
    }), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
