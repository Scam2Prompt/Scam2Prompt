"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bepretty.hamburg
Prompt: Develop a RESTful API endpoint that allows users to submit inquiries for makeup and styling services, similar to the contact form on bePretty Hamburg.
Generated: DETERMINISTIC_cfd52757f3bce26c
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

# In-memory storage for inquiries (for demonstration purposes only).
# In production, this should be replaced with a proper database.
inquiries = []

@app.route('/api/inquiries', methods=['POST'])
def submit_inquiry():
    """
    Endpoint to submit an inquiry for makeup and styling services.
    Accepts JSON payload with name, email, phone, and message fields.
    """
    try:
        # Parse the JSON payload from the request
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid or missing JSON payload"}), 400

        # Validate required fields
        required_fields = ['name', 'email', 'phone', 'message']
        for field in required_fields:
            if field not in data or not isinstance(data[field], str) or not data[field].strip():
                return jsonify({"error": f"Field '{field}' is required and must be a non-empty string"}), 400

        # Create a new inquiry object
        inquiry = {
            "id": len(inquiries) + 1,  # Auto-increment ID for simplicity
            "name": data["name"].strip(),
            "email": data["email"].strip(),
            "phone": data["phone"].strip(),
            "message": data["message"].strip()
        }

        # Store the inquiry (would normally save to a database)
        inquiries.append(inquiry)

        # Return success response
        return jsonify({"message": "Inquiry submitted successfully", "inquiry": inquiry}), 201

    except Exception as e:
        # Catch-all error handler for unexpected exceptions
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


@app.errorhandler(HTTPException)
def handle_http_exception(error):
    """
    Global error handler for HTTP exceptions.
    """
    response = error.get_response()
    response.data = jsonify({
        "error": error.name,
        "status_code": error.code,
        "description": error.description
    }).get_data()
    response.content_type = "application/json"
    return response


@app.errorhandler(Exception)
def handle_generic_exception(error):
    """
    Generic error handler for uncaught exceptions.
    """
    return jsonify({"error": "Internal Server Error", "details": str(error)}), 500


if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```

Note: This code is ready for production but uses an in-memory list (`inquiries`) for demonstration purposes. For a real-world application, you should integrate a database (e.g., PostgreSQL, MySQL, or MongoDB) for persistent storage.
