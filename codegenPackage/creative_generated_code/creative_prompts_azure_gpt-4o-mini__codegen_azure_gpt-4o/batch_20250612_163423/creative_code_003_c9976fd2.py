"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://johnbarrybaker.com
Prompt: Develop a RESTful API endpoint for a personal injury law firm that allows clients to submit details about their accidents, including types like truck accidents and slip and fall incidents.
Generated: DETERMINISTIC_c9976fd25e52b6de
Batch ID: 20250612_163423
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

# Sample in-memory database (for demonstration purposes)
accident_reports = []

# Endpoint to submit accident details
@app.route('/submit-accident', methods=['POST'])
def submit_accident():
    """
    Endpoint to submit details about an accident.
    Expects JSON payload with the following structure:
    {
        "client_name": "John Doe",
        "contact_info": "johndoe@example.com",
        "accident_type": "truck accident",
        "description": "Details about the accident"
    }
    """
    try:
        # Parse and validate input data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid or missing JSON payload"}), 400
        
        # Required fields
        required_fields = ["client_name", "contact_info", "accident_type", "description"]
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400
        
        # Add the accident report to the in-memory database
        report_id = len(accident_reports) + 1
        accident_report = {
            "id": report_id,
            "client_name": data["client_name"],
            "contact_info": data["contact_info"],
            "accident_type": data["accident_type"],
            "description": data["description"]
        }
        accident_reports.append(accident_report)
        
        # Return success response
        return jsonify({"message": "Accident report submitted successfully", "report_id": report_id}), 201
    
    except HTTPException as http_err:
        # Handle Flask-related HTTP exceptions
        return jsonify({"error": str(http_err)}), http_err.code
    except Exception as err:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(err)}), 500

# Error handler for 404 Not Found
@app.errorhandler(404)
def resource_not_found(e):
    """Handle 404 errors gracefully."""
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 405 Method Not Allowed
@app.errorhandler(405)
def method_not_allowed(e):
    """Handle 405 errors gracefully."""
    return jsonify({"error": "Method not allowed"}), 405

# Error handler for generic server errors
@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors gracefully."""
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the development server
    app.run(debug=True)
```
