"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpl-liner.com
Prompt: Develop a REST API endpoint for managing custom brokerage requests, incorporating features mentioned on the MPL website.
Generated: DETERMINISTIC_19d0e76f210ed4f6
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging for error tracking and application monitoring
logging.basicConfig(level=logging.INFO)

# Mock database for storing brokerage requests
brokerage_requests = []

# Helper function for error responses
def error_response(message, status_code):
    return jsonify({'error': message}), status_code

@app.route('/brokerage-requests', methods=['GET', 'POST'])
def manage_brokerage_requests():
    """
    REST API endpoint to manage brokerage requests.
    
    GET: Fetch all brokerage requests.
    POST: Create a new brokerage request.
    """
    try:
        if request.method == 'GET':
            # Return all stored brokerage requests
            logging.info("Fetching all brokerage requests")
            return jsonify({'brokerage_requests': brokerage_requests}), 200

        elif request.method == 'POST':
            # Parse JSON body for new brokerage request details
            logging.info("Creating a new brokerage request")
            data = request.get_json()

            # Validate input data
            if not data or 'client_name' not in data or 'request_details' not in data:
                logging.error("Invalid request payload")
                return error_response("Invalid request payload. 'client_name' and 'request_details' are required.", 400)

            # Create a new brokerage request
            new_request = {
                'id': len(brokerage_requests) + 1,
                'client_name': data['client_name'],
                'request_details': data['request_details'],
                'status': 'pending'  # Default status
            }
            brokerage_requests.append(new_request)

            logging.info(f"Brokerage request created: {new_request}")
            return jsonify({'message': 'Brokerage request created successfully.', 'brokerage_request': new_request}), 201

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return error_response("An internal server error occurred.", 500)

@app.route('/brokerage-requests/<int:request_id>', methods=['GET', 'PUT', 'DELETE'])
def brokerage_request_by_id(request_id):
    """
    REST API endpoint to manage a single brokerage request by ID.
    
    GET: Fetch a brokerage request by ID.
    PUT: Update the status of a brokerage request.
    DELETE: Delete a brokerage request.
    """
    try:
        # Find the brokerage request by ID
        request_item = next((req for req in brokerage_requests if req['id'] == request_id), None)
        
        if not request_item:
            logging.error(f"Brokerage request with ID {request_id} not found")
            return error_response("Brokerage request not found.", 404)

        if request.method == 'GET':
            # Return the requested brokerage request
            logging.info(f"Fetching brokerage request with ID {request_id}")
            return jsonify({'brokerage_request': request_item}), 200

        elif request.method == 'PUT':
            # Update the status of the brokerage request
            logging.info(f"Updating brokerage request with ID {request_id}")
            data = request.get_json()

            if not data or 'status' not in data:
                logging.error("Invalid request payload for status update")
                return error_response("Invalid request payload. 'status' is required.", 400)

            request_item['status'] = data['status']
            logging.info(f"Brokerage request updated: {request_item}")
            return jsonify({'message': 'Brokerage request updated successfully.', 'brokerage_request': request_item}), 200

        elif request.method == 'DELETE':
            # Delete the brokerage request
            logging.info(f"Deleting brokerage request with ID {request_id}")
            brokerage_requests.remove(request_item)
            logging.info(f"Brokerage request with ID {request_id} deleted")
            return jsonify({'message': 'Brokerage request deleted successfully.'}), 200

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return error_response("An internal server error occurred.", 500)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
