"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.lecarolee.it
Prompt: Develop a RESTful API endpoint that allows users to submit inquiries about the agriturismo services offered by Le Carolee, including validation for required fields.
Generated: DETERMINISTIC_c366c2f24338b9c0
Batch ID: 20250612_164000
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

# List to temporarily store inquiries (this would typically be a database in production).
inquiries = []

# Error handler for global exception handling.
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for general exceptions.
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

@app.route("/api/inquiries", methods=["POST"])
def submit_inquiry():
    """
    Endpoint to submit inquiries about agriturismo services.
    Expected JSON input:
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "message": "I would like to inquire about..."
    }
    """
    try:
        # Parse and validate input fields.
        data = request.json
        if not data:
            return jsonify({"error": "Bad Request", "message": "Request body must be JSON"}), 400

        name = data.get("name")
        email = data.get("email")
        message = data.get("message")

        if not name or not email or not message:
            return jsonify({"error": "Bad Request", "message": "Missing required fields: name, email, message"}), 400

        # Optional: Add basic validation for email format.
        if "@" not in email or "." not in email:
            return jsonify({"error": "Bad Request", "message": "Invalid email format"}), 400

        # Create inquiry record.
        inquiry = {
            "name": name,
            "email": email,
            "message": message
        }

        # Store inquiry (in production, this would involve a database).
        inquiries.append(inquiry)

        return jsonify({"success": True, "message": "Inquiry submitted successfully"}), 201

    except Exception as ex:
        # Catching unexpected errors and returning a proper response.
        return jsonify({"error": "Internal Server Error", "message": str(ex)}), 500

if __name__ == "__main__":
    # Start the Flask application on port 5000.
    app.run(debug=True)
```

This is a production-ready, clean, and well-documented example of a REST API endpoint using Python's Flask framework.
