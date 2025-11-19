"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dridmachine.com
Prompt: Develop a RESTful API endpoint that allows users to submit design requests for custom posters and record covers.
Generated: DETERMINISTIC_f4197394b7ba68e1
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid
import datetime

app = Flask(__name__)

# In-memory storage for design requests
design_requests = []

# Error messages
INVALID_DATA_ERROR = {"error": "Invalid data. Please provide all required fields."}

# Define the API endpoint for submitting design requests
@app.route('/api/design-requests', methods=['POST'])
def submit_design_request():
    """
    Endpoint to submit design requests for custom posters and record covers.
    Expects a JSON payload with the following fields:
      - name (str): Name of the user submitting the request.
      - email (str): Email address of the user.
      - design_type (str): Type of design ('poster' or 'record_cover').
      - description (str): Brief description of the design request.
    Returns:
      - JSON response with the unique ID of the created design request.
    """
    try:
        # Parse the JSON payload
        data = request.get_json()

        # Validate required fields
        if not data or 'name' not in data or 'email' not in data or 'design_type' not in data or 'description' not in data:
            return jsonify(INVALID_DATA_ERROR), 400

        # Validate the design_type
        if data['design_type'] not in ['poster', 'record_cover']:
            return jsonify({"error": "Invalid design_type. Must be 'poster' or 'record_cover'."}), 400

        # Create a new design request object
        new_request = {
            "id": str(uuid.uuid4()),  # Generate a unique ID for the request
            "name": data['name'],
            "email": data['email'],
            "design_type": data['design_type'],
            "description": data['description'],
            "submitted_at": datetime.datetime.utcnow().isoformat(),  # Timestamp for request submission
        }

        # Store the request in in-memory storage
        design_requests.append(new_request)

        # Return a success response with the generated ID
        return jsonify({"message": "Design request submitted successfully!", "id": new_request['id']}), 201
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": "An internal error occurred. Please try again later."}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
