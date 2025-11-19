"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fullteco.cl
Prompt: Generate a code snippet for a web application that allows users to request personalized lighting solutions in Puerto Montt, incorporating energy-efficient technologies.
Generated: DETERMINISTIC_fd37a3a2846f7561
Batch ID: 20250612_155916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask web application for requesting personalized lighting solutions in Puerto Montt

from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample database for storing user requests (in-memory for this example)
user_requests = []

# Route to handle personalized lighting solution requests
@app.route('/request-lighting-solution', methods=['POST'])
def request_lighting_solution():
    """
    Endpoint to handle user requests for personalized lighting solutions.
    Accepts user details and preferences as JSON input.
    """
    try:
        # Get the request data
        data = request.get_json()
        
        # Validate the input data
        if not data or 'name' not in data or 'email' not in data or 'preferences' not in data:
            return jsonify({"error": "Invalid input. 'name', 'email', and 'preferences' are required."}), 400
        
        # Extract user details
        name = data['name']
        email = data['email']
        preferences = data['preferences']
        
        # Save the user request (in a real-world app, you would save this to a database)
        user_request = {
            "id": len(user_requests) + 1,
            "name": name,
            "email": email,
            "preferences": preferences,
            "location": "Puerto Montt",
            "energy_efficient": True,  # Default to energy-efficient solutions
        }
        user_requests.append(user_request)
        
        # Return success response
        return jsonify({"message": "Request submitted successfully!", "request_id": user_request["id"]}), 201

    except Exception as e:
        # Handle unexpected server errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


# Route to retrieve all user requests
@app.route('/get-requests', methods=['GET'])
def get_requests():
    """
    Endpoint to retrieve all user requests.
    """
    return jsonify(user_requests), 200


# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Custom error handler for HTTP exceptions.
    Returns JSON response for HTTP errors.
    """
    return jsonify({"error": e.name, "description": e.description}), e.code


# Main application entry point
if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000, debug=False)
```
