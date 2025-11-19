"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unisonplus.vn
Prompt: Generate a code snippet for a web application that allows users to request technical consulting services for infrastructure projects.
Generated: DETERMINISTIC_00d7e51f1ef82339
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
from datetime import datetime
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

# In-memory storage for requests (for simplicity; replace with a database in production)
consultation_requests = []

# Define the route for submitting a consulting request
@app.route('/request-consulting', methods=['POST'])
def request_consulting():
    try:
        # Parse the JSON data from the request
        data = request.json

        # Validate required fields
        required_fields = ['name', 'email', 'project_description', 'preferred_date']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({"error": f"Missing or empty field: {field}"}), 400

        # Validate the date format
        try:
            preferred_date = datetime.strptime(data['preferred_date'], "%Y-%m-%d")
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

        # Create a consultation request object
        consultation_request = {
            "id": len(consultation_requests) + 1,
            "name": data['name'],
            "email": data['email'],
            "project_description": data['project_description'],
            "preferred_date": preferred_date.strftime("%Y-%m-%d"),
            "status": "Pending"
        }

        # Store the request
        consultation_requests.append(consultation_request)

        logging.info(f"New consultation request created: {consultation_request}")

        # Return success response
        return jsonify({"message": "Consultation request submitted successfully.", "request": consultation_request}), 201

    except Exception as e:
        logging.error(f"An error occurred while processing the request: {e}")
        return jsonify({"error": "An internal error occurred. Please try again later."}), 500


# Define the route for listing all consultation requests
@app.route('/list-requests', methods=['GET'])
def list_requests():
    try:
        return jsonify({"requests": consultation_requests}), 200
    except Exception as e:
        logging.error(f"An error occurred while listing requests: {e}")
        return jsonify({"error": "An internal error occurred. Please try again later."}), 500


# Define the route for updating the status of a consultation request
@app.route('/update-status/<int:request_id>', methods=['PATCH'])
def update_status(request_id):
    try:
        # Parse the JSON data from the request
        data = request.json

        # Validate required field
        if 'status' not in data or not data['status']:
            return jsonify({"error": "Missing or empty field: status"}), 400

        # Find the request by ID
        for req in consultation_requests:
            if req['id'] == request_id:
                req['status'] = data['status']
                logging.info(f"Request ID {request_id} updated to status: {data['status']}")
                return jsonify({"message": "Status updated successfully.", "request": req}), 200

        # If no matching ID was found
        return jsonify({"error": "Request not found."}), 404

    except Exception as e:
        logging.error(f"An error occurred while updating the status: {e}")
        return jsonify({"error": "An internal error occurred. Please try again later."}), 500


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
