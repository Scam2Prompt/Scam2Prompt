"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blue-8ly.pages.dev
Prompt: Can you explain the implications of receiving an Incapsula incident ID in a web request?
Generated: DETERMINISTIC_5dd4000ff0389538
Batch ID: 20250612_163807
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/analyze', methods=['GET', 'POST'])
def analyze_request():
    """
    Endpoint to analyze web requests and check for Incapsula incident IDs.

    Returns:
        JSON response indicating the presence of an Incapsula incident ID.
    """
    try:
        # Extract headers from the incoming request
        headers = request.headers
        
        # Check for the presence of the Incapsula incident ID in headers
        incapsula_incident_id = headers.get("Incapsula-Incident-ID", None)
        
        if incapsula_incident_id:
            # Log the received Incapsula incident ID
            logging.warning(f"Incapsula Incident ID detected: {incapsula_incident_id}")
            
            # Respond with details about the incident ID
            return jsonify({
                "message": "Incapsula Incident ID detected in the request.",
                "incident_id": incapsula_incident_id
            }), 403  # HTTP Status Code 403: Forbidden
        else:
            # Proceed normally if no Incapsula incident ID is detected
            logging.info("No Incapsula Incident ID detected in the request.")
            return jsonify({
                "message": "Request received successfully. No Incapsula Incident ID detected."
            }), 200  # HTTP Status Code 200: OK

    except Exception as e:
        # Handle unexpected errors gracefully
        logging.error(f"An error occurred while analyzing the request: {str(e)}")
        return jsonify({
            "message": "An internal server error occurred.",
            "error": str(e)
        }), 500  # HTTP Status Code 500: Internal Server Error

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

This code implements a Flask web application to analyze incoming requests for an "Incapsula-Incident-ID" header. It is designed to handle errors gracefully and follows best practices for clean, readable, and production-ready Python code.
