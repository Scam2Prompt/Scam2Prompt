"""
Generated Code Metadata:
========================
Original URL: https://solucionestecnologicasbogota.com
Prompt: Create a sample API call for a service that provides emergency electrical support, similar to the 24/7 service mentioned on the Space Technologies website.
Generated: DETERMINISTIC_f7468e8465ed6275
Batch ID: 20250612_162051
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

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample in-memory database for demonstration purposes
emergency_requests = []

@app.route('/api/emergency-support', methods=['POST'])
def request_emergency_support():
    """
    Endpoint to request emergency electrical support.
    Expects a JSON payload with the following fields:
    - name: Name of the requester (string)
    - contact: Contact information (string)
    - issue_description: Description of the electrical issue (string)
    - location: Location of the issue (string)
    """
    try:
        # Parse the incoming JSON payload
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400

        # Validate required fields
        required_fields = ['name', 'contact', 'issue_description', 'location']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({"error": f"Missing or empty field: {field}"}), 400

        # Log the request for debugging/auditing purposes
        logging.info(f"Received emergency support request: {data}")

        # Save the request to the in-memory database
        emergency_request = {
            "id": len(emergency_requests) + 1,
            "name": data['name'],
            "contact": data['contact'],
            "issue_description": data['issue_description'],
            "location": data['location'],
            "status": "Pending"  # Default status
        }
        emergency_requests.append(emergency_request)

        # Respond with the created request details
        return jsonify({
            "message": "Emergency support request submitted successfully.",
            "request": emergency_request
        }), 201

    except Exception as e:
        # Log the error and return a generic error response
        logging.error(f"Error processing emergency support request: {e}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500


@app.route('/api/emergency-support/<int:request_id>', methods=['GET'])
def get_emergency_request(request_id):
    """
    Endpoint to retrieve the details of a specific emergency support request by ID.
    """
    try:
        # Find the request by ID
        request_data = next((req for req in emergency_requests if req['id'] == request_id), None)
        if not request_data:
            return jsonify({"error": "Request not found"}), 404

        # Return the request details
        return jsonify(request_data), 200

    except Exception as e:
        # Log the error and return a generic error response
        logging.error(f"Error retrieving emergency support request: {e}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
