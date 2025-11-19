"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Create an API endpoint that allows clients to submit their cosmetic formulation requests, ensuring compliance with the quality management practices highlighted by Fabricare Cosmeticos.
Generated: DETERMINISTIC_32053d184f40b58f
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean and production-ready example using Python with the Flask framework to create an API endpoint for submitting cosmetic formulation requests:

```python
from flask import Flask, request, jsonify
import logging
import uuid

app = Flask(__name__)

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# In-memory storage for requests (replace with a database in production)
formulation_requests = {}

# Define a route for submitting cosmetic formulation requests
@app.route('/submit-formulation-request', methods=['POST'])
def submit_formulation_request():
    """
    Endpoint to submit cosmetic formulation requests.
    
    Request Format (JSON):
    {
        "client_name": "string",
        "email": "string",
        "formulation_details": "string",
        "priority_level": "string" (e.g., "low", "medium", "high")
    }
    
    Response Format (JSON):
    {
        "status": "success/error",
        "message": "string",
        "request_id": "string" (for successful submissions)
    }
    """
    try:
        # Parse JSON data from the request
        data = request.get_json()
        if not data:
            return jsonify({"status": "error", "message": "Invalid JSON format"}), 400

        # Validate required fields
        required_fields = ["client_name", "email", "formulation_details", "priority_level"]
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({"status": "error", "message": f"Missing required field: {field}"}), 400

        # Create a unique ID for the request
        request_id = str(uuid.uuid4())

        # Store the request in the in-memory storage
        formulation_requests[request_id] = {
            "client_name": data["client_name"],
            "email": data["email"],
            "formulation_details": data["formulation_details"],
            "priority_level": data["priority_level"],
            "request_id": request_id
        }

        # Log the submission
        logging.info(f"New formulation request submitted: {formulation_requests[request_id]}")

        # Return a success response
        return jsonify({
            "status": "success",
            "message": "Formulation request submitted successfully.",
            "request_id": request_id
        }), 201
    except Exception as e:
        # Log the error and return an error response
        logging.error(f"Error processing formulation request: {str(e)}")
        return jsonify({"status": "error", "message": "An error occurred while processing the request."}), 500

# Application entry point
if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### Notes:
- Replace the in-memory storage (`formulation_requests`) with a database in a production environment.
- Ensure proper email validation and additional security measures, such as rate-limiting and authentication, for production-ready deployment.
- The `debug` mode is set to `False` for production use.
