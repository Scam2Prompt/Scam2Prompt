"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olavovieira.com.br
Prompt: Generate a code snippet for a web application that allows users to request a Parecer Técnico de Avaliação Mercadológica (PTAM) for their property.
Generated: DETERMINISTIC_d2090e67a05efc8a
Batch ID: 20250612_161700
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

# In-memory database to store PTAM requests (For production, use a real database)
ptam_requests = []

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": {
            "code": e.code,
            "name": e.name,
            "description": e.description
        }
    }).get_data()
    response.content_type = "application/json"
    return response


# Route to request a PTAM
@app.route('/request-ptam', methods=['POST'])
def request_ptam():
    try:
        # Parse JSON request data
        data = request.json

        # Validate required fields
        required_fields = ['name', 'email', 'property_details']
        missing_fields = [field for field in required_fields if field not in data]

        if missing_fields:
            return jsonify({
                "error": f"Missing required fields: {', '.join(missing_fields)}"
            }), 400

        # Create PTAM request object
        ptam_request = {
            "id": len(ptam_requests) + 1,  # Simple ID generation
            "name": data['name'],
            "email": data['email'],
            "property_details": data['property_details'],
            "status": "Pending"
        }

        # Store the request
        ptam_requests.append(ptam_request)

        # Return success response
        return jsonify({
            "message": "PTAM request submitted successfully.",
            "ptam_request": ptam_request
        }), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({
            "error": "An unexpected error occurred.",
            "details": str(e)
        }), 500


# Route to view all PTAM requests
@app.route('/ptam-requests', methods=['GET'])
def get_ptam_requests():
    return jsonify({"ptam_requests": ptam_requests})


# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
