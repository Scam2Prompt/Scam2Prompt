"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renovation-toiture-toulouse.com
Prompt: Develop a REST API endpoint that allows users to submit requests for roofing services, including fields for type of service (repair, installation, etc.) and location in Toulouse.
Generated: DETERMINISTIC_9324e0a1c3dc31a1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory storage for submitted requests
service_requests = []

@app.route('/api/roofing-services', methods=['POST'])
def submit_roofing_service_request():
    """
    Endpoint to submit a request for roofing services.
    Expects JSON payload with 'service_type' and 'location'.
    """
    try:
        # Parse incoming JSON payload
        data = request.get_json()

        # Validate required fields
        if not data or 'service_type' not in data or 'location' not in data:
            return jsonify({
                'error': 'Missing required fields: service_type and/or location'
            }), 400

        # Validate service_type and location are non-empty strings
        service_type = data['service_type'].strip()
        location = data['location'].strip()

        if not service_type or not location:
            return jsonify({
                'error': 'Fields service_type and location must not be empty'
            }), 400

        # Only allow requests for Toulouse
        if location.lower() != 'toulouse':
            return jsonify({
                'error': 'Service location must be Toulouse'
            }), 400

        # Add the request to the in-memory storage
        request_entry = {
            'id': len(service_requests) + 1,  # Simple ID generation
            'service_type': service_type,
            'location': location
        }
        service_requests.append(request_entry)

        # Return success response
        return jsonify({
            'message': 'Roofing service request submitted successfully',
            'request': request_entry
        }), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({
            'error': 'An error occurred while processing the request',
            'details': str(e)
        }), 500


@app.route('/api/roofing-services', methods=['GET'])
def list_roofing_service_requests():
    """
    Endpoint to list all submitted roofing service requests.
    """
    return jsonify(service_requests), 200


@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Custom error handler for HTTP exceptions.
    """
    return jsonify({
        'error': e.name,
        'description': e.description
    }), e.code


@app.errorhandler(Exception)
def handle_generic_exception(e):
    """
    Generic error handler for unexpected exceptions.
    """
    return jsonify({
        'error': 'Internal Server Error',
        'details': str(e)
    }), 500


if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(host='0.0.0.0', port=5000, debug=False)
```
